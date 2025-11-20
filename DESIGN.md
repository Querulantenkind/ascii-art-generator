# ASCII Art Generator - Design Document

## Overview

The ASCII Art Generator is a modular, extensible terminal-based tool for creating various types of ASCII art. This document outlines the design decisions, architecture, and implementation details.

## Design Philosophy

### Core Principles

1. **Modularity**: Each art type is implemented as a separate generator module
2. **Extensibility**: Easy to add new fonts, patterns, and features without modifying core code
3. **User-Friendly**: Dual interface (interactive menu + command-line) for different use cases
4. **Minimal Dependencies**: Core features work without external libraries
5. **Terminal-First**: Optimized for terminal/console output with proper character handling

## Architecture

### High-Level Structure

```
┌─────────────────────────────────────────────────────────────┐
│                    ascii_art_generator.py                   │
│                    (Main Entry Point)                       │
└─────────────────────────────────────────────────────────────┘
                              │
                ┌─────────────┴─────────────┐
                │                           │
        ┌───────▼────────┐         ┌───────▼────────┐
        │  CLI Interface │         │   Generators   │
        └────────────────┘         └────────────────┘
                │                           │
        ┌───────▼────────┐         ┌───────▼────────┐
        │  Interactive   │         │  Text Art      │
        │     Mode       │         │  Image Art     │
        └────────────────┘         │  Pattern Art   │
                                   └────────────────┘
                                           │
                                   ┌───────▼────────┐
                                   │     Utils      │
                                   │   (Config)     │
                                   └────────────────┘
```

### Module Breakdown

#### 1. Main Entry Point (`ascii_art_generator.py`)

**Responsibilities:**
- Command-line argument parsing
- Routing to appropriate generator
- Output handling (stdout or file)
- Error handling and user feedback

**Design Decisions:**
- Uses `argparse` with subcommands for clean CLI structure
- Separates interactive and command-line modes
- Provides consistent interface across all generators

#### 2. Generators (`generators/`)

##### Text Art Generator (`text_art.py`)

**Responsibilities:**
- Convert text to ASCII art using various fonts
- Manage font definitions
- Handle text wrapping and formatting

**Design Decisions:**
- **Font System**: Each font is a separate class inheriting from `BaseFont`
- **Character Mapping**: Fonts store character definitions as multi-line strings
- **Extensibility**: New fonts can be added by creating a new class and registering it

**Font Implementation:**
```python
class BaseFont:
    - render(text) -> str  # Abstract method
    
class StandardFont(BaseFont):
    - char_map: dict       # Character definitions
    - height: int          # Font height in lines
    - render(text) -> str  # Implementation
```

**Available Fonts:**
1. **Standard**: FIGlet-style font with detailed characters
2. **Banner**: Large banner with hash borders
3. **Block**: Solid block characters (█)
4. **Slant**: Slanted text style
5. **Small**: Compact 3-line font
6. **Bubble**: Characters in bubbles

##### Image Art Generator (`image_art.py`)

**Responsibilities:**
- Convert images to ASCII art
- Handle image loading and processing
- Map pixel brightness to characters

**Design Decisions:**
- **Optional Dependency**: Gracefully handles missing Pillow library
- **Aspect Ratio**: Maintains image proportions (0.55 multiplier for character height)
- **Character Sets**: Multiple sets for different detail levels
- **Grayscale Conversion**: Simplifies brightness mapping

**Algorithm:**
```
1. Load image with PIL
2. Convert to grayscale
3. Resize to target width (maintaining aspect ratio)
4. Map each pixel brightness (0-255) to character index
5. Build ASCII string line by line
```

**Character Sets:**
- **Standard**: ` .:-=+*#%@` (10 chars)
- **Detailed**: 70+ characters for high detail
- **Simple**: ` .oO@` (5 chars)
- **Blocks**: ` ░▒▓█` (Unicode blocks)

##### Pattern Generator (`pattern_art.py`)

**Responsibilities:**
- Generate geometric patterns
- Create borders, boxes, and frames
- Handle different border styles

**Design Decisions:**
- **Box Drawing Characters**: Uses Unicode box-drawing characters for professional look
- **Style System**: Multiple border styles (single, double, thick, ascii)
- **Algorithmic Patterns**: Mathematical generation for diamonds, waves, etc.

**Border Styles:**
```python
box_chars = {
    'single': {'tl': '┌', 'tr': '┐', 'h': '─', 'v': '│', ...},
    'double': {'tl': '╔', 'tr': '╗', 'h': '═', 'v': '║', ...},
    'thick':  {'tl': '┏', 'tr': '┓', 'h': '━', 'v': '┃', ...},
    'ascii':  {'tl': '+', 'tr': '+', 'h': '-', 'v': '|', ...}
}
```

**Pattern Types:**
1. **Box**: Rectangular frame with corners
2. **Border**: Decorative frame with title area
3. **Line**: Horizontal or vertical lines
4. **Diamond**: Geometric diamond shape
5. **Wave**: Sine wave pattern
6. **Grid**: Table-like grid structure
7. **Banner**: Text in decorative frame

#### 3. CLI Interface (`cli/`)

##### Interactive Mode (`interactive.py`)

**Responsibilities:**
- Provide menu-driven interface
- Handle user input and validation
- Display examples and help
- Offer file save functionality

**Design Decisions:**
- **Menu System**: Hierarchical menu structure
- **Input Validation**: Graceful handling of invalid input
- **Examples Gallery**: Built-in examples for learning
- **Settings**: Runtime configuration changes

**Menu Structure:**
```
Main Menu
├── Text to ASCII Art
│   └── Font selection
├── Image to ASCII Art
│   └── Size and charset options
├── Generate Patterns
│   └── Pattern type selection
├── Generate Borders & Boxes
│   └── Style selection
├── Examples & Gallery
├── Settings
└── Help
```

#### 4. Utilities (`utils/`)

##### Configuration (`config.py`)

**Responsibilities:**
- Manage application settings
- Store character sets
- Handle color output

**Design Decisions:**
- **Centralized Config**: Single source of truth for settings
- **Runtime Modification**: Settings can be changed during execution
- **Color Support**: Optional ANSI color codes

## Key Design Decisions

### 1. No External Dependencies for Core Features

**Rationale**: Makes the tool immediately usable without installation steps.

**Implementation**: 
- Text art and patterns use only Python standard library
- Pillow is optional for image conversion
- Graceful degradation when dependencies missing

### 2. Dual Interface (Interactive + CLI)

**Rationale**: Serves different use cases:
- Interactive: Learning, exploration, one-off creations
- CLI: Scripting, automation, integration

**Implementation**:
- Shared generator code
- Separate interface layers
- Consistent output format

### 3. Unicode Box-Drawing Characters

**Rationale**: Professional appearance, better than ASCII alternatives

**Considerations**:
- Terminal must support UTF-8
- Fallback to ASCII style available
- Widely supported in modern terminals

### 4. Modular Font System

**Rationale**: Easy to add new fonts without modifying core code

**Implementation**:
```python
# Adding a new font:
1. Create class inheriting from BaseFont
2. Implement render() method
3. Register in TextArtGenerator._load_fonts()
```

### 5. Character Density Mapping for Images

**Rationale**: Different characters have different visual "weight"

**Implementation**:
- Characters ordered by density: ` .:-=+*#%@`
- Pixel brightness maps to character index
- Multiple character sets for different effects

## Extensibility Points

### Adding New Fonts

```python
class MyCustomFont(BaseFont):
    def __init__(self):
        super().__init__()
        self.height = 5
        self._init_chars()
    
    def _init_chars(self):
        self.char_map = {
            'A': ["line1", "line2", ...],
            # ... more characters
        }
    
    def render(self, text: str) -> str:
        # Implementation
        pass

# Register in TextArtGenerator
self.fonts['custom'] = MyCustomFont()
```

### Adding New Patterns

```python
# In PatternGenerator class
def generate_custom_pattern(self, width, height, **kwargs):
    lines = []
    for y in range(height):
        line = ""
        for x in range(width):
            # Your pattern logic
            line += char
        lines.append(line)
    return '\n'.join(lines)
```

### Adding New Character Sets

```python
# In config.py
self.charsets = {
    'custom': " .:-=+your_chars_here",
}
```

## Performance Considerations

### Text Art
- **Complexity**: O(n) where n is text length
- **Memory**: O(n * font_height)
- **Optimization**: Pre-computed character maps

### Image Art
- **Complexity**: O(w * h) where w, h are image dimensions
- **Memory**: O(w * h) for resized image
- **Optimization**: Resize before processing, grayscale conversion

### Patterns
- **Complexity**: O(w * h) for most patterns
- **Memory**: O(w * h)
- **Optimization**: Algorithmic generation (no storage)

## Future Enhancements

### Planned Features

1. **FIGlet Font Support**
   - Import standard FIGlet fonts
   - Expand font library significantly

2. **Color Gradients**
   - ANSI 256-color support
   - RGB color mapping for images

3. **Animation**
   - Frame generation
   - Terminal animation playback

4. **Template System**
   - Combine multiple elements
   - Reusable compositions

5. **Web Interface**
   - Browser-based generator
   - Share and export options

### Technical Debt

1. **Font System**: Could use external FIGlet fonts instead of hardcoded
2. **Testing**: Add comprehensive unit tests
3. **Documentation**: Add docstring examples
4. **Error Handling**: More specific error messages

## Testing Strategy

### Manual Testing
- Run examples.sh for visual verification
- Test interactive mode navigation
- Verify output formatting

### Automated Testing (Future)
```python
# Example test structure
def test_text_generation():
    gen = TextArtGenerator(Config())
    result = gen.generate("TEST", font='standard')
    assert len(result.split('\n')) == 6  # Standard font height
    assert "TEST" in result.upper()
```

## Deployment

### Installation
```bash
# Clone repository
git clone <repo-url>
cd ascii-art-generator

# Install optional dependencies
pip install -r requirements.txt

# Make executable
chmod +x ascii_art_generator.py
```

### Usage Patterns

**One-off Generation:**
```bash
python ascii_art_generator.py text "Hello" -f banner
```

**Scripting:**
```bash
for word in Hello World; do
    python ascii_art_generator.py text "$word" -o "${word}.txt"
done
```

**Interactive Exploration:**
```bash
python ascii_art_generator.py -i
```

## Conclusion

The ASCII Art Generator is designed to be:
- **Easy to use**: Both for beginners (interactive) and experts (CLI)
- **Easy to extend**: Modular architecture with clear extension points
- **Reliable**: Minimal dependencies, graceful error handling
- **Professional**: Unicode support, multiple styles, quality output

The modular design allows for future enhancements while maintaining backward compatibility and code quality.

