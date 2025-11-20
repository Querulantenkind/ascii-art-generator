# 🚀 Quick Start Guide - ASCII Art Generator

## Three Ways to Use the Generator

### 🎨 **Method 1: Interactive TUI Editor** (RECOMMENDED for beginners!)
### 📋 **Method 2: Interactive Menu Mode** (Good for exploration)
### ⚡ **Method 3: Command-Line Mode** (Best for scripting)

---

## 🎨 Method 1: Interactive TUI Editor (NEW!)

**Best for**: Visual editing, live preview, professional results

### Launch the Editor

```bash
python ascii_art_editor.py
```

### Your First ASCII Art (30 seconds!)

1. **Press `T`** - Add text layer
2. **Type**: "HELLO"
3. **Press `P`** - Apply preset
4. **Select**: "tech_modern" (use arrow keys + Enter)
5. **Press `C`** - Copy to clipboard
6. **Press `Q`** - Quit

**Done!** Your ASCII art is now in your clipboard! Paste it anywhere with `Ctrl+V`

### Try with Demo Content

```bash
python ascii_art_editor.py --demo
```

This launches with example content so you can explore immediately!

### Essential Keyboard Shortcuts

```
H or F1    - Help (shows all shortcuts)
T          - Add text layer
P          - Apply preset style
E          - Apply effect
F          - Change font
C          - Copy to clipboard
S          - Save project
X          - Export to file
Q          - Quit
```

---

## 📋 Method 2: Interactive Menu Mode

**Best for**: Exploring features, learning capabilities

### Launch Interactive Mode

```bash
python ascii_art_generator.py
```

You'll see a menu like this:

```
╔════════════════════════════════════════╗
║   ASCII Art Generator - Main Menu      ║
╚════════════════════════════════════════╝

1. Text Art
2. Image to ASCII
3. Pattern Generation
4. Advanced Features
5. Exit

Enter your choice:
```

### Example: Create Text Art

1. **Choose**: `1` (Text Art)
2. **Enter text**: "WELCOME"
3. **Choose font**: `2` (banner)
4. **View result**: Your ASCII art appears!
5. **Save**: Choose to save to file

---

## ⚡ Method 3: Command-Line Mode

**Best for**: Quick generation, scripting, automation

### Basic Text Generation

```bash
# Simple text art
python ascii_art_generator.py text "HELLO"

# With specific font
python ascii_art_generator.py text "HELLO" --font banner

# Save to file
python ascii_art_generator.py text "HELLO" --font banner --output hello.txt
```

### Image to ASCII

```bash
# Convert image
python ascii_art_generator.py image photo.jpg

# With custom width
python ascii_art_generator.py image photo.jpg --width 100

# Save to file
python ascii_art_generator.py image photo.jpg --output ascii_photo.txt
```

### Patterns

```bash
# Generate border
python ascii_art_generator.py pattern border --width 50 --height 10

# Create box
python ascii_art_generator.py pattern box --width 40 --height 8
```

---

## 🎯 Common Use Cases

### Use Case 1: Create a Banner for README

**Using TUI Editor (Easiest):**
```bash
python ascii_art_editor.py
# Press T → "MY PROJECT"
# Press P → "bold_impact"
# Press C → copy
# Paste into README.md
```

**Using Command-Line:**
```bash
python ascii_art_generator.py text "MY PROJECT" --font banner > banner.txt
```

### Use Case 2: Convert Your Logo

**Using TUI Editor:**
```bash
python ascii_art_editor.py
# Press I → select image file (coming soon)
# Or use command-line first, then edit
```

**Using Command-Line:**
```bash
python ascii_art_generator.py image logo.png --width 80 --output logo_ascii.txt
```

### Use Case 3: Create Styled Text

**Using TUI Editor (Best):**
```bash
python ascii_art_editor.py
# Press T → "AWESOME"
# Press P → "neon_glow"
# Press E → "shadow"
# Press C → copy
```

**Using Command-Line:**
```bash
python ascii_art_pro.py text "AWESOME" --preset neon_glow --effect shadow
```

---

## 🎨 Using Presets (20 Professional Styles!)

### In TUI Editor
```bash
python ascii_art_editor.py
# Press T → enter text
# Press P → browse presets
# Select with arrows + Enter
```

### From Command-Line
```bash
# List all presets
python -c "from styles.preset_library import PresetStyleLibrary; lib = PresetStyleLibrary(); print('\n'.join([p.name for p in lib.list_presets()]))"

# Use a preset
python ascii_art_pro.py text "HELLO" --preset tech_modern
```

### Available Preset Categories
- **Tech**: tech_modern, tech_circuit, tech_matrix
- **Retro**: retro_arcade, retro_terminal, retro_dos
- **Artistic**: artistic_sketch, artistic_brush, artistic_ink
- **Bold**: bold_impact, bold_solid, bold_heavy
- **Elegant**: elegant_minimal, elegant_serif, elegant_script
- **Fun**: fun_bubble, fun_cartoon
- **Professional**: professional_corporate, professional_clean
- **Decorative**: decorative_ornate, decorative_fancy

---

## 😊 Using ASCII Emojis

### In TUI Editor
```bash
python ascii_art_editor.py
# Press T → type emoji name like ":smile:"
# Or browse emoji library (coming soon)
```

### From Python
```python
from assets.emoji_library import EmojiLibrary

lib = EmojiLibrary()

# Get specific emoji
smile = lib.get_emoji('smile')
print(smile)

# List all categories
categories = lib.list_categories()
print(categories)

# Get all emojis in category
faces = lib.get_category('faces')
for name, emoji in faces.items():
    print(f"{name}:\n{emoji}\n")
```

---

## ⚡ Using Quick Templates

### From Python
```python
from templates.quick_templates import QuickTemplates

templates = QuickTemplates()

# Create header
header = templates.create_header("MY SECTION", width=60)
print(header)

# Create box
box = templates.create_box("Important Message", width=50, height=10)
print(box)

# Create banner
banner = templates.create_banner("WELCOME", style='double')
print(banner)
```

---

## 📊 Data Visualization

### Create Charts
```python
from generators.data_viz import DataVisualizer

viz = DataVisualizer()

# Bar chart
data = {'Jan': 100, 'Feb': 150, 'Mar': 120, 'Apr': 180}
chart = viz.create_bar_chart(data, title="Monthly Sales")
print(chart)

# Line graph
values = [10, 15, 13, 18, 22, 20, 25]
graph = viz.create_line_graph(values, title="Growth Trend")
print(graph)

# Table
table_data = [
    ['Name', 'Score', 'Grade'],
    ['Alice', '95', 'A'],
    ['Bob', '87', 'B'],
    ['Carol', '92', 'A']
]
table = viz.create_table(table_data)
print(table)
```

---

## 💾 Save and Export

### In TUI Editor
```bash
# Save project
Press S → enter "myproject.aap"

# Export to format
Press X → select format → enter filename

# Copy to clipboard
Press C
```

### From Command-Line
```bash
# Save as text
python ascii_art_generator.py text "HELLO" --output hello.txt

# Export as HTML
python ascii_art_pro.py text "HELLO" --export html --output hello.html

# Export as SVG
python ascii_art_pro.py text "HELLO" --export svg --output hello.svg
```

---

## 🔧 Advanced Features

### Smart Art Generation
```python
from generators.smart_art import SmartArtGenerator

smart = SmartArtGenerator()

# Auto-generate with smart suggestions
art = smart.generate_smart("TECH COMPANY", context="logo")
print(art)
```

### Animation
```python
from generators.animation import AnimationGenerator

anim = AnimationGenerator()

# Create spinner
frames = anim.create_spinner()
for frame in frames:
    print(frame)
    time.sleep(0.1)
```

### Text Effects
```python
from generators.text_effects import TextEffects

effects = TextEffects()

text = "HELLO"

# Add shadow
print(effects.add_shadow(text))

# Add 3D effect
print(effects.add_3d_effect(text))

# Add glow
print(effects.add_glow(text))
```

---

## 📚 Complete Command Reference

### ascii_art_editor.py (TUI Editor)
```bash
python ascii_art_editor.py [options]

Options:
  --load FILE          Load project file
  --width N            Canvas width (default: 80)
  --height N           Canvas height (default: 30)
  --demo               Launch with demo content
```

### ascii_art_generator.py (Basic)
```bash
python ascii_art_generator.py [command] [args]

Commands:
  text "TEXT"          Generate text art
  image FILE           Convert image to ASCII
  pattern TYPE         Generate pattern

Options:
  --font FONT          Font style
  --width N            Output width
  --height N           Output height
  --output FILE        Save to file
```

### ascii_art_pro.py (Advanced)
```bash
python ascii_art_pro.py [command] [args]

Commands:
  text "TEXT"          Generate text art
  image FILE           Convert image
  pattern TYPE         Generate pattern
  smart "TEXT"         Smart generation

Options:
  --preset NAME        Apply preset style
  --effect NAME        Apply effect
  --font FONT          Font style
  --export FORMAT      Export format (html, svg, png, etc.)
  --output FILE        Save to file
```

---

## 🎓 Learning Path

### Day 1: Basics (5 minutes)
1. Launch TUI editor: `python ascii_art_editor.py --demo`
2. Press `H` to see help
3. Press `T` to add text
4. Press `C` to copy
5. Done!

### Day 2: Styling (10 minutes)
1. Launch editor
2. Add text layer
3. Try different presets (`P`)
4. Try different effects (`E`)
5. Try different fonts (`F`)

### Day 3: Projects (15 minutes)
1. Create multi-layer composition
2. Save project (`S`)
3. Load project (`O`)
4. Export to different formats (`X`)

### Day 4: Advanced (30 minutes)
1. Explore command-line mode
2. Try Python API
3. Create custom scripts
4. Automate workflows

---

## 💡 Pro Tips

### Tip 1: Use TUI Editor for Everything
The TUI editor is the fastest way to create professional ASCII art. Use it first!

### Tip 2: Save Projects Frequently
Press `S` often in the editor to save your work.

### Tip 3: Explore Presets
The 20 presets cover most use cases. Try them all!

### Tip 4: Use Clipboard
Press `C` in the editor to copy instantly. No need to export to file.

### Tip 5: Learn Keyboard Shortcuts
Press `H` in the editor to see all shortcuts. Learn 5 shortcuts and you'll be 10x faster!

### Tip 6: Start with Demo
Use `--demo` flag to see examples and learn by exploring.

---

## 🐛 Troubleshooting

### Editor Won't Launch
```bash
# On Windows, install curses
pip install windows-curses

# On Linux/Mac, ensure Python 3.7+
python --version
```

### Import Errors
```bash
# Install all dependencies
pip install -r requirements.txt
```

### Display Issues
- Ensure terminal is at least 80x30
- Use UTF-8 encoding
- Try different terminal emulator

---

## 📖 More Resources

- **Full Editor Guide**: `docs/EDITOR_GUIDE.md`
- **API Reference**: `docs/API_REFERENCE.md`
- **Tutorials**: `docs/TUTORIALS.md`
- **Best Practices**: `docs/BEST_PRACTICES.md`
- **Feature List**: `CAPABILITIES_V4.md`

---

## 🎉 Quick Examples

### Example 1: 10-Second Banner
```bash
python ascii_art_editor.py
# T → "HELLO" → P → tech_modern → C → Q
```

### Example 2: README Header
```bash
python ascii_art_generator.py text "MY PROJECT" --font banner > header.txt
cat header.txt
```

### Example 3: Styled Text
```bash
python ascii_art_pro.py text "AWESOME" --preset neon_glow --effect shadow
```

### Example 4: Image Conversion
```bash
python ascii_art_generator.py image photo.jpg --width 100 --output photo_ascii.txt
```

### Example 5: Data Chart
```python
from generators.data_viz import DataVisualizer
viz = DataVisualizer()
print(viz.create_bar_chart({'A': 10, 'B': 20, 'C': 15}))
```

---

## 🚀 You're Ready!

**Start with the TUI Editor:**
```bash
python ascii_art_editor.py --demo
```

**Press `H` for help and explore!**

**Create professional ASCII art in 30 seconds! 🎨✨**
