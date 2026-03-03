#!/bin/bash
# landing-page-pro scaffold — Run this once to create all directories and placeholder files
# Usage: chmod +x scaffold.sh && ./scaffold.sh

set -e

echo "🚀 Scaffolding landing-page-pro plugin..."

# Root files
mkdir -p .claude-plugin
mkdir -p .claude
mkdir -p blueprint
mkdir -p orchestration
mkdir -p output

# Skills directories
SKILLS=(
  "niche-research"
  "competitor-analysis"
  "audience-persona"
  "design-brief"
  "landing-page-builder"
  "conversion-optimizer"
)

for skill in "${SKILLS[@]}"; do
  mkdir -p "skills/${skill}/references"
  mkdir -p "skills/${skill}/assets"
  mkdir -p "skills/${skill}/evals"
  touch "skills/${skill}/SKILL.md"
  echo '{"skill_name": "'${skill}'", "evals": []}' > "skills/${skill}/evals/evals.json"
  echo "  ✅ skills/${skill}/"
done

# Extra directories for specific skills
mkdir -p skills/competitor-analysis/scripts
mkdir -p skills/landing-page-builder/references/stack-guides

# Orchestration
touch orchestration/pipeline.md
touch orchestration/swarm-config.md

# Output with .gitkeep
touch output/.gitkeep

# Create .gitignore
cat > .gitignore << 'EOF'
# Plugin outputs (project-specific, don't commit)
output/*/

# OS
.DS_Store
Thumbs.db

# Node
node_modules/

# Python
__pycache__/
*.pyc
.venv/

# IDE
.idea/
.vscode/
*.swp
EOF

# Copy CLAUDE.md to root (no symlink — avoids cross-platform issues)
if [ -f ".claude/CLAUDE.md" ]; then
  cp .claude/CLAUDE.md CLAUDE.md
  echo "  ✅ CLAUDE.md copied to root from .claude/"
else
  echo "  ⚠️  .claude/CLAUDE.md not found — copy it first, then re-run"
fi

echo ""
echo "📁 Structure created:"
echo ""
find . -type f -not -path './.git/*' -not -path './node_modules/*' | sort | head -50
echo ""
echo "✅ Scaffold complete!"
echo ""
echo "Next steps:"
echo "  1. Copy CLAUDE.md to .claude/CLAUDE.md (if not already there)"
echo "  2. Copy blueprint/*.md files"
echo "  3. Open Claude Code and start Phase B: 'Implement niche-research skill'"
