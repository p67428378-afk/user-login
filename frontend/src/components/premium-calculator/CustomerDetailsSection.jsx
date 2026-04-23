import React from 'react';
import InputField from '../common/InputField';

const CustomerDetailsSection = ({ formData, handleChange }) => {
  return (
    <section>
      <div className='flex items-center gap-3 mb-8'>
        <span className='text-[11px] uppercase tracking-[0.05em] font-bold text-primary bg-primary/10 px-2 py-1 rounded'>Step 01</span>
        <h2 className='text-2xl font-bold tracking-[-0.02em] text-on-surface'>Customer Identity</h2>
      </div>
      <div className='grid grid-cols-1 md:grid-cols-2 gap-6'>
        <InputField
          label='Customer ID'
          name='customer_id'
          value={formData.customer_id}
          onChange={handleChange}
          placeholder='e.g. EQ-98234'
        />
        <InputField
          label='Policy ID'
          name='policy_id'
          value={formData.policy_id}
          onChange={handleChange}
          placeholder='e.g. POL-55621'
        />
      </div>
    </section>
  );
};

export default CustomerDetailsSection;
