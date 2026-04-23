import React from 'react';
import Header from './Header';
import Footer from './Footer';

const AppLayout = ({ children }) => {
  return (
    <div className='text-on-background bg-surface min-h-screen flex flex-col'>
      <Header />
      <main className='flex-grow w-full max-w-7xl mx-auto px-8 py-12'>
        {children}
      </main>
      <Footer />
    </div>
  );
};

export default AppLayout;
