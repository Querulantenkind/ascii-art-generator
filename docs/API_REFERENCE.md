# API Reference

Complete API documentation for programmatic usage of the ASCII Art Generator.

---

## Table of Contents

- [Text Generation](#text-generation)
- [Image Conversion](#image-conversion)
- [Pattern Generation](#pattern-generation)
- [Effects](#effects)
- [Colors & Gradients](#colors--gradients)
- [Animations](#animations)
- [Composition](#composition)
- [Templates](#templates)
- [Batch Processing](#batch-processing)
- [Diagrams](#diagrams)
- [Export](#export)

---

## Text Generation

### TextArtGenerator

Generate ASCII art from text using various fonts.

```python
from generators.text_art import TextArtGenerator
from utils.config import Config

config = Config()
generator = TextArtGenerator(config)
```

#### Methods

##### `generate(text, font='standard', width=None)`

Generate ASCII art from text.

**Parameters:**
- `text` (str): Text to convert
- `font` (str): Font style ('standard', 'banner', 'block', 'slant', 'small', 'bubble')
- `width` (int, optional): Maximum width

**Returns:** str - ASCII art

**Example:**
```python
art = generator.generate("Hello", font='banner')
print(art)
```

##### `list_fonts()`

Get list of available fonts.

**Returns:** List[str] - Font names

---

## Image Conversion

### ImageArtGenerator

Convert images to ASCII art.

```python
from generators.image_art import ImageArtGenerator
from utils.config import Config

config = Config()
generator = ImageArtGenerator(config)
```

#### Methods

##### `generate(image_path, width=80, charset='standard')`

Convert image to ASCII art.

**Parameters:**
- `image_path` (str): Path to image file
- `width` (int): Output width in characters
- `charset` (str): Character set ('standard', 'detailed', 'simple', 'blocks')

**Returns:** str - ASCII art

**Example:**
```python
ascii_art = generator.generate('photo.jpg', width=100, charset='detailed')
print(ascii_art)
```

---

## Pattern Generation

### PatternGenerator

Generate basic patterns and borders.

```python
from generators.pattern_art import PatternGenerator
from utils.config import Config

config = Config()
generator = PatternGenerator(config)
```

#### Methods

##### `generate_box(width, height, style='single')`

Generate a box pattern.

**Parameters:**
- `width` (int): Box width
- `height` (int): Box height
- `style` (str): Border style ('single', 'double', 'thick', 'ascii')

**Returns:** str - Box pattern

##### `generate_diamond(width, height)`

Generate a diamond pattern.

**Parameters:**
- `width` (int): Canvas width
- `height` (int): Canvas height

**Returns:** str - Diamond pattern

### AdvancedPatternGenerator

Generate complex mathematical patterns.

```python
from generators.advanced_patterns import AdvancedPatternGenerator

generator = AdvancedPatternGenerator()
```

#### Methods

##### `generate_mandelbrot(width=80, height=40, max_iter=20)`

Generate Mandelbrot set.

**Parameters:**
- `width` (int): Output width
- `height` (int): Output height
- `max_iter` (int): Maximum iterations

**Returns:** str - Mandelbrot set ASCII art

##### `generate_maze(width, height)`

Generate a maze using recursive backtracking.

**Parameters:**
- `width` (int): Maze width (must be odd)
- `height` (int): Maze height (must be odd)

**Returns:** str - Maze pattern

##### `generate_tree(height=15, style='pine')`

Generate ASCII tree.

**Parameters:**
- `height` (int): Tree height
- `style` (str): Tree style ('pine', 'oak', 'palm')

**Returns:** str - Tree pattern

---

## Effects

### TextEffects

Apply visual effects to ASCII art.

```python
from generators.text_effects import TextEffects

effects = TextEffects()
```

#### Methods

##### `add_shadow(text, direction='bottom-right', shadow_char='░')`

Add shadow effect.

**Parameters:**
- `text` (str): Input ASCII art
- `direction` (str): Shadow direction ('bottom-right', 'bottom', 'right')
- `shadow_char` (str): Character for shadow

**Returns:** str - ASCII art with shadow

##### `add_outline(text, outline_char='#', thickness=1)`

Add outline around ASCII art.

**Parameters:**
- `text` (str): Input ASCII art
- `outline_char` (str): Character for outline
- `thickness` (int): Outline thickness

**Returns:** str - ASCII art with outline

##### `add_3d_effect(text, depth=3, direction='right')`

Add 3D depth effect.

**Parameters:**
- `text` (str): Input ASCII art
- `depth` (int): Depth of 3D effect
- `direction` (str): Direction ('right', 'left', 'down', 'up')

**Returns:** str - ASCII art with 3D effect

##### `add_glow(text, intensity=2)`

Add glow effect around characters.

**Parameters:**
- `text` (str): Input ASCII art
- `intensity` (int): Glow radius

**Returns:** str - ASCII art with glow

##### `add_mirror(text, axis='vertical')`

Add mirror effect.

**Parameters:**
- `text` (str): Input ASCII art
- `axis` (str): Mirror axis ('vertical', 'horizontal')

**Returns:** str - Mirrored ASCII art

---

## Colors & Gradients

### GradientGenerator

Apply color gradients to ASCII art.

```python
from generators.color_art import GradientGenerator

gradient_gen = GradientGenerator()
```

#### Methods

##### `apply_gradient_to_text(text, gradient_type='rainbow')`

Apply color gradient to text.

**Parameters:**
- `text` (str): Input ASCII art
- `gradient_type` (str): Gradient type ('rainbow', 'fire', 'ocean', 'forest')

**Returns:** str - Colored ASCII art with ANSI codes

**Example:**
```python
colored = gradient_gen.apply_gradient_to_text(art, 'rainbow')
print(colored)  # Requires terminal with color support
```

##### `linear_gradient(start_color, end_color, steps)`

Generate linear gradient.

**Parameters:**
- `start_color` (Tuple[int, int, int]): Starting RGB color
- `end_color` (Tuple[int, int, int]): Ending RGB color
- `steps` (int): Number of steps

**Returns:** List[Tuple[int, int, int]] - List of RGB colors

### ColorImageConverter

Convert images to colored ASCII art.

```python
from generators.color_art import ColorImageConverter

converter = ColorImageConverter()
```

#### Methods

##### `convert_to_colored_ascii(image_path, width=80, charset=' .:-=+*#%@')`

Convert image to colored ASCII art.

**Parameters:**
- `image_path` (str): Path to image
- `width` (int): Output width
- `charset` (str): Character set

**Returns:** str - Colored ASCII art

---

## Animations

### AnimationGenerator

Generate ASCII animations.

```python
from generators.animation import AnimationGenerator

anim_gen = AnimationGenerator()
```

#### Methods

##### `wave_animation(width=60, height=15, frames=30)`

Generate wave animation.

**Parameters:**
- `width` (int): Canvas width
- `height` (int): Canvas height
- `frames` (int): Number of frames

**Returns:** Animation - Animation object

##### `matrix_rain(width=80, height=20, frames=50)`

Generate Matrix-style rain animation.

**Parameters:**
- `width` (int): Canvas width
- `height` (int): Canvas height
- `frames` (int): Number of frames

**Returns:** Animation - Animation object

##### `bouncing_ball(width=40, height=10, frames=20)`

Generate bouncing ball animation.

**Parameters:**
- `width` (int): Canvas width
- `height` (int): Canvas height
- `frames` (int): Number of frames

**Returns:** Animation - Animation object

### Animation Class

```python
animation = anim_gen.wave_animation(60, 15, 30)
```

#### Methods

##### `play(loop=False, clear_screen=True)`

Play animation in terminal.

**Parameters:**
- `loop` (bool): Whether to loop
- `clear_screen` (bool): Clear screen between frames

##### `export_frames(output_dir, prefix='frame')`

Export frames to files.

**Parameters:**
- `output_dir` (str): Output directory
- `prefix` (str): Filename prefix

---

## Composition

### Compositor

Compose multiple ASCII art elements.

```python
from generators.composition import Compositor

compositor = Compositor()
```

#### Methods

##### `horizontal_concat(*arts, spacing=2, alignment=Alignment.TOP)`

Concatenate ASCII arts horizontally.

**Parameters:**
- `*arts` (str): ASCII art strings
- `spacing` (int): Space between elements
- `alignment` (Alignment): Vertical alignment

**Returns:** str - Combined ASCII art

**Example:**
```python
from generators.composition import Alignment

art1 = "ASCII"
art2 = "ART"
combined = compositor.horizontal_concat(art1, art2, spacing=5)
```

##### `vertical_concat(*arts, spacing=1, alignment=Alignment.LEFT)`

Concatenate ASCII arts vertically.

**Parameters:**
- `*arts` (str): ASCII art strings
- `spacing` (int): Space between elements
- `alignment` (Alignment): Horizontal alignment

**Returns:** str - Combined ASCII art

##### `grid_layout(arts, cols, cell_width=None, cell_height=None, spacing=2)`

Arrange ASCII arts in grid.

**Parameters:**
- `arts` (List[str]): List of ASCII art strings
- `cols` (int): Number of columns
- `cell_width` (int, optional): Cell width
- `cell_height` (int, optional): Cell height
- `spacing` (int): Space between cells

**Returns:** str - Grid layout

##### `frame(content, title='', style='double', padding=1)`

Add frame around content.

**Parameters:**
- `content` (str): ASCII art content
- `title` (str): Optional title
- `style` (str): Frame style
- `padding` (int): Internal padding

**Returns:** str - Framed ASCII art

---

## Templates

### TemplateManager

Manage ASCII art templates.

```python
from templates.template_manager import TemplateManager

manager = TemplateManager()
```

#### Methods

##### `get_template(name)`

Get template by name.

**Parameters:**
- `name` (str): Template name

**Returns:** Template - Template object or None

##### `list_templates(category=None)`

List available templates.

**Parameters:**
- `category` (str, optional): Filter by category

**Returns:** List[Template] - List of templates

##### `list_categories()`

Get list of template categories.

**Returns:** List[str] - Category names

##### `search_templates(query)`

Search templates.

**Parameters:**
- `query` (str): Search query

**Returns:** List[Template] - Matching templates

### Template Class

```python
template = manager.get_template('welcome_banner')
```

#### Methods

##### `render(**kwargs)`

Render template with variables.

**Parameters:**
- `**kwargs`: Variable values

**Returns:** str - Rendered template

**Example:**
```python
output = template.render(
    title="MY APP",
    subtitle="Version 2.0"
)
```

---

## Batch Processing

### BatchProcessor

Process multiple files in parallel.

```python
from utils.batch_processor import BatchProcessor

processor = BatchProcessor(max_workers=4)
```

#### Methods

##### `process_files(input_pattern, output_dir, processor_func, **kwargs)`

Process multiple files.

**Parameters:**
- `input_pattern` (str): Glob pattern for input files
- `output_dir` (str): Output directory
- `processor_func` (Callable): Processing function
- `**kwargs`: Additional arguments

**Returns:** List[BatchResult] - Processing results

**Example:**
```python
from utils.batch_processor import BatchImageConverter

converter = BatchImageConverter(width=80)
results = processor.process_files(
    "images/*.jpg",
    "output",
    converter.convert
)
```

##### `get_summary()`

Get processing summary.

**Returns:** Dict[str, Any] - Summary statistics

##### `print_summary()`

Print processing summary.

---

## Diagrams

### FlowchartGenerator

Generate flowchart diagrams.

```python
from generators.diagrams import FlowchartGenerator

flow = FlowchartGenerator()
```

#### Methods

##### `add_node(node_id, label, node_type='process')`

Add node to flowchart.

**Parameters:**
- `node_id` (str): Unique node ID
- `label` (str): Node label
- `node_type` (str): Node type ('process', 'decision', 'start', 'end')

##### `add_edge(from_node, to_node, label='')`

Add edge between nodes.

**Parameters:**
- `from_node` (str): Source node ID
- `to_node` (str): Target node ID
- `label` (str, optional): Edge label

##### `generate()`

Generate the flowchart.

**Returns:** str - ASCII flowchart

**Example:**
```python
flow.add_node('start', 'Start', 'start')
flow.add_node('process', 'Process Data', 'process')
flow.add_edge('start', 'process')
diagram = flow.generate()
```

### UMLGenerator

Generate UML diagrams.

```python
from generators.diagrams import UMLGenerator

uml = UMLGenerator()
```

#### Methods

##### `class_diagram(classes)`

Generate UML class diagram.

**Parameters:**
- `classes` (Dict[str, Dict]): Class definitions

**Returns:** str - UML diagram

**Example:**
```python
diagram = uml.class_diagram({
    'User': {
        'attributes': ['name', 'email'],
        'methods': ['login()', 'logout()']
    }
})
```

---

### GanttChartGenerator

Generate Gantt charts for project management and timeline visualization.

```python
from generators.diagrams import GanttChartGenerator

gantt = GanttChartGenerator()
```

#### Methods

##### `add_task(name, start_day, duration, progress=0, dependencies=None)`

Add a task to the Gantt chart.

**Parameters:**
- `name` (str): Task name
- `start_day` (int): Start day (0-indexed)
- `duration` (int): Duration in days
- `progress` (int): Progress percentage (0-100)
- `dependencies` (List[str], optional): List of task names this depends on

**Example:**
```python
gantt.add_task("Requirements", start_day=0, duration=5, progress=100)
gantt.add_task("Design", start_day=5, duration=7, progress=75)
gantt.add_task("Development", start_day=12, duration=15, progress=40)
```

##### `generate(width=80, show_progress=True)`

Generate the Gantt chart.

**Parameters:**
- `width` (int): Chart width in characters
- `show_progress` (bool): Whether to show progress percentages

**Returns:** str - ASCII Gantt chart

**Example:**
```python
chart = gantt.generate(width=100, show_progress=True)
print(chart)
```

**Output:**
```
====================================================================================================
                                            Gantt Chart                                             
====================================================================================================

                       │ Prog. │ D0   D5   D10  D15  D20  
───────────────────────┼───────┼────────────────────────────
Requirements           │ 100% │ █████◆                     
Design                 │  75% │      ███████                
Development            │  40% │             ██████░░░░░░░  
====================================================================================================

Legend: █ Complete  ░ Remaining  ◆ Milestone
```

**Use Cases:**
- Project planning and tracking
- Sprint visualization
- Task timeline documentation
- Project status reports

---

### ERDGenerator

Generate Entity Relationship Diagrams for database schema documentation.

```python
from generators.diagrams import ERDGenerator

erd = ERDGenerator()
```

#### Methods

##### `add_entity(name, attributes)`

Add an entity (database table) to the diagram.

**Parameters:**
- `name` (str): Entity name
- `attributes` (List[Dict]): List of attribute dictionaries with keys:
  - `name` (str): Attribute name
  - `type` (str): Data type
  - `key` (str, optional): 'PK' for primary key, 'FK' for foreign key

**Example:**
```python
erd.add_entity("Users", [
    {'name': 'user_id', 'type': 'INT', 'key': 'PK'},
    {'name': 'username', 'type': 'VARCHAR(50)'},
    {'name': 'email', 'type': 'VARCHAR(100)'},
    {'name': 'created_at', 'type': 'TIMESTAMP'}
])

erd.add_entity("Orders", [
    {'name': 'order_id', 'type': 'INT', 'key': 'PK'},
    {'name': 'user_id', 'type': 'INT', 'key': 'FK'},
    {'name': 'total', 'type': 'DECIMAL(10,2)'}
])
```

##### `add_relationship(from_entity, to_entity, relationship_type, label='')`

Add a relationship between entities.

**Parameters:**
- `from_entity` (str): Source entity name
- `to_entity` (str): Target entity name
- `relationship_type` (str): Relationship type ('1:1', '1:N', 'N:M')
- `label` (str, optional): Relationship description

**Example:**
```python
erd.add_relationship("Users", "Orders", "1:N", "places")
erd.add_relationship("Orders", "OrderItems", "1:N", "contains")
erd.add_relationship("Products", "Categories", "N:1", "belongs to")
```

##### `generate()`

Generate the ERD diagram.

**Returns:** str - ASCII ERD diagram

**Example:**
```python
diagram = erd.generate()
print(diagram)
```

**Output:**
```
================================================================================
                          Entity Relationship Diagram                           
================================================================================

┌──────────────────────────────────┐
│              USERS               │
├──────────────────────────────────┤
│ [PK] user_id : INT               │
│      username : VARCHAR(50)      │
│      email : VARCHAR(100)        │
│      created_at : TIMESTAMP      │
└──────────────────────────────────┘

  Users ──────> Orders  (places)  [1:N]

┌────────────────────────────┐
│          ORDERS            │
├────────────────────────────┤
│ [PK] order_id : INT        │
│ [FK] user_id : INT         │
│      total : DECIMAL(10,2) │
└────────────────────────────┘

================================================================================
Legend:
  PK = Primary Key
  FK = Foreign Key
  1:1 = One-to-One
  1:N = One-to-Many
  N:M = Many-to-Many
```

**Use Cases:**
- Database schema documentation
- API documentation (data models)
- Technical specifications
- System architecture diagrams
- Teaching database design

---

## Export

### HTMLExporter

Export to HTML format.

```python
from exporters.formats import HTMLExporter

exporter = HTMLExporter()
```

#### Methods

##### `export(ascii_art, title='ASCII Art', font_family=None, bg_color=None, fg_color=None, font_size=14)`

Export to HTML.

**Parameters:**
- `ascii_art` (str): ASCII art content
- `title` (str): Page title
- `font_family` (str, optional): Font family
- `bg_color` (str, optional): Background color
- `fg_color` (str, optional): Foreground color
- `font_size` (int): Font size in pixels

**Returns:** str - HTML string

### SVGExporter

Export to SVG format.

```python
from exporters.formats import SVGExporter

exporter = SVGExporter()
```

#### Methods

##### `export(ascii_art, title='ASCII Art', font_size=14, font_family='monospace', fg_color='#000000', bg_color='#ffffff')`

Export to SVG.

**Parameters:**
- `ascii_art` (str): ASCII art content
- `title` (str): SVG title
- `font_size` (int): Font size
- `font_family` (str): Font family
- `fg_color` (str): Foreground color
- `bg_color` (str): Background color

**Returns:** str - SVG string

### MarkdownExporter

Export to Markdown format.

```python
from exporters.formats import MarkdownExporter

exporter = MarkdownExporter()
```

#### Methods

##### `export(ascii_art, title='ASCII Art', description='')`

Export to Markdown.

**Parameters:**
- `ascii_art` (str): ASCII art content
- `title` (str): Title
- `description` (str): Description

**Returns:** str - Markdown string

---

## Configuration

### Config

Global configuration object.

```python
from utils.config import Config

config = Config(color_enabled=True)
```

#### Attributes

- `color_enabled` (bool): Enable color output
- `default_width` (int): Default width (80)
- `default_height` (int): Default height (20)
- `charsets` (Dict): Available character sets

#### Methods

##### `get_charset(name='standard')`

Get character set by name.

**Parameters:**
- `name` (str): Charset name

**Returns:** str - Character set string

##### `colorize(text, color)`

Apply color to text.

**Parameters:**
- `text` (str): Text to colorize
- `color` (str): Color name

**Returns:** str - Colorized text

---

## Error Handling

All generators handle errors gracefully and return error messages as strings.

```python
try:
    art = generator.generate(text)
except Exception as e:
    print(f"Error: {e}")
```

---

## Best Practices

1. **Reuse Config Objects**: Create once, use everywhere
2. **Check Dependencies**: Use try/except for optional features
3. **Cache Results**: Store generated art for reuse
4. **Validate Input**: Check file paths and parameters
5. **Handle Errors**: Always catch exceptions

---

## Examples

See `examples/` directory for complete working examples.

---

## Support

- Documentation: See `docs/` directory
- Issues: GitHub Issues
- Discussions: GitHub Discussions
- Email: support@example.com

