import { motion } from 'framer-motion';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card } from '@/components/ui/card';
import { Network, Mail, Lock, Loader2 } from 'lucide-react';
import { useStore } from '../@/store/useStore';
import { useNavigate, Link } from 'react-router-dom';
import {useState} from 'react';
import axios from 'axios';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const login = useStore((state) => state.login);
  const navigate = useNavigate();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    // alert('Form intercept wrapper successfully caught event!');
  console.log('CRITICAL CHECK: Form submission actively working.');
    setIsLoading(true);
    setError(null);
    try{
      const body = {
        email,
        password
      }
      console.log('Attempting login with:', body);
      const response = await axios.post('http://localhost:8000/auth/login', body);
      console.log('Login successful:', response.data);
      localStorage.setItem('auth_token', response.data.access_token);
      const userData = await axios.get('http://localhost:8000/api/v1/me', {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('auth_token')}`
        }
      });
      console.log('User data:', userData.data);
      login(userData.data);
      navigate('/dashboard');
    }
    catch (error: any) {
      console.error('Login failed:', error);
      setError('Login failed. Please try again.');
    }
    finally {
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
            <h1 className="text-2xl font-bold tracking-tight">AI Research Studio</h1>
            <p className="text-sm text-zinc-500 dark:text-zinc-400 mt-2">Sign in to your workspace</p>
          </div>

          {/* Error Message Display */}
          {error && (
            <div className="mb-4 p-3 text-sm text-red-500 bg-red-50 dark:bg-red-950/30 border border-red-200 dark:border-red-900 rounded-md">
              {error}
            </div>
          )}

          <form onSubmit={handleLogin} className="space-y-4">
            <div className="space-y-2">
              <div className="relative">
                <Mail className="absolute left-3 top-3 h-4 w-4 text-zinc-400" />
                <Input type="email" placeholder="Email address" className="pl-10" required value={email} onChange={(e) => setEmail(e.target.value)} disabled={isLoading}/>
              </div>
            </div>
            <div className="space-y-2">
              <div className="relative">
                <Lock className="absolute left-3 top-3 h-4 w-4 text-zinc-400" />
                <Input type="password" placeholder="Password" className="pl-10" required value={password} onChange={(e) => setPassword(e.target.value)} disabled={isLoading} />
              </div>
            </div>
            
            <Button type="submit" className="w-full bg-blue-600 hover:bg-blue-700 text-white" disabled={isLoading}>
              {isLoading && <Loader2 className="h-4 w-4 animate-spin" />}
              {isLoading ? 'Signing in...' : 'Login to Workspace'}
            </Button>

            <div className="text-center mt-4">
              <p className="text-sm text-zinc-600 dark:text-zinc-400">
                Do not have an account?{' '}
                <Link to="/signup" className="text-blue-600 hover:underline font-medium">
                  Sign up
                </Link>
              </p>
            </div>
          </form>
        </Card>
      </motion.div>
    </div>
  );
}