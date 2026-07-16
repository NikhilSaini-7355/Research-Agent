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
  title: string;
  date: string;
  status: ResearchStatus;
  content: string;
  stats?: ResearchStats;
  progressStage?: number;
}