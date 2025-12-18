#!/usr/bin/env python3
"""
Extract key insights from transcripts for AI audits
"""

import json
import re
from pathlib import Path
from typing import List, Dict, Any

class InsightExtractor:
    """Extract structured insights from discovery call transcripts"""

    def __init__(self, transcript_path: str):
        """Initialize with transcript file path"""
        self.transcript_path = Path(transcript_path)
        self.transcript_text = self._load_transcript()
        self.insights = {
            "pain_points": [],
            "budget_indicators": [],
            "timeline_mentions": [],
            "decision_makers": [],
            "tech_stack": [],
            "business_goals": [],
            "current_processes": [],
            "competitors": [],
            "metrics": [],
            "objections": []
        }

    def _load_transcript(self) -> str:
        """Load transcript from file"""
        if not self.transcript_path.exists():
            raise FileNotFoundError(f"Transcript not found: {self.transcript_path}")
        return self.transcript_path.read_text()

    def extract_pain_points(self) -> List[Dict[str, str]]:
        """Extract pain points and challenges mentioned"""
        pain_keywords = [
            r"problem[s]?\s+(?:is|are|with)",
            r"challenge[s]?\s+(?:is|are|with)",
            r"struggle[s]?\s+(?:with|to)",
            r"difficult[y]?\s+(?:with|to|in)",
            r"issue[s]?\s+(?:with|is|are)",
            r"pain\s+point[s]?",
            r"frustrat(?:ing|ion|ed)",
            r"waste[s]?\s+(?:time|money|resources)",
            r"inefficient",
            r"manual(?:ly)?\s+(?:process|do|handle)",
            r"take[s]?\s+(?:forever|hours|too long)",
            r"(?:can't|cannot|unable to)\s+\w+",
            r"bottleneck[s]?",
            r"slow[s]?\s+(?:down|process)",
            r"error[s]?\s+(?:prone|rate|happen)"
        ]

        pain_points = []
        for pattern in pain_keywords:
            matches = re.finditer(pattern, self.transcript_text, re.IGNORECASE)
            for match in matches:
                # Get context (50 chars before and 150 after)
                start = max(0, match.start() - 50)
                end = min(len(self.transcript_text), match.end() + 150)
                context = self.transcript_text[start:end].strip()

                pain_points.append({
                    "keyword": match.group(),
                    "context": context,
                    "position": match.start()
                })

        self.insights["pain_points"] = pain_points
        return pain_points

    def extract_budget(self) -> List[Dict[str, str]]:
        """Extract budget-related mentions"""
        budget_patterns = [
            r"\$[\d,]+(?:\.\d{2})?(?:\s*(?:k|K|thousand|million|M))?",
            r"budget[s]?\s+(?:is|of|around|approximately)?\s*\$?[\d,]+",
            r"(?:spend|spending|invest|investment)\s+(?:of|around|approximately)?\s*\$?[\d,]+",
            r"(?:cost|costs|costing)\s+(?:us|around|approximately)?\s*\$?[\d,]+",
            r"(?:per|/)\s+(?:hour|day|week|month|year)\s+(?:cost|rate)?",
            r"ROI|return on investment",
            r"payback\s+period",
            r"(?:can|could|would)\s+(?:afford|pay|spend)"
        ]

        budget_indicators = []
        for pattern in budget_patterns:
            matches = re.finditer(pattern, self.transcript_text, re.IGNORECASE)
            for match in matches:
                start = max(0, match.start() - 50)
                end = min(len(self.transcript_text), match.end() + 100)
                context = self.transcript_text[start:end].strip()

                budget_indicators.append({
                    "mention": match.group(),
                    "context": context,
                    "position": match.start()
                })

        self.insights["budget_indicators"] = budget_indicators
        return budget_indicators

    def extract_timeline(self) -> List[Dict[str, str]]:
        """Extract timeline and urgency indicators"""
        timeline_patterns = [
            r"(?:by|before|within)\s+(?:end of)?\s*(?:Q[1-4]|January|February|March|April|May|June|July|August|September|October|November|December)",
            r"(?:in|within)\s+(?:the)?\s+(?:next)?\s*\d+\s*(?:day|week|month|year)[s]?",
            r"ASAP|immediately|urgent(?:ly)?|right away",
            r"(?:deadline|due date|target date)\s+(?:is|of)?",
            r"(?:need|want|must have)\s+(?:this|it)?\s+(?:by|before)",
            r"(?:start|begin|launch|go live)\s+(?:in|by|on)",
            r"timeline\s+(?:is|of|for)",
            r"(?:how long|time frame|duration)"
        ]

        timeline_mentions = []
        for pattern in timeline_patterns:
            matches = re.finditer(pattern, self.transcript_text, re.IGNORECASE)
            for match in matches:
                start = max(0, match.start() - 50)
                end = min(len(self.transcript_text), match.end() + 100)
                context = self.transcript_text[start:end].strip()

                timeline_mentions.append({
                    "mention": match.group(),
                    "context": context,
                    "position": match.start()
                })

        self.insights["timeline_mentions"] = timeline_mentions
        return timeline_mentions

    def extract_decision_makers(self) -> List[Dict[str, str]]:
        """Extract decision maker references"""
        decision_patterns = [
            r"(?:CEO|CTO|CFO|COO|President|VP|Director|Manager|Owner|Founder)",
            r"(?:my|our)\s+(?:boss|manager|supervisor|team lead)",
            r"(?:need to|have to|must)\s+(?:check with|run it by|get approval)",
            r"decision\s+(?:maker|makers|making)",
            r"(?:board|committee|leadership|executive)\s+(?:approval|meeting|decision)",
            r"stakeholder[s]?"
        ]

        decision_makers = []
        for pattern in decision_patterns:
            matches = re.finditer(pattern, self.transcript_text, re.IGNORECASE)
            for match in matches:
                start = max(0, match.start() - 50)
                end = min(len(self.transcript_text), match.end() + 100)
                context = self.transcript_text[start:end].strip()

                decision_makers.append({
                    "role": match.group(),
                    "context": context,
                    "position": match.start()
                })

        self.insights["decision_makers"] = decision_makers
        return decision_makers

    def extract_tech_stack(self) -> List[Dict[str, str]]:
        """Extract technology mentions"""
        # Common business software patterns
        tech_patterns = [
            # CRM systems
            r"(?:Salesforce|HubSpot|Pipedrive|Zoho|Microsoft Dynamics|CRM)",
            # Communication tools
            r"(?:Slack|Teams|Discord|Zoom|Google Meet)",
            # Project management
            r"(?:Asana|Trello|Monday\.com|Jira|Basecamp|ClickUp)",
            # Accounting/Finance
            r"(?:QuickBooks|Xero|FreshBooks|Wave|SAP|Oracle)",
            # E-commerce
            r"(?:Shopify|WooCommerce|Magento|BigCommerce)",
            # Marketing
            r"(?:Mailchimp|Constant Contact|SendGrid|Marketo)",
            # Cloud/Hosting
            r"(?:AWS|Azure|Google Cloud|Heroku|DigitalOcean)",
            # Databases
            r"(?:MySQL|PostgreSQL|MongoDB|Firebase|SQL Server)",
            # Development
            r"(?:GitHub|GitLab|Bitbucket|Jenkins|Docker)",
            # Analytics
            r"(?:Google Analytics|Mixpanel|Segment|Tableau)",
            # Generic mentions
            r"(?:software|platform|system|tool|application|database|spreadsheet)[s]?\s+(?:we use|using|have)"
        ]

        tech_mentions = []
        for pattern in tech_patterns:
            matches = re.finditer(pattern, self.transcript_text, re.IGNORECASE)
            for match in matches:
                start = max(0, match.start() - 30)
                end = min(len(self.transcript_text), match.end() + 70)
                context = self.transcript_text[start:end].strip()

                tech_mentions.append({
                    "technology": match.group(),
                    "context": context,
                    "position": match.start()
                })

        self.insights["tech_stack"] = tech_mentions
        return tech_mentions

    def extract_business_goals(self) -> List[Dict[str, str]]:
        """Extract business goals and objectives"""
        goal_patterns = [
            r"(?:goal|objective|aim|target)\s+(?:is|are)\s+(?:to)?",
            r"(?:want|need|plan|intend)\s+to\s+(?:grow|increase|improve|reduce|expand)",
            r"(?:looking to|trying to|working to)\s+\w+",
            r"(?:focus|focusing)\s+on\s+\w+",
            r"(?:priority|priorities)\s+(?:is|are)",
            r"(?:strategy|strategic)\s+\w+",
            r"(?:revenue|profit|margin|growth|efficiency)\s+(?:target|goal)",
            r"(?:scale|scaling)\s+(?:up|the|our)"
        ]

        goals = []
        for pattern in goal_patterns:
            matches = re.finditer(pattern, self.transcript_text, re.IGNORECASE)
            for match in matches:
                start = max(0, match.start() - 50)
                end = min(len(self.transcript_text), match.end() + 150)
                context = self.transcript_text[start:end].strip()

                goals.append({
                    "indicator": match.group(),
                    "context": context,
                    "position": match.start()
                })

        self.insights["business_goals"] = goals
        return goals

    def extract_all(self) -> Dict[str, Any]:
        """Extract all insights from transcript"""
        self.extract_pain_points()
        self.extract_budget()
        self.extract_timeline()
        self.extract_decision_makers()
        self.extract_tech_stack()
        self.extract_business_goals()

        # Add summary statistics
        self.insights["summary"] = {
            "total_pain_points": len(self.insights["pain_points"]),
            "budget_mentioned": len(self.insights["budget_indicators"]) > 0,
            "timeline_urgency": self._assess_urgency(),
            "decision_complexity": self._assess_decision_complexity(),
            "tech_sophistication": self._assess_tech_level(),
            "transcript_length": len(self.transcript_text),
            "word_count": len(self.transcript_text.split())
        }

        return self.insights

    def _assess_urgency(self) -> str:
        """Assess timeline urgency from mentions"""
        urgent_keywords = ["asap", "immediately", "urgent", "right away", "this week", "next week"]
        timeline_text = " ".join([t["mention"].lower() for t in self.insights["timeline_mentions"]])

        if any(keyword in timeline_text for keyword in urgent_keywords):
            return "high"
        elif self.insights["timeline_mentions"]:
            return "medium"
        else:
            return "low"

    def _assess_decision_complexity(self) -> str:
        """Assess decision-making complexity"""
        count = len(self.insights["decision_makers"])
        if count >= 3:
            return "complex"
        elif count >= 1:
            return "moderate"
        else:
            return "simple"

    def _assess_tech_level(self) -> str:
        """Assess technology sophistication level"""
        count = len(self.insights["tech_stack"])
        if count >= 5:
            return "advanced"
        elif count >= 2:
            return "moderate"
        else:
            return "basic"

    def save_insights(self, output_path: str = None):
        """Save insights to JSON file"""
        if output_path is None:
            output_path = self.transcript_path.with_suffix('.insights.json')

        output_path = Path(output_path)
        with open(output_path, 'w') as f:
            json.dump(self.insights, f, indent=2, default=str)

        print(f"✅ Insights saved to: {output_path}")
        return output_path

    def print_summary(self):
        """Print a summary of extracted insights"""
        print("\n" + "="*50)
        print("TRANSCRIPT INSIGHTS SUMMARY")
        print("="*50)

        print(f"\n📊 Overview:")
        print(f"  • Word count: {self.insights['summary']['word_count']:,}")
        print(f"  • Pain points found: {self.insights['summary']['total_pain_points']}")
        print(f"  • Budget mentioned: {'Yes' if self.insights['summary']['budget_mentioned'] else 'No'}")
        print(f"  • Timeline urgency: {self.insights['summary']['timeline_urgency'].upper()}")
        print(f"  • Decision complexity: {self.insights['summary']['decision_complexity'].upper()}")
        print(f"  • Tech sophistication: {self.insights['summary']['tech_sophistication'].upper()}")

        if self.insights["pain_points"]:
            print(f"\n🔥 Top Pain Points:")
            for i, pain in enumerate(self.insights["pain_points"][:3], 1):
                print(f"  {i}. {pain['context'][:100]}...")

        if self.insights["budget_indicators"]:
            print(f"\n💰 Budget Indicators:")
            for budget in self.insights["budget_indicators"][:3]:
                print(f"  • {budget['mention']}: {budget['context'][:80]}...")

        if self.insights["timeline_mentions"]:
            print(f"\n⏰ Timeline:")
            for timeline in self.insights["timeline_mentions"][:3]:
                print(f"  • {timeline['mention']}")

        if self.insights["tech_stack"]:
            print(f"\n🔧 Technologies Mentioned:")
            unique_tech = list(set([t["technology"] for t in self.insights["tech_stack"]]))
            print(f"  • {', '.join(unique_tech[:10])}")

        print("\n" + "="*50)


def main():
    """Main entry point for command-line usage"""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python extract-insights.py <transcript_file> [output_file]")
        sys.exit(1)

    transcript_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        # Extract insights
        extractor = InsightExtractor(transcript_file)
        insights = extractor.extract_all()

        # Print summary
        extractor.print_summary()

        # Save to file
        output_path = extractor.save_insights(output_file)

        print(f"\n✅ Analysis complete!")
        print(f"📁 Full insights saved to: {output_path}")

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()