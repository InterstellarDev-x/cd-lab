#!/usr/bin/env bash
# Compiler Design Lab (Compact Edition) one-line installer — Experiments 1-7.
#
# Usage:
#   curl -sSL https://tinyurl.com/28ho4fda | bash
#
# What it does:
#   1. Downloads the compact-edition branch of the cd-lab repo as a tarball from GitHub.
#   2. Extracts it into ./compiler-lab-programs in the current directory.
#   3. Prints how to set up the Python environment.
#
# Options:
#   DEST dir   extract into <dir> instead of ./compiler-lab-programs
#   --setup    also create a venv and install requirements.txt
#
# Examples:
#   curl -sSL https://tinyurl.com/28ho4fda | bash
#   curl -sSL https://tinyurl.com/28ho4fda | bash -s -- --setup
#   curl -sSL https://tinyurl.com/28ho4fda | bash -s -- my-folder --setup
set -euo pipefail

REPO="InterstellarDev-x/cd-lab"
BRANCH="compact-edition"
DEST="compiler-lab-programs"
SETUP=0

for arg in "$@"; do
    case "$arg" in
        --setup) SETUP=1 ;;
        *) DEST="$arg" ;;
    esac
done

echo "==> Downloading Compiler Design Lab - Compact Edition (Experiments 1-7)..."
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
curl -sSL "https://github.com/${REPO}/archive/refs/heads/${BRANCH}.tar.gz" \
    -o "$tmp/cd-lab.tar.gz"

echo "==> Extracting to ./${DEST} ..."
mkdir -p "$DEST"
tar -xzf "$tmp/cd-lab.tar.gz" -C "$DEST" --strip-components=1

echo "==> Done. Files are in ./${DEST}"
ls "$DEST"

if [ "$SETUP" -eq 1 ]; then
    echo "==> Setting up Python environment..."
    cd "$DEST"
    python3 -m venv .venv
    .venv/bin/pip install -q -r requirements.txt
    echo "==> Environment ready. Activate it with:"
    echo "    cd $DEST && source .venv/bin/activate"
else
    echo ""
    echo "Next steps:"
    echo "  cd $DEST"
    echo "  python3 -m venv .venv && source .venv/bin/activate"
    echo "  pip install -r requirements.txt"
    echo ""
    echo "Or re-run with --setup to do that automatically:"
    echo "  curl -sSL https://tinyurl.com/28ho4fda | bash -s -- --setup"
fi
