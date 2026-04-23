import React from 'react';

const ErrorMessage = ({ message }) => {
  return (
    <div className='p-4 border border-error/20 bg-error-container/30 rounded-lg flex gap-3 items-start'>
      <span className='material-symbols-outlined text-error'>info</span>
      <div>
        <p className='text-xs font-bold text-on-error-container uppercase tracking-wider'>System Notice</p>
        <p className='text-sm text-on-error-container/80'>{message}</p>
      </div>
    </div>
  );
};

export default ErrorMessage;
