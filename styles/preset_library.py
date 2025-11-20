"""Preset style library for quick professional results."""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
import json


@dataclass
class StylePreset:
    """Represents a complete style preset."""
    
    name: str
    category: str
    description: str
    font: str
    effect: Optional[str] = None
    gradient: Optional[str] = None
    border_style: Optional[str] = None
    border_enabled: bool = False
    tags: List[str] = None
    use_cases: List[str] = None
    
    def __post_init__(self):
        """Initialize default values."""
        if self.tags is None:
            self.tags = []
        if self.use_cases is None:
            self.use_cases = []


class PresetStyleLibrary:
    """Curated collection of professional style presets."""
    
    def __init__(self):
        """Initialize preset library."""
        self.presets: Dict[str, StylePreset] = {}
        self._load_builtin_presets()
    
    def _load_builtin_presets(self):
        """Load built-in style presets."""
        
        # Tech & Startup Styles
        self.presets['tech_modern'] = StylePreset(
            name='tech_modern',
            category='tech',
            description='Modern, clean tech aesthetic with 3D depth',
            font='banner',
            effect='3d',
            gradient='ocean',
            border_style='double',
            border_enabled=True,
            tags=['tech', 'modern', 'professional', 'startup'],
            use_cases=['startup logos', 'tech banners', 'app headers']
        )
        
        self.presets['tech_minimal'] = StylePreset(
            name='tech_minimal',
            category='tech',
            description='Minimalist tech style, clean and simple',
            font='standard',
            effect=None,
            gradient=None,
            border_style='single',
            border_enabled=True,
            tags=['tech', 'minimal', 'clean', 'simple'],
            use_cases=['documentation', 'cli tools', 'headers']
        )
        
        self.presets['tech_bold'] = StylePreset(
            name='tech_bold',
            category='tech',
            description='Bold, impactful tech style',
            font='block',
            effect='shadow',
            gradient='fire',
            border_style='thick',
            border_enabled=True,
            tags=['tech', 'bold', 'impact', 'strong'],
            use_cases=['announcements', 'alerts', 'warnings']
        )
        
        # Retro & Gaming Styles
        self.presets['retro_arcade'] = StylePreset(
            name='retro_arcade',
            category='retro',
            description='80s arcade game aesthetic with neon colors',
            font='block',
            effect='neon',
            gradient='rainbow',
            border_style='thick',
            border_enabled=True,
            tags=['retro', 'gaming', '80s', 'neon', 'arcade'],
            use_cases=['game titles', 'retro projects', 'fun headers']
        )
        
        self.presets['retro_terminal'] = StylePreset(
            name='retro_terminal',
            category='retro',
            description='Classic terminal green-on-black style',
            font='standard',
            effect='glow',
            gradient='forest',
            border_style='ascii',
            border_enabled=True,
            tags=['retro', 'terminal', 'classic', 'hacker'],
            use_cases=['terminal apps', 'cli tools', 'hacker aesthetic']
        )
        
        self.presets['pixel_art'] = StylePreset(
            name='pixel_art',
            category='retro',
            description='Pixel art style with blocky characters',
            font='block',
            effect=None,
            gradient=None,
            border_style='ascii',
            border_enabled=False,
            tags=['pixel', 'retro', 'gaming', 'blocky'],
            use_cases=['game graphics', 'retro logos', 'pixel art']
        )
        
        # Corporate & Professional Styles
        self.presets['corporate_clean'] = StylePreset(
            name='corporate_clean',
            category='corporate',
            description='Professional corporate style, clean and readable',
            font='standard',
            effect='outline',
            gradient=None,
            border_style='double',
            border_enabled=True,
            tags=['corporate', 'professional', 'business', 'formal'],
            use_cases=['business reports', 'presentations', 'official docs']
        )
        
        self.presets['corporate_elegant'] = StylePreset(
            name='corporate_elegant',
            category='corporate',
            description='Elegant professional style with subtle effects',
            font='slant',
            effect='shadow',
            gradient=None,
            border_style='double',
            border_enabled=True,
            tags=['corporate', 'elegant', 'refined', 'sophisticated'],
            use_cases=['executive presentations', 'annual reports', 'formal communications']
        )
        
        # Creative & Artistic Styles
        self.presets['creative_playful'] = StylePreset(
            name='creative_playful',
            category='creative',
            description='Fun, playful style with bubbles and colors',
            font='bubble',
            effect='glow',
            gradient='rainbow',
            border_style='ascii',
            border_enabled=True,
            tags=['creative', 'playful', 'fun', 'colorful'],
            use_cases=['party invites', 'fun projects', 'casual content']
        )
        
        self.presets['creative_artistic'] = StylePreset(
            name='creative_artistic',
            category='creative',
            description='Artistic style with unique effects',
            font='slant',
            effect='mirror',
            gradient='fire',
            border_style='single',
            border_enabled=True,
            tags=['creative', 'artistic', 'unique', 'expressive'],
            use_cases=['art projects', 'creative content', 'exhibitions']
        )
        
        self.presets['creative_psychedelic'] = StylePreset(
            name='creative_psychedelic',
            category='creative',
            description='Psychedelic style with intense colors and effects',
            font='banner',
            effect='double_vision',
            gradient='rainbow',
            border_style='thick',
            border_enabled=True,
            tags=['creative', 'psychedelic', 'intense', 'vibrant'],
            use_cases=['music posters', 'festival content', 'artistic projects']
        )
        
        # Minimalist Styles
        self.presets['minimal_clean'] = StylePreset(
            name='minimal_clean',
            category='minimalist',
            description='Ultra-minimal, clean and simple',
            font='small',
            effect=None,
            gradient=None,
            border_style='single',
            border_enabled=False,
            tags=['minimal', 'clean', 'simple', 'elegant'],
            use_cases=['subtle headers', 'clean docs', 'minimalist design']
        )
        
        self.presets['minimal_modern'] = StylePreset(
            name='minimal_modern',
            category='minimalist',
            description='Modern minimalist with subtle depth',
            font='standard',
            effect='shadow',
            gradient=None,
            border_style='single',
            border_enabled=True,
            tags=['minimal', 'modern', 'subtle', 'refined'],
            use_cases=['modern docs', 'clean interfaces', 'professional headers']
        )
        
        # Bold & Impact Styles
        self.presets['bold_impact'] = StylePreset(
            name='bold_impact',
            category='bold',
            description='Maximum impact with bold styling',
            font='banner',
            effect='3d',
            gradient='fire',
            border_style='thick',
            border_enabled=True,
            tags=['bold', 'impact', 'strong', 'attention'],
            use_cases=['announcements', 'alerts', 'important messages']
        )
        
        self.presets['bold_dramatic'] = StylePreset(
            name='bold_dramatic',
            category='bold',
            description='Dramatic style with strong effects',
            font='block',
            effect='outline',
            gradient='rainbow',
            border_style='double',
            border_enabled=True,
            tags=['bold', 'dramatic', 'striking', 'powerful'],
            use_cases=['event posters', 'dramatic announcements', 'impact headers']
        )
        
        # Elegant & Sophisticated Styles
        self.presets['elegant_classic'] = StylePreset(
            name='elegant_classic',
            category='elegant',
            description='Classic elegant style, timeless and refined',
            font='standard',
            effect='outline',
            gradient=None,
            border_style='double',
            border_enabled=True,
            tags=['elegant', 'classic', 'timeless', 'refined'],
            use_cases=['formal invitations', 'certificates', 'elegant headers']
        )
        
        self.presets['elegant_luxury'] = StylePreset(
            name='elegant_luxury',
            category='elegant',
            description='Luxurious style with premium feel',
            font='banner',
            effect='glow',
            gradient='ocean',
            border_style='double',
            border_enabled=True,
            tags=['elegant', 'luxury', 'premium', 'sophisticated'],
            use_cases=['premium products', 'luxury brands', 'high-end content']
        )
        
        # Status & Alert Styles
        self.presets['status_success'] = StylePreset(
            name='status_success',
            category='status',
            description='Success status with green theme',
            font='standard',
            effect='glow',
            gradient='forest',
            border_style='double',
            border_enabled=True,
            tags=['status', 'success', 'positive', 'green'],
            use_cases=['success messages', 'completion notices', 'positive alerts']
        )
        
        self.presets['status_error'] = StylePreset(
            name='status_error',
            category='status',
            description='Error status with red theme',
            font='banner',
            effect='shadow',
            gradient='fire',
            border_style='thick',
            border_enabled=True,
            tags=['status', 'error', 'alert', 'red'],
            use_cases=['error messages', 'warnings', 'critical alerts']
        )
        
        self.presets['status_info'] = StylePreset(
            name='status_info',
            category='status',
            description='Information status with blue theme',
            font='standard',
            effect=None,
            gradient='ocean',
            border_style='single',
            border_enabled=True,
            tags=['status', 'info', 'neutral', 'blue'],
            use_cases=['info messages', 'notifications', 'updates']
        )
    
    def get_preset(self, name: str) -> Optional[StylePreset]:
        """Get preset by name.
        
        Args:
            name: Preset name
            
        Returns:
            StylePreset or None
        """
        return self.presets.get(name)
    
    def list_presets(self, category: str = None) -> List[StylePreset]:
        """List available presets.
        
        Args:
            category: Filter by category (optional)
            
        Returns:
            List of presets
        """
        presets = list(self.presets.values())
        
        if category:
            presets = [p for p in presets if p.category == category]
        
        return presets
    
    def list_categories(self) -> List[str]:
        """Get list of preset categories.
        
        Returns:
            List of category names
        """
        categories = set(p.category for p in self.presets.values())
        return sorted(categories)
    
    def search_presets(self, query: str) -> List[StylePreset]:
        """Search presets by name, description, or tags.
        
        Args:
            query: Search query
            
        Returns:
            List of matching presets
        """
        query = query.lower()
        results = []
        
        for preset in self.presets.values():
            if (query in preset.name.lower() or
                query in preset.description.lower() or
                any(query in tag.lower() for tag in preset.tags) or
                any(query in use_case.lower() for use_case in preset.use_cases)):
                results.append(preset)
        
        return results
    
    def apply_preset(self, text: str, preset_name: str,
                    apply_colors: bool = True) -> str:
        """Apply preset style to text.
        
        Args:
            text: Text to style
            preset_name: Name of preset to apply
            apply_colors: Whether to apply color gradients
            
        Returns:
            Styled ASCII art
        """
        preset = self.get_preset(preset_name)
        
        if not preset:
            raise ValueError(f"Preset not found: {preset_name}")
        
        from generators.text_art import TextArtGenerator
        from generators.text_effects import TextEffects
        from generators.color_art import GradientGenerator
        from generators.composition import Compositor
        from utils.config import Config
        
        # Generate base art
        config = Config(color_enabled=apply_colors)
        gen = TextArtGenerator(config)
        art = gen.generate(text, font=preset.font)
        
        # Apply effect
        if preset.effect:
            effects = TextEffects()
            
            if preset.effect == '3d':
                art = effects.add_3d_effect(art, depth=3)
            elif preset.effect == 'shadow':
                art = effects.add_shadow(art)
            elif preset.effect == 'outline':
                art = effects.add_outline(art)
            elif preset.effect == 'glow':
                art = effects.add_glow(art, intensity=2)
            elif preset.effect == 'neon':
                art = effects.add_neon(art)
            elif preset.effect == 'mirror':
                art = effects.add_mirror(art)
            elif preset.effect == 'double_vision':
                art = effects.add_double_vision(art)
        
        # Apply gradient
        if preset.gradient and apply_colors:
            gradient_gen = GradientGenerator()
            art = gradient_gen.apply_gradient_to_text(art, preset.gradient)
        
        # Apply border
        if preset.border_enabled and preset.border_style:
            compositor = Compositor()
            art = compositor.frame(art, style=preset.border_style, padding=1)
        
        return art
    
    def preview_preset(self, preset_name: str, sample_text: str = "SAMPLE") -> str:
        """Generate preview of preset.
        
        Args:
            preset_name: Preset name
            sample_text: Text to use for preview
            
        Returns:
            Preview ASCII art
        """
        return self.apply_preset(sample_text, preset_name, apply_colors=False)
    
    def preview_all_presets(self, sample_text: str = "DEMO") -> str:
        """Generate previews of all presets.
        
        Args:
            sample_text: Text to use for previews
            
        Returns:
            Combined preview of all presets
        """
        result = []
        result.append("=" * 80)
        result.append("PRESET STYLE LIBRARY - PREVIEW".center(80))
        result.append("=" * 80)
        result.append("")
        
        for category in self.list_categories():
            result.append(f"\n{'='*80}")
            result.append(f"{category.upper()} STYLES".center(80))
            result.append(f"{'='*80}\n")
            
            presets = self.list_presets(category=category)
            
            for preset in presets:
                result.append(f"┌─ {preset.name} ─ {preset.description}")
                result.append(f"│  Tags: {', '.join(preset.tags)}")
                result.append("└" + "─" * 78)
                
                try:
                    preview = self.preview_preset(preset.name, sample_text)
                    result.append(preview)
                except Exception as e:
                    result.append(f"Error generating preview: {e}")
                
                result.append("")
        
        return '\n'.join(result)
    
    def get_recommendations(self, context: str, mood: str = None) -> List[StylePreset]:
        """Get preset recommendations based on context and mood.
        
        Args:
            context: Usage context ('logo', 'header', 'banner', 'alert', 'title')
            mood: Optional mood ('professional', 'fun', 'serious', 'creative')
            
        Returns:
            List of recommended presets
        """
        recommendations = []
        
        # Context-based filtering
        if context == 'logo':
            candidates = [p for p in self.presets.values() 
                         if 'logo' in ' '.join(p.use_cases).lower()]
        elif context == 'header':
            candidates = [p for p in self.presets.values() 
                         if 'header' in ' '.join(p.use_cases).lower()]
        elif context == 'banner':
            candidates = [p for p in self.presets.values() 
                         if 'banner' in ' '.join(p.use_cases).lower()]
        elif context == 'alert':
            candidates = [p for p in self.presets.values() 
                         if p.category == 'status']
        else:
            candidates = list(self.presets.values())
        
        # Mood-based filtering
        if mood:
            candidates = [p for p in candidates 
                         if mood.lower() in ' '.join(p.tags).lower()]
        
        return candidates[:5]  # Top 5 recommendations
    
    def save_custom_preset(self, preset: StylePreset, filepath: str = None):
        """Save custom preset to file.
        
        Args:
            preset: Preset to save
            filepath: Output file path
        """
        if filepath is None:
            filepath = f"custom_presets/{preset.name}.json"
        
        import os
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(asdict(preset), f, indent=2)
    
    def load_custom_preset(self, filepath: str):
        """Load custom preset from file.
        
        Args:
            filepath: Preset file path
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            preset = StylePreset(**data)
            self.presets[preset.name] = preset
    
    def create_custom_preset(self, name: str, category: str,
                            description: str, **kwargs) -> StylePreset:
        """Create custom preset.
        
        Args:
            name: Preset name
            category: Category
            description: Description
            **kwargs: Style parameters
            
        Returns:
            Created preset
        """
        preset = StylePreset(
            name=name,
            category=category,
            description=description,
            **kwargs
        )
        
        self.presets[name] = preset
        return preset

