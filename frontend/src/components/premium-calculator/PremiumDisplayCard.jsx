import React from 'react';

const PremiumDisplayCard = ({ premium }) => {
  const baseFare = 420.00;
  const ncbDiscount = 84.00;
  const taxesAndFees = 164.00;

  return (
    <div className='bg-surface-container-lowest rounded-xl p-8 shadow-[0_12px_32px_-4px_rgba(25,28,30,0.06)] overflow-hidden relative'>
      <div className='absolute top-0 right-0 p-4'>
        <span className='material-symbols-outlined text-surface-container-high text-6xl select-none'>verified_user</span>
      </div>
      <div className='relative z-10'>
        <h3 className='text-[11px] uppercase tracking-[0.1em] font-bold text-secondary mb-6'>Calculated Premium</h3>
        <div className='flex flex-col gap-1 mb-8'>
          <label className='text-sm font-medium text-on-surface-variant'>Final Premium Amount</label>
          <div className='flex items-baseline gap-2'>
            <span className='text-5xl font-extrabold tracking-tighter text-primary font-display'>
              {premium ? `$${premium.toFixed(2)}` : '$0.00'}
            </span>
            <span className='text-sm text-secondary font-medium'>/annually</span>
          </div>
        </div>
        <div className='space-y-4 pt-6 border-t border-surface-container-high'>
          <div className='flex justify-between items-center text-sm'>
            <span className='text-secondary'>Base Fare</span>
            <span className='font-semibold'>${baseFare.toFixed(2)}</span>
          </div>
          <div className='flex justify-between items-center text-sm'>
            <span className='text-secondary'>NCB Discount (20%)</span>
            <span className='font-semibold text-tertiary'>-${ncbDiscount.toFixed(2)}</span>
          </div>
          <div className='flex justify-between items-center text-sm'>
            <span className='text-secondary'>Taxes & Fees</span>
            <span className='font-semibold'>${taxesAndFees.toFixed(2)}</span>
          </div>
        </div>
        <div className='mt-8 p-4 bg-tertiary/5 rounded-lg flex gap-3 items-center'>
          <span className='material-symbols-outlined text-tertiary' style={{fontVariationSettings: '\'FILL\' 1'}}>check_circle</span>
          <p className='text-xs font-medium text-on-tertiary-fixed-variant leading-relaxed'>
            Calculation verified based on Equitas Precision Ledger standards. Premium valid for 30 days.
          </p>
        </div>
      </div>
    </div>
  );
};

export default PremiumDisplayCard;
