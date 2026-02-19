import React from 'react';
import { Button, Select, Slider, Space } from 'antd';
import { css } from '@emotion/react';
import { Play, Settings } from 'lucide-react';
import { FileDropZone } from './FileDropZone';
import { MetricSelector } from './MetricSelector';
import { useTraceContext } from '../../context/TraceContext';

const uploadViewStyle = css`
  max-width: 1400px;
  margin: 0 auto;
  padding: 48px 24px;

  .header {
    margin-bottom: 48px;
  }

  .title {
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 12px;
    text-align: center;
  }

  .subtitle {
    font-size: 1.125rem;
    color: var(--text-secondary);
    text-align: center;
  }

  .upload-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
    margin-bottom: 48px;
  }

  .section {
    background-color: var(--bg-surface);
    border: 1px solid var(--border-default);
    border-radius: 12px;
    padding: 24px;
  }

  .section-title {
    font-size: 1.125rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .section-icon {
    color: var(--accent-cyan);
  }

  .metrics-section {
    grid-column: 1 / -1;
  }

  .settings-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
    margin-bottom: 24px;
  }

  .setting-item {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .setting-label {
    font-size: 14px;
    font-weight: 500;
    color: var(--text-primary);
  }

  .setting-hint {
    font-size: 12px;
    color: var(--text-secondary);
  }

  .actions {
    display: flex;
    justify-content: center;
    margin-top: 48px;
  }

  .run-button {
    height: 56px;
    font-size: 18px;
    font-weight: 600;
    padding: 0 48px;
    border-radius: 8px;
    display: flex;
    align-items: center;
    gap: 12px;
    box-shadow: var(--glow-info);
    transition: all 0.3s ease;

    &:hover {
      transform: translateY(-2px);
      box-shadow: 0 0 30px rgba(0, 217, 255, 0.5);
    }

    &:disabled {
      opacity: 0.5;
      box-shadow: none;
      transform: none;
    }
  }

  @media (max-width: 968px) {
    .upload-grid {
      grid-template-columns: 1fr;
    }

    .settings-grid {
      grid-template-columns: 1fr;
    }
  }
`;

const JUDGE_MODELS = [
  'gemini-2.5-flash',
  'gemini-2.0-flash',
  'claude-3.5-sonnet',
  'gpt-4o',
];

export const UploadView: React.FC = () => {
  const { state, actions } = useTraceContext();

  const canRunEvaluation = state.traceFiles.length > 0 && state.selectedMetrics.length > 0;

  return (
    <div css={uploadViewStyle}>
      <div className="header">
        <h1 className="title">Trace Analysis Laboratory</h1>
        <p className="subtitle">
          Evaluate agent behavior from OpenTelemetry traces without re-running agents
        </p>
      </div>

      <div className="upload-grid">
        <div className="section">
          <div className="section-title">
            <span className="section-icon">📊</span>
            Trace Files
          </div>
          <FileDropZone
            title="Drop trace files here"
            description="Upload one or more Jaeger JSON trace files"
            multiple
            onChange={actions.setTraceFiles}
          />
          {state.traceFiles.length > 0 && (
            <div style={{ marginTop: 16, color: 'var(--text-secondary)' }}>
              {state.traceFiles.length} file(s) selected
            </div>
          )}
        </div>

        <div className="section">
          <div className="section-title">
            <span className="section-icon">🎯</span>
            Eval Set (Optional)
          </div>
          <FileDropZone
            title="Drop eval set file here"
            description="Upload golden eval set JSON for comparison"
            onChange={(files) => actions.setEvalSet(files[0] || null)}
          />
          {state.evalSetFile && (
            <div style={{ marginTop: 16, color: 'var(--text-secondary)' }}>
              {state.evalSetFile.name}
            </div>
          )}
        </div>

        <div className="section metrics-section">
          <div className="section-title">
            <span className="section-icon">📏</span>
            Metrics Configuration
          </div>
          <MetricSelector
            selectedMetrics={state.selectedMetrics}
            onToggleMetric={actions.toggleMetric}
          />
        </div>

        <div className="section">
          <div className="section-title">
            <span className="section-icon">
              <Settings size={20} />
            </span>
            Evaluation Settings
          </div>

          <div className="settings-grid">
            <div className="setting-item">
              <label className="setting-label">Judge Model</label>
              <Select
                value={state.judgeModel}
                onChange={actions.setJudgeModel}
                options={JUDGE_MODELS.map((model) => ({ label: model, value: model }))}
                style={{ width: '100%' }}
              />
              <span className="setting-hint">
                LLM used for judge-based metrics (hallucinations, safety, etc.)
              </span>
            </div>

            <div className="setting-item">
              <label className="setting-label">Pass Threshold: {state.threshold}</label>
              <Slider
                min={0}
                max={1}
                step={0.05}
                value={state.threshold}
                onChange={actions.setThreshold}
              />
              <span className="setting-hint">
                Minimum score required for metrics to pass
              </span>
            </div>
          </div>
        </div>
      </div>

      <div className="actions">
        <Button
          type="primary"
          size="large"
          className="run-button"
          onClick={actions.runEvaluation}
          disabled={!canRunEvaluation}
          loading={state.isEvaluating}
        >
          <Play size={24} />
          {state.isEvaluating ? 'Running Evaluation...' : 'Run Evaluation'}
        </Button>
      </div>
    </div>
  );
};
