import React from 'react';

const InputField = ({ label, name, value, onChange, placeholder, type = 'text' }) => {
  return (
    <div className='space-y-2'>
      <label className='text-[11px] uppercase tracking-[0.05em] font-semibold text-secondary'>{label}</label>
      <input
        type={type}
        name={name}
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        className='w-full bg-surface-container-highest border-none rounded-lg p-4 text-sm focus:ring-2 focus:ring-surface-tint focus:bg-surface-container-lowest transition-all'
      />
    </div>
  );
};

export default InputField;
