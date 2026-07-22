import { useState, useEffect } from 'react';
import ProgressTracker from './ProgressTracker';
import axios from 'axios';

interface StatusResponse {
  job_id: string;
  status: string;
  progress: number; // e.g. 0 to 11
}

interface ResearchViewProps {
  jobId: string;
  onComplete?: (finalContent: string) => void;
}

function get_level(progress: number): number {
    if (progress <= 10) return 0;
    else if (progress <= 20) return 1;
    else if (progress <= 30) return 2;
    else if (progress <= 40) return 3;
    else if (progress <= 50) return 4;
    else if (progress <= 60) return 5;
    else if (progress <= 75) return 6;
    else if (progress <= 80) return 7;
    else if (progress <= 85) return 8;
    else if (progress <= 95) return 9;
    else return 10;
}

export default function ResearchView({ jobId, onComplete }: ResearchViewProps) {
  const [currentStage, setCurrentStage] = useState<number>(0);
  const [isCompleted, setIsCompleted] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!jobId || isCompleted) return;

    // Poll the status endpoint every 2 seconds
    const interval = setInterval(async () => {
      try {
        const response = await axios.get(`http://localhost:8000/api/v1/research/${jobId}/status`, {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('auth_token')}`
          }
        });

        const data: StatusResponse = response.data;

        // Assuming data.progress is the stage index (0 to 11)
        const stageIndex = get_level(data.progress);
        setCurrentStage(stageIndex);

        // Stop polling when completed or failed
        if (data.status === 'completed' || stageIndex >= 10) {
          setIsCompleted(true);
          clearInterval(interval);
          
          // Fetch final markdown result from backend
          const resultRes = await axios.get(`http://localhost:8000/api/v1/research/${jobId}/result`, {
            headers: {
              'Authorization': `Bearer ${localStorage.getItem('auth_token')}`
            }
          });

          // Pass final text back to parent/store
          if (onComplete) {
            onComplete(resultRes.data.final_markdown);
          }

        }
      } catch (err: any) {
        setError(err.message || 'Error fetching status');
        clearInterval(interval);
      }
    }, 2000);

    return () => clearInterval(interval);
  }, [jobId, isCompleted, onComplete]);

  return (
    <div className="p-4 space-y-4">
      {error && <p className="text-red-500 text-center">Error: {error}</p>}
      
      {/* Pass the calculated stage index to your ProgressTracker */}
      <ProgressTracker currentStage={currentStage} />
    </div>
  );
}