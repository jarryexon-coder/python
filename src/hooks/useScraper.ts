// src/hooks/useScraper.ts
import { useQuery } from '@tanstack/react-query';

const API_BASE = import.meta.env.VITE_API_BASE || 'https://pleasing-determination-production.up.railway.app';

// Secret Phrases hook
export const useSecretPhrases = (options = {}) => {
  return useQuery({
    queryKey: ['scraper', 'secret-phrases'],
    queryFn: async () => {
      const response = await fetch(`${API_BASE}/api/secret-phrases`);
      if (!response.ok) throw new Error('Failed to scrape secret phrases');
      return response.json();
    },
    staleTime: 15 * 60 * 1000, // 15 minutes
    cacheTime: 30 * 60 * 1000,
    retry: 2,
    refetchOnWindowFocus: false,
    ...options,
  });
};

// Predictions Outcome hook
export const usePredictionOutcomes = (sport = 'nba', options = {}) => {
  return useQuery({
    queryKey: ['scraper', 'prediction-outcomes', sport],
    queryFn: async () => {
      const response = await fetch(`${API_BASE}/api/predictions/outcome?sport=${sport}`);
      if (!response.ok) throw new Error('Failed to scrape prediction outcomes');
      return response.json();
    },
    staleTime: 10 * 60 * 1000, // 10 minutes
    cacheTime: 20 * 60 * 1000,
    retry: 2,
    ...options,
  });
};

// Advanced scraper hook
export const useAdvancedScraper = (url: string, selector: string, enabled = true) => {
  return useQuery({
    queryKey: ['scraper', 'advanced', url, selector],
    queryFn: async () => {
      const params = new URLSearchParams({ url, selector });
      const response = await fetch(`${API_BASE}/api/scrape/advanced?${params}`);
      if (!response.ok) throw new Error('Advanced scraping failed');
      return response.json();
    },
    staleTime: 5 * 60 * 1000,
    cacheTime: 10 * 60 * 1000,
    enabled: !!url && !!selector && enabled,
    retry: 1,
  });
};

// Real-time odds scraper
export const useRealTimeOdds = (sport = 'nba', options = {}) => {
  return useQuery({
    queryKey: ['scraper', 'realtime-odds', sport],
    queryFn: async () => {
      const response = await fetch(`${API_BASE}/api/scrape/odds?sport=${sport}`);
      if (!response.ok) throw new Error('Failed to scrape real-time odds');
      return response.json();
    },
    staleTime: 2 * 60 * 1000, // 2 minutes for odds
    cacheTime: 5 * 60 * 1000,
    refetchInterval: 2 * 60 * 1000, // Auto-refresh every 2 minutes
    refetchIntervalInBackground: true,
    ...options,
  });
};
