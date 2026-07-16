import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { useStore } from './@/store/useStore';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import { useEffect } from 'react';

export default function App() {
  const theme = useStore((state) => state.theme);
  const user = useStore((state) => state.user);

  useEffect(() => {
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [theme]);

  return (
    <BrowserRouter>
      <div className="min-h-screen bg-zinc-50 dark:bg-zinc-950 text-zinc-900 dark:text-zinc-50 font-sans transition-colors duration-300">
        <Routes>
          <Route path="/login" element={!user ? <Login /> : <Navigate to="/dashboard" />} />
          <Route path="/dashboard" element={user ? <Dashboard /> : <Navigate to="/login" />} />
          <Route path="*" element={<Navigate to={user ? "/dashboard" : "/login"} />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}