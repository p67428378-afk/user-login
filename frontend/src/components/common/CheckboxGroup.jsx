import React from 'react';

const CheckboxGroup = ({ label, name, options, selectedOptions, onChange }) => {
  return (
    <div className='space-y-4'>
      <label className='text-[11px] uppercase tracking-[0.05em] font-semibold text-secondary'>{label}</label>
      <div className='grid grid-cols-2 md:grid-cols-4 gap-4'>
        {options.map((option) => (
          <label key={option} className='flex items-center gap-3 p-4 bg-surface-container-low rounded-lg cursor-pointer hover:bg-surface-container-high transition-colors group'>
            <input
              type='checkbox'
              name={name}
              value={option}
              checked={selectedOptions.includes(option)}
              onChange={onChange}
              className='w-5 h-5 rounded border-outline-variant text-primary focus:ring-primary'
            />
            <span className='text-sm font-medium text-on-surface-variant group-hover:text-on-surface'>{option}</span>
          </label>
        ))}
      </div>
    </div>
  );
};

export default CheckboxGroup;
