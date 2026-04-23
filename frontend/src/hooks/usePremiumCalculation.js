import { useState } from 'react';
import { calculatePremium as apiCalculatePremium } from '../services/api';

const usePremiumCalculation = () => {
  const [calculatedPremium, setCalculatedPremium] = useState(null);
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const calculatePremium = async (formData) => {
    setIsLoading(true);
    setError(null);
    try {
      const response = await apiCalculatePremium(formData);
      setCalculatedPremium(response.data.calculated_premium);
    } catch (err) {
      setError(err.response?.data?.detail || 'An unexpected error occurred.');
    }
    setIsLoading(false);
  };

  return { calculatedPremium, error, isLoading, calculatePremium };
};

export default usePremiumCalculation;
