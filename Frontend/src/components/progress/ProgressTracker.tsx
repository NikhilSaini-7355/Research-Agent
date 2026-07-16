import { motion } from 'framer-motion';
import { CheckCircle2, Circle, Loader2 } from 'lucide-react';

const STAGES = [
  "Topic Analysis",
  "Persona Generation",
  "Question Generation",
  "Parallel Web Search",
  "Content Extraction",
  "Embedding Generation",
  "Vector Database Indexing",
  "Research Synthesis",
  "Outline Generation",
  "Section Writing",
  "Fact Checking & Citations",
  "Formatting Output"
];

export default function ProgressTracker({ currentStage }: { currentStage: number }) {
  return (
    <div className="max-w-2xl w-full mx-auto space-y-6 bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl p-8 shadow-sm">
      <div className="flex justify-between items-center mb-6">
        <h3 className="font-semibold text-lg">Agent Workflow Active</h3>
        <span className="text-sm font-medium text-blue-600 dark:text-blue-400">
          {Math.round((currentStage / STAGES.length) * 100)}% Complete
        </span>
      </div>
      
      <div className="space-y-4">
        {STAGES.map((stage, index) => {
          const isCompleted = index < currentStage;
          const isCurrent = index === currentStage;
          
          return (
            <motion.div 
              key={stage}
              initial={{ opacity: 0, x: -10 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: index * 0.1 }}
              className="flex items-center gap-4"
            >
              {isCompleted ? (
                <CheckCircle2 className="h-5 w-5 text-green-500" />
              ) : isCurrent ? (
                <Loader2 className="h-5 w-5 text-blue-500 animate-spin" />
              ) : (
                <Circle className="h-5 w-5 text-zinc-300 dark:text-zinc-700" />
              )}
              <span className={isCompleted || isCurrent ? "text-zinc-900 dark:text-zinc-100 font-medium" : "text-zinc-400 dark:text-zinc-600"}>
                {stage}
              </span>
            </motion.div>
          );
        })}
      </div>
    </div>
  );
}