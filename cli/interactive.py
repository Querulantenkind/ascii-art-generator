"""Interactive CLI mode for ASCII art generator."""

import sys
from generators.text_art import TextArtGenerator
from generators.image_art import ImageArtGenerator
from generators.pattern_art import PatternGenerator


class InteractiveMode:
    """Interactive command-line interface for ASCII art generation."""
    
    def __init__(self, config):
        """Initialize interactive mode.
        
        Args:
            config: Configuration object
        """
        self.config = config
        self.text_gen = TextArtGenerator(config)
        self.image_gen = ImageArtGenerator(config)
        self.pattern_gen = PatternGenerator(config)
        self.running = True
    
    def run(self):
        """Run the interactive mode."""
        self.print_welcome()
        
        while self.running:
            try:
                self.show_main_menu()
                choice = input("\nEnter your choice: ").strip()
                self.handle_choice(choice)
            except KeyboardInterrupt:
                print("\n\nExiting...")
                break
            except EOFError:
                break
    
    def print_welcome(self):
        """Print welcome banner."""
        banner = """
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║           ASCII ART GENERATOR - Interactive Mode              ║
║                                                               ║
║              Create amazing ASCII art in your terminal!       ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
"""
        print(banner)
    
    def show_main_menu(self):
        """Display main menu."""
        menu = """
┌───────────────────────────────────────────────────────────────┐
│                         MAIN MENU                             │
├───────────────────────────────────────────────────────────────┤
│  1. Text to ASCII Art                                         │
│  2. Image to ASCII Art                                        │
│  3. Generate Patterns                                         │
│  4. Generate Borders & Boxes                                  │
│  5. Examples & Gallery                                        │
│  6. Settings                                                  │
│  7. Help                                                      │
│  0. Exit                                                      │
└───────────────────────────────────────────────────────────────┘
"""
        print(menu)
    
    def handle_choice(self, choice: str):
        """Handle user menu choice.
        
        Args:
            choice: User's menu selection
        """
        if choice == '1':
            self.text_art_menu()
        elif choice == '2':
            self.image_art_menu()
        elif choice == '3':
            self.pattern_menu()
        elif choice == '4':
            self.border_menu()
        elif choice == '5':
            self.show_examples()
        elif choice == '6':
            self.settings_menu()
        elif choice == '7':
            self.show_help()
        elif choice == '0':
            self.running = False
            print("\nThank you for using ASCII Art Generator!")
        else:
            print("\n❌ Invalid choice. Please try again.")
    
    def text_art_menu(self):
        """Handle text art generation."""
        print("\n" + "=" * 60)
        print("TEXT TO ASCII ART")
        print("=" * 60)
        
        text = input("\nEnter text to convert: ").strip()
        if not text:
            print("❌ No text entered.")
            return
        
        # Show available fonts
        print("\nAvailable fonts:")
        fonts = self.text_gen.list_fonts()
        for i, font in enumerate(fonts, 1):
            print(f"  {i}. {font}")
        
        font_choice = input(f"\nSelect font (1-{len(fonts)}) or press Enter for 'standard': ").strip()
        
        if font_choice.isdigit() and 1 <= int(font_choice) <= len(fonts):
            font = fonts[int(font_choice) - 1]
        else:
            font = 'standard'
        
        print(f"\nGenerating ASCII art with '{font}' font...\n")
        print("-" * 60)
        
        result = self.text_gen.generate(text, font=font)
        print(result)
        
        print("-" * 60)
        
        self.offer_save(result)
    
    def image_art_menu(self):
        """Handle image to ASCII art conversion."""
        print("\n" + "=" * 60)
        print("IMAGE TO ASCII ART")
        print("=" * 60)
        
        image_path = input("\nEnter image file path: ").strip()
        if not image_path:
            print("❌ No path entered.")
            return
        
        width = input("Enter width (default 80): ").strip()
        width = int(width) if width.isdigit() else 80
        
        print("\nCharacter sets:")
        print("  1. standard (default)")
        print("  2. detailed")
        print("  3. simple")
        print("  4. blocks")
        
        charset_choice = input("\nSelect character set (1-4) or press Enter for 'standard': ").strip()
        charset_map = {'1': 'standard', '2': 'detailed', '3': 'simple', '4': 'blocks'}
        charset = charset_map.get(charset_choice, 'standard')
        
        print(f"\nConverting image to ASCII art...\n")
        print("-" * 60)
        
        result = self.image_gen.generate(image_path, width=width, charset=charset)
        print(result)
        
        print("-" * 60)
        
        self.offer_save(result)
    
    def pattern_menu(self):
        """Handle pattern generation."""
        print("\n" + "=" * 60)
        print("PATTERN GENERATOR")
        print("=" * 60)
        
        print("\nAvailable patterns:")
        print("  1. Diamond")
        print("  2. Wave")
        print("  3. Grid")
        
        choice = input("\nSelect pattern (1-3): ").strip()
        
        width = input("Enter width (default 60): ").strip()
        width = int(width) if width.isdigit() else 60
        
        height = input("Enter height (default 10): ").strip()
        height = int(height) if height.isdigit() else 10
        
        print("\n" + "-" * 60)
        
        if choice == '1':
            result = self.pattern_gen.generate_diamond(width, height)
        elif choice == '2':
            result = self.pattern_gen.generate_wave(width, height)
        elif choice == '3':
            cols = input("Number of columns (default 5): ").strip()
            cols = int(cols) if cols.isdigit() else 5
            rows = input("Number of rows (default 3): ").strip()
            rows = int(rows) if rows.isdigit() else 3
            result = self.pattern_gen.generate_grid(cols, rows)
        else:
            print("❌ Invalid choice.")
            return
        
        print(result)
        print("-" * 60)
        
        self.offer_save(result)
    
    def border_menu(self):
        """Handle border and box generation."""
        print("\n" + "=" * 60)
        print("BORDERS & BOXES")
        print("=" * 60)
        
        print("\nOptions:")
        print("  1. Simple Box")
        print("  2. Border Frame")
        print("  3. Banner with Text")
        
        choice = input("\nSelect option (1-3): ").strip()
        
        width = input("Enter width (default 60): ").strip()
        width = int(width) if width.isdigit() else 60
        
        print("\nBorder styles:")
        print("  1. single")
        print("  2. double")
        print("  3. thick")
        print("  4. ascii")
        
        style_choice = input("\nSelect style (1-4) or press Enter for 'single': ").strip()
        style_map = {'1': 'single', '2': 'double', '3': 'thick', '4': 'ascii'}
        style = style_map.get(style_choice, 'single')
        
        print("\n" + "-" * 60)
        
        if choice == '1':
            height = input("Enter height (default 10): ").strip()
            height = int(height) if height.isdigit() else 10
            result = self.pattern_gen.generate_box(width, height, style)
        elif choice == '2':
            result = self.pattern_gen.generate_border(width, style)
        elif choice == '3':
            text = input("Enter banner text: ").strip()
            result = self.pattern_gen.generate_banner(text, width, style)
        else:
            print("❌ Invalid choice.")
            return
        
        print(result)
        print("-" * 60)
        
        self.offer_save(result)
    
    def show_examples(self):
        """Show example ASCII art."""
        print("\n" + "=" * 60)
        print("EXAMPLES GALLERY")
        print("=" * 60)
        
        examples = [
            ("Text Art - Standard Font", self.text_gen.generate("HELLO", font='standard')),
            ("Text Art - Banner Font", self.text_gen.generate("ASCII", font='banner')),
            ("Pattern - Diamond", self.pattern_gen.generate_diamond(30, 10)),
            ("Border - Double Style", self.pattern_gen.generate_border(50, style='double')),
        ]
        
        for title, art in examples:
            print(f"\n{title}:")
            print("-" * 60)
            print(art)
            print("-" * 60)
            
            cont = input("\nPress Enter to see next example (or 'q' to return to menu): ").strip()
            if cont.lower() == 'q':
                break
    
    def settings_menu(self):
        """Handle settings."""
        print("\n" + "=" * 60)
        print("SETTINGS")
        print("=" * 60)
        
        print(f"\nCurrent settings:")
        print(f"  Color output: {'Enabled' if self.config.color_enabled else 'Disabled'}")
        print(f"  Default width: {self.config.default_width}")
        print(f"  Default height: {self.config.default_height}")
        
        print("\nOptions:")
        print("  1. Toggle color output")
        print("  2. Set default width")
        print("  3. Set default height")
        print("  0. Back to main menu")
        
        choice = input("\nEnter your choice: ").strip()
        
        if choice == '1':
            self.config.color_enabled = not self.config.color_enabled
            print(f"✓ Color output {'enabled' if self.config.color_enabled else 'disabled'}")
        elif choice == '2':
            width = input("Enter default width: ").strip()
            if width.isdigit():
                self.config.default_width = int(width)
                print(f"✓ Default width set to {self.config.default_width}")
        elif choice == '3':
            height = input("Enter default height: ").strip()
            if height.isdigit():
                self.config.default_height = int(height)
                print(f"✓ Default height set to {self.config.default_height}")
    
    def show_help(self):
        """Display help information."""
        help_text = """
╔═══════════════════════════════════════════════════════════════╗
║                            HELP                               ║
╚═══════════════════════════════════════════════════════════════╝

ASCII ART GENERATOR FEATURES:

1. TEXT TO ASCII ART
   Convert any text into stylized ASCII art using various fonts.
   Available fonts: standard, banner, block, slant, small, bubble

2. IMAGE TO ASCII ART
   Convert images (JPG, PNG, etc.) into ASCII art.
   Requires: Pillow library (install with: pip install Pillow)
   
   Character sets:
   - standard: Basic characters for general use
   - detailed: Many characters for high detail
   - simple: Few characters for simple output
   - blocks: Unicode block characters

3. PATTERNS
   Generate geometric patterns like diamonds, waves, and grids.

4. BORDERS & BOXES
   Create decorative borders, boxes, and banners.
   
   Styles: single, double, thick, ascii

COMMAND-LINE USAGE:
  python ascii_art_generator.py text "Hello World"
  python ascii_art_generator.py image photo.jpg -w 100
  python ascii_art_generator.py pattern diamond -w 40 -h 15

For more information, visit the README.md file.
"""
        print(help_text)
        input("\nPress Enter to continue...")
    
    def offer_save(self, content: str):
        """Offer to save generated art to file.
        
        Args:
            content: ASCII art content to save
        """
        save = input("\nSave to file? (y/n): ").strip().lower()
        if save == 'y':
            filename = input("Enter filename: ").strip()
            if filename:
                try:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"✓ Saved to {filename}")
                except Exception as e:
                    print(f"❌ Error saving file: {e}")

