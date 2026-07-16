import { create } from 'zustand';
import type { ResearchSession, ResearchStatus } from '../../types';
import { mockSessions } from './../../data/mockData';

interface AppState {
  user: { name: string; email: string } | null;
  sessions: ResearchSession[];
  activeSessionId: string | null;
  theme: 'light' | 'dark';
  login: () => void;
  logout: () => void;
  setActiveSession: (id: string | null) => void;
  toggleTheme: () => void;
  startNewResearch: (query: string, depth: string, style: string) => void;
}

export const useStore = create<AppState>((set) => ({
  user: { name: 'Dr. Jane Doe', email: 'jane@research.ai' },
  sessions: mockSessions,
  activeSessionId: null,
  theme: 'dark',
  
  login: () => set({ user: { name: 'Dr. Jane Doe', email: 'jane@research.ai' } }),
  logout: () => set({ user: null, activeSessionId: null }),
  setActiveSession: (id) => set({ activeSessionId: id }),
  toggleTheme: () => set((state) => ({ theme: state.theme === 'light' ? 'dark' : 'light' })),
  
  startNewResearch: (query) => {
    const newSession: ResearchSession = {
      id: Date.now().toString(),
      title: query,
      date: new Date().toISOString().split('T')[0],
      status: 'generating',
      content: '',
      progressStage: 0,
    };
    
    set((state) => ({
      sessions: [newSession, ...state.sessions],
      activeSessionId: newSession.id,
    }));

    // Simulate multi-agent backend progression
    let step = 0;
    const interval = setInterval(() => {
      step += 1;
      set((state) => ({
        sessions: state.sessions.map((s) =>
          s.id === newSession.id ? { ...s, progressStage: step } : s
        ),
      }));

      if (step >= 10) {
        clearInterval(interval);
        set((state) => ({
          sessions: state.sessions.map((s) =>
            s.id === newSession.id
              ? { ...s, status: 'completed', content: '# ' + query + '\n\nThis is the generated research report...' }
              : s
          ),
        }));
      }
    }, 2000);
  },
}));