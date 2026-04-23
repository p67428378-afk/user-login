import React, { useState } from 'react';
import CustomerDetailsSection from './CustomerDetailsSection';
import VehicleDetailsSection from './VehicleDetailsSection';
import NoClaimBonusSection from './NoClaimBonusSection';
import PremiumDisplayCard from './PremiumDisplayCard';
import ErrorMessage from '../common/ErrorMessage';
import usePremiumCalculation from '../../hooks/usePremiumCalculation';

const PremiumCalculatorForm = () => {
  const [formData, setFormData] = useState({
    customer_id: '',
    policy_id: '',
    vehicle_type: 'Sedan',
    vehicle_make: '',
    vehicle_model: '',
    age_band: '0-1 Years',
    safety_features: [],
    years_no_claim: 0,
  });

  const { calculatedPremium, error, isLoading, calculatePremium } = usePremiumCalculation();

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    if (type === 'checkbox') {
      setFormData((prev) => ({
        ...prev,
        safety_features: checked
          ? [...prev.safety_features, value]
          : prev.safety_features.filter((feature) => feature !== value),
      }));
    } else {
      setFormData((prev) => ({ ...prev, [name]: value }));
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    calculatePremium(formData);
  };

  const handleReset = () => {
    setFormData({
      customer_id: '',
      policy_id: '',
      vehicle_type: 'Sedan',
      vehicle_make: '',
      vehicle_model: '',
      age_band: '0-1 Years',
      safety_features: [],
      years_no_claim: 0,
    });
  };

  return (
    <div className='grid grid-cols-1 lg:grid-cols-12 gap-12 items-start'>
      <div className='lg:col-span-7 space-y-16'>
        <form onSubmit={handleSubmit}>
          <CustomerDetailsSection formData={formData} handleChange={handleChange} />
          <VehicleDetailsSection formData={formData} handleChange={handleChange} />
          <NoClaimBonusSection formData={formData} handleChange={handleChange} />
          <div className='flex flex-col sm:flex-row items-center gap-4 pt-8'>
            <button type='submit' className='w-full sm:w-auto px-12 py-4 bg-blue-600 text-white font-bold rounded-lg shadow-lg hover:opacity-90 active:scale-[0.98] transition-all'>
              Calculate Premium
            </button>
            <button type='button' onClick={handleReset} className='w-full sm:w-auto px-12 py-4 text-blue-600 font-bold border-2 border-blue-600/10 rounded-lg hover:bg-gray-100 transition-all'>
              Reset Ledger
            </button>
          </div>
        </form>
      </div>
      <div className='lg:col-span-5 space-y-8 sticky top-32'>
        <PremiumDisplayCard premium={calculatedPremium} />
        {error && <ErrorMessage message={error} />}
      </div>
    </div>
  );
};

export default PremiumCalculatorForm;
