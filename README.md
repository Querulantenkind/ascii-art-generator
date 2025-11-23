# ASCII Art Generator

<div align="center">

```
   ___    ____    ____  ___  ___      ___    ____   _____ 
  / _ \  / ___|  / ___||_ _||_ _|    / _ \  |  _ \ |_   _|
 / /_\ \ \___ \ | |     | |  | |    / /_\ \ | |_) |  | |  
/  _  \ \ ___) || |___  | |  | |   /  _  \ \|  _ <   | |  
\_/ \_/ /|____/  \____||___||___|  \_/ \_/ /|_| \_\  |_|  
```

**The Ultimate Terminal-Based ASCII Art Creation Suite**

[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](https://github.com/yourusername/ascii-art-generator)
[![Python](https://img.shields.io/badge/python-3.7+-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[Features](#features) • [Installation](#installation) • [Quick Start](#quick-start) • [Documentation](#documentation) • [Examples](#examples)

</div>

---

## 📖 Overview

A **professional-grade**, **feature-rich** ASCII art generator that transforms text, images, and data into stunning ASCII art. From simple text conversion to complex animations, diagrams, and batch processing - this is your complete ASCII art toolkit.

### 🎯 Why Choose This Tool?

- **🚀 75+ Features**: Text effects, patterns, animations, diagrams, plugins, and more
- **⚡ High Performance**: Parallel batch processing, optimized algorithms
- **🎨 Professional Quality**: Production-ready output for any use case
- **📦 Zero Dependencies**: Core features work out of the box
- **🔧 Extensible**: Template system, plugin architecture (NEW!)
- **📚 Comprehensive Docs**: Detailed guides, examples, and API reference
- **🌐 Multiple Formats**: Export to HTML, SVG, Markdown, PNG, and more

## ✨ Features

### 📊 Feature Matrix

| Category | Basic | Pro | Ultra | Count |
|----------|:-----:|:---:|:-----:|:-----:|
| **Text Fonts** | ✅ | ✅ | ✅ | 7+ |
| **Visual Effects** | ❌ | ✅ | ✅ | 10+ |
| **Color Gradients** | ❌ | ✅ | ✅ | 4+ |
| **Patterns** | ✅ | ✅ | ✅ | 15+ |
| **Animations** | ❌ | ✅ | ✅ | 8+ |
| **Diagrams** | ❌ | ❌ | ✅ | 4+ |
| **Templates** | ❌ | ❌ | ✅ | 12+ |
| **Batch Processing** | ❌ | ❌ | ✅ | ✅ |
| **Video Support** | ❌ | ❌ | ✅ | ✅ |
| **QR Codes** | ❌ | ❌ | ✅ | ✅ |
| **Export Formats** | 1 | 6 | 6 | 6 |
| **Composition** | ❌ | ✅ | ✅ | 6+ |

### 🎨 Core Art Types

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

### 🚀 Three Usage Modes

- **🎨 Interactive TUI Editor**: Professional real-time editor with live preview (NEW!)
- **📋 Interactive Menu Mode**: User-friendly menu-driven interface
- **⚡ Command-Line Mode**: Direct command execution for scripting

## 📦 Installation

### Quick Install

```bash
# Clone the repository
git clone https://github.com/yourusername/ascii-art-generator.git
cd ascii-art-generator

# Basic installation (no dependencies required!)
# You can start using text and pattern features immediately

# Optional: Install dependencies for advanced features
pip install -r requirements.txt
```

### Dependencies Breakdown

| Feature | Dependency | Required? |
|---------|-----------|-----------|
| **Core Features** | None | ✅ Always available |
| **Image Conversion** | `Pillow>=10.0.0` | Optional |
| **QR Codes** | `qrcode[pil]>=7.4.0` | Optional |
| **Video Processing** | `opencv-python` or `ffmpeg` | Optional |

### Installation Options

```bash
# Minimal (text & patterns only)
# No installation needed!

# Standard (includes image support)
pip install Pillow

# Full (all features)
pip install -r requirements.txt

# Development (with testing tools)
pip install -r requirements.txt
pip install pytest black mypy
```

## 🚀 Quick Start

### 🎨 NEW: Interactive Editor (Recommended!)

```bash
# Launch the professional TUI editor
python ascii_art_editor.py --demo

# Press T to add text
# Press P to apply preset
# Press C to copy
# Press Q to quit
```

**Create professional ASCII art in 30 seconds with live preview!**

### 30-Second Command-Line Demo

```bash
# Generate your first ASCII art
python ascii_art_generator.py text "HELLO WORLD"

# Try with effects
python ascii_art_pro.py text "AWESOME" --effect shadow

# Create a pattern
python ascii_art_pro.py pattern mandelbrot -w 80 --height 40

# Use a template
python -c "
from templates.template_manager import TemplateManager
manager = TemplateManager()
template = manager.get_template('welcome_banner')
print(template.render(title='MY PROJECT', subtitle='v1.0'))
"
```

## 📘 Usage Guide

### 🎮 Interactive Mode

Launch the interactive menu for guided creation:

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
2. **Extensibility**: Easy to add new fonts, patterns, and features via Plugin System
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

## 📚 Documentation

### Complete Documentation Suite

| Document | Description | Link |
|----------|-------------|------|
| **Quick Start** | Get started in 5 minutes | [QUICKSTART.md](QUICKSTART.md) |
| **API Reference** | Complete API documentation | [docs/API_REFERENCE.md](docs/API_REFERENCE.md) |
| **Tutorials** | Step-by-step guides | [docs/TUTORIALS.md](docs/TUTORIALS.md) |
| **Best Practices** | Guidelines and tips | [docs/BEST_PRACTICES.md](docs/BEST_PRACTICES.md) |
| **Features Guide** | Pro features documentation | [FEATURES.md](FEATURES.md) |
| **Ultra Features** | Latest enhancements | [ULTRA_FEATURES.md](ULTRA_FEATURES.md) |
| **Plugin Guide** | How to create and use plugins | [docs/PLUGIN_GUIDE.md](docs/PLUGIN_GUIDE.md) |
| **Design Document** | Architecture details | [DESIGN.md](DESIGN.md) |
| **Future Roadmap** | Upcoming features | [FUTURE_ROADMAP.md](FUTURE_ROADMAP.md) |
| **Examples** | Code examples | [examples/](examples/) |

### Quick Links

- 🚀 [Installation Guide](#installation)
- 📖 [Usage Examples](#usage-guide)
- 🎨 [Feature Matrix](#feature-matrix)
- 💡 [Tutorials](docs/TUTORIALS.md)
- 📘 [API Reference](docs/API_REFERENCE.md)
- ⚡ [Best Practices](docs/BEST_PRACTICES.md)

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

1. **Report Bugs**: Open an issue with details
2. **Suggest Features**: Share your ideas
3. **Submit PRs**: Fix bugs or add features
4. **Improve Docs**: Help make docs better
5. **Share Examples**: Show what you've created

### Development Setup

```bash
# Clone repository
git clone https://github.com/yourusername/ascii-art-generator.git
cd ascii-art-generator

# Install dev dependencies
pip install -r requirements.txt
pip install pytest black mypy

# Run tests
pytest

# Format code
black .

# Type check
mypy .
```

### Code Style

- Follow PEP 8
- Use type hints
- Write docstrings
- Add tests for new features
- Update documentation

---

## 🎯 Use Cases

### Professional Applications

- **Software Development**: README headers, documentation, CLI tools
- **DevOps**: Terminal dashboards, monitoring displays
- **Education**: Algorithm visualization, teaching materials
- **Marketing**: Social media content, promotional materials
- **Art & Design**: Creative projects, digital art

### Real-World Examples

```bash
# CI/CD Success Banner
python ascii_art_pro.py text "BUILD SUCCESS" --effect 3d --gradient rainbow

# Terminal Dashboard
python -c "
from templates.template_manager import TemplateManager
manager = TemplateManager()
status = manager.get_template('status_box')
print(status.render(status='Running', time='12:34:56', user='admin'))
"

# QR Code for Documentation
python -c "
from generators.qr_ascii import QRCodeASCII
qr = QRCodeASCII()
print(qr.generate_with_border('https://docs.example.com', title='DOCS'))
"
```

---

## 📊 Project Statistics

- **Lines of Code**: 10,000+
- **Modules**: 20+
- **Features**: 70+
- **Templates**: 12+
- **Export Formats**: 6
- **Documentation Pages**: 8+
- **Test Coverage**: Growing!

---

## 🏆 Achievements

- ✅ **70+ Features** across all categories
- ✅ **Zero Dependencies** for core features
- ✅ **Production Ready** code quality
- ✅ **Comprehensive Documentation** with tutorials
- ✅ **Active Development** with regular updates
- ✅ **Community Friendly** with contribution guidelines

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Inspired by FIGlet and ASCII art community
- Built with Python and love for terminal aesthetics
- Thanks to all contributors and users

---

## 📧 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/ascii-art-generator/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/ascii-art-generator/discussions)
- **Email**: support@example.com
- **Twitter**: [@asciiartgen](https://twitter.com/asciiartgen)

---

## 🌟 Star History

If you find this project useful, please consider giving it a star! ⭐

---

## 🔮 Future Roadmap

### Phase 3 (Next 3 Months)
- [x] Interactive real-time editor
- [x] Plugin system
- [ ] Enhanced diagram generator
- [ ] Sound visualization

### Phase 4 (3-6 Months)
- [ ] Web-based platform
- [ ] AI-powered features
- [ ] Collaborative editing
- [ ] Mobile apps

See [FUTURE_ROADMAP.md](FUTURE_ROADMAP.md) for complete roadmap.

---

<div align="center">

**Made with ❤️ for ASCII art enthusiasts**

```
 _____ _   _    _    _   _ _  __ __   _____  _   _ 
|_   _| | | |  / \  | \ | | |/ / \ \ / / _ \| | | |
  | | | |_| | / _ \ |  \| | ' /   \ V / | | | | | |
  | | |  _  |/ ___ \| |\  | . \    | || |_| | |_| |
  |_| |_| |_/_/   \_\_| \_|_|\_\   |_| \___/ \___/ 
```

[⬆ Back to Top](#ascii-art-generator)

</div>
