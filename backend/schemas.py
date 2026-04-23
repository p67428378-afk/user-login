
from pydantic import BaseModel
from typing import List, Optional

class PolicyBase(BaseModel):
    customer_id: str
    policy_id: str
    vehicle_type: str
    vehicle_make: str
    vehicle_model: str
    age_band: str
    safety_features: List[str]
    years_no_claim: int

class PolicyCreate(PolicyBase):
    pass

class Policy(PolicyBase):
    id: int
    calculated_premium: float

    class Config:
        from_attributes = True

class PremiumCalculationRequest(BaseModel):
    customer_id: str
    policy_id: str
    vehicle_type: str
    vehicle_make: str
    vehicle_model: str
    age_band: str
    safety_features: List[str]
    years_no_claim: int

class PremiumCalculationResponse(BaseModel):
    policy_id: str
    calculated_premium: float
