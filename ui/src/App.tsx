import React from 'react';
import { TraceProvider } from './context/TraceProvider';
import { useTraceContext } from './context/TraceContext';
import { UploadView } from './components/upload/UploadView';
import { DashboardView } from './components/dashboard/DashboardView';

function AppContent() {
  const { state } = useTraceContext();

  return (
    <>
      {state.currentView === 'upload' && <UploadView />}
      {state.currentView === 'dashboard' && <DashboardView />}
      {/* Inspector and Comparison views will be added in later phases */}
      {state.currentView === 'inspector' && (
        <div style={{ padding: 48, textAlign: 'center', color: 'var(--text-secondary)' }}>
          Inspector view coming soon...
        </div>
      )}
      {state.currentView === 'comparison' && (
        <div style={{ padding: 48, textAlign: 'center', color: 'var(--text-secondary)' }}>
          Comparison view coming soon...
        </div>
      )}
    </>
  );
}

function App() {
  return (
    <TraceProvider>
      <AppContent />
    </TraceProvider>
  );
}

export default App;
