# ASCII Art Generator

A comprehensive terminal-based ASCII art generator that creates various types of ASCII art based on user input. Transform text, images, and generate patterns with an intuitive command-line interface.

## Features

### 🎨 Multiple Art Types

1. **Text to ASCII Art**
   - Convert text into stylized ASCII art
   - 6 different font styles: standard, banner, block, slant, small, bubble
   - Customizable width and formatting

2. **Image to ASCII Art**
   - Convert images (JPG, PNG, etc.) to ASCII art
   - Multiple character sets for different detail levels
   - Adjustable output width
   - Maintains aspect ratio

3. **Pattern Generation**
   - Geometric patterns: diamonds, waves, grids
   - Decorative elements for terminal output
   - Customizable dimensions

4. **Borders & Boxes**
   - Create boxes, borders, and banners
   - 4 border styles: single, double, thick, ascii
   - Perfect for framing text or creating UI elements

### 🚀 Two Usage Modes

- **Interactive Mode**: User-friendly menu-driven interface
- **Command-Line Mode**: Direct command execution for scripting

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ascii-art-generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

**Note**: Pillow is only required for image-to-ASCII conversion. All other features work without additional dependencies.

## Usage

### Interactive Mode

Launch the interactive menu:

```bash
python ascii_art_generator.py -i
```

or simply:

```bash
python ascii_art_generator.py
```

Navigate through the menu to:
- Generate text art with different fonts
- Convert images to ASCII
- Create patterns and borders
- View examples
- Configure settings

### Command-Line Mode

#### Text to ASCII Art

```bash
# Basic text art
python ascii_art_generator.py text "Hello World"

# With specific font
python ascii_art_generator.py text "ASCII" -f banner

# With width limit
python ascii_art_generator.py text "Code" -f block -w 60
```

Available fonts: `standard`, `banner`, `block`, `slant`, `small`, `bubble`

#### Image to ASCII Art

```bash
# Basic image conversion
python ascii_art_generator.py image photo.jpg

# Custom width and character set
python ascii_art_generator.py image photo.jpg -w 100 -c detailed

# Save to file
python ascii_art_generator.py image photo.jpg -w 80 -o output.txt
```

Character sets:
- `standard`: Basic characters (default)
- `detailed`: High detail with many characters
- `simple`: Minimal characters
- `blocks`: Unicode block characters

#### Pattern Generation

```bash
# Diamond pattern
python ascii_art_generator.py pattern diamond -w 40 -h 15

# Wave pattern
python ascii_art_generator.py pattern wave -w 60 -h 10

# Box with double border
python ascii_art_generator.py pattern box -w 50 -h 10 -s double
```

Pattern types: `box`, `border`, `line`, `diamond`, `wave`

Border styles: `single`, `double`, `thick`, `ascii`

### Saving Output

Save any output to a file using the `-o` flag:

```bash
python ascii_art_generator.py text "Save Me" -f banner -o art.txt
```

### Color Output

Enable color output (where supported):

```bash
python ascii_art_generator.py text "Colorful" --color
```

## Examples

### Text Art Example

```
   ___   
  / _ \  
 / /_\ \ 
/  _  \ \
\_/ \_/ /
        
```

### Border Example

```
╔═══════════════════════════════════════════════════╗
║                                                   ║
║                   ASCII ART                       ║
║                                                   ║
╚═══════════════════════════════════════════════════╝
```

### Diamond Pattern Example

```
        *
       ***
      *****
     *******
    *********
     *******
      *****
       ***
        *
```

## Project Structure

```
ascii-art-generator/
├── ascii_art_generator.py    # Main entry point
├── generators/
│   ├── __init__.py
│   ├── text_art.py           # Text-to-ASCII generator
│   ├── image_art.py          # Image-to-ASCII converter
│   └── pattern_art.py        # Pattern generator
├── cli/
│   ├── __init__.py
│   └── interactive.py        # Interactive mode interface
├── utils/
│   ├── __init__.py
│   └── config.py             # Configuration management
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── LICENSE                   # License information
```

## Design Philosophy

The ASCII Art Generator is designed with the following principles:

1. **Modularity**: Each art type has its own generator module
2. **Extensibility**: Easy to add new fonts, patterns, and features
3. **User-Friendly**: Both interactive and command-line modes
4. **No Heavy Dependencies**: Core features work without external libraries
5. **Terminal-First**: Optimized for terminal/console output

## Advanced Usage

### Using as a Library

You can import and use the generators in your own Python code:

```python
from generators.text_art import TextArtGenerator
from utils.config import Config

config = Config()
generator = TextArtGenerator(config)
art = generator.generate("Hello", font='banner')
print(art)
```

### Custom Character Sets

Modify character sets in `utils/config.py`:

```python
self.charsets = {
    'custom': " .:-=+*#%@",
    # Add your own character sets
}
```

## Requirements

- Python 3.7+
- Pillow (optional, for image conversion)

## Contributing

Contributions are welcome! Areas for enhancement:

- Additional font styles
- More pattern types
- Color gradient support
- Animation capabilities
- Export to various formats (HTML, SVG)

## License

See LICENSE file for details.

## Tips & Tricks

1. **Best Image Results**: Use high-contrast images with clear subjects
2. **Terminal Width**: Most terminals are 80-120 characters wide
3. **Font Selection**: Experiment with different fonts for different effects
4. **Combining Elements**: Use borders to frame text art
5. **File Output**: Save complex art to files for reuse

## Troubleshooting

**Issue**: Image conversion not working
- **Solution**: Install Pillow: `pip install Pillow`

**Issue**: Unicode characters not displaying
- **Solution**: Ensure your terminal supports UTF-8 encoding

**Issue**: Art appears distorted
- **Solution**: Adjust width parameter or try a different font

## 🚀 ASCII Art Generator Pro & Ultra

Two **enhanced versions** with progressively advanced features are available!

### Pro Version (`ascii_art_pro.py`)

### ✨ Additional Features

- **🎨 Text Effects**: Shadow, outline, 3D, glow, mirror, neon effects
- **🌈 Color Gradients**: Rainbow, fire, ocean, forest gradients with ANSI colors
- **🔮 Advanced Patterns**: Mandelbrot set, Julia set, mazes, spirals, fractals, trees
- **🎬 Animations**: Wave, bouncing ball, Matrix rain, progress bars, typewriter effects
- **🧩 Composition System**: Combine multiple elements with layering and layouts
- **📤 Export Formats**: HTML, SVG, Markdown, JSON, PNG image export

### Quick Pro Examples

```bash
# Text with effects
python ascii_art_pro.py text "SHADOW" --effect shadow
python ascii_art_pro.py text "RAINBOW" --gradient rainbow --color

# Advanced patterns
python ascii_art_pro.py pattern mandelbrot -w 80 --height 40
python ascii_art_pro.py pattern maze -w 51 --height 31
python ascii_art_pro.py pattern tree --height 15 --tree-style pine

# Animations
python ascii_art_pro.py animate wave -w 60 --height 15 --play
python ascii_art_pro.py animate matrix -w 80 --height 20 --play --loop

# Export formats
python ascii_art_pro.py text "HTML" -o output.html --format html
python ascii_art_pro.py text "IMAGE" -o output.png --format png
```

**📚 See `FEATURES.md` for complete documentation of Pro features!**

### Ultra Features (Latest Enhancements!)

The tool now includes **cutting-edge capabilities**:

- **📋 Template System**: 12+ pre-made templates (banners, menus, alerts, tables)
- **⚡ Batch Processing**: Process multiple files in parallel with progress tracking
- **🎬 Video to ASCII**: Convert videos to ASCII art animations
- **📱 QR Code Generator**: Create scannable QR codes in ASCII
- **🔄 Multi-format Export**: Export to HTML, SVG, Markdown, PNG simultaneously

**Usage Examples**:
```python
# Use templates
from templates.template_manager import TemplateManager
manager = TemplateManager()
template = manager.get_template('welcome_banner')
print(template.render(title="HELLO", subtitle="World"))

# Batch process images
from utils.batch_processor import BatchImageConverter, BatchProcessor
converter = BatchImageConverter(width=80)
processor = BatchProcessor(max_workers=4)
processor.process_files("images/*.jpg", "output", converter.convert)

# Generate QR code
from generators.qr_ascii import QRCodeASCII
qr = QRCodeASCII()
print(qr.generate_with_border("https://example.com", title="SCAN ME"))
```

**📚 See `ULTRA_FEATURES.md` for complete Ultra documentation!**

---

## Future Enhancements

- [x] FIGlet font support ✅
- [x] Color gradients and ANSI color support ✅
- [x] Animation and frame generation ✅
- [x] Export to multiple formats ✅
- [x] Composition system ✅
- [ ] Web interface
- [ ] Real-time preview mode
- [ ] Plugin system for custom generators

---

**Made with ❤️ for ASCII art enthusiasts**
