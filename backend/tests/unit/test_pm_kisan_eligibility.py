"""
Unit and regression tests for PM-KISAN scheme eligibility evaluation.
Verifies the June 2019 Cabinet decision expanding eligibility to all landholding farmer families,
confirming that landholding size (> 2 hectares) alone does not disqualify an applicant,
while all 7 statutory exclusions (institutional landholders, constitutional posts, elected representatives,
regular government employees, pensioners >= 10k, tax payees, professionals) are enforced,
and statutory exceptions (Class IV / Group D / MTS employees and pensioners) are preserved.
Also verifies that unverified or uncertain land records yield VERIFICATION_NEEDED.
"""

import pytest
from backend.app.government.services.eligibility import (
    check_eligibility,
    evaluate_eligibility,
    evaluate_pm_kisan_eligibility,
)
from data.seed.seed_government_services import SEED_GOVERNMENT_SCHEMES


@pytest.fixture
def pm_kisan_rules():
    for scheme in SEED_GOVERNMENT_SCHEMES:
        if scheme["service_id"] == "gov_pm_kisan":
            return scheme["eligibility_rules"]
    pytest.fail("gov_pm_kisan not found in seed schemes")


# 1. Farmers with > 2 hectares eligible post June 2019 expansion
def test_pm_kisan_eligible_over_two_hectares(pm_kisan_rules):
    """
    REGRESSION TEST: Farmers with > 2 hectares (e.g. 5.2 ha) must be ELIGIBLE.
    The 2-hectare ceiling was abolished on June 7, 2019 by the Union Cabinet.
    """
    citizen_context = {
        "occupation": "Farmer",
        "exclusion_criteria": "None",
        "annual_income": 350000,
        "landholding_hectares": 5.2,
        "owns_cultivable_land": True,
        "land_records_verified": True,
        "state_verification_status": "verified",
    }
    # Test via generic rules
    result = check_eligibility(pm_kisan_rules, citizen_context)
    assert result["status"] == "CONFIRMED", f"Expected CONFIRMED, got {result['status']}: {result.get('failed')}"
    assert len(result["failed"]) == 0
    assert result["percent_complete"] == 100

    contract_res = evaluate_eligibility(pm_kisan_rules, citizen_context)
    assert contract_res.is_eligible is True
    assert contract_res.confidence == 1.0

    # Test via statutory PM-KISAN evaluator
    pm_eval = evaluate_pm_kisan_eligibility(citizen_context)
    assert pm_eval["status"] == "CONFIRMED"
    assert pm_eval["is_eligible"] is True
    assert pm_eval["confidence"] == 1.0
    assert any("5.2 ha" in c for c in pm_eval["confirmed_checks"])


# 2. Small/Marginal farmer (< 2 ha) eligible
def test_pm_kisan_small_marginal_farmer_eligible(pm_kisan_rules):
    """Small and marginal farmers (< 2 ha) remain fully eligible."""
    citizen_context = {
        "occupation": "Farmer",
        "exclusion_criteria": "None",
        "annual_income": 120000,
        "landholding_hectares": 1.2,
        "owns_cultivable_land": True,
        "land_records_verified": True,
        "state_verification_status": "verified",
    }
    result = check_eligibility(pm_kisan_rules, citizen_context)
    assert result["status"] == "CONFIRMED"

    pm_eval = evaluate_pm_kisan_eligibility(citizen_context)
    assert pm_eval["status"] == "CONFIRMED"
    assert pm_eval["is_eligible"] is True


# 3. Institutional landholders excluded
def test_pm_kisan_ineligible_institutional_landholder(pm_kisan_rules):
    """Institutional landholders (trusts, societies, institutions) are excluded."""
    citizen_context = {
        "occupation": "Farmer",
        "exclusion_criteria": "Institutional Landholders",
        "annual_income": 200000,
        "landholding_hectares": 3.0,
        "is_institutional_landholder": True,
        "owns_cultivable_land": True,
        "land_records_verified": True,
        "state_verification_status": "verified",
    }
    result = check_eligibility(pm_kisan_rules, citizen_context)
    assert result["status"] == "FAILED"
    assert any(f["field"] == "exclusion_criteria" for f in result["failed"])

    pm_eval = evaluate_pm_kisan_eligibility(citizen_context)
    assert pm_eval["status"] == "FAILED"
    assert pm_eval["is_eligible"] is False
    assert any("Institutional" in r for r in pm_eval["failed_checks"])


# 4. Constitutional post holders excluded
def test_pm_kisan_ineligible_constitutional_post_holder(pm_kisan_rules):
    """Former or present holders of constitutional posts are excluded."""
    citizen_context = {
        "occupation": "Farmer",
        "exclusion_criteria": "Constitutional Post Holders",
        "annual_income": 500000,
        "landholding_hectares": 4.0,
        "is_constitutional_post_holder": True,
        "owns_cultivable_land": True,
        "land_records_verified": True,
        "state_verification_status": "verified",
    }
    result = check_eligibility(pm_kisan_rules, citizen_context)
    assert result["status"] == "FAILED"

    pm_eval = evaluate_pm_kisan_eligibility(citizen_context)
    assert pm_eval["status"] == "FAILED"
    assert pm_eval["is_eligible"] is False
    assert any("Constitutional" in r for r in pm_eval["failed_checks"])


# 5. Elected representatives excluded
def test_pm_kisan_ineligible_elected_representative(pm_kisan_rules):
    """Former/present Ministers, MPs, MLAs, MLCs, Mayors, ZP Chairpersons are excluded."""
    citizen_context = {
        "occupation": "Farmer",
        "exclusion_criteria": "Elected Representatives",
        "annual_income": 600000,
        "landholding_hectares": 6.0,
        "is_elected_representative": True,
        "elected_office": "Member of Legislative Assembly (MLA)",
        "owns_cultivable_land": True,
        "land_records_verified": True,
        "state_verification_status": "verified",
    }
    result = check_eligibility(pm_kisan_rules, citizen_context)
    assert result["status"] == "FAILED"

    pm_eval = evaluate_pm_kisan_eligibility(citizen_context)
    assert pm_eval["status"] == "FAILED"
    assert pm_eval["is_eligible"] is False
    assert any("Elected" in r for r in pm_eval["failed_checks"])


# 6. Regular serving/retired government employees excluded
def test_pm_kisan_ineligible_regular_gov_employee(pm_kisan_rules):
    """Serving or retired regular govt/PSE officers (non-Group D) are excluded."""
    citizen_context = {
        "occupation": "Farmer",
        "exclusion_criteria": "Serving/Retired Gov Employee",
        "annual_income": 750000,
        "landholding_hectares": 2.0,
        "is_gov_employee": True,
        "employee_category": "Class I Officer",
        "owns_cultivable_land": True,
        "land_records_verified": True,
        "state_verification_status": "verified",
    }
    result = check_eligibility(pm_kisan_rules, citizen_context)
    assert result["status"] == "FAILED"

    pm_eval = evaluate_pm_kisan_eligibility(citizen_context)
    assert pm_eval["status"] == "FAILED"
    assert pm_eval["is_eligible"] is False
    assert any("Government Employee" in r for r in pm_eval["failed_checks"])


# 7. Group D / MTS government employee exception preserved (Eligible)
def test_pm_kisan_eligible_group_d_gov_employee_exception():
    """Multi Tasking Staff / Class IV / Group D government employees are NOT excluded."""
    citizen_context = {
        "occupation": "Farmer",
        "exclusion_criteria": "None",
        "annual_income": 320000,
        "landholding_hectares": 2.5,
        "is_gov_employee": True,
        "is_class_iv_or_mts": True,
        "employee_category": "Group D",
        "owns_cultivable_land": True,
        "land_records_verified": True,
        "state_verification_status": "verified",
    }
    pm_eval = evaluate_pm_kisan_eligibility(citizen_context)
    assert pm_eval["status"] == "CONFIRMED"
    assert pm_eval["is_eligible"] is True
    assert any("Group D" in exp for exp in pm_eval["exceptions_applied"])


# 8. High monthly pensioners (>= INR 10,000/mo) excluded
def test_pm_kisan_ineligible_high_pensioner(pm_kisan_rules):
    """Pensioners receiving >= INR 10,000 per month (excluding Class IV/Group D) are ineligible."""
    citizen_context = {
        "occupation": "Farmer",
        "exclusion_criteria": "Pensioner >= 10k",
        "annual_income": 400000,
        "landholding_hectares": 3.0,
        "monthly_pension": 18500,
        "owns_cultivable_land": True,
        "land_records_verified": True,
        "state_verification_status": "verified",
    }
    result = check_eligibility(pm_kisan_rules, citizen_context)
    assert result["status"] == "FAILED"

    pm_eval = evaluate_pm_kisan_eligibility(citizen_context)
    assert pm_eval["status"] == "FAILED"
    assert pm_eval["is_eligible"] is False
    assert any("Pensioner" in r for r in pm_eval["failed_checks"])


# 9. Group D / MTS pensioner exception preserved (Eligible)
def test_pm_kisan_eligible_group_d_pensioner_exception():
    """Retired Class IV / Group D / MTS pensioners are NOT excluded even if pension >= INR 10,000."""
    citizen_context = {
        "occupation": "Farmer",
        "exclusion_criteria": "None",
        "annual_income": 250000,
        "landholding_hectares": 1.8,
        "monthly_pension": 12000,
        "is_class_iv_or_mts": True,
        "is_pensioner_group_d": True,
        "owns_cultivable_land": True,
        "land_records_verified": True,
        "state_verification_status": "verified",
    }
    pm_eval = evaluate_pm_kisan_eligibility(citizen_context)
    assert pm_eval["status"] == "CONFIRMED"
    assert pm_eval["is_eligible"] is True
    assert any("Group D" in exp for exp in pm_eval["exceptions_applied"])


# 10. Income tax payees in last assessment year excluded
def test_pm_kisan_ineligible_income_tax_payee(pm_kisan_rules):
    """Income tax payees are excluded from PM-KISAN benefits."""
    citizen_context = {
        "occupation": "Farmer",
        "exclusion_criteria": "Income Tax Payees",
        "annual_income": 1200000,
        "paid_income_tax_last_ay": True,
        "landholding_hectares": 3.5,
        "owns_cultivable_land": True,
        "land_records_verified": True,
        "state_verification_status": "verified",
    }
    result = check_eligibility(pm_kisan_rules, citizen_context)
    assert result["status"] == "FAILED"

    pm_eval = evaluate_pm_kisan_eligibility(citizen_context)
    assert pm_eval["status"] == "FAILED"
    assert pm_eval["is_eligible"] is False
    assert any("Income Tax" in r for r in pm_eval["failed_checks"])


# 11. Registered practicing professionals excluded
def test_pm_kisan_ineligible_practicing_professional(pm_kisan_rules):
    """Doctors, Engineers, Lawyers, Chartered Accountants, and Architects are excluded."""
    citizen_context = {
        "occupation": "Farmer",
        "exclusion_criteria": "Practicing Professionals",
        "annual_income": 500000,
        "landholding_hectares": 4.0,
        "professional_practice": "Chartered Accountant",
        "is_practicing_professional": True,
        "owns_cultivable_land": True,
        "land_records_verified": True,
        "state_verification_status": "verified",
    }
    result = check_eligibility(pm_kisan_rules, citizen_context)
    assert result["status"] == "FAILED"

    pm_eval = evaluate_pm_kisan_eligibility(citizen_context)
    assert pm_eval["status"] == "FAILED"
    assert pm_eval["is_eligible"] is False
    assert any("Practicing Professional" in r for r in pm_eval["failed_checks"])


# 12. Uncertain or unverified land records return VERIFICATION_NEEDED
def test_pm_kisan_verification_needed_unverified_land_records():
    """Pending land records or state verification must return VERIFICATION_NEEDED."""
    citizen_context = {
        "occupation": "Farmer",
        "exclusion_criteria": "None",
        "annual_income": 200000,
        "landholding_hectares": 2.0,
        "owns_cultivable_land": True,
        "land_records_verified": "pending",
        "state_verification_status": "unverified",
    }
    pm_eval = evaluate_pm_kisan_eligibility(citizen_context)
    assert pm_eval["status"] == "VERIFICATION_NEEDED"
    assert pm_eval["is_eligible"] is False
    assert pm_eval["confidence"] == 0.5
    assert len(pm_eval["unknown_checks"]) > 0
    assert any("district nodal officer" in r for r in pm_eval["reasons"])
