import React from 'react';
import SelectField from '../common/SelectField';

const NoClaimBonusSection = ({ formData, handleChange }) => {
  const ncbYears = [0, 1, 2, 3, 4, 5];

  return (
    <section>
      <div className='flex items-center gap-3 mb-8'>
        <span className='text-[11px] uppercase tracking-[0.05em] font-bold text-primary bg-primary/10 px-2 py-1 rounded'>Step 03</span>
        <h2 className='text-2xl font-bold tracking-[-0.02em] text-on-surface'>No-Claim Bonus (NCB)</h2>
      </div>
      <div className='space-y-2 max-w-xs'>
        <SelectField
          label='Years of No Claims'
          name='years_no_claim'
          value={formData.years_no_claim}
          onChange={handleChange}
          options={ncbYears.map(year => `${year} Year${year === 1 ? '' : 's'}`)}
          optionValues={ncbYears}
        />
      </div>
    </section>
  );
};

export default NoClaimBonusSection;
