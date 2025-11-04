#!/bin/bash
#
# Package a Custom Skill into a ZIP file for distribution
#
# Usage: ./scripts/package-skill.sh [skill-directory] [output-name]
# Example: ./scripts/package-skill.sh skill-creator skill-creator-1.0.0

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default values
SKILL_DIR="${1:-skill-creator}"
OUTPUT_NAME="${2:-skill-creator}"

# Functions
print_header() {
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

# Check if skill directory exists
if [ ! -d "$SKILL_DIR" ]; then
    print_error "Skill directory not found: $SKILL_DIR"
    exit 1
fi

# Check if Skill.md exists
if [ ! -f "$SKILL_DIR/Skill.md" ]; then
    print_error "Skill.md not found in $SKILL_DIR"
    exit 1
fi

print_header "Packaging Custom Skill"
print_info "Skill directory: $SKILL_DIR"
print_info "Output name: $OUTPUT_NAME"
echo ""

# Validate skill structure if Python is available
if command -v python3 &> /dev/null; then
    print_info "Running validation checks..."
    if [ -f ".github/scripts/validate-skill.py" ]; then
        if python3 .github/scripts/validate-skill.py "$SKILL_DIR"; then
            print_success "Validation passed"
        else
            print_error "Validation failed"
            exit 1
        fi
    else
        print_warning "Validation script not found, skipping validation"
    fi
    echo ""
fi

# Create temporary working directory
TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

print_info "Preparing package..."

# Copy skill to temp directory
cp -r "$SKILL_DIR" "$TEMP_DIR/"
SKILL_NAME=$(basename "$SKILL_DIR")

# Remove development files
cd "$TEMP_DIR/$SKILL_NAME"
find . -name ".DS_Store" -delete 2>/dev/null || true
find . -name "*.pyc" -delete 2>/dev/null || true
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
find . -name ".git*" -delete 2>/dev/null || true

# Count files
TOTAL_FILES=$(find . -type f | wc -l)
TOTAL_SIZE=$(du -sh . | cut -f1)

print_success "Cleaned up development files"
print_info "Total files: $TOTAL_FILES"
print_info "Total size: $TOTAL_SIZE"
echo ""

# Create ZIP
cd "$TEMP_DIR"
ZIP_NAME="${OUTPUT_NAME}.zip"
ZIP_PATH="$(pwd)/$ZIP_NAME"

print_info "Creating ZIP archive..."
zip -r "$ZIP_NAME" "$SKILL_NAME" \
    -x "*/.git/*" \
    -x "*/__pycache__/*" \
    -x "*.pyc" \
    -x "*/.DS_Store" \
    > /dev/null

# Move ZIP to current directory
ORIGINAL_DIR="$OLDPWD"
mv "$ZIP_PATH" "$ORIGINAL_DIR/"

cd "$ORIGINAL_DIR"

print_success "Package created successfully!"
echo ""

# Display package info
print_header "Package Information"
ls -lh "$ZIP_NAME"
echo ""

print_info "Package contents:"
unzip -l "$ZIP_NAME" | head -n 20
echo ""

# Display next steps
print_header "Next Steps"
echo "1. Test the package by extracting it:"
echo "   unzip -t $ZIP_NAME"
echo ""
echo "2. Upload to Claude:"
echo "   - Open Claude and go to Settings > Capabilities"
echo "   - Click 'Upload Skill' and select: $ZIP_NAME"
echo "   - Enable the skill in your capabilities list"
echo ""
echo "3. For release on GitHub:"
echo "   - Create a new tag: git tag v1.0.0"
echo "   - Push the tag: git push origin v1.0.0"
echo "   - GitHub Actions will automatically create a release"
echo ""

print_success "Packaging complete! 🎉"
