# Speed to Lead Command

Rapidly respond to a new lead with personalized outreach and discovery call booking.

## Usage
```
/speed-to-lead [lead info]
```

## Input Required
Provide any of the following about the new lead:
- Name
- - Company
  - - Email
    - - LinkedIn URL
      - - How they found us (source)
        - - Any context about their needs
         
          - ## What This Command Does
         
          - ### Step 1: Lead Enrichment
          - I will research the lead to gather:
          - - Company size, industry, and revenue signals
            - - Recent company news or announcements
              - - LinkedIn activity and posts
                - - Tech stack indicators
                  - - Pain point signals
                   
                    - ### Step 2: ICP Qualification
                    - Check against AriseGroup.ai Ideal Client Profile:
                    - - **Company Size**: 20-500 employees
                      - - **Revenue**: $2M-50M annually
                        - - **Industry**: Professional services, SaaS, consulting, agencies
                          - - **Role**: Founder, CEO, COO, VP Operations
                            - - **Budget Signals**: Recent funding, growth, hiring
                             
                              - ### Step 3: Personalized Outreach Draft
                              - Generate a personalized message using this framework:
                              - 1. **Hook**: Specific observation about them/their company
                                2. 2. **Credibility**: Relevant AriseGroup.ai background
                                   3. 3. **Value Offer**: Free AI Readiness Audit
                                      4. 4. **CTA**: Calendar link for discovery call
                                        
                                         5. ### Step 4: Output Package
                                         6. Deliver:
                                         7. 1. **Lead Score** (1-10) with qualification notes
                                            2. 2. **LinkedIn Message** (ready to send)
                                               3. 3. **Email Draft** (backup channel)
                                                  4. 4. **Suggested Call Times** (based on their timezone)
                                                     5. 5. **Discovery Call Prep Notes** (talking points specific to them)
                                                       
                                                        6. ---
                                                       
                                                        7. ## Response Templates
                                                       
                                                        8. ### LinkedIn Message Template
                                                        9. ```
                                                           Hi [Name],

                                                           [Personalized hook based on their recent post/company news].

                                                           I help [their industry] companies systematically adopt AI without the chaos. Built our own AI operating system that reduced daily planning from 30 min to 1 min.

                                                           Would you be open to a free AI Readiness Audit? I map your current operations to AI opportunities—no sales pitch, just actionable insights.

                                                           Worth 15 minutes to explore?

                                                           Matt
                                                           AriseGroup.ai
                                                           ```

                                                           ### Email Template
                                                           ```
                                                           Subject: AI opportunity for [Company]

                                                           Hi [Name],

                                                           [Personalized observation about their company/challenge].

                                                           Many [their role]s in [industry] are exploring AI but struggling with systematic adoption—lots of tools, no cohesive strategy.

                                                           I'd like to offer a free AI Readiness Audit—30-minute conversation where I map your operations to specific AI opportunities. No sales pitch, just actionable framework.

                                                           Interested in exploring this week?

                                                           Best,
                                                           Matt
                                                           Founder, AriseGroup.ai
                                                           ```

                                                           ---

                                                           ## Speed Targets
                                                           - **Response Time**: < 5 minutes from lead received
                                                           - - **Personalization Depth**: At least 2 specific observations
                                                             - - **Call Booking**: Within 24-48 hours of first contact
                                                              
                                                               - ## Integration Points
                                                               - - **Cal.com**: https://cal.com/arisegroup (for booking links)
                                                                 - - **CRM**: Log interaction to HubSpot/Notion after outreach
                                                                   - - **Follow-up**: Set reminder for Day 3 if no response
                                                                    
                                                                     - ---

                                                                     ## Example Usage

                                                                     **Input:**
                                                                     ```
                                                                     /speed-to-lead John Smith, CEO of TechFlow Solutions, found us through LinkedIn post about AI automation, email: john@techflow.io
                                                                     ```

                                                                     **Output:**
                                                                     I'll research TechFlow Solutions, score the lead, and generate personalized outreach ready to send within 2 minutes.
