#!/bin/bash

# git_auto_pull.sh - Auto pull with automatic directory change

set -e

# Auto CD to script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Configuration - now relative to script location
BRANCH="main"
LOG_FILE="$SCRIPT_DIR/git_auto_pull.log"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log() {
    local message="$1"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo -e "${YELLOW}[$timestamp]${NC} $message" | tee -a "$LOG_FILE"
}

main() {
    log "Script running from: $SCRIPT_DIR"
    log "Current directory: $(pwd)"
    
    # Check if this is a git repository
    if [ ! -d ".git" ]; then
        log "${RED}Error: Not a git repository${NC}"
        log "Please run this script from a git repository directory"
        exit 1
    fi
    
    # Rest of your git pull logic...
    log "Fetching latest changes..."
    git fetch origin
    
    LOCAL_COMMIT=$(git rev-parse @)
    REMOTE_COMMIT=$(git rev-parse @{u})
    
    if [ "$LOCAL_COMMIT" = "$REMOTE_COMMIT" ]; then
        log "${GREEN}Already up-to-date.${NC}"
    else
        log "Pulling new changes..."
        git pull origin "$BRANCH"
        log "${GREEN}Successfully updated!${NC}"
    fi
}

main "$@"