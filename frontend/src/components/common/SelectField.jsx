import React from 'react';

const SelectField = ({ label, name, value, onChange, options, optionValues }) => {
  return (
    <div className='space-y-2'>
      <label className='text-[11px] uppercase tracking-[0.05em] font-semibold text-secondary'>{label}</label>
      <select
        name={name}
        value={value}
        onChange={onChange}
        className='w-full bg-surface-container-highest border-none rounded-lg p-4 text-sm focus:ring-2 focus:ring-surface-tint focus:bg-surface-container-lowest transition-all appearance-none'
      >
        {options.map((option, index) => (
          <option key={option} value={optionValues ? optionValues[index] : option}>
            {option}
          </option>
        ))}
      </select>
    </div>
  );
};

export default SelectField;
