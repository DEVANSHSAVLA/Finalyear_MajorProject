"""
Unit and regression tests for PM-KISAN scheme eligibility evaluation.
Verifies the June 2019 Cabinet decision expanding eligibility to all landholding farmer families,
confirming that landholding size (> 2 hectares) alone does not disqualify an applicant,
while statutory exclusions (institutional landholders, income tax payees) remain enforced.
"""

import pytest
from backend.app.government.services.eligibility import check_eligibility, evaluate_eligibility
from data.seed.seed_government_services import SEED_GOVERNMENT_SCHEMES


@pytest.fixture
def pm_kisan_rules():
    for scheme in SEED_GOVERNMENT_SCHEMES:
        if scheme["service_id"] == "gov_pm_kisan":
            return scheme["eligibility_rules"]
    pytest.fail("gov_pm_kisan not found in seed schemes")


def test_pm_kisan_eligible_over_two_hectares(pm_kisan_rules):
    """
    REGRESSION TEST: Farmers with > 2 hectares (e.g. 4.5 ha or 5.0 ha) must be ELIGIBLE.
    The 2-hectare ceiling was abolished on June 7, 2019 by the Union Cabinet.
    """
    citizen_context = {
        "occupation": "Farmer",
        "exclusion_criteria": "None",
        "annual_income": 350000,
        "landholding_hectares": 5.2,  # Substantially greater than legacy 2 ha limit
    }
    result = check_eligibility(pm_kisan_rules, citizen_context)
    assert result["status"] == "CONFIRMED", f"Expected CONFIRMED, got {result['status']}: {result.get('failed')}"
    assert len(result["failed"]) == 0
    assert result["percent_complete"] == 100

    contract_res = evaluate_eligibility(pm_kisan_rules, citizen_context)
    assert contract_res.is_eligible is True
    assert contract_res.confidence == 1.0


def test_pm_kisan_small_marginal_farmer_eligible(pm_kisan_rules):
    """Small and marginal farmers (< 2 ha) remain fully eligible."""
    citizen_context = {
        "occupation": "Farmer",
        "exclusion_criteria": "None",
        "annual_income": 120000,
        "landholding_hectares": 1.2,
    }
    result = check_eligibility(pm_kisan_rules, citizen_context)
    assert result["status"] == "CONFIRMED"
    assert len(result["failed"]) == 0


def test_pm_kisan_ineligible_institutional_landholder(pm_kisan_rules):
    """Institutional landholders are explicitly excluded from PM-KISAN benefits."""
    citizen_context = {
        "occupation": "Farmer",
        "exclusion_criteria": "Institutional Landholders",
        "annual_income": 200000,
        "landholding_hectares": 3.0,
    }
    result = check_eligibility(pm_kisan_rules, citizen_context)
    assert result["status"] == "FAILED"
    assert any(f["field"] == "exclusion_criteria" for f in result["failed"])


def test_pm_kisan_ineligible_high_income_tax_payee(pm_kisan_rules):
    """Income tax payees are excluded from PM-KISAN benefits."""
    citizen_context = {
        "occupation": "Farmer",
        "exclusion_criteria": "None",
        "annual_income": 1500000,  # Exceeds threshold
        "landholding_hectares": 2.5,
    }
    result = check_eligibility(pm_kisan_rules, citizen_context)
    assert result["status"] == "FAILED"
    assert any(f["field"] == "annual_income" for f in result["failed"])


def test_pm_kisan_non_farmer_rejected(pm_kisan_rules):
    """Non-farmers are not eligible for PM-KISAN."""
    citizen_context = {
        "occupation": "Software Engineer",
        "exclusion_criteria": "None",
        "annual_income": 400000,
        "landholding_hectares": 0.0,
    }
    result = check_eligibility(pm_kisan_rules, citizen_context)
    assert result["status"] == "FAILED"
    assert any(f["field"] == "occupation" for f in result["failed"])
