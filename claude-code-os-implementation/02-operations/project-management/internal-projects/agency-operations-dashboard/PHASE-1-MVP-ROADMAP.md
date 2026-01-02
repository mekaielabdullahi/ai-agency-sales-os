# Phase 1 MVP Roadmap - Agency Operations Dashboard

**Phase:** Phase 1 - Read-Only Dashboard
**Timeline:** 8-12 hours (targeting Week 1, early January 2026)
**Goal:** Visual overview better than markdown files
**Status:** Planning Complete - Ready for Execution

---

## Phase 1 Objective

**Build a read-only dashboard that displays all projects and revenue in a single view, deployed to internal demo site.**

**Success Criteria:**
- [ ] Can see all projects and revenue in <5 seconds
- [ ] Visual status indicators work (🟢 On track, 🟡 At risk, 🔴 Blocked)
- [ ] Revenue totals calculate correctly
- [ ] Accessible via demo site URL
- [ ] Responsive design (desktop + tablet minimum)

---

## Deliverables (Phase 1)

### 1. Tab 1: Projects & Revenue Tracker (Primary Focus)
**Estimated Time:** 6-8 hours

**Features:**
- Project grid/card layout showing all active projects
- Each project card displays:
  - Project name
  - Client name
  - Current phase (badge/tag)
  - Status indicator (colored dot or badge)
  - Revenue received (green text)
  - Revenue projected (gray text)
  - Next deadline (with proximity indicator)
- Revenue summary header:
  - Total received YTD
  - Total projected
  - Current month total
- Visual status indicators:
  - 🟢 Green = On track
  - 🟡 Yellow = At risk
  - 🔴 Red = Critical/Blocked
  - ✅ Blue/Check = Complete
- Filter buttons (top of view):
  - All Projects (default)
  - P0 - Critical
  - P1 - High Priority
  - By Phase (dropdown)
  - By Status (dropdown)

**Data:**
- Static JSON file with current projects (see DATA-SCHEMA.md)
- Manually populated from january-2026-project-inventory.md

### 2. Tab Navigation Skeleton (Other Tabs)
**Estimated Time:** 1-2 hours

**Features:**
- Tab bar across top:
  - Tab 1: Projects & Revenue ✅ (active)
  - Tab 2: Client Process (placeholder)
  - Tab 3: Opportunity Matrix (placeholder)
  - Tab 4: Pricing (placeholder)
  - Tab 5: Objectives (placeholder)
  - Tab 6: Dev Kanban (placeholder)
  - Tab 7: Validation (placeholder)
- Clicking non-active tabs shows "Coming Soon" message
- Active tab highlighted
- Smooth transitions between tabs

### 3. Responsive Layout
**Estimated Time:** 1-2 hours

**Features:**
- Desktop: Multi-column card grid (3-4 columns)
- Tablet: 2-column card grid
- Mobile: Single column (future, not Phase 1 priority)
- Cards resize gracefully
- Revenue summary stays visible (sticky header or always visible)

---

## Technical Implementation

### Tech Stack (Phase 1)
- **Framework:** React 18+ (via v0.app export)
- **Styling:** Tailwind CSS (v0.app default)
- **State:** React useState/useContext (simple, no external lib needed)
- **Data:** Static JSON file (`/src/data/projects.json`)
- **Routing:** None needed (tab switching via state)
- **Build:** Vite or Create React App (v0.app export default)
- **Deployment:** Vercel or Netlify (via Trent's demo setup)

### File Structure

```
agency-ops-dashboard/
├── public/
│   └── favicon.ico
├── src/
│   ├── components/
│   │   ├── ProjectCard.jsx         # Individual project card
│   │   ├── RevenueSummary.jsx      # Revenue summary header
│   │   ├── FilterBar.jsx           # Filter/sort controls
│   │   ├── TabNavigation.jsx       # Tab bar
│   │   └── ComingSoon.jsx          # Placeholder for inactive tabs
│   ├── data/
│   │   └── projects.json           # Static project data
│   ├── utils/
│   │   └── helpers.js              # Calculate totals, filter logic
│   ├── App.jsx                     # Main app component
│   ├── index.css                   # Global styles (Tailwind)
│   └── main.jsx                    # Entry point
├── package.json
├── vite.config.js
└── README.md
```

### Component Breakdown

#### 1. App.jsx (Main Container)
```jsx
// Pseudo-code structure
import { useState } from 'react'
import TabNavigation from './components/TabNavigation'
import ProjectsTab from './components/ProjectsTab'
import ComingSoon from './components/ComingSoon'
import projectsData from './data/projects.json'

function App() {
  const [activeTab, setActiveTab] = useState('projects')

  return (
    <div className="min-h-screen bg-gray-50">
      <header>
        <h1>Agency Operations Dashboard</h1>
      </header>

      <TabNavigation activeTab={activeTab} onTabChange={setActiveTab} />

      <main>
        {activeTab === 'projects' && <ProjectsTab data={projectsData} />}
        {activeTab !== 'projects' && <ComingSoon tabName={activeTab} />}
      </main>
    </div>
  )
}
```

#### 2. ProjectsTab.jsx (Tab 1)
```jsx
// Pseudo-code structure
import { useState } from 'react'
import RevenueSummary from './RevenueSummary'
import FilterBar from './FilterBar'
import ProjectCard from './ProjectCard'

function ProjectsTab({ data }) {
  const [filters, setFilters] = useState({ priority: 'all', status: 'all' })

  // Filter projects based on active filters
  const filteredProjects = data.projects.filter(project => {
    if (filters.priority !== 'all' && project.priority !== filters.priority) return false
    if (filters.status !== 'all' && project.status !== filters.status) return false
    return true
  })

  return (
    <div>
      <RevenueSummary summary={data.revenueSummary} />
      <FilterBar filters={filters} onFilterChange={setFilters} />

      <div className="grid grid-cols-3 gap-6">
        {filteredProjects.map(project => (
          <ProjectCard key={project.id} project={project} />
        ))}
      </div>
    </div>
  )
}
```

#### 3. ProjectCard.jsx (Individual Project)
```jsx
// Pseudo-code structure
function ProjectCard({ project }) {
  const statusColors = {
    'in_progress': 'bg-yellow-500',
    'complete': 'bg-blue-500',
    'blocked': 'bg-red-500',
    'not_started': 'bg-gray-400'
  }

  const riskColors = {
    'high': 'border-red-500',
    'medium': 'border-yellow-500',
    'low': 'border-green-500'
  }

  return (
    <div className={`border-l-4 ${riskColors[project.riskLevel]} bg-white rounded-lg shadow p-6`}>
      <div className="flex items-center justify-between mb-2">
        <h3 className="font-semibold text-lg">{project.name}</h3>
        <span className={`h-3 w-3 rounded-full ${statusColors[project.status]}`}></span>
      </div>

      <p className="text-sm text-gray-600">{project.client.company}</p>

      <div className="mt-4">
        <span className="inline-block bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded">
          {project.phaseLabel}
        </span>
        <span className="inline-block bg-purple-100 text-purple-800 text-xs px-2 py-1 rounded ml-2">
          {project.priority}
        </span>
      </div>

      <div className="mt-4 border-t pt-4">
        <div className="flex justify-between text-sm">
          <span className="text-gray-600">Received:</span>
          <span className="font-semibold text-green-600">${project.revenue.received.toLocaleString()}</span>
        </div>
        <div className="flex justify-between text-sm mt-1">
          <span className="text-gray-600">Projected:</span>
          <span className="font-semibold text-gray-700">${project.revenue.projected.toLocaleString()}</span>
        </div>
      </div>

      <div className="mt-4">
        <p className="text-xs text-gray-500">Deadline: {project.deadline}</p>
        {project.riskLevel === 'high' && (
          <p className="text-xs text-red-600 mt-1">⚠️ {project.riskNotes}</p>
        )}
      </div>
    </div>
  )
}
```

#### 4. RevenueSummary.jsx (Header Stats)
```jsx
// Pseudo-code structure
function RevenueSummary({ summary }) {
  return (
    <div className="bg-white rounded-lg shadow p-6 mb-6">
      <h2 className="text-lg font-semibold mb-4">Revenue Overview</h2>

      <div className="grid grid-cols-3 gap-6">
        <div>
          <p className="text-sm text-gray-600">Received (YTD)</p>
          <p className="text-2xl font-bold text-green-600">
            ${summary.received.toLocaleString()}
          </p>
        </div>

        <div>
          <p className="text-sm text-gray-600">Projected</p>
          <p className="text-2xl font-bold text-gray-700">
            ${summary.projected.toLocaleString()}
          </p>
        </div>

        <div>
          <p className="text-sm text-gray-600">Total Potential</p>
          <p className="text-2xl font-bold text-blue-600">
            ${summary.total.toLocaleString()}
          </p>
        </div>
      </div>
    </div>
  )
}
```

---

## Step-by-Step Build Plan

### Step 1: Generate UI in v0.app (2-3 hours)
**Owner:** Matt (Architect)

1. **Prompt for v0.app:**
   ```
   Create a React dashboard with Tailwind CSS for an agency operations tool.

   Layout:
   - Header with "Agency Operations Dashboard" title
   - Tab navigation bar with 7 tabs (Projects & Revenue, Client Process, Opportunity Matrix, Pricing, Objectives, Dev Kanban, Validation)
   - Main content area

   Tab 1 (Projects & Revenue) should display:
   - Revenue summary section with 3 stats: Received, Projected, Total
   - Filter bar with dropdowns for Priority (All, P0, P1) and Status (All, In Progress, Complete, Blocked)
   - Grid of project cards (3 columns on desktop, responsive)

   Each project card should show:
   - Project name (large, bold)
   - Client name (smaller, gray)
   - Phase badge (blue background)
   - Priority badge (purple background)
   - Status indicator (colored dot: green=on track, yellow=at risk, red=critical)
   - Revenue section with "Received" (green) and "Projected" (gray)
   - Deadline with date
   - Risk warning (red text if high risk)
   - Left border colored by risk level (red=high, yellow=medium, green=low)

   Use a clean, professional design with card shadows and spacing.
   ```

2. **Iterate in v0.app:**
   - Adjust card layout and spacing
   - Fine-tune colors and typography
   - Test responsiveness
   - Export code when satisfied

3. **Deliverable:** React components exported from v0.app

### Step 2: Set Up Project Structure (30 min)
**Owner:** AutoClaude or Matt

1. Create new React project:
   ```bash
   npm create vite@latest agency-ops-dashboard -- --template react
   cd agency-ops-dashboard
   npm install
   ```

2. Install Tailwind CSS:
   ```bash
   npm install -D tailwindcss postcss autoprefixer
   npx tailwindcss init -p
   ```

3. Configure Tailwind (tailwind.config.js):
   ```js
   module.exports = {
     content: ["./index.html", "./src/**/*.{js,jsx}"],
     theme: { extend: {} },
     plugins: [],
   }
   ```

4. Add Tailwind directives to src/index.css:
   ```css
   @tailwind base;
   @tailwind components;
   @tailwind utilities;
   ```

5. Create folder structure (see above)

### Step 3: Create Sample Data File (1 hour)
**Owner:** AutoClaude or Matt

1. Create `src/data/projects.json`
2. Populate with current projects from `january-2026-project-inventory.md`
3. Use DATA-SCHEMA.md as reference
4. Include at least 6 projects (Trevor, S&S Wolf, Invoice, Plotter, AntSavvy, Goldfinch)
5. Calculate revenue summary totals

**Deliverable:** `projects.json` with real project data

### Step 4: Integrate v0.app Components (2-3 hours)
**Owner:** AutoClaude

1. Copy v0.app exported components into `/src/components/`
2. Adjust import paths and component exports
3. Connect data from `projects.json` to components
4. Implement filter logic in `ProjectsTab.jsx`
5. Calculate revenue totals in `RevenueSummary.jsx`
6. Test all functionality locally (`npm run dev`)

**Deliverable:** Fully functional Tab 1 with data integration

### Step 5: Build Tab Navigation (1 hour)
**Owner:** AutoClaude

1. Create `TabNavigation.jsx` component
2. Implement tab state management in `App.jsx`
3. Create `ComingSoon.jsx` placeholder for other tabs
4. Style active tab indicator
5. Test tab switching

**Deliverable:** Tab navigation with Tab 1 active, others showing "Coming Soon"

### Step 6: Polish & Responsive Design (1-2 hours)
**Owner:** AutoClaude

1. Test responsive breakpoints (desktop, tablet)
2. Fix any layout issues
3. Add loading states (optional)
4. Add hover effects on cards
5. Final QA testing

**Deliverable:** Polished, responsive dashboard

### Step 7: Deploy to Demo Site (1-2 hours)
**Owner:** Matt (with Trent's guidance)

1. Build production bundle:
   ```bash
   npm run build
   ```

2. Deploy to Vercel/Netlify (via Trent's demo setup):
   - Connect GitHub repo
   - Configure build settings
   - Deploy
   - Get demo URL

3. Test live deployment
4. Share demo URL with team

**Deliverable:** Live demo site URL

---

## Testing Checklist

### Functional Testing
- [ ] All projects display correctly
- [ ] Revenue totals calculate correctly (match manual calculation)
- [ ] Status indicators show correct colors
- [ ] Filter by Priority works (P0, P1, All)
- [ ] Filter by Status works (In Progress, Complete, Blocked, All)
- [ ] Tab navigation switches between tabs
- [ ] "Coming Soon" message shows for inactive tabs
- [ ] Risk warnings display for high-risk projects

### Visual/UI Testing
- [ ] Cards align properly in grid
- [ ] Colors match design (green for on track, yellow for at risk, red for critical)
- [ ] Typography is readable and consistent
- [ ] Spacing and padding look clean
- [ ] Hover effects work on interactive elements

### Responsive Testing
- [ ] Desktop view (1920x1080): 3-4 column grid
- [ ] Tablet view (768x1024): 2 column grid
- [ ] Cards resize gracefully
- [ ] Revenue summary stays visible
- [ ] No horizontal scrolling

### Data Accuracy Testing
- [ ] Trevor project shows: Received $500, Projected $1,500, Total $2,000
- [ ] S&S Wolf shows: Received $0, Projected $10,000
- [ ] Plotter shows: Received $1,250, Projected $2,500
- [ ] Revenue summary totals match sum of all projects
- [ ] Deadlines display correctly
- [ ] Risk notes show for Trevor (ultra-critical)

---

## Acceptance Criteria (Phase 1)

**Phase 1 is complete when:**

1. ✅ **Tab 1 (Projects & Revenue) fully functional**
   - All current projects display with correct data
   - Revenue summary calculates correctly
   - Filters work (Priority, Status)
   - Visual status indicators accurate

2. ✅ **Tab navigation implemented**
   - All 7 tabs visible
   - Tab 1 active by default
   - Tabs 2-7 show "Coming Soon" placeholder
   - Smooth tab switching

3. ✅ **Responsive design**
   - Works on desktop (1920x1080)
   - Works on tablet (768x1024)
   - Cards resize gracefully
   - No layout breaks

4. ✅ **Deployed to demo site**
   - Accessible via URL
   - Loads in <3 seconds
   - No console errors
   - Stable and functional

5. ✅ **Team validation**
   - Matt (Architect) reviews and approves
   - Faster than opening markdown files
   - Data accuracy confirmed
   - Ready for internal use

---

## Phase 1 Completion Triggers Phase 2

**When Phase 1 is complete:**
- Share demo URL with team
- Collect feedback (what's most useful? what's missing?)
- Prioritize which of the remaining 6 tabs to build next in Phase 2
- Likely sequence: Tab 5 (Objectives) or Tab 6 (Dev Kanban) next (most actionable)

---

## Dependencies & Blockers

### Dependencies
- [ ] **Trent's demo setup documentation** - Need deployment process
- [ ] **v0.app access** - Generate UI components
- [ ] **Project data** - Extract from `january-2026-project-inventory.md`

### Potential Blockers
- Trent's demo setup not documented → Use standard Vercel deployment
- v0.app unavailable → Build UI manually with Tailwind
- Data extraction complex → Start with minimal sample data (3-4 projects)

---

## Time Breakdown (8-12 hours total)

| Task | Estimated Time | Owner |
|------|----------------|-------|
| 1. Generate UI in v0.app | 2-3 hours | Matt (Architect) |
| 2. Set up project structure | 30 min | AutoClaude |
| 3. Create sample data file | 1 hour | AutoClaude |
| 4. Integrate v0.app components | 2-3 hours | AutoClaude |
| 5. Build tab navigation | 1 hour | AutoClaude |
| 6. Polish & responsive design | 1-2 hours | AutoClaude |
| 7. Deploy to demo site | 1-2 hours | Matt (with Trent) |
| **TOTAL** | **8-12 hours** | - |

---

## Success Metrics (Phase 1)

**Time Savings:**
- Current: 5-10 min to answer "What's our revenue status?" (open files, calculate)
- Target: <5 seconds (load dashboard)
- **Savings:** 5-10 min/use × 10 uses/week = 50-100 min/week

**Visibility Improvement:**
- Current: Can't see all projects at once
- Target: See all 6+ projects in single view
- **Impact:** Faster prioritization, better decision-making

**Team Alignment:**
- Current: Matt is single source of truth (bottleneck)
- Target: Team can self-serve project status
- **Impact:** Reduced interruptions, team autonomy

---

**Status:** Ready for Execution
**Next Action:** Generate UI in v0.app, then hand off to AutoClaude for integration
**Timeline:** Target completion by Jan 3, 2026
