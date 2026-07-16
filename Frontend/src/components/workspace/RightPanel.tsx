import { useStore } from '@/store/useStore';
import { FileSearch, BookOpen, ShieldCheck, Clock } from 'lucide-react';
import { Separator } from '@/components/ui/separator';

export default function RightPanel() {
  const { activeSessionId, sessions } = useStore();
  const session = sessions.find(s => s.id === activeSessionId);

  if (!session || session.status !== 'completed') return null;

  // Mock stats if none exist
  const stats = session.stats || {
    sources: 24,
    wordCount: 3150,
    readingTime: 12,
    confidenceScore: 94,
    credibilityScore: 8.9,
  };

  return (
    <aside className="w-72 border-l border-zinc-200 dark:border-zinc-800 bg-zinc-50 dark:bg-zinc-900/30 p-6 hidden lg:block overflow-y-auto">
      <h3 className="font-semibold text-sm uppercase tracking-wider text-zinc-500 mb-6">Research Intelligence</h3>
      
      <div className="space-y-6">
        <div>
          <div className="flex items-center gap-2 mb-2 text-zinc-600 dark:text-zinc-300">
            <ShieldCheck className="h-4 w-4" />
            <span className="text-sm font-medium">Credibility Score</span>
          </div>
          <div className="flex items-end gap-1">
            <span className="text-3xl font-bold text-green-600 dark:text-green-400">{stats.credibilityScore}</span>
            <span className="text-sm text-zinc-500 mb-1">/ 10</span>
          </div>
        </div>

        <Separator />

        <div className="grid grid-cols-2 gap-4">
          <div>
            <div className="flex items-center gap-2 mb-1 text-zinc-500">
              <FileSearch className="h-4 w-4" />
              <span className="text-xs">Sources</span>
            </div>
            <span className="font-semibold">{stats.sources}</span>
          </div>
          <div>
            <div className="flex items-center gap-2 mb-1 text-zinc-500">
              <BookOpen className="h-4 w-4" />
              <span className="text-xs">Words</span>
            </div>
            <span className="font-semibold">{stats.wordCount.toLocaleString()}</span>
          </div>
          <div>
            <div className="flex items-center gap-2 mb-1 text-zinc-500">
              <Clock className="h-4 w-4" />
              <span className="text-xs">Read Time</span>
            </div>
            <span className="font-semibold">{stats.readingTime} min</span>
          </div>
        </div>
      </div>
    </aside>
  );
}