/**
 * Utility functions for Onboarding Agent
 */

/**
 * Generate a URL-safe slug from client name
 * Used for Slack channel naming: client-{slug}
 */
export function generateSlug(name: string): string {
  return name
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '')
    .substring(0, 50);
}

/**
 * Sleep for specified milliseconds
 */
export function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

/**
 * Get first name from full name
 */
export function getFirstName(fullName: string): string {
  return fullName.split(' ')[0] || fullName;
}

/**
 * Format currency for display
 */
export function formatCurrency(amount: number): string {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 0,
  }).format(amount);
}

/**
 * Check if current time is within business hours (9am-6pm PT)
 */
export function isBusinessHours(): boolean {
  const now = new Date();
  const ptTime = new Date(now.toLocaleString('en-US', { timeZone: 'America/Los_Angeles' }));
  const hour = ptTime.getHours();
  const day = ptTime.getDay();

  // Monday-Friday, 9am-6pm PT
  return day >= 1 && day <= 5 && hour >= 9 && hour < 18;
}

/**
 * Get next business day start time
 */
export function getNextBusinessDayStart(): Date {
  const now = new Date();
  const ptTime = new Date(now.toLocaleString('en-US', { timeZone: 'America/Los_Angeles' }));

  // Start at 9am
  ptTime.setHours(9, 0, 0, 0);

  // If it's already past 9am today, or it's a weekend, move to next business day
  const hour = now.getHours();
  const day = ptTime.getDay();

  if (hour >= 9 || day === 0 || day === 6) {
    ptTime.setDate(ptTime.getDate() + 1);
  }

  // Skip weekends
  while (ptTime.getDay() === 0 || ptTime.getDay() === 6) {
    ptTime.setDate(ptTime.getDate() + 1);
  }

  return ptTime;
}
