import React from 'react';
import InputField from '../common/InputField';
import SelectField from '../common/SelectField';
import CheckboxGroup from '../common/CheckboxGroup';

const VehicleDetailsSection = ({ formData, handleChange }) => {
  const vehicleTypes = ['Sedan', 'SUV', 'Hatchback', 'Sports Car', 'Truck'];
  const ageBands = ['0-1 Years', '2-5 Years', '6-10 Years', '10+ Years'];
  const safetyFeatures = ['ABS', 'Airbags', 'ADAS', 'Sensors'];

  return (
    <section>
      <div className='flex items-center gap-3 mb-8'>
        <span className='text-[11px] uppercase tracking-[0.05em] font-bold text-primary bg-primary/10 px-2 py-1 rounded'>Step 02</span>
        <h2 className='text-2xl font-bold tracking-[-0.02em] text-on-surface'>Vehicle Specification</h2>
      </div>
      <div className='grid grid-cols-1 md:grid-cols-2 gap-6 mb-8'>
        <SelectField
          label='Vehicle Type'
          name='vehicle_type'
          value={formData.vehicle_type}
          onChange={handleChange}
          options={vehicleTypes}
        />
        <SelectField
          label='Vehicle Age Band'
          name='age_band'
          value={formData.age_band}
          onChange={handleChange}
          options={ageBands}
        />
        <InputField
          label='Make'
          name='vehicle_make'
          value={formData.vehicle_make}
          onChange={handleChange}
          placeholder='e.g. BMW'
        />
        <InputField
          label='Model'
          name='vehicle_model'
          value={formData.vehicle_model}
          onChange={handleChange}
          placeholder='e.g. M3 Competition'
        />
      </div>
      <CheckboxGroup
        label='Advanced Safety Features'
        name='safety_features'
        options={safetyFeatures}
        selectedOptions={formData.safety_features}
        onChange={handleChange}
      />
    </section>
  );
};

export default VehicleDetailsSection;
