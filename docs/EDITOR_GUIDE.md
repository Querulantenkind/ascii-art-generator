# Interactive TUI Editor Guide

## 🎨 ASCII Art Editor - Professional Real-Time Editing

The Interactive TUI (Terminal User Interface) Editor provides a professional, real-time editing environment for creating ASCII art with live preview, layer management, and comprehensive keyboard shortcuts.

---

## 🚀 Quick Start

### Launch the Editor

```bash
# Basic launch
python ascii_art_editor.py

# Launch with demo content
python ascii_art_editor.py --demo

# Open existing project
python ascii_art_editor.py --load myproject.aap

# Custom canvas size
python ascii_art_editor.py --width 100 --height 40
```

---

## 🖥️ Editor Interface

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ [N]ew [T]ext [E]ffect [F]ont [P]reset [S]ave [O]pen [C]opy e[X]port [Q]uit │
├──────────────────────────────────────────────┬──────────────────────────────┤
│                                              │  Layers                      │
│                                              │  ┌────────────────────────┐  │
│                                              │  │ >● Text: HELLO         │  │
│            [Live Preview Area]               │  │  ● Layer 2             │  │
│                                              │  │  ○ Background          │  │
│         [Your ASCII art appears here         │  └────────────────────────┘  │
│          with real-time updates]             │                              │
│                                              │  [L] Toggle panel            │
│                                              │                              │
├──────────────────────────────────────────────┴──────────────────────────────┤
│ Layers: 3 | Current: Text: HELLO | Font: banner | Undo: ✓ | Redo: ✗       │
│ ℹ Layer added successfully                                                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## ⌨️ Keyboard Shortcuts

### General
| Key | Action | Description |
|-----|--------|-------------|
| `H` or `F1` | Help | Toggle help overlay |
| `Q` | Quit | Exit editor (with confirmation) |
| `Ctrl+Z` | Undo | Undo last action |
| `Ctrl+Y` | Redo | Redo last undone action |

### Layers
| Key | Action | Description |
|-----|--------|-------------|
| `N` | New Layer | Create empty layer |
| `T` | Text Layer | Add text layer with input |
| `L` | Toggle Layers | Cycle through layers |
| `Arrow Keys` | Move Layer | Move current layer position |

### Styling
| Key | Action | Description |
|-----|--------|-------------|
| `F` | Font | Change font style |
| `E` | Effect | Apply visual effect |
| `P` | Preset | Apply preset style |

### File Operations
| Key | Action | Description |
|-----|--------|-------------|
| `S` | Save | Save project to file |
| `O` | Open | Open existing project |
| `C` | Copy | Copy to clipboard |
| `X` | Export | Export to various formats |

---

## 🎯 Features

### 1. **Live Preview**
- Real-time rendering
- Instant feedback
- Layer composition
- Visual editing

### 2. **Layer Management**
- Multiple layers
- Z-index ordering
- Show/hide layers
- Layer selection
- Position control

### 3. **Undo/Redo System**
- 50-step history
- State management
- Non-destructive editing
- History navigation

### 4. **Preset Integration**
- 20 professional presets
- One-click application
- Style preview
- Context-aware suggestions

### 5. **Effect System**
- Shadow, 3D, Outline
- Glow, Mirror, Neon
- Real-time application
- Effect stacking

### 6. **Project Management**
- Save/Load projects (.aap format)
- JSON-based format
- Metadata storage
- Version tracking

### 7. **Export System**
- Text, HTML, SVG
- Markdown, PNG
- Multiple formats
- One-click export

### 8. **Clipboard Integration**
- Cross-platform support
- One-key copy
- Seamless workflow
- Paste anywhere

---

## 📚 Workflows

### Workflow 1: Create Simple Banner

1. Launch editor: `python ascii_art_editor.py`
2. Press `T` to add text layer
3. Enter text: "HELLO"
4. Press `P` to apply preset
5. Select: "tech_modern"
6. Press `C` to copy to clipboard
7. Press `Q` to quit

**Time: 30 seconds!**

### Workflow 2: Multi-Layer Composition

1. Launch editor
2. Press `T` and add "TITLE"
3. Press `T` and add "SUBTITLE"
4. Use arrow keys to position layers
5. Press `E` to add effects
6. Press `S` to save project
7. Press `X` to export as HTML

### Workflow 3: Edit Existing Project

1. Launch: `python ascii_art_editor.py --load myproject.aap`
2. Press `L` to select layer
3. Press `E` to modify effects
4. Press `F` to change font
5. Press `S` to save changes

---

## 🎨 Layer System

### Layer Types
- **Text Layers**: Generated from text input
- **Pattern Layers**: Geometric patterns
- **Image Layers**: Converted images
- **Empty Layers**: Manual content

### Layer Properties
- **Name**: Layer identifier
- **Content**: ASCII art content
- **Position**: X, Y coordinates
- **Z-Index**: Stacking order
- **Visibility**: Show/hide toggle

### Layer Operations
- **Create**: Add new layers
- **Select**: Choose active layer
- **Move**: Reposition with arrows
- **Toggle**: Show/hide layers
- **Delete**: Remove layers (coming soon)

---

## 💾 Project File Format

Projects are saved as `.aap` (ASCII Art Project) files in JSON format:

```json
{
  "version": "1.0",
  "layers": [
    {
      "id": 1,
      "name": "Text: HELLO",
      "content": "ASCII art content here",
      "visible": true,
      "x": 10,
      "y": 5,
      "z_index": 0
    }
  ],
  "settings": {
    "font": "banner",
    "effect": "3d",
    "preset": "tech_modern"
  },
  "metadata": {
    "created": "2025-11-20T12:00:00",
    "layer_count": 1
  }
}
```

---

## 🔧 Advanced Features

### Undo/Redo System
- **History Size**: 50 states
- **Shortcuts**: Ctrl+Z (undo), Ctrl+Y (redo)
- **State Management**: Full layer state preservation
- **Non-Destructive**: All changes reversible

### Mouse Support
- **Click**: Select layers (coming soon)
- **Drag**: Move layers (coming soon)
- **Scroll**: Navigate canvas (coming soon)

### Auto-Save
- **Coming Soon**: Automatic project backup
- **Interval**: Every 5 minutes
- **Recovery**: Crash recovery

---

## 💡 Tips & Tricks

### 1. Use Presets for Quick Results
Press `P` and select a preset for instant professional styling.

### 2. Layer Organization
Name your layers descriptively for easy management.

### 3. Keyboard Workflow
Learn keyboard shortcuts for 10x faster editing.

### 4. Save Often
Use `S` frequently to save your work.

### 5. Preview Before Export
Check the preview before exporting to ensure quality.

### 6. Use Undo Liberally
Don't be afraid to experiment - Ctrl+Z is your friend!

---

## 🐛 Troubleshooting

### Editor Won't Launch

**Issue**: `ImportError: No module named '_curses'`

**Solution** (Windows):
```bash
pip install windows-curses
```

**Solution** (Linux/Mac):
Curses is built-in, but ensure you're using Python 3.7+

### Display Issues

**Issue**: Characters not displaying correctly

**Solution**:
- Ensure terminal supports UTF-8
- Try different terminal emulator
- Check terminal size (minimum 80x30)

### Mouse Not Working

**Issue**: Mouse clicks not registering

**Solution**:
- Ensure terminal supports mouse events
- Try different terminal (xterm, gnome-terminal work well)
- Mouse support varies by terminal

---

## 📖 Tutorial: First Project

### Step-by-Step Guide

1. **Launch Editor**
   ```bash
   python ascii_art_editor.py --demo
   ```

2. **Explore Interface**
   - See the demo layer in preview
   - Notice the layers panel on the right
   - Check the toolbar at top
   - View status bar at bottom

3. **Add New Text Layer**
   - Press `T`
   - Enter text: "MY PROJECT"
   - See it appear in preview

4. **Apply Preset Style**
   - Press `P`
   - Use arrow keys to select "tech_modern"
   - Press Enter
   - See instant professional styling!

5. **Move Layer**
   - Use arrow keys to reposition
   - See live preview update

6. **Apply Effect**
   - Press `E`
   - Select "shadow"
   - See effect applied instantly

7. **Save Project**
   - Press `S`
   - Enter filename: "myproject.aap"
   - Project saved!

8. **Copy to Clipboard**
   - Press `C`
   - Art copied to clipboard
   - Paste anywhere with Ctrl+V

9. **Export**
   - Press `X`
   - Select format (HTML, SVG, etc.)
   - Enter filename
   - File exported!

10. **Quit**
    - Press `Q`
    - Confirm if unsaved changes
    - Done!

---

## 🎓 Advanced Tutorial: Complex Composition

### Creating a Multi-Layer Design

1. **Setup**
   ```bash
   python ascii_art_editor.py --width 100 --height 40
   ```

2. **Create Title Layer**
   - Press `T`, enter "TITLE"
   - Press `P`, select "bold_impact"
   - Position at top with arrows

3. **Create Subtitle Layer**
   - Press `T`, enter "Subtitle text"
   - Press `F`, select "small"
   - Position below title

4. **Add Decorative Elements**
   - Press `T`, enter "---"
   - Position as divider

5. **Apply Effects**
   - Select each layer with `L`
   - Apply different effects with `E`

6. **Fine-Tune Positions**
   - Use arrow keys for pixel-perfect positioning
   - Check preview constantly

7. **Save and Export**
   - Save project: `S`
   - Export as HTML: `X` → html
   - Copy to clipboard: `C`

---

## 🔮 Coming Soon

### Planned Features
- [ ] Layer deletion
- [ ] Layer duplication
- [ ] Layer opacity
- [ ] Color picker
- [ ] Grid snapping
- [ ] Ruler guides
- [ ] Zoom in/out
- [ ] Pan canvas
- [ ] Search and replace
- [ ] Batch operations
- [ ] Macro recording
- [ ] Plugin support

---

## 📊 Performance

### System Requirements
- **Minimum**: 80x30 terminal
- **Recommended**: 100x40 or larger
- **Memory**: ~50MB
- **CPU**: Minimal (real-time rendering)

### Optimization Tips
- Keep layer count reasonable (<20)
- Use smaller canvas for complex compositions
- Disable unused features
- Save frequently

---

## 🤝 Feedback

Found a bug? Have a suggestion?

- **GitHub Issues**: Report bugs
- **GitHub Discussions**: Feature requests
- **Email**: editor-feedback@example.com

---

## 📚 Additional Resources

- [API Reference](API_REFERENCE.md)
- [Tutorials](TUTORIALS.md)
- [Best Practices](BEST_PRACTICES.md)
- [Keyboard Shortcuts Reference](SHORTCUTS.md) (coming soon)

---

**Happy Editing! 🎨✨**

