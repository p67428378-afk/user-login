
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Policy(Base):
    __tablename__ = "policies"

    id = Column(Integer, primary_key=True, index=True)
    policy_id = Column(String, unique=True, index=True)
    customer_id = Column(String)
    vehicle_type = Column(String)
    vehicle_make = Column(String)
    vehicle_model = Column(String)
    age_band = Column(String)
    safety_features = Column(String)
    years_no_claim = Column(Integer)
    calculated_premium = Column(Float)

class NCBTier(Base):
    __tablename__ = "ncb_tiers"

    id = Column(Integer, primary_key=True, index=True)
    years_no_claim = Column(Integer, unique=True)
    discount_percentage = Column(Float)

class VehicleMultiplier(Base):
    __tablename__ = "vehicle_multipliers"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_type = Column(String)
    vehicle_make = Column(String)
    vehicle_model = Column(String)
    age_band = Column(String)
    safety_features = Column(String)
    multiplier_value = Column(Float)
