## ASCII Art Generator Pro - Extended Features Guide

This document describes all the advanced features added to the ASCII Art Generator.

---

## 🎨 Text Effects

Apply stunning visual effects to your ASCII art text.

### Available Effects

#### Shadow Effect
Add depth with drop shadows:
```bash
python ascii_art_pro.py text "SHADOW" --effect shadow
```

#### Outline Effect
Frame your text with borders:
```bash
python ascii_art_pro.py text "OUTLINE" --effect outline
```

#### 3D Effect
Create perspective depth:
```bash
python ascii_art_pro.py text "3D TEXT" --effect 3d
```

#### Glow Effect
Add a glowing aura:
```bash
python ascii_art_pro.py text "GLOW" --effect glow
```

#### Mirror Effect
Create symmetrical reflections:
```bash
python ascii_art_pro.py text "MIRROR" --effect mirror
```

#### Neon Effect
Simulate neon signs:
```bash
python ascii_art_pro.py text "NEON" --effect neon
```

---

## 🌈 Color Gradients

Apply beautiful color gradients to ASCII art (requires terminal color support).

### Available Gradients

```bash
# Rainbow gradient
python ascii_art_pro.py text "RAINBOW" --gradient rainbow --color

# Fire gradient (red to yellow)
python ascii_art_pro.py text "FIRE" --gradient fire --color

# Ocean gradient (blue to cyan)
python ascii_art_pro.py text "OCEAN" --gradient ocean --color

# Forest gradient (dark to light green)
python ascii_art_pro.py text "FOREST" --gradient forest --color
```

### Colored Image Conversion

Convert images to colored ASCII art:
```bash
python ascii_art_pro.py image photo.jpg --colored --color -w 100
```

---

## 🔮 Advanced Patterns

Generate complex mathematical and algorithmic patterns.

### Mandelbrot Set
```bash
python ascii_art_pro.py pattern mandelbrot -w 80 -h 40
```

### Julia Set
```bash
python ascii_art_pro.py pattern julia -w 80 -h 40
```

### Maze Generator
```bash
# Width and height must be odd numbers
python ascii_art_pro.py pattern maze -w 51 -h 31
```

### Spiral
```bash
python ascii_art_pro.py pattern spiral --size 25
```

### Sierpinski Triangle
```bash
python ascii_art_pro.py pattern sierpinski --size 6
```

### Cellular Automaton
```bash
# Rule 30 (chaotic)
python ascii_art_pro.py pattern cellular -w 80 -h 40 --rule 30

# Rule 90 (Sierpinski)
python ascii_art_pro.py pattern cellular -w 80 -h 40 --rule 90

# Rule 110 (complex)
python ascii_art_pro.py pattern cellular -w 80 -h 40 --rule 110
```

### Lissajous Curves
```bash
python ascii_art_pro.py pattern lissajous -w 60 -h 30
```

### ASCII Trees
```bash
# Pine tree
python ascii_art_pro.py pattern tree -h 15 --tree-style pine

# Oak tree
python ascii_art_pro.py pattern tree -h 15 --tree-style oak

# Palm tree
python ascii_art_pro.py pattern tree -h 15 --tree-style palm
```

---

## 🎬 Animations

Create animated ASCII art with multiple frames.

### Wave Animation
```bash
# Preview first frame
python ascii_art_pro.py animate wave -w 60 -h 15 --frames 30

# Play in terminal
python ascii_art_pro.py animate wave -w 60 -h 15 --frames 30 --play

# Loop continuously
python ascii_art_pro.py animate wave -w 60 -h 15 --frames 30 --play --loop

# Export frames to directory
python ascii_art_pro.py animate wave -w 60 -h 15 --frames 30 -o ./frames/
```

### Bouncing Ball
```bash
python ascii_art_pro.py animate bounce -w 40 -h 10 --frames 20 --play
```

### Matrix Rain
```bash
python ascii_art_pro.py animate matrix -w 80 -h 20 --frames 50 --play --loop
```

### Spinning Loader
```bash
python ascii_art_pro.py animate spinner --frames 8 --play --loop
```

### Progress Bar
```bash
python ascii_art_pro.py animate progress -w 50 --frames 20 --play
```

### Scrolling Text
```bash
python ascii_art_pro.py animate scroll --text "Welcome to ASCII Art!" -w 80 --play
```

### Typewriter Effect
```bash
python ascii_art_pro.py animate typewriter --text "Hello World!" --play
```

---

## 🧩 Composition System

Combine multiple ASCII art elements into complex compositions.

### Horizontal Concatenation
```bash
python ascii_art_pro.py compose --horizontal "LEFT" "CENTER" "RIGHT" -o combined.txt
```

### Vertical Stacking
```bash
python ascii_art_pro.py compose --vertical "TOP" "MIDDLE" "BOTTOM" -o stacked.txt
```

### Grid Layout
```bash
# 2x2 grid
python ascii_art_pro.py compose --grid "A" "B" "C" "D" --cols 2 -o grid.txt

# 3x2 grid
python ascii_art_pro.py compose --grid "1" "2" "3" "4" "5" "6" --cols 3 -o grid.txt
```

### Programmatic Composition (Python API)

```python
from generators.composition import Compositor, Composition
from generators.text_art import TextArtGenerator
from utils.config import Config

# Create compositor
compositor = Compositor()

# Generate some art
config = Config()
gen = TextArtGenerator(config)
art1 = gen.generate("HELLO", font='standard')
art2 = gen.generate("WORLD", font='banner')

# Combine horizontally
combined = compositor.horizontal_concat(art1, art2, spacing=5)
print(combined)

# Or use layered composition
composition = Composition(width=100, height=30)
composition.add_layer(art1, x=10, y=5, z_index=1)
composition.add_layer(art2, x=50, y=10, z_index=2)
result = composition.render()
print(result)
```

---

## 📤 Export Formats

Export your ASCII art to various formats for different use cases.

### HTML Export
```bash
python ascii_art_pro.py text "HTML" -o output.html --format html
```

Features:
- Monospace font styling
- Customizable colors
- Responsive design
- Border and padding

### SVG Export
```bash
python ascii_art_pro.py text "SVG" -o output.svg --format svg
```

Features:
- Vector format (scalable)
- Embedded fonts
- Customizable colors
- XML-based

### Markdown Export
```bash
python ascii_art_pro.py text "MARKDOWN" -o output.md --format markdown
```

Features:
- Code block formatting
- Metadata support
- Compatible with GitHub, GitLab, etc.

### PNG Image Export
```bash
python ascii_art_pro.py text "IMAGE" -o output.png --format png
```

Features:
- Raster image format
- Monospace font rendering
- Customizable colors
- Requires Pillow library

### JSON Export
```bash
python ascii_art_pro.py text "JSON" -o output.json --format json
```

Features:
- Structured data format
- Includes metadata
- Line-by-line array
- Dimensions included

---

## 🎯 Use Cases & Examples

### 1. Create a Fancy Terminal Banner

```bash
# Generate text with 3D effect and gradient
python ascii_art_pro.py text "WELCOME" --effect 3d --gradient rainbow --color

# Frame it
python ascii_art_pro.py text "WELCOME" --effect outline -o banner.txt
```

### 2. Generate a Loading Animation

```bash
# Create and play a spinner
python ascii_art_pro.py animate spinner --frames 8 --play --loop
```

### 3. Create ASCII Art Wallpaper

```bash
# Generate Mandelbrot set
python ascii_art_pro.py pattern mandelbrot -w 120 -h 60 -o mandelbrot.txt

# Export as image
python ascii_art_pro.py pattern mandelbrot -w 120 -h 60 -o mandelbrot.png --format png
```

### 4. Build a Dashboard Layout

```bash
# Create split-screen layout with composition
python ascii_art_pro.py compose --horizontal "STATUS" "METRICS" "LOGS" -o dashboard.txt
```

### 5. Generate Procedural Art

```bash
# Cellular automaton with different rules
python ascii_art_pro.py pattern cellular -w 100 -h 50 --rule 30 -o rule30.txt
python ascii_art_pro.py pattern cellular -w 100 -h 50 --rule 90 -o rule90.txt
python ascii_art_pro.py pattern cellular -w 100 -h 50 --rule 110 -o rule110.txt
```

### 6. Create Animated GIF (with external tools)

```bash
# Export animation frames
python ascii_art_pro.py animate wave -w 60 -h 20 --frames 30 -o ./frames/

# Convert each frame to PNG
for f in frames/*.txt; do
    python ascii_art_pro.py text "$(cat $f)" -o "${f%.txt}.png" --format png
done

# Use ImageMagick to create GIF
convert -delay 10 -loop 0 frames/*.png animation.gif
```

---

## 🔧 Python API Usage

All features are available as Python modules for programmatic use.

### Text Effects Example

```python
from generators.text_art import TextArtGenerator
from generators.text_effects import TextEffects
from utils.config import Config

config = Config()
gen = TextArtGenerator(config)
effects = TextEffects()

# Generate text
art = gen.generate("HELLO", font='standard')

# Apply effects
shadowed = effects.add_shadow(art)
outlined = effects.add_outline(art)
glowing = effects.add_glow(art, intensity=3)

print(glowing)
```

### Animation Example

```python
from generators.animation import AnimationGenerator

gen = AnimationGenerator()

# Create animation
animation = gen.wave_animation(width=60, height=15, frames=30)

# Play it
animation.play(loop=True)

# Or export frames
animation.export_frames('./output', prefix='wave')
```

### Color Gradient Example

```python
from generators.color_art import GradientGenerator
from generators.text_art import TextArtGenerator
from utils.config import Config

config = Config(color_enabled=True)
gen = TextArtGenerator(config)
gradient_gen = GradientGenerator()

# Generate text
art = gen.generate("RAINBOW", font='banner')

# Apply gradient
colored = gradient_gen.apply_gradient_to_text(art, 'rainbow')

print(colored)
```

### Pattern Generation Example

```python
from generators.advanced_patterns import AdvancedPatternGenerator

gen = AdvancedPatternGenerator()

# Generate various patterns
mandelbrot = gen.generate_mandelbrot(width=80, height=40)
maze = gen.generate_maze(width=51, height=31)
spiral = gen.generate_spiral(size=25)
tree = gen.generate_tree(height=15, style='pine')

print(tree)
```

---

## 💡 Tips & Best Practices

1. **Terminal Size**: Check your terminal width before generating large art
   ```bash
   tput cols  # Get terminal width
   tput lines # Get terminal height
   ```

2. **Color Support**: Test if your terminal supports colors
   ```bash
   python ascii_art_pro.py text "TEST" --gradient rainbow --color
   ```

3. **Performance**: Large patterns and high frame counts may be slow
   - Start with smaller dimensions
   - Reduce frame count for animations
   - Use simpler character sets for images

4. **File Formats**:
   - Use **text** for terminal display
   - Use **HTML** for web embedding
   - Use **SVG** for scalable graphics
   - Use **PNG** for sharing images
   - Use **Markdown** for documentation

5. **Composition**:
   - Plan your layout before composing
   - Use consistent dimensions
   - Test individual elements first

6. **Animations**:
   - Press Ctrl+C to stop playback
   - Export frames for complex editing
   - Use `--loop` for continuous display

---

## 🚀 Advanced Techniques

### Combining Multiple Effects

```python
from generators.text_art import TextArtGenerator
from generators.text_effects import TextEffects
from generators.color_art import GradientGenerator
from utils.config import Config

config = Config(color_enabled=True)
gen = TextArtGenerator(config)
effects = TextEffects()
gradient_gen = GradientGenerator()

# Generate text
art = gen.generate("EPIC", font='banner')

# Apply multiple effects
art = effects.add_3d_effect(art, depth=5)
art = effects.add_glow(art, intensity=2)
art = gradient_gen.apply_gradient_to_text(art, 'fire')

print(art)
```

### Custom Compositions

```python
from generators.composition import Composition, Compositor
from generators.pattern_art import PatternGenerator
from generators.text_art import TextArtGenerator
from utils.config import Config

config = Config()
compositor = Compositor()
pattern_gen = PatternGenerator(config)
text_gen = TextArtGenerator(config)

# Create elements
title = text_gen.generate("MY APP", font='banner')
border = pattern_gen.generate_box(80, 30, style='double')

# Frame the title
framed = compositor.frame(title, title="Welcome", style='double')

print(framed)
```

---

## 📚 Further Reading

- See `DESIGN.md` for architecture details
- See `README.md` for basic usage
- See `QUICKSTART.md` for getting started
- Check source code for advanced customization

---

**Enjoy creating amazing ASCII art! 🎨**

