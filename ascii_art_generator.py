#!/usr/bin/env python3
"""
ASCII Art Generator - Main Entry Point
A comprehensive terminal-based ASCII art generator supporting multiple art types.
"""

import sys
import argparse
from generators.text_art import TextArtGenerator
from generators.image_art import ImageArtGenerator
from generators.pattern_art import PatternGenerator
from cli.interactive import InteractiveMode
from utils.config import Config


def main():
    """Main entry point for the ASCII art generator."""
    parser = argparse.ArgumentParser(
        description="Terminal-based ASCII Art Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -i                           # Interactive mode
  %(prog)s text "Hello World"           # Generate text art
  %(prog)s text "Hello" -f banner       # Use specific font
  %(prog)s image photo.jpg              # Convert image to ASCII
  %(prog)s pattern box -w 40 -h 10      # Generate box pattern
  %(prog)s pattern border -w 50         # Generate border
        """
    )
    
    parser.add_argument('-i', '--interactive', action='store_true',
                        help='Launch interactive mode')
    parser.add_argument('-o', '--output', type=str,
                        help='Output file path (default: print to stdout)')
    parser.add_argument('--color', action='store_true',
                        help='Enable color output (where supported)')
    
    subparsers = parser.add_subparsers(dest='command', help='Art generation commands')
    
    # Text art subcommand
    text_parser = subparsers.add_parser('text', help='Generate text-based ASCII art')
    text_parser.add_argument('text', type=str, help='Text to convert to ASCII art')
    text_parser.add_argument('-f', '--font', type=str, default='standard',
                             help='Font style (standard, banner, block, slant, etc.)')
    text_parser.add_argument('-w', '--width', type=int,
                             help='Maximum width of output')
    
    # Image art subcommand
    image_parser = subparsers.add_parser('image', help='Convert image to ASCII art')
    image_parser.add_argument('image_path', type=str, help='Path to image file')
    image_parser.add_argument('-w', '--width', type=int, default=80,
                              help='Width of ASCII art (default: 80)')
    image_parser.add_argument('-c', '--charset', type=str, default='standard',
                              choices=['standard', 'detailed', 'simple', 'blocks'],
                              help='Character set to use')
    
    # Pattern art subcommand
    pattern_parser = subparsers.add_parser('pattern', help='Generate patterns and borders')
    pattern_parser.add_argument('pattern_type', type=str,
                                choices=['box', 'border', 'line', 'diamond', 'wave'],
                                help='Type of pattern to generate')
    pattern_parser.add_argument('-w', '--width', type=int, default=60,
                                help='Width of pattern')
    pattern_parser.add_argument('--height', type=int, default=10,
                                help='Height of pattern')
    pattern_parser.add_argument('-s', '--style', type=str, default='single',
                                choices=['single', 'double', 'thick', 'ascii'],
                                help='Border style')
    
    args = parser.parse_args()
    
    # Initialize configuration
    config = Config(color_enabled=args.color)
    
    # Interactive mode
    if args.interactive or not args.command:
        interactive = InteractiveMode(config)
        interactive.run()
        return
    
    # Generate art based on command
    output = None
    
    if args.command == 'text':
        generator = TextArtGenerator(config)
        output = generator.generate(args.text, font=args.font, width=args.width)
    
    elif args.command == 'image':
        generator = ImageArtGenerator(config)
        output = generator.generate(args.image_path, width=args.width, charset=args.charset)
    
    elif args.command == 'pattern':
        generator = PatternGenerator(config)
        output = generator.generate(args.pattern_type, width=args.width,
                                   height=args.height, style=args.style)
    
    # Output result
    if output:
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(output)
            print(f"ASCII art saved to {args.output}")
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
        sys.exit(1)

