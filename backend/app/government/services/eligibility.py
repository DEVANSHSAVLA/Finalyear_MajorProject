"""
Eligibility Engine for Government Service Navigator (Module B).
Evaluates citizen profile against service eligibility rules.
"""

from typing import Dict, Any, List, Optional
import logging

logger = logging.getLogger("civicsphere.government.eligibility")


def evaluate_rule(user_value: Any, operator: str, required_value: Any) -> bool:
    """Evaluates a single eligibility rule against citizen profile value."""
    # Normalize booleans
    norm_user = user_value
    if isinstance(user_value, str):
        if user_value.lower() == "true":
            norm_user = True
        elif user_value.lower() == "false":
            norm_user = False

    norm_req = required_value
    if isinstance(required_value, str):
        if required_value.lower() == "true":
            norm_req = True
        elif required_value.lower() == "false":
            norm_req = False

    op = operator.lower().strip()
    if op in ("equals", "==", "="):
        return norm_user == norm_req
    elif op in ("not_equals", "!="):
        return norm_user != norm_req
    elif op in ("greater_than", ">"):
        try:
            return float(norm_user) > float(norm_req)
        except (ValueError, TypeError):
            return False
    elif op in ("less_than", "<"):
        try:
            return float(norm_user) < float(norm_req)
        except (ValueError, TypeError):
            return False
    elif op in ("greater_than_or_equal", ">="):
        try:
            return float(norm_user) >= float(norm_req)
        except (ValueError, TypeError):
            return False
    elif op in ("less_than_or_equal", "<="):
        try:
            return float(norm_user) <= float(norm_req)
        except (ValueError, TypeError):
            return False
    elif op == "contains":
        if isinstance(norm_user, list):
            return norm_req in norm_user
        if isinstance(norm_user, str):
            return str(norm_req).lower() in norm_user.lower()
        return False
    elif op == "in":
        if isinstance(norm_req, list):
            return norm_user in norm_req
        return False
    elif op in ("not_in", "not in"):
        if isinstance(norm_req, list):
            if isinstance(norm_user, list):
                return not any(item in norm_req for item in norm_user)
            return norm_user not in norm_req
        return True
    elif op == "boolean":
        return bool(norm_user) == bool(norm_req)
    return False


def check_eligibility(rules: List[Dict[str, Any]], citizen_context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Checks list of eligibility rules against citizen context.
    Returns {status: CONFIRMED|FAILED|UNKNOWN, confirmed: [], failed: [], unknown: [], percent_complete: int}
    """
    confirmed = []
    failed = []
    unknown = []

    if not rules:
        return {
            "status": "CONFIRMED",
            "confirmed": [],
            "failed": [],
            "unknown": [],
            "percent_complete": 100
        }

    for rule in rules:
        field = rule.get("field") or rule.get("field_name", "")
        op = rule.get("operator", "equals")
        req_val = rule.get("value") if "value" in rule else rule.get("threshold_value")
        desc = rule.get("description") or rule.get("error_message", f"Field '{field}' is required.")

        if field not in citizen_context or citizen_context[field] is None or citizen_context[field] == "":
            unknown.append({
                "field": field,
                "description": desc,
                "operator": op,
                "required_value": req_val,
            })
            continue

        user_val = citizen_context[field]
        passed = evaluate_rule(user_val, op, req_val)

        evaluated_item = {
            "field": field,
            "operator": op,
            "required_value": req_val,
            "user_value": user_val,
            "description": desc,
        }

        if passed:
            confirmed.append(evaluated_item)
        else:
            failed.append(evaluated_item)

    if failed:
        status = "FAILED"
    elif unknown:
        status = "UNKNOWN"
    else:
        status = "CONFIRMED"

    total = len(rules)
    known = len(confirmed) + len(failed)
    percent = round((known / total) * 100) if total > 0 else 100

    return {
        "status": status,
        "confirmed": confirmed,
        "failed": failed,
        "unknown": unknown,
        "percent_complete": percent,
    }


def evaluate_eligibility(rules: List[Dict[str, Any]], citizen_context: Dict[str, Any]):
    """Evaluates rules and returns an EligibilityResult-compatible object."""
    from packages.schemas.contracts import EligibilityResult
    res = check_eligibility(rules, citizen_context)
    is_eligible = res["status"] == "CONFIRMED"
    reasons = [f["description"] for f in res["failed"]]
    return EligibilityResult(
        is_eligible=is_eligible,
        confidence=1.0 if res["status"] != "UNKNOWN" else 0.5,
        reasons=reasons,
        matching_rules_count=len(res["confirmed"]),
        total_rules_count=len(rules)
    )


def evaluate_pm_kisan_eligibility(citizen_context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Comprehensive PM-KISAN eligibility evaluator implementing all official June 2019
    Union Cabinet expansion rules and statutory exclusion conditions:
    1. All cultivable landholding farmer families eligible regardless of landholding size (> 2 ha).
    2. Institutional landholders excluded.
    3. Constitutional and elected-office holders (Ministers, MPs, MLAs, MLCs, Mayors, District Panchayat Chairpersons) excluded.
    4. Serving and retired government/PSE/local body employees excluded, WITH PRESCRIBED EXCEPTION for Class IV / Group D / MTS employees (eligible).
    5. Pensioners receiving >= INR 10,000/month excluded, WITH PRESCRIBED EXCEPTION for Class IV / Group D / MTS pensioners (eligible).
    6. Income tax payees in last assessment year excluded.
    7. Registered practicing professionals (Doctors, Engineers, Lawyers, CAs, Architects) excluded.
    8. If land ownership, land-record dates, or State verification is uncertain/pending, returns VERIFICATION_NEEDED.
    """
    reasons = []
    exclusions_applied = []
    exceptions_applied = []
    failed_checks = []
    confirmed_checks = []
    unknown_checks = []

    # 1. Occupation / Farmer check
    occupation = str(citizen_context.get("occupation", "")).lower().strip()
    is_farmer = (
        occupation == "farmer"
        or citizen_context.get("is_farmer") is True
        or citizen_context.get("landholder_family") is True
    )
    if not is_farmer:
        failed_checks.append("Applicant must be a landholding farmer family.")
        reasons.append("Non-farming occupations are not eligible for PM-KISAN income support.")
    else:
        confirmed_checks.append("Applicant is a farmer / cultivable landholding family.")

    # 2. Land Ownership & State Verification Check
    owns_land = citizen_context.get("owns_cultivable_land")
    land_verified = citizen_context.get("land_records_verified")
    state_verified = citizen_context.get("state_verification_status")

    if owns_land is False:
        failed_checks.append("Family does not own cultivable land.")
        reasons.append("Applicant must possess cultivable agricultural landholding.")
    elif (
        owns_land is None
        or land_verified in (None, False, "pending", "uncertain")
        or state_verified in ("pending", "uncertain", "unverified")
    ):
        unknown_checks.append("Agricultural land record ownership and State nodal verification are pending confirmation.")
        reasons.append("Verification needed: State land record (RoR / 7/12 extract) ownership and e-KYC require district nodal officer confirmation.")
    else:
        confirmed_checks.append("Agricultural land ownership verified in official State records.")

    # 3. Institutional Landholder Exclusion
    exclusion_list = citizen_context.get("exclusion_criteria", [])
    if isinstance(exclusion_list, str):
        exclusion_list = [exclusion_list]
    norm_exclusions = [str(x).lower().strip() for x in exclusion_list]

    if (
        citizen_context.get("is_institutional_landholder") is True
        or "institutional landholders" in norm_exclusions
        or "institutional landholder" in norm_exclusions
    ):
        failed_checks.append("Institutional Landholder")
        exclusions_applied.append("Excluded: Institutional landholders (trusts, societies, corporate or government entities) are ineligible.")
        reasons.append("Institutional landholders are ineligible under PM-KISAN guidelines.")

    # 4. Constitutional Post Holders Exclusion
    if (
        citizen_context.get("is_constitutional_post_holder") is True
        or "constitutional post holders" in norm_exclusions
        or "constitutional post holder" in norm_exclusions
    ):
        failed_checks.append("Constitutional Post Holder")
        exclusions_applied.append("Excluded: Former and present holders of constitutional posts.")
        reasons.append("Holders of constitutional posts are ineligible under PM-KISAN guidelines.")

    # 5. Elected Office Holders Exclusion (Ministers, MPs, MLAs, MLCs, Mayors, District Panchayat Chairpersons)
    elected_office = citizen_context.get("elected_office") or citizen_context.get("is_elected_representative") is True
    if elected_office or "elected representatives" in norm_exclusions:
        failed_checks.append("Elected Representative")
        exclusions_applied.append("Excluded: Former and present Ministers, MPs, MLAs, MLCs, Mayors of Municipal Corporations, and Chairpersons of District Panchayats.")
        reasons.append("Former or present elected representatives of statutory bodies are excluded.")

    # 6. Serving or Retired Government / PSE / Local Body Employees
    # Prescribed Exception: Multi-Tasking Staff / Class IV / Group D are NOT excluded.
    gov_emp = (
        citizen_context.get("is_gov_employee") is True
        or citizen_context.get("is_government_employee") is True
        or str(citizen_context.get("gov_service_status", "")).lower() in ("serving", "retired")
        or "serving/retired gov employee" in norm_exclusions
    )
    is_group_d = (
        citizen_context.get("is_class_iv_or_mts") is True
        or str(citizen_context.get("employee_category", "")).lower() in ("class iv", "class 4", "group d", "mts", "multi tasking staff")
        or str(citizen_context.get("cadre", "")).lower() in ("class iv", "group d", "mts")
    )

    if gov_emp:
        if is_group_d:
            exceptions_applied.append("Exception Preserved: Multi Tasking Staff / Class IV / Group D employees are eligible under PM-KISAN scheme rules.")
            confirmed_checks.append("Government Service (Class IV/Group D Exception)")
        else:
            failed_checks.append("Government Employee (Officer/Regular Non-Group D)")
            exclusions_applied.append("Excluded: All serving or retired officers and regular employees of Central/State Govt ministries, PSEs, and local bodies (excluding Class IV/Group D).")
            reasons.append("Government and regular public sector employees (non-Group D) are excluded from PM-KISAN.")

    # 7. Pensioners Receiving Monthly Pension >= INR 10,000
    # Prescribed Exception: Multi-Tasking Staff / Class IV / Group D pensioners are NOT excluded.
    monthly_pension = float(citizen_context.get("monthly_pension", 0) or 0)
    if monthly_pension >= 10000:
        if is_group_d or citizen_context.get("is_pensioner_group_d") is True:
            exceptions_applied.append("Exception Preserved: Retired Class IV / Group D pensioners are eligible even if monthly pension is INR 10,000 or more.")
            confirmed_checks.append("Pensioner (Class IV/Group D Exception)")
        else:
            failed_checks.append("Pensioner >= INR 10,000/month")
            exclusions_applied.append("Excluded: Superannuated/retired pensioners whose monthly pension is INR 10,000 or more (excluding Class IV/Group D).")
            reasons.append("Pensioners with monthly pension of INR 10,000 or more (non-Group D) are excluded from PM-KISAN.")

    # 8. Income Tax Payees in Last Assessment Year
    paid_tax = (
        citizen_context.get("paid_income_tax_last_ay") is True
        or citizen_context.get("is_income_tax_payee") is True
        or float(citizen_context.get("annual_income", 0) or 0) >= 1000000
        or "income tax payees" in norm_exclusions
    )
    if paid_tax:
        failed_checks.append("Income Tax Payee")
        exclusions_applied.append("Excluded: All persons who paid income tax in the last assessment year.")
        reasons.append("Income tax payees of the previous assessment year are ineligible under PM-KISAN rules.")

    # 9. Registered Practicing Professionals (Doctors, Engineers, Lawyers, CAs, Architects)
    profession = str(citizen_context.get("professional_practice", "")).lower()
    is_practicing_prof = (
        citizen_context.get("is_practicing_professional") is True
        or any(p in profession for p in ["doctor", "engineer", "lawyer", "advocate", "ca", "chartered accountant", "architect"])
        or "practicing professionals" in norm_exclusions
    )
    if is_practicing_prof:
        failed_checks.append("Practicing Professional")
        exclusions_applied.append("Excluded: Registered professionals (Doctors, Engineers, Lawyers, Chartered Accountants, Architects) undertaking practice.")
        reasons.append("Registered practicing professionals are excluded from PM-KISAN benefits.")

    # 10. Landholding Size (> 2 ha) - Affirmatively confirmed!
    landholding = float(citizen_context.get("landholding_hectares", 0) or 0)
    if landholding > 0:
        confirmed_checks.append(f"Cultivable landholding of {landholding} ha (Abolished 2-hectare ceiling satisfied post-June 2019 expansion)")

    # Determine Final Status
    if failed_checks:
        status = "FAILED"
        is_eligible = False
        confidence = 1.0
    elif unknown_checks:
        status = "VERIFICATION_NEEDED"
        is_eligible = False
        confidence = 0.5
    else:
        status = "CONFIRMED"
        is_eligible = True
        confidence = 1.0

    return {
        "status": status,
        "is_eligible": is_eligible,
        "confidence": confidence,
        "reasons": reasons,
        "failed_checks": failed_checks,
        "confirmed_checks": confirmed_checks,
        "unknown_checks": unknown_checks,
        "exclusions_applied": exclusions_applied,
        "exceptions_applied": exceptions_applied,
    }

