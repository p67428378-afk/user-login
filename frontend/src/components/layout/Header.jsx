import React from 'react';

const Header = () => {
  return (
    <header className='sticky top-0 w-full z-50 bg-[#f7f9fb]/80 backdrop-blur-xl shadow-[0_12px_32px_-4px_rgba(25,28,30,0.06)]'>
      <div className='flex justify-between items-center w-full px-8 py-4 max-w-[1440px] mx-auto'>
        <div className='text-xl font-extrabold tracking-tighter text-[#0058be] font-headline'>
          Vehicle Insurance Premium Calculator
        </div>
        <nav className='hidden md:flex items-center space-x-8 text-sm font-medium tracking-[-0.02em]'>
          <a className='text-[#0058be] border-b-2 border-[#0058be] pb-1' href='#'>Calculators</a>
          <a className='text-slate-500 hover:text-slate-900 transition-colors duration-200' href='#'>Claims</a>
          <a className='text-slate-500 hover:text-slate-900 transition-colors duration-200' href='#'>Support</a>
          <a className='text-slate-500 hover:text-slate-900 transition-colors duration-200' href='#'>Policy</a>
        </nav>
        <div className='flex items-center gap-4'>
          <button className='p-2 text-slate-500 hover:bg-slate-100 rounded-full transition-colors'>
            <span className='material-symbols-outlined'>notifications</span>
          </button>
          <button className='flex items-center gap-2 px-4 py-2 text-sm font-medium text-[#0058be] bg-white rounded-lg shadow-sm border border-slate-200 hover:bg-slate-50 transition-all'>
            <span className='material-symbols-outlined' style={{fontVariationSettings: '\'FILL\' 1'}}>account_circle</span>
            Sign In
          </button>
        </div>
      </div>
    </header>
  );
};

export default Header;
