"""Command-line interface for ASCII art generator."""

import argparse
import sys

from .text_generator import TextASCIIGenerator
from .image_generator import ImageASCIIGenerator


def create_text_parser(subparsers):
    """Create parser for text-to-ASCII command."""
    parser = subparsers.add_parser('text', help='Generate ASCII art from text')
    parser.add_argument('input', help='Text to convert to ASCII art')
    parser.add_argument('-f', '--font', default='standard',
                       help='Font style to use (default: standard)')
    parser.add_argument('-w', '--width', type=int, default=None,
                       help='Maximum width for output (default: auto)')
    parser.add_argument('-l', '--list-fonts', action='store_true',
                       help='List all available fonts')
    return parser


def create_image_parser(subparsers):
    """Create parser for image-to-ASCII command."""
    parser = subparsers.add_parser('image', help='Convert image to ASCII art')
    parser.add_argument('input', help='Path to image file')
    parser.add_argument('-w', '--width', type=int, default=80,
                       help='Output width in characters (default: 80)')
    parser.add_argument('--height', type=int, default=None,
                       help='Output height in characters (default: auto)')
    parser.add_argument('-c', '--charset', default='medium',
                       choices=['dense', 'medium', 'sparse', 'blocks', 'simple', 'detailed'],
                       help='Character set to use (default: medium)')
    parser.add_argument('-i', '--invert', action='store_true',
                       help='Invert brightness')
    parser.add_argument('-l', '--list-charsets', action='store_true',
                       help='List all available character sets')
    return parser


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='ASCII Art Generator - Create beautiful ASCII art from text or images',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s text "Hello World" -f big
  %(prog)s text "Python" -f slant -w 60
  %(prog)s image photo.jpg -w 100 -c dense
  %(prog)s image photo.png -w 80 -c blocks --invert
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Create subcommands
    create_text_parser(subparsers)
    create_image_parser(subparsers)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    try:
        if args.command == 'text':
            generator = TextASCIIGenerator(font=args.font)
            
            if args.list_fonts:
                print("Available fonts:")
                fonts = generator.list_fonts()
                for i, font in enumerate(fonts, 1):
                    print(f"  {font}", end='  ')
                    if i % 5 == 0:
                        print()
                print()
                return
            
            result = generator.generate(args.input, width=args.width)
            print(result)
        
        elif args.command == 'image':
            generator = ImageASCIIGenerator(
                char_set=args.charset,
                width=args.width,
                height=args.height,
                invert=args.invert
            )
            
            if args.list_charsets:
                print("Available character sets:")
                for charset in generator.list_char_sets():
                    print(f"  {charset}: {generator.CHAR_SETS[charset]}")
                return
            
            result = generator.generate(args.input)
            print(result)
    
    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()

