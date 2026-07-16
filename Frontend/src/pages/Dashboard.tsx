import Sidebar from './../components/sidebar/Sidebar';
import MainWorkspace from './../components/workspace/MainWorkspace';
import RightPanel from './../components/workspace/RightPanel';
import { useStore } from '@/store/useStore';

export default function Dashboard() {
  const activeSessionId = useStore((state) => state.activeSessionId);

  return (
    <div className="flex h-screen overflow-hidden bg-zinc-50 dark:bg-zinc-950">
      <Sidebar />
      <main className="flex-1 flex overflow-hidden">
        <MainWorkspace />
        {activeSessionId && <RightPanel />}
      </main>
    </div>
  );
}