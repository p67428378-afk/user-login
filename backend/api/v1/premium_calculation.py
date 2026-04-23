
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend import crud, schemas
from backend.database import get_db

router = APIRouter()

BASE_PREMIUM = 500.0

@router.post("/", response_model=schemas.PremiumCalculationResponse)
def calculate_premium(request: schemas.PremiumCalculationRequest, db: Session = Depends(get_db)):
    # 1. Get NCB discount
    ncb_tier = crud.get_ncb_tier(db, request.years_no_claim)
    if not ncb_tier:
        raise HTTPException(status_code=404, detail="NCB tier not found")
    ncb_discount = ncb_tier.discount_percentage

    # 2. Get vehicle multiplier
    vehicle_multiplier = crud.get_vehicle_multiplier(
        db,
        vehicle_type=request.vehicle_type,
        vehicle_make=request.vehicle_make,
        vehicle_model=request.vehicle_model,
        age_band=request.age_band,
        safety_features=request.safety_features,
    )
    if not vehicle_multiplier:
        raise HTTPException(status_code=404, detail="Vehicle multiplier not found")
    multiplier = vehicle_multiplier.multiplier_value

    # 3. Calculate premium
    premium_before_multiplier = BASE_PREMIUM * (1 - ncb_discount)
    calculated_premium = premium_before_multiplier * multiplier

    # 4. Create policy record
    policy_data = schemas.PolicyCreate(**request.dict())
    crud.create_policy(db, policy=policy_data, calculated_premium=calculated_premium)

    return schemas.PremiumCalculationResponse(
        policy_id=request.policy_id,
        calculated_premium=round(calculated_premium, 2)
    )
