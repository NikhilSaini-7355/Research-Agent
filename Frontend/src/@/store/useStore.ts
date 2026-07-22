import { create } from 'zustand';
import type { ResearchSession, ResearchStatus } from '../../types';
import axios from 'axios';

interface AppState {
  user: { id: string; name: string; email: string } | null;
  sessions: ResearchSession[];
  activeSessionId: string | null;
  theme: 'light' | 'dark';
  login: (userData: { id:string; name: string; email: string }) => void;
  logout: () => void;
  setActiveSession: (id: string | null) => void;
  toggleTheme: () => void;
  setSessions: (sessions: ResearchSession[]) => void; // 1. Added setSessions
  fetchSessions: () => Promise<void>;                // 2. Added fetchSessions
  startNewResearch: (query: string, id: string, jobId: string) => void;
  completeResearch: (id: string, finalContent: string) => void;
  fetchSessionContent: (sessionId: string) => Promise<void>;
}

export const useStore = create<AppState>((set, get) => ({
  user: null,
  sessions: [],
  activeSessionId: null,
  theme: 'dark',
  login: (userData) =>{ 
    set({ user: userData })
    get().fetchSessions();
  },
  logout: () => {
    localStorage.removeItem('auth_token'); // Clean up persistent token
    set({ user: null, activeSessionId: null, sessions:[] });
  },
  setActiveSession: (id) => {
    set({ activeSessionId: id })
    if (id) {
      get().fetchSessionContent(id); //Fetch content whenever active session changes
    }  
  },
  toggleTheme: () => set((state) => ({ theme: state.theme === 'light' ? 'dark' : 'light' })),
  setSessions: (sessions)=>set({sessions}),
  fetchSessions: async ()=>{
    const token = localStorage.getItem('auth_token');
    if (!token) return;
    console.log("Token check:", token);
    try {
      const response = await axios.get(`http://localhost:8000/api/v1/projects`,{headers: {
          Authorization: `Bearer ${token}`,
        },});
      const projectsList = Array.isArray(response.data) ? response.data : [];
      const userSessions: ResearchSession[] = projectsList.map((item: any) => ({
      id: item.id,
      query: item.topic,                          // Backend 'topic' -> Frontend 'query'
      job_id: item.job_id ?? item.id,  // issue here                    
      user_id: item.user_id,
      date: item.created_at.split('T')[0],        // Formats "2026-07-22T05:23:54..." to "2026-07-22"
      status: (item.status=='CREATED')?'completed':'generating',       
      content: '',                                // Default empty content until fetched individually
      progressStage: 0,
    }));
      set({ sessions: userSessions });
    } catch (error) {
      console.error('Failed to fetch user sessions:', error);
    }
  },
  startNewResearch: (query,id,jobId) => {
    const user = get().user;
    const newSession: ResearchSession = {
      id: id,
      job_id: jobId,
      user_id: user?.id,
      query: query,
      date: new Date().toISOString().split('T')[0],
      status: 'generating',
      content: '',
      progressStage: 0,
    };
    
    set((state) => ({
      sessions: [newSession, ...state.sessions],
      activeSessionId: newSession.id,
    }));
  },
  // Inside your useStore definition:
  completeResearch: (id, finalContent) => set((state) => ({
    sessions: state.sessions.map((s) => 
      s.id === id 
        ? { ...s, status: 'completed', content: finalContent } 
        : s
    )
  })),
  fetchSessionContent: async (sessionId: string) => {
    const session = get().sessions.find((s) => s.id === sessionId);
    
    // Skip fetching if session content already exists or session doesn't exist
    if (!session || session.content) return;

    const token = localStorage.getItem('auth_token');
    if (!token) return;

    try {
      // Endpoint to get full job details / final report content
      const response = await axios.get(`http://localhost:8000/api/v1/research/${session.job_id}/result`, {
        headers: { Authorization: `Bearer ${token}` },
      });

      // Adjust `response.data.result` or `response.data.content` based on your exact FastAPI response structure
      const finalReportText = response.data.final_markdown || '';

      set((state) => ({
        sessions: state.sessions.map((s) =>
          s.id === sessionId ? { ...s, content: finalReportText } : s
        ),
      }));
    } catch (error) {
      console.error(`Failed to fetch report content for session ${sessionId}:`, error);
    }
  }
}));
