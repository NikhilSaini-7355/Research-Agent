import { ScrollArea } from '@/components/ui/scroll-area';
import { Button } from '@/components/ui/button';
import { Plus, Network, FileText, Settings, LogOut, Moon, Sun } from 'lucide-react';
import { useStore } from '@/store/useStore';
import { clsx } from 'clsx';

export default function Sidebar() {
  const { sessions, activeSessionId, setActiveSession, user, logout, theme, toggleTheme } = useStore();

  return (
    <aside className="w-72 border-r border-zinc-200 dark:border-zinc-800 bg-zinc-100/50 dark:bg-zinc-900/50 flex flex-col h-full hidden md:flex">
      <div className="p-4 flex items-center gap-3">
        <div className="h-8 w-8 bg-blue-600 rounded-lg flex items-center justify-center">
          <Network className="text-white h-4 w-4" />
        </div>
        <span className="font-semibold text-lg">Research Studio</span>
      </div>

      <div className="px-4 py-2">
        <Button 
          onClick={() => setActiveSession(null)} 
          className="w-full justify-start gap-2 bg-blue-600 hover:bg-blue-700 text-white"
        >
          <Plus className="h-4 w-4" /> New Research
        </Button>
      </div>

      <div className="px-4 py-2 mt-4">
        <h3 className="text-xs font-semibold text-zinc-500 uppercase tracking-wider mb-2">Recent Research</h3>
      </div>
      
      <ScrollArea className="flex-1 px-2">
        <div className="space-y-1">
          {sessions.map((session) => (
            <button
              key={session.id}
              onClick={() => setActiveSession(session.id)}
              className={clsx(
                "w-full text-left px-3 py-2 rounded-md text-sm flex items-center gap-3 transition-colors",
                activeSessionId === session.id 
                  ? "bg-zinc-200 dark:bg-zinc-800 text-zinc-900 dark:text-zinc-50 font-medium" 
                  : "text-zinc-600 dark:text-zinc-400 hover:bg-zinc-200/50 dark:hover:bg-zinc-800/50"
              )}
            >
              <FileText className="h-4 w-4 shrink-0" />
              <span className="truncate">{session.title}</span>
            </button>
          ))}
        </div>
      </ScrollArea>

      <div className="p-4 border-t border-zinc-200 dark:border-zinc-800">
        <div className="flex items-center gap-3 mb-4">
          <div className="h-9 w-9 rounded-full bg-gradient-to-tr from-blue-500 to-purple-500 flex items-center justify-center text-white font-medium">
            {user?.name.charAt(0)}
          </div>
          <div className="flex-1 overflow-hidden">
            <p className="text-sm font-medium truncate">{user?.name}</p>
            <p className="text-xs text-zinc-500 truncate">{user?.email}</p>
          </div>
        </div>
        
        <div className="flex gap-1">
          <Button variant="ghost" size="icon" onClick={toggleTheme} className="h-8 w-8">
            {theme === 'dark' ? <Sun className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
          </Button>
          <Button variant="ghost" size="icon" className="h-8 w-8">
            <Settings className="h-4 w-4" />
          </Button>
          <Button variant="ghost" size="icon" onClick={logout} className="h-8 w-8 ml-auto text-red-500 hover:text-red-600 hover:bg-red-50 dark:hover:bg-red-950">
            <LogOut className="h-4 w-4" />
          </Button>
        </div>
      </div>
    </aside>
  );
}