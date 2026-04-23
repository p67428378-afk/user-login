import React from 'react';

const Footer = () => {
  return (
    <footer className='w-full border-t border-slate-200/50 bg-[#f7f9fb] mt-auto'>
      <div className='flex flex-col md:flex-row justify-between items-center px-8 py-12 w-full max-w-7xl mx-auto gap-6'>
        <div className='flex flex-col gap-2'>
          <div className='text-sm font-bold text-slate-400'>EQUITAS PRECISION LEDGER</div>
          <p className='text-[11px] uppercase tracking-[0.05em] text-slate-500 max-w-md'>
            © 2024 Equitas Precision Ledger. All rights reserved. Licensed Insurance Provider.
          </p>
        </div>
        <nav className='flex gap-8'>
          <a className='text-[11px] uppercase tracking-[0.05em] text-slate-500 hover:text-blue-600 transition-colors font-bold' href='#'>Privacy Policy</a>
          <a className='text-[11px] uppercase tracking-[0.05em] text-slate-500 hover:text-blue-600 transition-colors font-bold' href='#'>Terms of Service</a>
          <a className='text-[11px] uppercase tracking-[0.05em] text-slate-500 hover:text-blue-600 transition-colors font-bold' href='#'>Security</a>
          <a className='text-[11px] uppercase tracking-[0.05em] text-slate-500 hover:text-blue-600 transition-colors font-bold' href='#'>Accessibility</a>
        </nav>
      </div>
    </footer>
  );
};

export default Footer;
