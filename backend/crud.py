
from sqlalchemy.orm import Session
from . import models, schemas

def get_policy(db: Session, policy_id: str):
    return db.query(models.Policy).filter(models.Policy.policy_id == policy_id).first()

def create_policy(db: Session, policy: schemas.PolicyCreate, calculated_premium: float):
    db_policy = models.Policy(
        customer_id=policy.customer_id,
        policy_id=policy.policy_id,
        vehicle_type=policy.vehicle_type,
        vehicle_make=policy.vehicle_make,
        vehicle_model=policy.vehicle_model,
        age_band=policy.age_band,
        safety_features=",".join(policy.safety_features),
        years_no_claim=policy.years_no_claim,
        calculated_premium=calculated_premium
    )
    db.add(db_policy)
    db.commit()
    db.refresh(db_policy)
    return db_policy

def get_ncb_tier(db: Session, years_no_claim: int):
    # Get the highest tier that is less than or equal to the years of no claim
    return db.query(models.NCBTier).filter(models.NCBTier.years_no_claim <= years_no_claim).order_by(models.NCBTier.years_no_claim.desc()).first()

def get_vehicle_multiplier(db: Session, vehicle_type: str, vehicle_make: str, vehicle_model: str, age_band: str, safety_features: list[str]):
    # This is a simplified lookup. A real implementation might have more complex logic.
    # This example will look for a generic multiplier for the vehicle type if a specific one is not found.
    safety_features_str = ",".join(sorted(safety_features))
    multiplier = db.query(models.VehicleMultiplier).filter(
        models.VehicleMultiplier.vehicle_type == vehicle_type,
        models.VehicleMultiplier.vehicle_make == vehicle_make,
        models.VehicleMultiplier.vehicle_model == vehicle_model,
        models.VehicleMultiplier.age_band == age_band,
        models.VehicleMultiplier.safety_features == safety_features_str
    ).first()

    if not multiplier:
        multiplier = db.query(models.VehicleMultiplier).filter(
            models.VehicleMultiplier.vehicle_type == vehicle_type,
            models.VehicleMultiplier.vehicle_make == vehicle_make,
            models.VehicleMultiplier.vehicle_model == vehicle_model,
            models.VehicleMultiplier.age_band == age_band,
            models.VehicleMultiplier.safety_features == ""
        ).first()
    
    if not multiplier:
        multiplier = db.query(models.VehicleMultiplier).filter(
            models.VehicleMultiplier.vehicle_type == vehicle_type,
            models.VehicleMultiplier.vehicle_make == vehicle_make,
            models.VehicleMultiplier.vehicle_model == vehicle_model,
            models.VehicleMultiplier.safety_features == ""
        ).first()

    if not multiplier:
        multiplier = db.query(models.VehicleMultiplier).filter(
            models.VehicleMultiplier.vehicle_type == vehicle_type,
            models.VehicleMultiplier.safety_features == ""
        ).first()

    return multiplier
