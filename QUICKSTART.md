# Quick Start Guide

Get started with ASCII Art Generator in 3 easy steps!

## Step 1: Install (Optional Dependencies)

For basic text and pattern generation, no installation needed! Just run:

```bash
python ascii_art_generator.py
```

For image-to-ASCII conversion, install Pillow:

```bash
pip install -r requirements.txt
```

## Step 2: Try It Out

### Interactive Mode (Recommended for Beginners)

```bash
python ascii_art_generator.py -i
```

Follow the on-screen menu to explore all features!

### Quick Command-Line Examples

```bash
# Generate text art
python ascii_art_generator.py text "HELLO"

# Try different fonts
python ascii_art_generator.py text "ASCII" -f banner
python ascii_art_generator.py text "CODE" -f block

# Create patterns
python ascii_art_generator.py pattern diamond -w 30 --height 10
python ascii_art_generator.py pattern box -w 50 --height 8 -s double

# Convert an image (requires Pillow)
python ascii_art_generator.py image photo.jpg -w 80
```

## Step 3: Save Your Art

Add `-o filename.txt` to save output:

```bash
python ascii_art_generator.py text "SAVE ME" -f banner -o myart.txt
```

## Common Use Cases

### 1. Create a Banner for Your Terminal

```bash
python ascii_art_generator.py text "Welcome" -f banner
```

### 2. Frame Text with a Border

```bash
# First create a border
python ascii_art_generator.py pattern box -w 60 --height 8 -s double
```

### 3. Generate Decorative Patterns

```bash
# Diamond
python ascii_art_generator.py pattern diamond -w 40 --height 15

# Wave
python ascii_art_generator.py pattern wave -w 60 --height 10
```

### 4. Convert Your Photo to ASCII

```bash
python ascii_art_generator.py image selfie.jpg -w 100 -c detailed
```

## Tips

- **Terminal Width**: Most terminals are 80-120 characters wide
- **Font Selection**: Try different fonts to see which looks best
- **Image Quality**: High-contrast images work best for conversion
- **Unicode Support**: Use `-s ascii` if Unicode characters don't display properly

## Need Help?

Run with `-h` for help:

```bash
python ascii_art_generator.py -h
python ascii_art_generator.py text -h
python ascii_art_generator.py image -h
python ascii_art_generator.py pattern -h
```

Or launch interactive mode and select option 7 (Help) from the menu.

## Run All Examples

```bash
./examples.sh
```

Enjoy creating ASCII art! 🎨

