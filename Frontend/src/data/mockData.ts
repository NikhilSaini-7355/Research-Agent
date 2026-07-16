import type { ResearchSession } from '../types';

export const mockSessions: ResearchSession[] = [
  {
    id: '1',
    title: 'The Impact of CRISPR Gene Editing',
    date: '2023-10-24',
    status: 'completed',
    content: '# The Impact of CRISPR Gene Editing\n\nCRISPR-Cas9 has revolutionized genomic engineering, providing unprecedented precision in DNA modification...',
    stats: {
      sources: 34,
      wordCount: 4200,
      readingTime: 18,
      confidenceScore: 96,
      credibilityScore: 9.2,
    },
    progressStage: 12,
  },
  {
    id: '2',
    title: 'Quantum Computing in Cryptography',
    date: '2023-10-22',
    status: 'completed',
    content: '# Quantum Computing in Cryptography\n\nAs quantum processors scale, traditional public-key cryptography faces existential threats...',
    stats: {
      sources: 18,
      wordCount: 2100,
      readingTime: 9,
      confidenceScore: 88,
      credibilityScore: 8.5,
    },
    progressStage: 12,
  },
  {
    id: '3',
    title: 'AGI Safety Protocols',
    date: '2023-10-20',
    status: 'completed',
    content: '# AGI Safety Protocols\n\nDeveloping aligned Artificial General Intelligence requires robust reward modeling...',
    stats: {
      sources: 42,
      wordCount: 5100,
      readingTime: 22,
      confidenceScore: 91,
      credibilityScore: 9.5,
    },
    progressStage: 12,
  }
];