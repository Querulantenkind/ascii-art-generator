#!/bin/bash
# Showcase script for ASCII Art Generator Pro features

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                                                               ║"
echo "║      ASCII ART GENERATOR PRO - Feature Showcase              ║"
echo "║                                                               ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Function to pause between examples
pause() {
    echo ""
    read -p "Press Enter to continue..."
    clear
}

clear

# 1. Advanced Patterns
echo "=== 1. ADVANCED PATTERNS ==="
echo ""
echo "Mandelbrot Set:"
python ascii_art_pro.py pattern mandelbrot -w 60 --height 25
pause

echo "=== Sierpinski Triangle (Fractal) ==="
python ascii_art_pro.py pattern sierpinski --size 5
pause

echo "=== Spiral Pattern ==="
python ascii_art_pro.py pattern spiral --size 20
pause

echo "=== ASCII Tree (Pine) ==="
python ascii_art_pro.py pattern tree --height 15 --tree-style pine
pause

echo "=== Lissajous Curve ==="
python ascii_art_pro.py pattern lissajous -w 50 --height 25
pause

# 2. Text Effects
echo "=== 2. TEXT EFFECTS ==="
echo ""
echo "Basic Text:"
python ascii_art_generator.py text "HELLO"
echo ""
echo "With Shadow Effect:"
python ascii_art_pro.py text "HELLO" --effect shadow
pause

echo "=== 3D Effect ==="
python ascii_art_pro.py text "3D" --effect 3d
pause

echo "=== Outline Effect ==="
python ascii_art_pro.py text "FRAME" --effect outline
pause

# 3. Composition
echo "=== 3. COMPOSITION ==="
echo ""
echo "Horizontal Combination:"
python ascii_art_pro.py compose --horizontal "ASCII" "ART" "PRO"
pause

echo "=== Grid Layout ==="
python ascii_art_pro.py compose --grid "A" "B" "C" "D" --cols 2
pause

# 4. Cellular Automaton
echo "=== 4. CELLULAR AUTOMATON ==="
echo ""
echo "Rule 30 (Chaotic):"
python ascii_art_pro.py pattern cellular -w 70 --height 30 --rule 30
pause

echo "=== Rule 90 (Sierpinski Pattern) ==="
python ascii_art_pro.py pattern cellular -w 70 --height 30 --rule 90
pause

# 5. Trees
echo "=== 5. DIFFERENT TREE STYLES ==="
echo ""
echo "Pine Tree:"
python ascii_art_pro.py pattern tree --height 12 --tree-style pine
echo ""
echo "Oak Tree:"
python ascii_art_pro.py pattern tree --height 12 --tree-style oak
pause

# 6. Export Demo
echo "=== 6. EXPORT FORMATS ==="
echo ""
echo "Generating exports..."

# Create output directory
mkdir -p showcase_output

# Export to different formats
python ascii_art_pro.py text "EXPORT" -o showcase_output/demo.html --format html
python ascii_art_pro.py text "EXPORT" -o showcase_output/demo.svg --format svg
python ascii_art_pro.py text "EXPORT" -o showcase_output/demo.md --format markdown
python ascii_art_pro.py pattern tree --height 10 --tree-style pine -o showcase_output/tree.txt

echo "✓ HTML export: showcase_output/demo.html"
echo "✓ SVG export: showcase_output/demo.svg"
echo "✓ Markdown export: showcase_output/demo.md"
echo "✓ Text export: showcase_output/tree.txt"
echo ""
echo "Open these files in your browser or editor to view!"
pause

# 7. Animation Preview
echo "=== 7. ANIMATION PREVIEW ==="
echo ""
echo "First frame of wave animation:"
python ascii_art_pro.py animate wave -w 60 --height 12 --frames 20
echo ""
echo "To play animations, use: --play flag"
echo "Example: python ascii_art_pro.py animate wave -w 60 --height 12 --play"
pause

# 8. Maze Generation
echo "=== 8. PROCEDURAL MAZE ==="
python ascii_art_pro.py pattern maze -w 41 --height 21
pause

# Summary
clear
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                                                               ║"
echo "║                    SHOWCASE COMPLETE!                         ║"
echo "║                                                               ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""
echo "Features Demonstrated:"
echo "  ✓ Advanced mathematical patterns (Mandelbrot, fractals)"
echo "  ✓ Text effects (shadow, 3D, outline)"
echo "  ✓ Composition system (horizontal, grid layouts)"
echo "  ✓ Cellular automata (Rule 30, 90)"
echo "  ✓ Procedural generation (trees, mazes)"
echo "  ✓ Export formats (HTML, SVG, Markdown)"
echo "  ✓ Animation capabilities"
echo ""
echo "For more information:"
echo "  - See FEATURES.md for complete documentation"
echo "  - Run: python ascii_art_pro.py --help"
echo "  - Try: python ascii_art_pro.py animate matrix --play --loop"
echo ""
echo "Exported files are in: showcase_output/"
echo ""

