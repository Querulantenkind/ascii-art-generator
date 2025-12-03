"""Color palette management system for ASCII art."""

import json
import os
from typing import List, Tuple, Optional, Dict, Any
from dataclasses import dataclass, field, asdict
from pathlib import Path


@dataclass
class ColorPalette:
    """Represents a color palette with gradient support."""
    
    name: str
    colors: List[Tuple[int, int, int]]  # List of RGB tuples
    gradient_type: str = 'linear'  # 'linear', 'smooth', 'custom'
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Validate palette after initialization."""
        if len(self.colors) < 2:
            raise ValueError("Palette must have at least 2 colors")
        if not all(isinstance(c, tuple) and len(c) == 3 for c in self.colors):
            raise ValueError("All colors must be RGB tuples (r, g, b)")
        if not all(0 <= c <= 255 for color in self.colors for c in color):
            raise ValueError("RGB values must be between 0 and 255")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert palette to dictionary for JSON serialization.
        
        Returns:
            Dictionary representation
        """
        return {
            'name': self.name,
            'colors': [list(c) for c in self.colors],  # Convert tuples to lists
            'gradient_type': self.gradient_type,
            'metadata': self.metadata
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ColorPalette':
        """Create palette from dictionary.
        
        Args:
            data: Dictionary with palette data
            
        Returns:
            ColorPalette instance
        """
        colors = [tuple(c) for c in data['colors']]  # Convert lists to tuples
        return cls(
            name=data['name'],
            colors=colors,
            gradient_type=data.get('gradient_type', 'linear'),
            metadata=data.get('metadata', {})
        )
    
    def get_gradient(self, steps: int) -> List[Tuple[int, int, int]]:
        """Generate gradient from palette colors.
        
        Args:
            steps: Number of gradient steps
            
        Returns:
            List of RGB colors
        """
        if self.gradient_type == 'linear':
            return self._linear_gradient(steps)
        elif self.gradient_type == 'smooth':
            return self._smooth_gradient(steps)
        else:
            return self._linear_gradient(steps)
    
    def _linear_gradient(self, steps: int) -> List[Tuple[int, int, int]]:
        """Generate linear gradient between palette colors.
        
        Args:
            steps: Number of steps
            
        Returns:
            List of RGB colors
        """
        if steps <= len(self.colors):
            return self.colors[:steps]
        
        gradient = []
        segments = len(self.colors) - 1
        steps_per_segment = steps // segments
        
        for i in range(segments):
            start_color = self.colors[i]
            end_color = self.colors[i + 1]
            
            segment_steps = steps_per_segment if i < segments - 1 else steps - len(gradient)
            
            for j in range(segment_steps):
                t = j / (segment_steps - 1) if segment_steps > 1 else 0
                r = int(start_color[0] + (end_color[0] - start_color[0]) * t)
                g = int(start_color[1] + (end_color[1] - start_color[1]) * t)
                b = int(start_color[2] + (end_color[2] - start_color[2]) * t)
                gradient.append((r, g, b))
        
        return gradient
    
    def _smooth_gradient(self, steps: int) -> List[Tuple[int, int, int]]:
        """Generate smooth gradient using cosine interpolation.
        
        Args:
            steps: Number of steps
            
        Returns:
            List of RGB colors
        """
        import math
        
        if steps <= len(self.colors):
            return self.colors[:steps]
        
        gradient = []
        segments = len(self.colors) - 1
        steps_per_segment = steps // segments
        
        for i in range(segments):
            start_color = self.colors[i]
            end_color = self.colors[i + 1]
            
            segment_steps = steps_per_segment if i < segments - 1 else steps - len(gradient)
            
            for j in range(segment_steps):
                t = j / (segment_steps - 1) if segment_steps > 1 else 0
                # Smooth interpolation using cosine
                smooth_t = (1 - math.cos(t * math.pi)) / 2
                
                r = int(start_color[0] + (end_color[0] - start_color[0]) * smooth_t)
                g = int(start_color[1] + (end_color[1] - start_color[1]) * smooth_t)
                b = int(start_color[2] + (end_color[2] - start_color[2]) * smooth_t)
                gradient.append((r, g, b))
        
        return gradient


class PaletteManager:
    """Manages color palettes with file I/O."""
    
    def __init__(self, palettes_dir: Optional[str] = None):
        """Initialize palette manager.
        
        Args:
            palettes_dir: Directory for palette files (default: palettes/ in project root)
        """
        if palettes_dir is None:
            # Get project root (parent of utils/)
            project_root = Path(__file__).parent.parent
            palettes_dir = str(project_root / 'palettes')
        
        self.palettes_dir = Path(palettes_dir)
        self.palettes_dir.mkdir(exist_ok=True)
        
        # Cache for loaded palettes
        self._palette_cache: Dict[str, ColorPalette] = {}
    
    def create_palette(self, name: str, colors: List[Tuple[int, int, int]],
                      gradient_type: str = 'linear',
                      metadata: Optional[Dict[str, Any]] = None) -> ColorPalette:
        """Create a new color palette.
        
        Args:
            name: Palette name
            colors: List of RGB color tuples
            gradient_type: Type of gradient ('linear', 'smooth')
            metadata: Optional metadata dictionary
            
        Returns:
            Created ColorPalette instance
        """
        palette = ColorPalette(
            name=name,
            colors=colors,
            gradient_type=gradient_type,
            metadata=metadata or {}
        )
        
        self._palette_cache[name] = palette
        return palette
    
    def save_palette(self, palette: ColorPalette, filename: Optional[str] = None) -> str:
        """Save palette to file.
        
        Args:
            palette: ColorPalette to save
            filename: Optional filename (default: palette name + .json)
            
        Returns:
            Path to saved file
        """
        if filename is None:
            # Sanitize name for filename
            safe_name = "".join(c for c in palette.name if c.isalnum() or c in (' ', '-', '_')).strip()
            safe_name = safe_name.replace(' ', '_').lower()
            filename = f"{safe_name}.json"
        
        if not filename.endswith('.json'):
            filename += '.json'
        
        filepath = self.palettes_dir / filename
        
        # Convert to dict and save
        palette_dict = palette.to_dict()
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(palette_dict, f, indent=2, ensure_ascii=False)
        
        # Update cache
        self._palette_cache[palette.name] = palette
        
        return str(filepath)
    
    def load_palette(self, name_or_path: str) -> ColorPalette:
        """Load palette by name or file path.
        
        Args:
            name_or_path: Palette name or file path
            
        Returns:
            Loaded ColorPalette instance
        """
        # Check cache first
        if name_or_path in self._palette_cache:
            return self._palette_cache[name_or_path]
        
        # Try as file path
        if os.path.exists(name_or_path):
            filepath = Path(name_or_path)
        else:
            # Try as filename in palettes directory
            if not name_or_path.endswith('.json'):
                name_or_path += '.json'
            filepath = self.palettes_dir / name_or_path
        
        if not filepath.exists():
            raise FileNotFoundError(f"Palette not found: {name_or_path}")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        palette = ColorPalette.from_dict(data)
        self._palette_cache[palette.name] = palette
        
        return palette
    
    def list_palettes(self) -> List[str]:
        """List all available palette names.
        
        Returns:
            List of palette names
        """
        palettes = []
        
        # List JSON files in palettes directory
        for filepath in self.palettes_dir.glob('*.json'):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    palettes.append(data.get('name', filepath.stem))
            except Exception:
                continue
        
        return sorted(palettes)
    
    def get_palette(self, name: str) -> Optional[ColorPalette]:
        """Get palette by name (loads if not cached).
        
        Args:
            name: Palette name
            
        Returns:
            ColorPalette or None if not found
        """
        if name in self._palette_cache:
            return self._palette_cache[name]
        
        # Try to load
        try:
            return self.load_palette(name)
        except FileNotFoundError:
            return None
    
    def delete_palette(self, name: str) -> bool:
        """Delete palette by name.
        
        Args:
            name: Palette name
            
        Returns:
            True if deleted, False if not found
        """
        # Find file
        for filepath in self.palettes_dir.glob('*.json'):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if data.get('name') == name:
                        filepath.unlink()
                        if name in self._palette_cache:
                            del self._palette_cache[name]
                        return True
            except Exception:
                continue
        
        return False
    
    def get_builtin_palettes(self) -> Dict[str, ColorPalette]:
        """Get built-in palette library.
        
        Returns:
            Dictionary of built-in palettes
        """
        return {
            'rainbow': ColorPalette(
                name='Rainbow',
                colors=[(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0),
                       (0, 0, 255), (75, 0, 130), (148, 0, 211)],
                gradient_type='linear',
                metadata={'author': 'System', 'description': 'Classic rainbow gradient', 'tags': ['bright', 'colorful']}
            ),
            'fire': ColorPalette(
                name='Fire',
                colors=[(255, 0, 0), (255, 100, 0), (255, 200, 0), (255, 255, 0)],
                gradient_type='linear',
                metadata={'author': 'System', 'description': 'Fire gradient (red to yellow)', 'tags': ['warm', 'hot']}
            ),
            'ocean': ColorPalette(
                name='Ocean',
                colors=[(0, 50, 150), (0, 100, 200), (0, 150, 255), (0, 200, 255), (100, 220, 255)],
                gradient_type='smooth',
                metadata={'author': 'System', 'description': 'Ocean gradient (deep blue to cyan)', 'tags': ['cool', 'water']}
            ),
            'forest': ColorPalette(
                name='Forest',
                colors=[(0, 50, 0), (0, 100, 0), (34, 139, 34), (124, 252, 0), (144, 238, 144)],
                gradient_type='smooth',
                metadata={'author': 'System', 'description': 'Forest gradient (dark to light green)', 'tags': ['nature', 'green']}
            ),
            'sunset': ColorPalette(
                name='Sunset',
                colors=[(255, 94, 77), (255, 154, 0), (255, 206, 84), (255, 236, 153)],
                gradient_type='smooth',
                metadata={'author': 'System', 'description': 'Sunset gradient', 'tags': ['warm', 'orange']}
            ),
            'aurora': ColorPalette(
                name='Aurora',
                colors=[(0, 255, 127), (0, 255, 255), (0, 191, 255), (138, 43, 226)],
                gradient_type='smooth',
                metadata={'author': 'System', 'description': 'Aurora borealis gradient', 'tags': ['cool', 'magical']}
            ),
            'monochrome': ColorPalette(
                name='Monochrome',
                colors=[(0, 0, 0), (64, 64, 64), (128, 128, 128), (192, 192, 192), (255, 255, 255)],
                gradient_type='linear',
                metadata={'author': 'System', 'description': 'Grayscale gradient', 'tags': ['grayscale', 'minimal']}
            ),
            'neon': ColorPalette(
                name='Neon',
                colors=[(255, 0, 255), (0, 255, 255), (255, 255, 0), (0, 255, 0)],
                gradient_type='linear',
                metadata={'author': 'System', 'description': 'Neon colors gradient', 'tags': ['bright', 'electric']}
            ),
        }

