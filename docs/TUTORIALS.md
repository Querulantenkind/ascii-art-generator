# Tutorials

Step-by-step tutorials for common use cases.

---

## Table of Contents

1. [Getting Started](#tutorial-1-getting-started)
2. [Creating a Project Banner](#tutorial-2-creating-a-project-banner)
3. [Batch Processing Images](#tutorial-3-batch-processing-images)
4. [Building an Animated Logo](#tutorial-4-building-an-animated-logo)
5. [Creating Documentation](#tutorial-5-creating-documentation)
6. [Generating QR Codes](#tutorial-6-generating-qr-codes)
7. [Making Diagrams](#tutorial-7-making-diagrams)
8. [Advanced Composition](#tutorial-8-advanced-composition)

---

## Tutorial 1: Getting Started

### Goal
Create your first ASCII art in under 5 minutes.

### Steps

#### 1. Install the Tool
```bash
git clone https://github.com/yourusername/ascii-art-generator.git
cd ascii-art-generator
```

#### 2. Generate Simple Text Art
```bash
python ascii_art_generator.py text "Hello World"
```

**Output:**
```
 _   _  _____  _      _       ___    __        __  ___   ____   _      ____  
| | | ||  ___|| |    | |     / _ \   \ \      / / / _ \ |  _ \ | |    |  _ \ 
| |_| || |__  | |    | |    | | | |   \ \ /\ / / | | | || |_) || |    | | | |
|  _  ||  __| | |___ | |___ | |_| |    \ V  V /  | |_| ||  _ < | |___ | |_| |
|_| |_||_____||_____||_____| \___/      \_/\_/    \___/ |_| \_\|_____||____/ 
```

#### 3. Try Different Fonts
```bash
python ascii_art_generator.py text "ASCII" -f banner
python ascii_art_generator.py text "CODE" -f block
python ascii_art_generator.py text "ART" -f bubble
```

#### 4. Save to File
```bash
python ascii_art_generator.py text "Save Me" -o myart.txt
```

### What You Learned
- Basic text generation
- Font selection
- Saving output

---

## Tutorial 2: Creating a Project Banner

### Goal
Create a professional banner for your GitHub README.

### Steps

#### 1. Generate the Logo
```python
from generators.text_art import TextArtGenerator
from generators.text_effects import TextEffects
from utils.config import Config

# Initialize
config = Config()
text_gen = TextArtGenerator(config)
effects = TextEffects()

# Generate text
logo = text_gen.generate("MY PROJECT", font='banner')

# Add effects
logo = effects.add_3d_effect(logo, depth=3)
logo = effects.add_outline(logo, outline_char='=')

print(logo)
```

#### 2. Add a Frame
```python
from generators.composition import Compositor

compositor = Compositor()

# Frame the logo
framed_logo = compositor.frame(
    logo,
    title="Version 2.0",
    style='double',
    padding=2
)

print(framed_logo)
```

#### 3. Add Color (Optional)
```python
from generators.color_art import GradientGenerator

gradient_gen = GradientGenerator()

# Apply gradient
colored_logo = gradient_gen.apply_gradient_to_text(framed_logo, 'rainbow')

print(colored_logo)
```

#### 4. Export to Multiple Formats
```python
from exporters.formats import HTMLExporter, SVGExporter, MarkdownExporter

# HTML for website
html_exporter = HTMLExporter()
html = html_exporter.export(framed_logo, title="My Project")
with open('banner.html', 'w') as f:
    f.write(html)

# SVG for scaling
svg_exporter = SVGExporter()
svg = svg_exporter.export(framed_logo, title="My Project")
with open('banner.svg', 'w') as f:
    f.write(svg)

# Markdown for README
md_exporter = MarkdownExporter()
md = md_exporter.export(framed_logo, title="My Project", 
                        description="An awesome project")
with open('banner.md', 'w') as f:
    f.write(md)
```

### Result
You now have a professional banner in multiple formats ready for your project!

---

## Tutorial 3: Batch Processing Images

### Goal
Convert 100 images to ASCII art in parallel.

### Steps

#### 1. Organize Your Images
```bash
mkdir input_images
mkdir ascii_output
# Place your images in input_images/
```

#### 2. Create Processing Script
```python
# batch_convert.py
from utils.batch_processor import BatchImageConverter, BatchProcessor

# Configure converter
converter = BatchImageConverter(
    width=80,
    charset='detailed'
)

# Create processor with 8 parallel workers
processor = BatchProcessor(max_workers=8)

# Process all images
results = processor.process_files(
    input_pattern="input_images/*.jpg",
    output_dir="ascii_output",
    processor_func=converter.convert
)

# Print summary
processor.print_summary()
```

#### 3. Run the Script
```bash
python batch_convert.py
```

**Output:**
```
✓ Processed: input_images/photo1.jpg -> ascii_output/photo1_processed.txt
✓ Processed: input_images/photo2.jpg -> ascii_output/photo2_processed.txt
...
============================================================
BATCH PROCESSING SUMMARY
============================================================
Total files:     100
Successful:      98
Failed:          2
Success rate:    98.0%
Total time:      45.23s
Average time:    0.45s
============================================================
```

#### 4. Export to HTML Gallery
```python
from exporters.formats import HTMLExporter
import os

exporter = HTMLExporter()

# Create index.html
html_content = "<html><body><h1>ASCII Art Gallery</h1>"

for filename in os.listdir('ascii_output'):
    if filename.endswith('.txt'):
        with open(f'ascii_output/{filename}', 'r') as f:
            ascii_art = f.read()
        
        html_content += f"<h2>{filename}</h2>"
        html_content += f"<pre>{ascii_art}</pre><hr>"

html_content += "</body></html>"

with open('gallery.html', 'w') as f:
    f.write(html_content)
```

### What You Learned
- Batch processing
- Parallel execution
- Gallery creation

---

## Tutorial 4: Building an Animated Logo

### Goal
Create an animated ASCII logo for terminal display.

### Steps

#### 1. Generate Base Logo
```python
from generators.text_art import TextArtGenerator
from utils.config import Config

config = Config()
gen = TextArtGenerator(config)

logo = gen.generate("LOGO", font='banner')
```

#### 2. Create Animation Frames
```python
from generators.text_effects import TextEffects
from generators.animation import Animation, AnimationFrame

effects = TextEffects()
animation = Animation()

# Frame 1: Normal
animation.add_frame(logo, duration=0.5)

# Frame 2: With shadow
frame2 = effects.add_shadow(logo)
animation.add_frame(frame2, duration=0.5)

# Frame 3: With glow
frame3 = effects.add_glow(logo, intensity=2)
animation.add_frame(frame3, duration=0.5)

# Frame 4: 3D effect
frame4 = effects.add_3d_effect(logo, depth=3)
animation.add_frame(frame4, duration=0.5)
```

#### 3. Add Color Transitions
```python
from generators.color_art import GradientGenerator

gradient_gen = GradientGenerator()

# Rainbow transition
for gradient_type in ['rainbow', 'fire', 'ocean', 'forest']:
    colored = gradient_gen.apply_gradient_to_text(logo, gradient_type)
    animation.add_frame(colored, duration=0.3)
```

#### 4. Play the Animation
```python
# Play once
animation.play(loop=False)

# Or loop continuously
animation.play(loop=True)
```

#### 5. Export Frames
```python
# Export for external use
animation.export_frames('logo_frames', prefix='logo')
```

### What You Learned
- Animation creation
- Effect sequencing
- Color transitions

---

## Tutorial 5: Creating Documentation

### Goal
Generate complete project documentation with ASCII art.

### Steps

#### 1. Create README Header
```python
from templates.template_manager import TemplateManager

manager = TemplateManager()

# Use template
header_template = manager.get_template('readme_header')
header = header_template.render(
    project_name="Awesome Project",
    tagline="The best project ever",
    version="2.0.0",
    license="MIT",
    description="A comprehensive tool for doing awesome things"
)

print(header)
```

#### 2. Add Logo
```python
from generators.text_art import TextArtGenerator
from utils.config import Config

config = Config()
gen = TextArtGenerator(config)

logo = gen.generate("AWESOME", font='banner')
```

#### 3. Create Section Dividers
```python
divider_template = manager.get_template('section_divider')

features_divider = divider_template.render(section_name="FEATURES")
install_divider = divider_template.render(section_name="INSTALLATION")
usage_divider = divider_template.render(section_name="USAGE")
```

#### 4. Add Code Blocks
```python
code_template = manager.get_template('code_block')

example_code = code_template.render(
    filename="example.py",
    code="""
import awesome

app = awesome.App()
app.run()
    """.strip()
)
```

#### 5. Assemble Complete README
```python
readme = f"""
```
{logo}
```

{header}

{features_divider}

- Feature 1
- Feature 2
- Feature 3

{install_divider}

```bash
pip install awesome-project
```

{usage_divider}

{example_code}

"""

with open('README.md', 'w') as f:
    f.write(readme)
```

### What You Learned
- Template usage
- Documentation generation
- Content assembly

---

## Tutorial 6: Generating QR Codes

### Goal
Create ASCII QR codes for URLs and data.

### Steps

#### 1. Basic QR Code
```python
from generators.qr_ascii import QRCodeASCII

qr_gen = QRCodeASCII()

# Generate QR code
qr_code = qr_gen.generate(
    data="https://github.com/yourproject",
    error_correction='M',
    scale=1
)

print(qr_code)
```

#### 2. QR Code with Border
```python
qr_with_border = qr_gen.generate_with_border(
    data="https://github.com/yourproject",
    title="GITHUB REPO",
    scale=2
)

print(qr_with_border)
```

#### 3. Multiple QR Codes for Menu
```python
from generators.composition import Compositor

compositor = Compositor()

# Generate QR codes
website_qr = qr_gen.generate_with_border(
    "https://example.com",
    title="WEBSITE"
)

github_qr = qr_gen.generate_with_border(
    "https://github.com/user/repo",
    title="GITHUB"
)

contact_qr = qr_gen.generate_with_border(
    "mailto:hello@example.com",
    title="EMAIL"
)

# Arrange in grid
qr_grid = compositor.grid_layout(
    [website_qr, github_qr, contact_qr],
    cols=3,
    spacing=2
)

print(qr_grid)
```

#### 4. Export QR Codes
```python
from exporters.formats import HTMLExporter, ImageExporter

# HTML export
html_exporter = HTMLExporter()
html = html_exporter.export(qr_with_border, title="QR Code")
with open('qr_code.html', 'w') as f:
    f.write(html)

# PNG export (requires Pillow)
img_exporter = ImageExporter()
img_exporter.export_to_png(qr_with_border, 'qr_code.png')
```

### What You Learned
- QR code generation
- Multiple QR codes
- Export options

---

## Tutorial 7: Making Diagrams

### Goal
Create flowcharts and UML diagrams.

### Steps

#### 1. Simple Flowchart
```python
from generators.diagrams import FlowchartGenerator

flow = FlowchartGenerator()

# Add nodes
flow.add_node('start', 'Start', 'start')
flow.add_node('input', 'Get User Input', 'process')
flow.add_node('validate', 'Valid Input?', 'decision')
flow.add_node('process', 'Process Data', 'process')
flow.add_node('error', 'Show Error', 'process')
flow.add_node('end', 'End', 'end')

# Add edges
flow.add_edge('start', 'input')
flow.add_edge('input', 'validate')
flow.add_edge('validate', 'process', 'Yes')
flow.add_edge('validate', 'error', 'No')
flow.add_edge('process', 'end')
flow.add_edge('error', 'input')

# Generate
diagram = flow.generate()
print(diagram)
```

#### 2. UML Class Diagram
```python
from generators.diagrams import UMLGenerator

uml = UMLGenerator()

diagram = uml.class_diagram({
    'User': {
        'attributes': [
            '- id: int',
            '- name: string',
            '- email: string'
        ],
        'methods': [
            '+ login(): bool',
            '+ logout(): void',
            '+ updateProfile(): void'
        ]
    },
    'Admin': {
        'inherits': 'User',
        'attributes': [
            '- permissions: list'
        ],
        'methods': [
            '+ grantAccess(): void',
            '+ revokeAccess(): void'
        ]
    }
})

print(diagram)
```

#### 3. Network Diagram
```python
from generators.diagrams import NetworkDiagram

network = NetworkDiagram()

topology = network.generate({
    'router': {
        'type': 'router',
        'connects_to': ['switch1', 'switch2', 'internet']
    },
    'switch1': {
        'type': 'switch',
        'connects_to': ['pc1', 'pc2', 'pc3']
    },
    'switch2': {
        'type': 'switch',
        'connects_to': ['server1', 'server2']
    },
    'internet': {
        'type': 'cloud'
    }
})

print(topology)
```

#### 4. Export Diagrams
```python
from exporters.formats import SVGExporter

svg_exporter = SVGExporter()

# Export flowchart as SVG
svg = svg_exporter.export(diagram, title="System Flowchart")
with open('flowchart.svg', 'w') as f:
    f.write(svg)
```

### What You Learned
- Flowchart creation
- UML diagrams
- Network topology
- Diagram export

---

## Tutorial 8: Advanced Composition

### Goal
Create complex multi-element compositions.

### Steps

#### 1. Create Individual Elements
```python
from generators.text_art import TextArtGenerator
from generators.pattern_art import PatternGenerator
from generators.text_effects import TextEffects
from utils.config import Config

config = Config()
text_gen = TextArtGenerator(config)
pattern_gen = PatternGenerator(config)
effects = TextEffects()

# Title
title = text_gen.generate("MY APP", font='banner')
title = effects.add_3d_effect(title)

# Subtitle
subtitle = text_gen.generate("Version 2.0", font='small')

# Decorative border
border = pattern_gen.generate_box(60, 20, style='double')

# Status box
status = pattern_gen.generate_banner("READY", 40, style='thick')
```

#### 2. Compose Elements
```python
from generators.composition import Compositor, Composition

compositor = Compositor()

# Vertical stack
header = compositor.vertical_concat(
    title,
    subtitle,
    spacing=1
)

# Frame the header
framed_header = compositor.frame(
    header,
    title="Application",
    style='double',
    padding=2
)

# Add status below
complete = compositor.vertical_concat(
    framed_header,
    status,
    spacing=2
)

print(complete)
```

#### 3. Layer-Based Composition
```python
composition = Composition(width=100, height=40, fill_char=' ')

# Add layers
composition.add_layer(border, x=0, y=0, z_index=0)
composition.add_layer(title, x=20, y=5, z_index=1)
composition.add_layer(subtitle, x=25, y=12, z_index=1)
composition.add_layer(status, x=30, y=30, z_index=2)

# Render
result = composition.render()
print(result)
```

#### 4. Split-Screen Layout
```python
# Left side: Logo and info
left_side = compositor.vertical_concat(
    title,
    subtitle,
    status
)

# Right side: Menu
from templates.template_manager import TemplateManager

manager = TemplateManager()
menu_template = manager.get_template('menu')
right_side = menu_template.render(
    title="MAIN MENU",
    option1="1. Start",
    option2="2. Settings",
    option3="3. Help",
    option4="4. About"
)

# Combine
split_screen = compositor.split_screen(left_side, right_side)
print(split_screen)
```

### What You Learned
- Multi-element composition
- Layer system
- Split-screen layouts
- Complex arrangements

---

## Next Steps

- Explore the [API Reference](API_REFERENCE.md)
- Check out [Examples](../examples/)
- Read [Best Practices](BEST_PRACTICES.md)
- Join the community

---

## Need Help?

- Documentation: `docs/` directory
- Issues: GitHub Issues
- Discussions: GitHub Discussions

