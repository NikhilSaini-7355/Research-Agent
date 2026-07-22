export type ResearchStatus = 'idle' | 'generating' | 'completed' | 'failed';

export interface ResearchStats {
  sources: number;
  wordCount: number;
  readingTime: number;
  confidenceScore: number;
  credibilityScore: number;
}

export interface ResearchSession {
  id: string;
  query: string;
  job_id: string;
  user_id?: string;
  date: string;
  status: ResearchStatus;
  content: string;
  stats?: ResearchStats;
  progressStage?: number;
}