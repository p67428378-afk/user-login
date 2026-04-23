
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from backend import models

# Test case 1: Basic premium calculation with no NCB and default multiplier
def test_calculate_premium_basic(client: TestClient, session: Session):
    # Populate mock data
    session.add(models.NCBTier(years_no_claim=0, discount_percentage=0))
    session.add(models.VehicleMultiplier(vehicle_type="Sedan", vehicle_make="Toyota", vehicle_model="Camry", age_band="2-5 Years", safety_features="", multiplier_value=1.0))
    session.commit()

    response = client.post(
        "/api/v1/premium-calculation/",
        json={
            "customer_id": "CUST-001",
            "policy_id": "POL-001",
            "vehicle_type": "Sedan",
            "vehicle_make": "Toyota",
            "vehicle_model": "Camry",
            "age_band": "2-5 Years",
            "safety_features": [],
            "years_no_claim": 0,
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["policy_id"] == "POL-001"
    assert data["calculated_premium"] == 500.0

# Test case 2: Premium calculation with 2 years NCB
def test_calculate_premium_with_ncb(client: TestClient, session: Session):
    session.add(models.NCBTier(years_no_claim=2, discount_percentage=0.29))
    session.add(models.VehicleMultiplier(vehicle_type="Sedan", vehicle_make="Toyota", vehicle_model="Camry", age_band="2-5 Years", safety_features="", multiplier_value=1.0))
    session.commit()

    response = client.post(
        "/api/v1/premium-calculation/",
        json={
            "customer_id": "CUST-002",
            "policy_id": "POL-002",
            "vehicle_type": "Sedan",
            "vehicle_make": "Toyota",
            "vehicle_model": "Camry",
            "age_band": "2-5 Years",
            "safety_features": [],
            "years_no_claim": 2,
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["policy_id"] == "POL-002"
    assert data["calculated_premium"] == 355.0  # 500 * (1 - 0.29)

# Test case 3: Premium calculation with max NCB (5 years)
def test_calculate_premium_with_max_ncb(client: TestClient, session: Session):
    session.add(models.NCBTier(years_no_claim=5, discount_percentage=0.50))
    session.add(models.VehicleMultiplier(vehicle_type="Sedan", vehicle_make="Toyota", vehicle_model="Camry", age_band="2-5 Years", safety_features="", multiplier_value=1.0))
    session.commit()

    response = client.post(
        "/api/v1/premium-calculation/",
        json={
            "customer_id": "CUST-003",
            "policy_id": "POL-003",
            "vehicle_type": "Sedan",
            "vehicle_make": "Toyota",
            "vehicle_model": "Camry",
            "age_band": "2-5 Years",
            "safety_features": [],
            "years_no_claim": 5,
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["policy_id"] == "POL-003"
    assert data["calculated_premium"] == 250.0  # 500 * (1 - 0.50)

# Test case 4: Premium calculation with vehicle multiplier
def test_calculate_premium_with_multiplier(client: TestClient, session: Session):
    session.add(models.NCBTier(years_no_claim=0, discount_percentage=0))
    session.add(models.VehicleMultiplier(vehicle_type="Sports Car", vehicle_make="Ferrari", vehicle_model="488", age_band="0-1 Years", safety_features="", multiplier_value=1.6))
    session.commit()

    response = client.post(
        "/api/v1/premium-calculation/",
        json={
            "customer_id": "CUST-004",
            "policy_id": "POL-004",
            "vehicle_type": "Sports Car",
            "vehicle_make": "Ferrari",
            "vehicle_model": "488",
            "age_band": "0-1 Years",
            "safety_features": [],
            "years_no_claim": 0,
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["policy_id"] == "POL-004"
    assert data["calculated_premium"] == 800.0  # 500 * 1.6

# Test case 5: Premium calculation with both NCB and vehicle multiplier
def test_calculate_premium_with_ncb_and_multiplier(client: TestClient, session: Session):
    session.add(models.NCBTier(years_no_claim=3, discount_percentage=0.35))
    session.add(models.VehicleMultiplier(vehicle_type="SUV", vehicle_make="Land Rover", vehicle_model="Defender", age_band="6-10 Years", safety_features="ABS,Airbags", multiplier_value=1.2))
    session.commit()

    response = client.post(
        "/api/v1/premium-calculation/",
        json={
            "customer_id": "CUST-005",
            "policy_id": "POL-005",
            "vehicle_type": "SUV",
            "vehicle_make": "Land Rover",
            "vehicle_model": "Defender",
            "age_band": "6-10 Years",
            "safety_features": ["ABS", "Airbags"],
            "years_no_claim": 3,
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["policy_id"] == "POL-005"
    assert data["calculated_premium"] == 390.0  # 500 * (1 - 0.35) * 1.2

# Test case 6: Invalid input - missing field
def test_calculate_premium_invalid_input(client: TestClient):
    response = client.post(
        "/api/v1/premium-calculation/",
        json={
            "customer_id": "CUST-006",
            # Missing policy_id
            "vehicle_type": "Sedan",
            "vehicle_make": "Toyota",
            "vehicle_model": "Camry",
            "age_band": "2-5 Years",
            "safety_features": [],
            "years_no_claim": 0,
        },
    )
    assert response.status_code == 422

# Test case 7: NCB tier not found
def test_calculate_premium_ncb_not_found(client: TestClient, session: Session):
    session.add(models.VehicleMultiplier(vehicle_type="Sedan", vehicle_make="Toyota", vehicle_model="Camry", age_band="2-5 Years", safety_features="", multiplier_value=1.0))
    session.commit()

    response = client.post(
        "/api/v1/premium-calculation/",
        json={
            "customer_id": "CUST-007",
            "policy_id": "POL-007",
            "vehicle_type": "Sedan",
            "vehicle_make": "Toyota",
            "vehicle_model": "Camry",
            "age_band": "2-5 Years",
            "safety_features": [],
            "years_no_claim": 99, # Assuming this tier doesn't exist
        },
    )
    assert response.status_code == 404
    assert "NCB tier not found" in response.text

# Test case 8: Vehicle multiplier not found
def test_calculate_premium_multiplier_not_found(client: TestClient, session: Session):
    session.add(models.NCBTier(years_no_claim=0, discount_percentage=0))
    session.commit()

    response = client.post(
        "/api/v1/premium-calculation/",
        json={
            "customer_id": "CUST-008",
            "policy_id": "POL-008",
            "vehicle_type": "Exotic", # Assuming this type doesn't exist
            "vehicle_make": "Pagani",
            "vehicle_model": "Huayra",
            "age_band": "0-1 Years",
            "safety_features": [],
            "years_no_claim": 0,
        },
    )
    assert response.status_code == 404
    assert "Vehicle multiplier not found" in response.text
