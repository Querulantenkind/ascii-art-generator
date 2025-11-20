#!/bin/bash
# Example usage of ASCII Art Generator

echo "=== ASCII Art Generator Examples ==="
echo ""

echo "1. Text Art - Standard Font"
python ascii_art_generator.py text "HELLO"
echo ""

echo "2. Text Art - Block Font"
python ascii_art_generator.py text "CODE" -f block
echo ""

echo "3. Text Art - Bubble Font"
python ascii_art_generator.py text "ASCII" -f bubble
echo ""

echo "4. Diamond Pattern"
python ascii_art_generator.py pattern diamond -w 25 --height 9
echo ""

echo "5. Wave Pattern"
python ascii_art_generator.py pattern wave -w 50 --height 8
echo ""

echo "6. Box with Single Border"
python ascii_art_generator.py pattern box -w 50 --height 6 -s single
echo ""

echo "7. Box with Double Border"
python ascii_art_generator.py pattern box -w 50 --height 6 -s double
echo ""

echo "8. Border Frame"
python ascii_art_generator.py pattern border -w 60 -s thick
echo ""

echo "=== All examples completed! ==="

