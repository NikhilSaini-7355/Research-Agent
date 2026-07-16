import { useStore } from '@/store/useStore';
import { useState } from 'react';
import { Search, Sparkles } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import MarkdownViewer from '../markdown/MarkdownViewer';
import ProgressTracker from '../progress/ProgressTracker';
import { motion } from 'framer-motion';

export default function MainWorkspace() {
  const { activeSessionId, sessions, startNewResearch } = useStore();
  const [query, setQuery] = useState('');

  const activeSession = sessions.find(s => s.id === activeSessionId);

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (query.trim()) {
      startNewResearch(query, 'Advanced', 'Academic');
      setQuery('');
    }
  };

  // State 1: Empty / New Search
  if (!activeSessionId || !activeSession) {
    return (
      <div className="flex-1 flex flex-col items-center justify-center p-8">
        <motion.div 
          initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }}
          className="max-w-2xl w-full space-y-8 text-center"
        >
          <div className="space-y-4">
            <div className="mx-auto w-16 h-16 bg-blue-100 dark:bg-blue-900/30 rounded-2xl flex items-center justify-center mb-6">
              <Sparkles className="h-8 w-8 text-blue-600 dark:text-blue-400" />
            </div>
            <h2 className="text-3xl font-bold tracking-tight">What would you like to research?</h2>
            <p className="text-zinc-500 dark:text-zinc-400">Launch a multi-agent workflow to synthesize complex topics.</p>
          </div>

          <form onSubmit={handleSearch} className="relative flex items-center w-full shadow-lg rounded-full bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 p-2 focus-within:ring-2 focus-within:ring-blue-500 transition-all">
            <Search className="absolute left-6 h-5 w-5 text-zinc-400" />
            <Input 
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="e.g., The Impact of CRISPR Gene Editing on Cardiovascular Therapeutics..." 
              className="border-0 focus-visible:ring-0 pl-14 pr-32 h-12 text-base bg-transparent"
            />
            <Button type="submit" className="absolute right-2 rounded-full px-6 bg-blue-600 hover:bg-blue-700">
              Generate
            </Button>
          </form>
        </motion.div>
      </div>
    );
  }

  // State 2: Generating
  if (activeSession.status === 'generating') {
    return (
      <div className="flex-1 flex flex-col p-8 overflow-hidden">
        <h2 className="text-2xl font-bold mb-8">{activeSession.title}</h2>
        <ProgressTracker currentStage={activeSession.progressStage || 0} />
      </div>
    );
  }

  // State 3: Completed Markdown View
  return (
    <div className="flex-1 flex flex-col bg-white dark:bg-zinc-950">
      <div className="h-14 border-b border-zinc-200 dark:border-zinc-800 flex items-center justify-between px-6 bg-white/80 dark:bg-zinc-950/80 backdrop-blur-md sticky top-0 z-10">
        <h2 className="font-semibold truncate pr-4">{activeSession.title}</h2>
        <div className="flex gap-2">
          <Button variant="outline" size="sm">Export PDF</Button>
          <Button variant="outline" size="sm">Share</Button>
        </div>
      </div>
      <div className="flex-1 overflow-y-auto">
        <div className="max-w-4xl mx-auto py-12 px-8">
          <MarkdownViewer content={activeSession.content} />
        </div>
      </div>
    </div>
  );
}