# Google Integration Setup

This folder contains Google API integrations for the /new-lead workflow.

## Quick Setup

### Option 1: Gmail Draft Creation

Creates email drafts directly in your Gmail.

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project or select existing one
3. Enable **Gmail API**
4. Go to **APIs & Services → Credentials**
5. Create **OAuth 2.0 Client ID** (Desktop app)
6. Download and save as `credentials.json` in this folder
7. Run `python3 gmail_draft.py --check` to verify
8. First use will open browser for authorization

### Option 2: Google Docs Proposals

Creates proposal documents in Google Docs.

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Enable **Google Docs API** and **Google Drive API**
3. Go to **IAM & Admin → Service Accounts**
4. Create service account
5. Create key (JSON) and save as `service_account.json` in this folder
6. Share your proposals folder with the service account email
7. Add folder ID to `agentic/.env`:
   ```
   GOOGLE_DRIVE_FOLDER_ID=your_folder_id_here
   ```
8. Run `python3 docs_proposal.py --check` to verify

## Files

- `gmail_draft.py` - Create Gmail drafts
- `docs_proposal.py` - Create Google Docs proposals
- `credentials.json` - OAuth credentials (you create this)
- `service_account.json` - Service account key (you create this)
- `token.json` - Auto-generated after Gmail authorization

## Without Google API

Both tools work without credentials - they output formatted text you can copy/paste:
- Email → Copy to Gmail
- Proposal → Copy to Google Docs

## Usage

```bash
# Check setup status
python3 gmail_draft.py --check
python3 docs_proposal.py --check

# Create email draft
python3 gmail_draft.py --to "john@company.com" --subject "AI Solutions" --body "Email content..."

# Create proposal
python3 docs_proposal.py --company "Acme Corp" --contact "John Smith" --industry "Manufacturing"
```

## Security Notes

- `credentials.json` and `service_account.json` are gitignored
- `token.json` contains your OAuth token - also gitignored
- Never commit these files to version control
