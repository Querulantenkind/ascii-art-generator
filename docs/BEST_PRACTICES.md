# Best Practices

Guidelines for using the ASCII Art Generator effectively and efficiently.

---

## Table of Contents

- [Performance](#performance)
- [Code Organization](#code-organization)
- [Error Handling](#error-handling)
- [Resource Management](#resource-management)
- [Output Quality](#output-quality)
- [Maintenance](#maintenance)
- [Security](#security)

---

## Performance

### 1. Reuse Configuration Objects

**❌ Don't:**
```python
for text in texts:
    config = Config()  # Creates new config each time
    gen = TextArtGenerator(config)
    art = gen.generate(text)
```

**✅ Do:**
```python
config = Config()  # Create once
gen = TextArtGenerator(config)

for text in texts:
    art = gen.generate(text)  # Reuse generator
```

### 2. Use Batch Processing for Multiple Files

**❌ Don't:**
```python
for image in images:
    # Process one at a time
    ascii_art = convert_image(image)
```

**✅ Do:**
```python
from utils.batch_processor import BatchProcessor

processor = BatchProcessor(max_workers=8)
results = processor.process_files(
    "images/*.jpg",
    "output",
    convert_image
)
```

### 3. Cache Expensive Operations

**✅ Do:**
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def generate_pattern(width, height, pattern_type):
    # Expensive operation
    return pattern
```

### 4. Choose Appropriate Character Sets

**For Speed:**
- Use 'simple' charset (fewer characters)
- Lower resolution (smaller width)

**For Quality:**
- Use 'detailed' charset (more characters)
- Higher resolution (larger width)

```python
# Fast preview
preview = generator.generate(image, width=40, charset='simple')

# High quality
final = generator.generate(image, width=120, charset='detailed')
```

### 5. Optimize Parallel Workers

```python
import os

# Don't exceed CPU count
cpu_count = os.cpu_count()
optimal_workers = min(cpu_count, 8)

processor = BatchProcessor(max_workers=optimal_workers)
```

---

## Code Organization

### 1. Structure Your Projects

```
my_project/
├── generators/      # Custom generators
├── templates/       # Custom templates
├── output/          # Generated art
├── scripts/         # Automation scripts
└── config.py        # Configuration
```

### 2. Use Configuration Files

```python
# config.py
from utils.config import Config

# Development config
DEV_CONFIG = Config(
    color_enabled=True,
    default_width=80
)

# Production config
PROD_CONFIG = Config(
    color_enabled=False,
    default_width=120
)
```

### 3. Create Reusable Functions

```python
def generate_project_banner(project_name, version):
    """Generate standardized project banner."""
    from generators.text_art import TextArtGenerator
    from generators.text_effects import TextEffects
    from utils.config import Config
    
    config = Config()
    gen = TextArtGenerator(config)
    effects = TextEffects()
    
    logo = gen.generate(project_name, font='banner')
    logo = effects.add_3d_effect(logo)
    
    subtitle = f"Version {version}"
    
    return f"{logo}\n\n{subtitle.center(60)}"
```

### 4. Use Type Hints

```python
from typing import Optional, List

def process_images(
    image_paths: List[str],
    width: int = 80,
    charset: str = 'standard'
) -> List[str]:
    """Process multiple images to ASCII art."""
    results = []
    for path in image_paths:
        art = convert_image(path, width, charset)
        results.append(art)
    return results
```

---

## Error Handling

### 1. Always Handle Exceptions

**❌ Don't:**
```python
art = generator.generate(text)  # May fail
```

**✅ Do:**
```python
try:
    art = generator.generate(text)
except Exception as e:
    print(f"Error generating art: {e}")
    art = fallback_art
```

### 2. Validate Input

```python
def generate_safe(text: str, font: str = 'standard') -> str:
    """Generate art with validation."""
    # Validate text
    if not text or not text.strip():
        raise ValueError("Text cannot be empty")
    
    # Validate font
    valid_fonts = ['standard', 'banner', 'block']
    if font not in valid_fonts:
        raise ValueError(f"Invalid font. Choose from: {valid_fonts}")
    
    return generator.generate(text, font=font)
```

### 3. Provide Meaningful Error Messages

**❌ Don't:**
```python
raise Exception("Error")
```

**✅ Do:**
```python
raise ValueError(
    f"Invalid width: {width}. Must be between 10 and 200."
)
```

### 4. Use Context Managers

```python
from contextlib import contextmanager

@contextmanager
def ascii_art_session(config):
    """Context manager for ASCII art generation."""
    generator = TextArtGenerator(config)
    try:
        yield generator
    finally:
        # Cleanup if needed
        pass

# Usage
with ascii_art_session(config) as gen:
    art = gen.generate("Hello")
```

---

## Resource Management

### 1. Clean Up Temporary Files

```python
import tempfile
import os

# Create temp file
temp_file = tempfile.NamedTemporaryFile(delete=False)
temp_path = temp_file.name

try:
    # Use temp file
    process_file(temp_path)
finally:
    # Always clean up
    if os.path.exists(temp_path):
        os.remove(temp_path)
```

### 2. Limit Memory Usage

```python
# Process large files in chunks
def process_large_video(video_path, chunk_size=100):
    """Process video in chunks to limit memory."""
    total_frames = get_frame_count(video_path)
    
    for start in range(0, total_frames, chunk_size):
        end = min(start + chunk_size, total_frames)
        process_frame_range(video_path, start, end)
        # Memory is freed after each chunk
```

### 3. Use Generators for Large Datasets

**❌ Don't:**
```python
def get_all_frames(video_path):
    frames = []
    for frame in extract_frames(video_path):
        frames.append(frame)  # Loads all into memory
    return frames
```

**✅ Do:**
```python
def get_frames(video_path):
    """Generator that yields frames one at a time."""
    for frame in extract_frames(video_path):
        yield frame  # Memory efficient
```

---

## Output Quality

### 1. Choose Appropriate Dimensions

```python
# Terminal display
terminal_width = 80
terminal_height = 24

# Web display
web_width = 120
web_height = 60

# Print/PDF
print_width = 200
print_height = 100
```

### 2. Test Different Fonts

```python
def find_best_font(text):
    """Test all fonts and return best looking one."""
    fonts = ['standard', 'banner', 'block', 'slant']
    results = {}
    
    for font in fonts:
        art = generator.generate(text, font=font)
        # Score based on criteria
        score = calculate_quality_score(art)
        results[font] = score
    
    return max(results, key=results.get)
```

### 3. Optimize for Medium

```python
# Terminal (monospace, limited colors)
terminal_art = generate_for_terminal(
    text,
    width=80,
    use_colors=True,
    charset='standard'
)

# Web (flexible sizing, full colors)
web_art = generate_for_web(
    text,
    width=120,
    use_colors=True,
    charset='detailed',
    export_format='html'
)

# Print (high resolution, no colors)
print_art = generate_for_print(
    text,
    width=200,
    use_colors=False,
    charset='detailed',
    export_format='pdf'
)
```

### 4. Preview Before Final Generation

```python
# Quick preview
preview = generator.generate(text, width=40)
print("Preview:", preview)

# If satisfied, generate full quality
if input("Generate full quality? (y/n): ").lower() == 'y':
    final = generator.generate(text, width=120)
```

---

## Maintenance

### 1. Version Your Output

```python
import datetime

def save_with_version(art, base_name):
    """Save with timestamp version."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{base_name}_{timestamp}.txt"
    
    with open(filename, 'w') as f:
        f.write(art)
    
    return filename
```

### 2. Document Your Code

```python
def generate_complex_composition(
    elements: List[str],
    layout: str = 'grid',
    **kwargs
) -> str:
    """
    Generate complex composition from multiple elements.
    
    Args:
        elements: List of ASCII art strings to compose
        layout: Layout type ('grid', 'horizontal', 'vertical')
        **kwargs: Additional layout-specific parameters
            - For 'grid': cols (int), spacing (int)
            - For 'horizontal': spacing (int), alignment (str)
            - For 'vertical': spacing (int), alignment (str)
    
    Returns:
        Composed ASCII art string
    
    Example:
        >>> elements = ["ART1", "ART2", "ART3"]
        >>> result = generate_complex_composition(
        ...     elements,
        ...     layout='grid',
        ...     cols=2,
        ...     spacing=3
        ... )
    """
    # Implementation
    pass
```

### 3. Log Important Operations

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def batch_process_with_logging(files):
    """Process files with logging."""
    logger.info(f"Starting batch processing of {len(files)} files")
    
    for i, file in enumerate(files):
        try:
            process_file(file)
            logger.info(f"Processed {i+1}/{len(files)}: {file}")
        except Exception as e:
            logger.error(f"Failed to process {file}: {e}")
    
    logger.info("Batch processing complete")
```

### 4. Create Tests

```python
import unittest

class TestTextGeneration(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        self.generator = TextArtGenerator(self.config)
    
    def test_basic_generation(self):
        """Test basic text generation."""
        art = self.generator.generate("TEST")
        self.assertIsNotNone(art)
        self.assertIn("TEST", art.upper())
    
    def test_font_selection(self):
        """Test different fonts."""
        for font in ['standard', 'banner', 'block']:
            art = self.generator.generate("A", font=font)
            self.assertIsNotNone(art)
```

---

## Security

### 1. Validate File Paths

```python
import os

def safe_file_path(path, allowed_dir):
    """Ensure file path is within allowed directory."""
    abs_path = os.path.abspath(path)
    abs_allowed = os.path.abspath(allowed_dir)
    
    if not abs_path.startswith(abs_allowed):
        raise ValueError(f"Path {path} is outside allowed directory")
    
    return abs_path
```

### 2. Sanitize User Input

```python
import re

def sanitize_text(text):
    """Sanitize user input."""
    # Remove control characters
    text = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', text)
    
    # Limit length
    max_length = 1000
    if len(text) > max_length:
        text = text[:max_length]
    
    return text
```

### 3. Limit Resource Usage

```python
def generate_with_limits(text, max_width=200, max_height=100):
    """Generate with resource limits."""
    if len(text) > 1000:
        raise ValueError("Text too long")
    
    if max_width > 200 or max_height > 100:
        raise ValueError("Dimensions too large")
    
    return generator.generate(text)
```

### 4. Handle Untrusted Input

```python
def process_user_template(template_data):
    """Process template from untrusted source."""
    # Validate template structure
    required_fields = ['name', 'content', 'variables']
    for field in required_fields:
        if field not in template_data:
            raise ValueError(f"Missing required field: {field}")
    
    # Sanitize content
    template_data['content'] = sanitize_text(template_data['content'])
    
    # Limit variable count
    if len(template_data['variables']) > 50:
        raise ValueError("Too many variables")
    
    return template_data
```

---

## Common Pitfalls

### 1. Not Checking Terminal Size

```python
import shutil

def get_terminal_size():
    """Get terminal dimensions."""
    columns, rows = shutil.get_terminal_size()
    return columns, rows

# Use terminal size for output
width, height = get_terminal_size()
art = generator.generate(text, width=width-10)  # Leave margin
```

### 2. Ignoring Character Encoding

```python
# Always specify encoding
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(ascii_art)
```

### 3. Not Testing on Target Platform

```python
# Test on actual deployment environment
# - Terminal type
# - Color support
# - Font availability
# - Character encoding
```

---

## Performance Checklist

- [ ] Reuse configuration objects
- [ ] Use batch processing for multiple files
- [ ] Cache expensive operations
- [ ] Choose appropriate character sets
- [ ] Optimize parallel workers
- [ ] Profile code for bottlenecks
- [ ] Monitor memory usage
- [ ] Use generators for large datasets

## Quality Checklist

- [ ] Test different fonts
- [ ] Preview before final generation
- [ ] Validate output dimensions
- [ ] Check terminal compatibility
- [ ] Test color support
- [ ] Verify character encoding
- [ ] Review output on target medium

## Maintenance Checklist

- [ ] Version your output
- [ ] Document your code
- [ ] Log important operations
- [ ] Create tests
- [ ] Handle errors gracefully
- [ ] Clean up resources
- [ ] Monitor performance

---

## Additional Resources

- [API Reference](API_REFERENCE.md)
- [Tutorials](TUTORIALS.md)
- [Examples](../examples/)
- [FAQ](FAQ.md)

