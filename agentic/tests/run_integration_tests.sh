#!/bin/bash
# Integration Test Runner for Agentic Tools
# Usage: ./tests/run_integration_tests.sh

set -e

cd "$(dirname "$0")/.."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

PASSED=0
FAILED=0
SKIPPED=0

log_pass() {
    echo -e "${GREEN}[PASS]${NC} $1"
    ((PASSED++))
}

log_fail() {
    echo -e "${RED}[FAIL]${NC} $1"
    ((FAILED++))
}

log_skip() {
    echo -e "${YELLOW}[SKIP]${NC} $1"
    ((SKIPPED++))
}

log_header() {
    echo ""
    echo "=========================================="
    echo "$1"
    echo "=========================================="
}

# Check if a command succeeds
run_test() {
    local name="$1"
    shift
    if "$@" > /dev/null 2>&1; then
        log_pass "$name"
        return 0
    else
        log_fail "$name"
        return 1
    fi
}

# Check if env var is set
check_env() {
    if [ -z "${!1}" ]; then
        return 1
    fi
    return 0
}

echo "Agentic Tools Integration Test Suite"
echo "====================================="
echo "Started at: $(date)"
echo ""

# Load environment
source .env 2>/dev/null || true

# ==========================================
# Module 1: Diagrams (no external API needed for basic tests)
# ==========================================
log_header "Module: Diagrams"

run_test "Mermaid generation" bash -c 'cat tests/fixtures/test_diagram.json | ./run modules/diagrams/tool/generate_mermaid.py --stdin'
run_test "Draw.io generation" bash -c 'cat tests/fixtures/test_diagram.json | ./run modules/diagrams/tool/generate_drawio.py --stdin'

# ==========================================
# Module 2: Slack
# ==========================================
log_header "Module: Slack"

if check_env SLACK_BOT_TOKEN; then
    run_test "Slack channels list" ./run modules/slack/tool/slack_api.py channels list
    run_test "Slack groups list" ./run modules/slack/tool/slack_api.py groups list
    run_test "Slack users list" ./run modules/slack/tool/slack_api.py users list
else
    log_skip "Slack tests (SLACK_BOT_TOKEN not set)"
fi

# ==========================================
# Module 3: Infrastructure
# ==========================================
log_header "Module: Infrastructure"

if check_env CLOUDFLARE_API_TOKEN; then
    run_test "Cloudflare zones list" ./run modules/infrastructure/tool/cloudflare_api.py zones list
else
    log_skip "Cloudflare tests (CLOUDFLARE_API_TOKEN not set)"
fi

if check_env DOKPLOY_API_KEY && check_env DOKPLOY_URL; then
    run_test "Dokploy compose list" ./run modules/infrastructure/tool/dokploy_api.py compose list
else
    log_skip "Dokploy tests (DOKPLOY_API_KEY or DOKPLOY_URL not set)"
fi

# ==========================================
# Module 4: N8N
# ==========================================
log_header "Module: N8N"

if check_env N8N_API_KEY && check_env N8N_API_URL; then
    run_test "N8N workflows list" ./run modules/n8n/tool/n8n_api.py list
else
    log_skip "N8N tests (N8N_API_KEY or N8N_API_URL not set)"
fi

# ==========================================
# Module 5: MD Export
# ==========================================
log_header "Module: MD Export"

run_test "MD to DOCX" ./run modules/md-export/tool/md_to_docx.py tests/fixtures/test.md --output .tmp/test_output.docx

if [ -f "credentials.json" ] || [ -f "token.json" ]; then
    run_test "MD to GDoc (dry-run)" ./run modules/md-export/tool/md_to_gdoc.py tests/fixtures/test.md --dry-run
else
    log_skip "MD to GDoc tests (Google credentials not found)"
fi

# ==========================================
# Module 6: Proposal
# ==========================================
log_header "Module: Proposal"

run_test "Proposal validation" bash -c 'cat tests/fixtures/test_proposal.json | ./run modules/proposal/tool/generate_proposal.py'

# ==========================================
# Summary
# ==========================================
log_header "Test Summary"
echo ""
echo -e "Passed:  ${GREEN}${PASSED}${NC}"
echo -e "Failed:  ${RED}${FAILED}${NC}"
echo -e "Skipped: ${YELLOW}${SKIPPED}${NC}"
echo ""
echo "Completed at: $(date)"

if [ $FAILED -gt 0 ]; then
    exit 1
fi
