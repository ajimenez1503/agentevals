import React from 'react';
import { Checkbox, Button } from 'antd';
import type { CheckboxChangeEvent } from 'antd/es/checkbox';
import { css } from '@emotion/react';
import { AVAILABLE_METRICS } from '../../lib/types';

interface MetricSelectorProps {
  selectedMetrics: string[];
  onToggleMetric: (metric: string) => void;
}

const selectorStyle = css`
  .metric-categories {
    display: flex;
    flex-direction: column;
    gap: 24px;
  }

  .metric-category {
    background-color: var(--bg-surface);
    border: 1px solid var(--border-default);
    border-radius: 8px;
    padding: 16px;
  }

  .category-title {
    color: var(--accent-cyan);
    font-size: 14px;
    font-weight: 600;
    text-transform: uppercase;
    margin-bottom: 12px;
    letter-spacing: 0.5px;
  }

  .metric-list {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .metric-item {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }

  .metric-name {
    color: var(--text-primary);
    font-family: var(--font-mono);
    font-size: 13px;
  }

  .metric-description {
    color: var(--text-secondary);
    font-size: 12px;
    margin-left: 24px;
  }

  .metric-badges {
    display: flex;
    gap: 6px;
    margin-left: 24px;
  }

  .metric-badge {
    font-size: 10px;
    padding: 2px 6px;
    border-radius: 3px;
    font-weight: 500;
  }

  .badge-eval-set {
    background-color: rgba(124, 255, 107, 0.1);
    color: var(--status-success);
    border: 1px solid rgba(124, 255, 107, 0.3);
  }

  .badge-llm {
    background-color: rgba(167, 139, 250, 0.1);
    color: var(--accent-purple);
    border: 1px solid rgba(167, 139, 250, 0.3);
  }

  .selector-actions {
    display: flex;
    gap: 12px;
    margin-top: 16px;
  }

  .ant-checkbox-wrapper {
    color: var(--text-primary);
  }

  .ant-checkbox-checked .ant-checkbox-inner {
    background-color: var(--accent-cyan);
    border-color: var(--accent-cyan);
  }
`;

export const MetricSelector: React.FC<MetricSelectorProps> = ({
  selectedMetrics,
  onToggleMetric,
}) => {
  // Group metrics by category
  const categorizedMetrics = AVAILABLE_METRICS.reduce(
    (acc, metric) => {
      if (!acc[metric.category]) {
        acc[metric.category] = [];
      }
      acc[metric.category].push(metric);
      return acc;
    },
    {} as Record<string, typeof AVAILABLE_METRICS>
  );

  const handleSelectAll = () => {
    AVAILABLE_METRICS.forEach((metric) => {
      if (!selectedMetrics.includes(metric.name)) {
        onToggleMetric(metric.name);
      }
    });
  };

  const handleClearAll = () => {
    selectedMetrics.forEach((metric) => {
      onToggleMetric(metric);
    });
  };

  return (
    <div css={selectorStyle}>
      <div className="metric-categories">
        {Object.entries(categorizedMetrics).map(([category, metrics]) => (
          <div key={category} className="metric-category">
            <div className="category-title">{category}</div>
            <div className="metric-list">
              {metrics.map((metric) => (
                <div key={metric.name} className="metric-item">
                  <Checkbox
                    checked={selectedMetrics.includes(metric.name)}
                    onChange={(e: CheckboxChangeEvent) => onToggleMetric(metric.name)}
                  >
                    <span className="metric-name">{metric.name}</span>
                  </Checkbox>
                  <div className="metric-description">{metric.description}</div>
                  <div className="metric-badges">
                    {metric.requiresEvalSet && (
                      <span className="metric-badge badge-eval-set">Requires Eval Set</span>
                    )}
                    {metric.requiresLLM && (
                      <span className="metric-badge badge-llm">Uses LLM</span>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>

      <div className="selector-actions">
        <Button size="small" onClick={handleSelectAll}>
          Select All
        </Button>
        <Button size="small" onClick={handleClearAll}>
          Clear All
        </Button>
      </div>
    </div>
  );
};
