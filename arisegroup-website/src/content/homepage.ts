// Homepage Content
export const homepageContent = {
  hero: {
    eyebrow: 'AI Transformation for Defense, Industrial, E-commerce & Construction',
    headline: '80% of AI transformation is documentation, integration, and infrastructure.',
    subheadline: 'Only 20% is actual Gen AI. Most agencies skip the 80%. We build the foundation first.',
    cta: {
      primary: 'Book Discovery Call',
      secondary: 'See How We Work',
    },
  },

  problem: {
    headline: 'Why Most AI Projects Fail',
    description:
      'You hired an AI agency. They built an AI feature. It didn't work because your systems weren't integrated. Project failed, money wasted, leadership loses trust.',
    stats: [
      {
        number: '80%',
        label: 'AI projects fail due to missing prerequisites',
      },
      {
        number: '$50K+',
        label: 'Average wasted on failed AI implementations',
      },
      {
        number: '6-12 months',
        label: 'Lost time before restarting with the right approach',
      },
    ],
  },

  solution: {
    headline: 'Our Prerequisites-First Approach',
    description:
      'We're not a typical AI agency. We're strategic advisors who happen to build AI solutions. We document, integrate, and build infrastructure before touching AI.',
    phases: [
      {
        phase: 'Phase 0',
        title: 'Q1-Q5 Discovery',
        description:
          'Five questions that document your operation and identify what's missing. No generic pitch—diagnostic conversation.',
        duration: '15-20 minutes',
      },
      {
        phase: 'Phase 1',
        title: 'Prerequisites (60% of work)',
        description:
          'System integration, data infrastructure, workflow documentation. The foundation AI needs to actually work.',
        duration: '4-8 weeks',
      },
      {
        phase: 'Phase 2',
        title: 'AI Implementation (40% of work)',
        description:
          'Now we build the AI layer on top of solid infrastructure. It works because the foundation exists.',
        duration: '3-6 weeks',
      },
      {
        phase: 'Phase 3',
        title: 'Engineering-as-a-Service',
        description:
          'Ongoing optimization, expansion, and strategic partnership. One-time projects are the starting point, not the end.',
        duration: 'Recurring',
      },
    ],
  },

  verticals: {
    headline: 'Deep Vertical Expertise',
    description:
      'We're not generic "AI consultants." Each founder owns their vertical with years of operational experience.',
    list: [
      {
        vertical: 'Defense',
        icon: '🛡️',
        founder: 'Mekaiel',
        credentials: '9 years DoD/DoS network security, Active Secret Clearance',
        painPoints: [
          'Legacy systems that won't integrate',
          'Security compliance slowing AI adoption',
          'Manual operations processes',
          'Siloed data across departments',
        ],
        cta: 'Book Defense Discovery Call',
      },
      {
        vertical: 'Industrial',
        icon: '🏭',
        founder: '4.0 Hero',
        credentials: '22 years industrial automation, OT/IT convergence',
        painPoints: [
          'Production data exists but isn't actionable',
          'IIoT projects stall due to complexity',
          'Disconnected SCADA/MES/ERP systems',
          'Manual workflows in engineering',
        ],
        cta: 'Book Industrial Discovery Call',
      },
      {
        vertical: 'E-commerce',
        icon: '🛒',
        founder: 'Matthew',
        credentials: '6 years Amazon SWE, owns e-commerce business',
        painPoints: [
          'Manual customer service at scale',
          'Inventory chaos across platforms',
          'Content creation bottleneck',
          'Can't scale without more headcount',
        ],
        cta: 'Book E-commerce Discovery Call',
      },
      {
        vertical: 'Construction',
        icon: '🏗️',
        founder: 'Chris',
        credentials: '11+ years construction, recovered $500K+ lost revenue',
        painPoints: [
          'Manual estimating (slow, error-prone)',
          'Project tracking chaos',
          'Communication gaps field-to-office',
          'Revenue leakage from poor change orders',
        ],
        cta: 'Book Construction Discovery Call',
      },
    ],
  },

  methodology: {
    headline: 'The Q1-Q5 Framework',
    description:
      'Every discovery call follows the same 5 questions. This isn't a sales pitch—it's a diagnostic conversation.',
    questions: [
      {
        question: 'Q1: What do you do (specifically)?',
        purpose: 'Understand your core operation and identify automation opportunities.',
      },
      {
        question: 'Q2: What does this cost you monthly?',
        purpose: 'Quantify the pain in dollars and hours. This drives pricing and ROI.',
      },
      {
        question: 'Q3: What have you tried before?',
        purpose: 'Understand what didn't work and why. Learn from previous failures.',
      },
      {
        question: 'Q4: Why didn't it work?',
        purpose: 'Identify the REAL root cause. This reveals missing prerequisites.',
      },
      {
        question: 'Q5: Magic wand solution?',
        purpose: 'Understand your vision. Then we prescribe the actual solution with prerequisites.',
      },
    ],
  },

  social_proof: {
    headline: 'Built by Operators, Not Consultants',
    founders: [
      {
        name: 'Mekaiel',
        vertical: 'Defense',
        bio: 'Secured Pentagon networks, NATO operations, and 15 U.S. embassies. Active Secret Clearance. Former DoD/DoS network security engineer. I know zero-failure standards.',
        linkedin: 'https://linkedin.com/in/mekaiel',
      },
      {
        name: '4.0 Hero',
        vertical: 'Industrial',
        bio: '22 years building production systems across every industry. I know what works on plant floors, not just in PowerPoints. Industrial automation expert.',
        linkedin: 'https://linkedin.com/in/40hero',
      },
      {
        name: 'Matthew',
        vertical: 'E-commerce',
        bio: '6 years at Amazon (Alexa team SWE), plus I own InfinityVault e-commerce business. I understand both the tech side and operator side.',
        linkedin: 'https://linkedin.com/in/matthew',
      },
      {
        name: 'Chris',
        vertical: 'Construction',
        bio: '11+ years in construction and GRC. Recovered $500K+ in lost revenue through process improvements. Part 107 drone pilot for project tracking.',
        linkedin: 'https://linkedin.com/in/chris',
      },
    ],
  },

  pricing: {
    headline: 'Transparent Pricing Model',
    description:
      'No black-box estimates. We price based on your monthly cost (Q2) using our proven formula.',
    formula: {
      base: 'Your monthly cost (Q2) × 30-50% = Base project fee',
      prerequisites: 'Prerequisites (integration, infrastructure) priced separately',
      retainer: 'Ongoing Engineering-as-a-Service: 10-30% of project value/month',
    },
    tiers: [
      {
        tier: 'Tier 1: Mercenary',
        whenToUse: 'Monthly cost <$15K',
        structure: 'Cash-for-service. You own all IP.',
        typical: '$5K-$25K one-time',
      },
      {
        tier: 'Tier 2: Partnership',
        whenToUse: 'Monthly cost $15K-$50K with measurable ROI',
        structure: 'Base fee + 20% of savings for 12-24 months',
        typical: '$10K-$50K base + performance upside',
      },
      {
        tier: 'Tier 3: Missionary',
        whenToUse: 'Monthly cost $50K+ with massive distribution potential',
        structure: 'Reduced cash + equity stake (30-50% co-ownership)',
        typical: 'Custom deal, strategic partnership',
      },
    ],
  },

  cta: {
    headline: 'Start with a 15-Minute Discovery Call',
    description:
      'No pitch. No pressure. Just 5 questions to understand your operation. Then we'll give you a custom roadmap.',
    steps: [
      'Select your vertical (Defense, Industrial, E-commerce, Construction)',
      'Book 15 minutes with the founder who specializes in your industry',
      'We ask Q1-Q5 and document your current state',
      'Within 48 hours, you get a custom proposal with prerequisites + AI approach',
    ],
    button: 'Book Your Discovery Call',
  },

  footer: {
    tagline: 'AriseGroup | AI Transformation Built on Prerequisites',
    description:
      'We're not a typical AI agency. We build the foundation first: documentation, integration, infrastructure. Then AI on top.',
    links: {
      verticals: [
        'Defense',
        'Industrial',
        'E-commerce',
        'Construction',
      ],
      resources: [
        'Case Studies',
        'Insights Blog',
        'Q1-Q5 Framework',
        'Prerequisites Methodology',
      ],
      company: [
        'About',
        'Team',
        'Contact',
        'Book Discovery',
      ],
    },
    email: 'hello@arisegroup.ai',
    social: {
      linkedin: 'https://linkedin.com/company/arisegroup',
      twitter: 'https://twitter.com/arisegroup',
    },
  },
}
