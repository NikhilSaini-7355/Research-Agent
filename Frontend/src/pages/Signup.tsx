import { useState } from 'react';
import { motion } from 'framer-motion';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card } from '@/components/ui/card';
import { Network, Mail, Lock, User, Loader2 } from 'lucide-react';
import { useStore } from '../@/store/useStore';
import { useNavigate, Link } from 'react-router-dom';
import axios from 'axios';

export default function Signup() {
  const [firstname, setFirstname] = useState('');
  const [lastname, setLastname] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const login = useStore((state) => state.login);
  const navigate = useNavigate();

  const handleSignup = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    setError(null);

    try {
      const body = {
        firstname,
        lastname,
        email,
        password
      };
      
      console.log('Attempting registration with:', { firstname, lastname, email });
      
      // 1. Submit signup payload to backend
      const response = await axios.post('http://localhost:8000/auth/signup', body);
      console.log('Signup successful:', response.data);
      
      // 2. Automatically log the user in if backend returns an access token on registration
      // If your backend only returns a success message, redirect to '/login' instead.
      if (response.data.access_token) {
        localStorage.setItem('auth_token', response.data.access_token);
        
        // Fetch profile payload for the newly created workspace user
        const userData = await axios.get('http://localhost:8000/api/v1/me', {
          headers: {
            'Authorization': `Bearer ${response.data.access_token}`
          }
        });
        
        login(userData.data);
        navigate('/dashboard');
      } else {
        // Fallback if your API requires users to manually log in after signing up
        navigate('/login');
      }
    } catch (error: any) {
      console.error('Signup failed:', error);
      // Fallback to custom message if backend message is missing
      const serverMessage = error.response?.data?.detail || error.response?.data?.message;
      setError(serverMessage || 'Registration failed. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-zinc-100 to-zinc-200 dark:from-zinc-900 dark:to-zinc-950 p-4">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <Card className="w-full max-w-md p-8 shadow-xl border-zinc-200 dark:border-zinc-800 bg-white/80 dark:bg-zinc-900/80 backdrop-blur-xl">
          <div className="flex flex-col items-center mb-8">
            <div className="h-12 w-12 bg-blue-600 rounded-xl flex items-center justify-center mb-4">
              <Network className="text-white h-6 w-6" />
            </div>
            <h1 className="text-2xl font-bold tracking-tight">Create Workspace</h1>
            <p className="text-sm text-zinc-500 dark:text-zinc-400 mt-2">Get started with AI Research Studio</p>
          </div>

          {/* Error Message Display */}
          {error && (
            <div className="mb-4 p-3 text-sm text-red-500 bg-red-50 dark:bg-red-950/30 border border-red-200 dark:border-red-900 rounded-md">
              {error}
            </div>
          )}

          <form onSubmit={handleSignup} className="space-y-4">
            {/* Full Name Input field */}
            <div className="space-y-2">
              <div className="relative">
                <User className="absolute left-3 top-3 h-4 w-4 text-zinc-400" />
                <Input 
                  type="text" 
                  placeholder="First name" 
                  className="pl-10" 
                  required 
                  value={firstname} 
                  onChange={(e) => setFirstname(e.target.value)} 
                  disabled={isLoading}
                />
              </div>
            </div>

            <div className="space-y-2">
              <div className="relative">
                <User className="absolute left-3 top-3 h-4 w-4 text-zinc-400" />
                <Input 
                  type="text" 
                  placeholder="Last name" 
                  className="pl-10" 
                  required 
                  value={lastname} 
                  onChange={(e) => setLastname(e.target.value)} 
                  disabled={isLoading}
                />
              </div>
            </div>

            {/* Email Input Field */}
            <div className="space-y-2">
              <div className="relative">
                <Mail className="absolute left-3 top-3 h-4 w-4 text-zinc-400" />
                <Input 
                  type="email" 
                  placeholder="Email address" 
                  className="pl-10" 
                  required 
                  value={email} 
                  onChange={(e) => setEmail(e.target.value)} 
                  disabled={isLoading}
                />
              </div>
            </div>

            {/* Password Input Field */}
            <div className="space-y-2">
              <div className="relative">
                <Lock className="absolute left-3 top-3 h-4 w-4 text-zinc-400" />
                <Input 
                  type="password" 
                  placeholder="Create password" 
                  className="pl-10" 
                  required 
                  value={password} 
                  onChange={(e) => setPassword(e.target.value)} 
                  disabled={isLoading} 
                />
              </div>
            </div>
            
            <Button type="submit" className="w-full bg-blue-600 hover:bg-blue-700 text-white flex items-center justify-center gap-2" disabled={isLoading}>
              {isLoading && <Loader2 className="h-4 w-4 animate-spin" />}
              {isLoading ? 'Creating account...' : 'Register Account'}
            </Button>
            
            <div className="text-center mt-4">
              <p className="text-sm text-zinc-600 dark:text-zinc-400">
                Already have an account?{' '}
                <Link to="/login" className="text-blue-600 hover:underline font-medium">
                  Sign in
                </Link>
              </p>
            </div>
          </form>
        </Card>
      </motion.div>
    </div>
  );
}