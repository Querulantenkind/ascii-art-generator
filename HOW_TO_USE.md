# 🎨 How to Use the ASCII Art Generator

## 📋 Table of Contents
1. [Absolute Beginner Start](#absolute-beginner-start)
2. [Three Usage Methods](#three-usage-methods)
3. [Common Tasks](#common-tasks)
4. [Real Examples](#real-examples)
5. [Next Steps](#next-steps)

---

## 🌟 Absolute Beginner Start

### Your First ASCII Art (30 Seconds!)

**Step 1**: Open your terminal in this directory

**Step 2**: Run this command:
```bash
python ascii_art_editor.py --demo
```

**Step 3**: You'll see the interactive editor. Press these keys:
- Press `H` - See help
- Press `T` - Add text (type "HELLO")
- Press `P` - Apply preset (select "tech_modern")
- Press `C` - Copy to clipboard
- Press `Q` - Quit

**Step 4**: Paste anywhere with `Ctrl+V` (or `Cmd+V` on Mac)

**🎉 Congratulations! You just created professional ASCII art!**

---

## 🎯 Three Usage Methods

### Method 1: 🎨 Interactive TUI Editor (BEST for most users!)

**What it is**: A visual editor with live preview, like Photoshop for ASCII art

**When to use**: Creating anything visual, experimenting with styles, professional work

**How to launch**:
```bash
python ascii_art_editor.py
```

**What you can do**:
- ✅ See your art in real-time
- ✅ Try different styles instantly
- ✅ Manage multiple layers
- ✅ Undo/Redo (Ctrl+Z/Y)
- ✅ Copy to clipboard (C key)
- ✅ Save projects (S key)
- ✅ Export to files (X key)

**Example workflow**:
```
Launch → Press T → Type text → Press P → Select style → Press C → Done!
```

---

### Method 2: 📋 Interactive Menu Mode (GOOD for exploring)

**What it is**: A menu-driven interface that guides you through options

**When to use**: Learning features, exploring capabilities, guided creation

**How to launch**:
```bash
python ascii_art_generator.py
```

**What you see**:
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

**Example workflow**:
```
Launch → Choose 1 → Enter text → Choose font → View result → Save
```

---

### Method 3: ⚡ Command-Line Mode (BEST for automation)

**What it is**: Direct commands for quick generation

**When to use**: Scripting, automation, quick one-offs, batch processing

**How to use**:
```bash
# Basic syntax
python ascii_art_generator.py [command] [text/file] [options]
```

**Example workflow**:
```bash
python ascii_art_generator.py text "HELLO" --font banner
```

---

## 🔥 Common Tasks

### Task 1: Create a Text Banner

**Using TUI Editor** (Easiest):
```bash
python ascii_art_editor.py
# Press T → "MY BANNER" → P → bold_impact → C
```

**Using Command-Line** (Fastest):
```bash
python ascii_art_generator.py text "MY BANNER" --font banner
```

**Result**:
```
 ##################################################
#                                                  #
#    M      Y            B      A      N      N    #
#                                                  #
 ##################################################
```

---

### Task 2: Create Styled Text with Preset

**Using TUI Editor**:
```bash
python ascii_art_editor.py
# Press T → "COOL" → P → neon_glow → C
```

**Using Command-Line**:
```bash
python ascii_art_pro.py text "COOL" --preset neon_glow
```

**Result**: Professional styled text with borders and effects!

---

### Task 3: Convert Image to ASCII

**Using Command-Line**:
```bash
python ascii_art_generator.py image yourphoto.jpg --width 80
```

**Save to file**:
```bash
python ascii_art_generator.py image yourphoto.jpg --width 80 --output photo_ascii.txt
```

---

### Task 4: Create README Header

**Quick method**:
```bash
python ascii_art_generator.py text "MY PROJECT" --font banner > header.txt
```

**Then in your README.md**:
```markdown
# My Project

```
[paste ASCII art here]
```

Welcome to my project!
```

---

### Task 5: Create Multi-Layer Composition

**Using TUI Editor** (Only way):
```bash
python ascii_art_editor.py

# Add title layer
Press T → "TITLE"
Press P → bold_impact

# Add subtitle layer
Press T → "subtitle"
Press F → small

# Position layers
Use arrow keys to move

# Save project
Press S → "myproject.aap"

# Export
Press X → html → "output.html"
```

---

### Task 6: Use ASCII Emojis

**From Python**:
```python
from assets.emoji_library import EmojiLibrary

lib = EmojiLibrary()

# Get a smiley
print(lib.get_emoji('smile'))

# List all
for name in lib.list_emojis():
    print(name)
```

**Result**:
```
  ^___^
 ( o.o )
  > ^ <
```

---

### Task 7: Create Data Visualization

**From Python**:
```python
from generators.data_viz import DataVisualizer

viz = DataVisualizer()

# Bar chart
data = {'Jan': 100, 'Feb': 150, 'Mar': 120}
print(viz.create_bar_chart(data, title="Sales"))
```

**Result**:
```
Sales
─────────────────────────
Jan  ████████████ 100
Feb  ██████████████████ 150
Mar  ██████████████ 120
```

---

### Task 8: Quick Templates

**From Python**:
```python
from templates.quick_templates import QuickTemplates

templates = QuickTemplates()

# Create header
print(templates.create_header("SECTION", width=50))

# Create box
print(templates.create_box("Important!", width=40, height=8))

# Create banner
print(templates.create_banner("WELCOME"))
```

---

## 💡 Real Examples

### Example 1: GitHub README Header

```bash
# Generate
python ascii_art_generator.py text "AWESOME PROJECT" --font banner > header.txt

# Use in README.md
```

**README.md**:
```markdown
```
 ##################################################
#    AWESOME PROJECT                               #
 ##################################################
```

[![License](https://img.shields.io/badge/license-MIT-blue.svg)]()

> An awesome project that does awesome things
```

---

### Example 2: Terminal App Banner

```python
#!/usr/bin/env python3
from generators.text_art import TextArtGenerator
from utils.config import Config

def show_banner():
    config = Config()
    gen = TextArtGenerator(config)
    banner = gen.generate("MY APP", font='banner')
    print(banner)
    print("Version 1.0.0\n")

if __name__ == '__main__':
    show_banner()
    # Rest of your app...
```

---

### Example 3: Status Dashboard

```python
from generators.data_viz import DataVisualizer
from templates.quick_templates import QuickTemplates

viz = DataVisualizer()
templates = QuickTemplates()

# Header
print(templates.create_header("SYSTEM STATUS", width=60))

# Metrics
metrics = {
    'CPU': 45,
    'Memory': 62,
    'Disk': 78,
    'Network': 23
}

print(viz.create_bar_chart(metrics, title="Resource Usage", max_value=100))

# Progress bars
print("\nActive Tasks:")
print(viz.create_progress_bar(75, width=40, label="Task 1"))
print(viz.create_progress_bar(30, width=40, label="Task 2"))
```

---

### Example 4: Automated Report

```bash
#!/bin/bash
# generate_report.sh

# Header
python ascii_art_generator.py text "DAILY REPORT" --font banner > report.txt

# Add date
echo "" >> report.txt
echo "Date: $(date)" >> report.txt
echo "" >> report.txt

# Add data visualization
python -c "
from generators.data_viz import DataVisualizer
viz = DataVisualizer()
data = {'Mon': 120, 'Tue': 145, 'Wed': 132, 'Thu': 156, 'Fri': 170}
print(viz.create_bar_chart(data, title='Weekly Performance'))
" >> report.txt

echo "Report generated: report.txt"
```

---

### Example 5: Interactive CLI Tool

```python
#!/usr/bin/env python3
from styles.preset_library import PresetStyleLibrary

def main():
    lib = PresetStyleLibrary()
    
    print("Welcome to Style Generator!")
    print("Available presets:", ", ".join([p.name for p in lib.list_presets()]))
    
    text = input("\nEnter text: ")
    preset = input("Choose preset: ")
    
    art = lib.apply_preset(text, preset, apply_colors=False)
    print("\n" + art)
    
    # Copy to clipboard
    from utils.clipboard import ClipboardManager
    clipboard = ClipboardManager()
    if clipboard.copy(art):
        print("\n✓ Copied to clipboard!")

if __name__ == '__main__':
    main()
```

---

## 🎓 Learning Path

### Week 1: Basics
**Day 1**: Try TUI editor with demo
```bash
python ascii_art_editor.py --demo
```

**Day 2**: Create your first text art
```bash
python ascii_art_editor.py
# Press T, enter text, press C
```

**Day 3**: Try all presets
```bash
# In editor, press P and try each one
```

**Day 4**: Learn keyboard shortcuts
```bash
# In editor, press H to see all shortcuts
```

**Day 5**: Save and load projects
```bash
# Press S to save, O to open
```

---

### Week 2: Command-Line
**Day 1**: Basic text generation
```bash
python ascii_art_generator.py text "TEST"
```

**Day 2**: Try different fonts
```bash
python ascii_art_generator.py text "TEST" --font banner
python ascii_art_generator.py text "TEST" --font block
```

**Day 3**: Image conversion
```bash
python ascii_art_generator.py image photo.jpg
```

**Day 4**: Use presets
```bash
python ascii_art_pro.py text "TEST" --preset tech_modern
```

**Day 5**: Export to files
```bash
python ascii_art_generator.py text "TEST" --output test.txt
```

---

### Week 3: Advanced
**Day 1**: Multi-layer compositions
**Day 2**: Python API usage
**Day 3**: Data visualization
**Day 4**: Custom scripts
**Day 5**: Automation

---

## 🚀 Next Steps

### 1. Read Full Documentation
- `QUICKSTART.md` - Quick reference
- `docs/EDITOR_GUIDE.md` - Complete editor guide
- `docs/TUTORIALS.md` - Step-by-step tutorials
- `docs/API_REFERENCE.md` - Python API docs

### 2. Try Examples
```bash
# Run demo script
python demo_new_features.py

# Try showcase
bash showcase_pro.sh
```

### 3. Explore Features
- Try all 20 presets
- Browse 185+ emojis
- Test quick templates
- Create data visualizations

### 4. Build Something
- Create README headers
- Design terminal banners
- Build CLI tools
- Generate reports

---

## 🎯 Quick Reference Card

```
╔═══════════════════════════════════════════════════════════════╗
║                    QUICK REFERENCE                            ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  TUI EDITOR (Recommended!)                                    ║
║  └─ python ascii_art_editor.py --demo                         ║
║                                                               ║
║  KEYBOARD SHORTCUTS:                                          ║
║  ├─ H/F1    Help          ├─ S    Save                       ║
║  ├─ T       Add text      ├─ O    Open                       ║
║  ├─ P       Preset        ├─ C    Copy                       ║
║  ├─ E       Effect        ├─ X    Export                     ║
║  ├─ F       Font          ├─ Q    Quit                       ║
║  └─ Arrows  Move layer    └─ Ctrl+Z/Y  Undo/Redo            ║
║                                                               ║
║  COMMAND-LINE:                                                ║
║  ├─ python ascii_art_generator.py text "TEXT"                ║
║  ├─ python ascii_art_generator.py image FILE                 ║
║  └─ python ascii_art_pro.py text "TEXT" --preset STYLE       ║
║                                                               ║
║  INTERACTIVE MENU:                                            ║
║  └─ python ascii_art_generator.py                            ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## ❓ FAQ

**Q: Which method should I use?**
A: Start with the TUI Editor (`python ascii_art_editor.py --demo`). It's the easiest and most powerful!

**Q: How do I save my work?**
A: In TUI editor, press `S`. From command-line, use `--output filename.txt`.

**Q: Can I use this in my project?**
A: Yes! Use the Python API or command-line in your scripts.

**Q: How do I copy to clipboard?**
A: In TUI editor, press `C`. Or use the ClipboardManager class in Python.

**Q: What are presets?**
A: 20 professional styles you can apply instantly. Try them with `P` in the editor!

**Q: Can I convert images?**
A: Yes! Use `python ascii_art_generator.py image yourfile.jpg`

**Q: Is there a GUI?**
A: The TUI editor IS the GUI! It runs in your terminal with full interactivity.

---

## 🎉 You're Ready!

**Start creating now:**
```bash
python ascii_art_editor.py --demo
```

**Press `H` for help and explore!**

**Have fun creating ASCII art! 🎨✨**

