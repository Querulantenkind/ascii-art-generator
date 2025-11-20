#!/usr/bin/env python3
"""
ASCII Art Generator Pro - Enhanced Version
Extended features including animations, effects, advanced patterns, and exports.
"""

import sys
import argparse
from generators.text_art import TextArtGenerator
from generators.image_art import ImageArtGenerator
from generators.pattern_art import PatternGenerator
from generators.advanced_patterns import AdvancedPatternGenerator
from generators.animation import AnimationGenerator
from generators.text_effects import TextEffects
from generators.color_art import GradientGenerator, ColorImageConverter
from generators.composition import Compositor
from exporters.formats import HTMLExporter, SVGExporter, MarkdownExporter, ImageExporter
from utils.config import Config


def main():
    """Main entry point for ASCII Art Generator Pro."""
    parser = argparse.ArgumentParser(
        description="ASCII Art Generator Pro - Extended Features",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic text art with effects
  %(prog)s text "HELLO" --effect shadow
  %(prog)s text "3D TEXT" --effect 3d
  
  # Colored text art
  %(prog)s text "RAINBOW" --gradient rainbow
  
  # Advanced patterns
  %(prog)s pattern mandelbrot -w 80 -h 40
  %(prog)s pattern maze -w 51 -h 31
  %(prog)s pattern spiral --size 20
  
  # Animations
  %(prog)s animate wave -w 60 -h 15 --frames 30
  %(prog)s animate matrix -w 80 -h 20 --play
  
  # Export formats
  %(prog)s text "EXPORT" -o output.html --format html
  %(prog)s text "SVG" -o output.svg --format svg
  
  # Composition
  %(prog)s compose --horizontal "Art1" "Art2" -o combined.txt
        """
    )
    
    parser.add_argument('-o', '--output', type=str,
                        help='Output file path')
    parser.add_argument('--format', type=str, default='text',
                        choices=['text', 'html', 'svg', 'markdown', 'json', 'png'],
                        help='Output format')
    parser.add_argument('--color', action='store_true',
                        help='Enable color output')
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Text command with effects
    text_parser = subparsers.add_parser('text', help='Generate text art with effects')
    text_parser.add_argument('text', type=str, help='Text to convert')
    text_parser.add_argument('-f', '--font', type=str, default='standard',
                             help='Font style')
    text_parser.add_argument('--effect', type=str,
                             choices=['shadow', 'outline', '3d', 'glow', 'mirror', 'neon'],
                             help='Text effect to apply')
    text_parser.add_argument('--gradient', type=str,
                             choices=['rainbow', 'fire', 'ocean', 'forest'],
                             help='Color gradient to apply')
    
    # Pattern command (advanced)
    pattern_parser = subparsers.add_parser('pattern', help='Generate advanced patterns')
    pattern_parser.add_argument('pattern_type', type=str,
                                choices=['mandelbrot', 'julia', 'maze', 'spiral',
                                       'sierpinski', 'cellular', 'lissajous', 'tree'],
                                help='Pattern type')
    pattern_parser.add_argument('-w', '--width', type=int, default=80)
    pattern_parser.add_argument('--height', type=int, default=40)
    pattern_parser.add_argument('--size', type=int, help='Size parameter')
    pattern_parser.add_argument('--rule', type=int, default=30,
                               help='Rule number for cellular automaton')
    pattern_parser.add_argument('--tree-style', type=str, default='pine',
                               choices=['pine', 'oak', 'palm'],
                               help='Tree style')
    
    # Animation command
    anim_parser = subparsers.add_parser('animate', help='Generate animations')
    anim_parser.add_argument('anim_type', type=str,
                            choices=['wave', 'bounce', 'matrix', 'spinner',
                                   'progress', 'scroll', 'typewriter'],
                            help='Animation type')
    anim_parser.add_argument('-w', '--width', type=int, default=60)
    anim_parser.add_argument('--height', type=int, default=15)
    anim_parser.add_argument('--frames', type=int, default=30)
    anim_parser.add_argument('--play', action='store_true',
                            help='Play animation in terminal')
    anim_parser.add_argument('--loop', action='store_true',
                            help='Loop animation')
    anim_parser.add_argument('--text', type=str,
                            help='Text for scroll/typewriter animations')
    
    # Compose command
    compose_parser = subparsers.add_parser('compose', help='Compose multiple elements')
    compose_parser.add_argument('--horizontal', nargs='+',
                               help='Combine horizontally')
    compose_parser.add_argument('--vertical', nargs='+',
                               help='Combine vertically')
    compose_parser.add_argument('--grid', nargs='+',
                               help='Arrange in grid')
    compose_parser.add_argument('--cols', type=int, default=2,
                               help='Columns for grid layout')
    
    # Image command with color
    image_parser = subparsers.add_parser('image', help='Convert image with color')
    image_parser.add_argument('image_path', type=str)
    image_parser.add_argument('-w', '--width', type=int, default=80)
    image_parser.add_argument('--colored', action='store_true',
                             help='Generate colored ASCII art')
    
    args = parser.parse_args()
    
    config = Config(color_enabled=args.color)
    output = None
    
    # Handle commands
    if args.command == 'text':
        generator = TextArtGenerator(config)
        output = generator.generate(args.text, font=args.font)
        
        # Apply effects
        if args.effect:
            effects = TextEffects()
            if args.effect == 'shadow':
                output = effects.add_shadow(output)
            elif args.effect == 'outline':
                output = effects.add_outline(output)
            elif args.effect == '3d':
                output = effects.add_3d_effect(output)
            elif args.effect == 'glow':
                output = effects.add_glow(output)
            elif args.effect == 'mirror':
                output = effects.add_mirror(output)
            elif args.effect == 'neon':
                output = effects.add_neon(output)
        
        # Apply gradient
        if args.gradient:
            gradient_gen = GradientGenerator()
            output = gradient_gen.apply_gradient_to_text(output, args.gradient)
    
    elif args.command == 'pattern':
        adv_gen = AdvancedPatternGenerator()
        
        if args.pattern_type == 'mandelbrot':
            output = adv_gen.generate_mandelbrot(args.width, args.height)
        elif args.pattern_type == 'julia':
            output = adv_gen.generate_julia_set(args.width, args.height)
        elif args.pattern_type == 'maze':
            output = adv_gen.generate_maze(args.width, args.height)
        elif args.pattern_type == 'spiral':
            size = args.size or 20
            output = adv_gen.generate_spiral(size)
        elif args.pattern_type == 'sierpinski':
            order = args.size or 5
            output = adv_gen.generate_sierpinski_triangle(order)
        elif args.pattern_type == 'cellular':
            output = adv_gen.generate_cellular_automaton(args.width, args.height, args.rule)
        elif args.pattern_type == 'lissajous':
            output = adv_gen.generate_lissajous(args.width, args.height)
        elif args.pattern_type == 'tree':
            output = adv_gen.generate_tree(args.height, args.tree_style)
    
    elif args.command == 'animate':
        anim_gen = AnimationGenerator()
        animation = None
        
        if args.anim_type == 'wave':
            animation = anim_gen.wave_animation(args.width, args.height, args.frames)
        elif args.anim_type == 'bounce':
            animation = anim_gen.bouncing_ball(args.width, args.height, args.frames)
        elif args.anim_type == 'matrix':
            animation = anim_gen.matrix_rain(args.width, args.height, args.frames)
        elif args.anim_type == 'spinner':
            animation = anim_gen.spinning_loader(args.frames)
        elif args.anim_type == 'progress':
            animation = anim_gen.progress_bar(args.width, args.frames)
        elif args.anim_type == 'scroll':
            text = args.text or "ASCII Art Generator Pro"
            animation = anim_gen.text_scroll(text, args.width)
        elif args.anim_type == 'typewriter':
            text = args.text or "Hello World!"
            animation = anim_gen.typewriter_effect(text)
        
        if animation:
            if args.play:
                animation.play(loop=args.loop)
                return
            elif args.output:
                # Export frames
                animation.export_frames(args.output, prefix='frame')
                print(f"Animation frames exported to {args.output}/")
                return
            else:
                # Show first frame
                output = animation.frames[0].content if animation.frames else ""
    
    elif args.command == 'compose':
        compositor = Compositor()
        
        if args.horizontal:
            # Generate text art for each element
            gen = TextArtGenerator(config)
            arts = [gen.generate(text) for text in args.horizontal]
            output = compositor.horizontal_concat(*arts)
        
        elif args.vertical:
            gen = TextArtGenerator(config)
            arts = [gen.generate(text) for text in args.vertical]
            output = compositor.vertical_concat(*arts)
        
        elif args.grid:
            gen = TextArtGenerator(config)
            arts = [gen.generate(text) for text in args.grid]
            output = compositor.grid_layout(arts, args.cols)
    
    elif args.command == 'image':
        if args.colored:
            converter = ColorImageConverter()
            output = converter.convert_to_colored_ascii(args.image_path, args.width)
        else:
            generator = ImageArtGenerator(config)
            output = generator.generate(args.image_path, width=args.width)
    
    # Handle output
    if output:
        if args.output:
            # Export based on format
            if args.format == 'html':
                exporter = HTMLExporter()
                content = exporter.export(output, title='ASCII Art')
                with open(args.output, 'w', encoding='utf-8') as f:
                    f.write(content)
            
            elif args.format == 'svg':
                exporter = SVGExporter()
                content = exporter.export(output, title='ASCII Art')
                with open(args.output, 'w', encoding='utf-8') as f:
                    f.write(content)
            
            elif args.format == 'markdown':
                exporter = MarkdownExporter()
                content = exporter.export(output, title='ASCII Art')
                with open(args.output, 'w', encoding='utf-8') as f:
                    f.write(content)
            
            elif args.format == 'png':
                exporter = ImageExporter()
                exporter.export_to_png(output, args.output)
            
            else:  # text
                with open(args.output, 'w', encoding='utf-8') as f:
                    f.write(output)
            
            print(f"Output saved to {args.output}")
        else:
            print(output)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting...")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

