#!/usr/bin/env python3
"""
ASCII Art Editor - Interactive TUI Editor
Launch the real-time interactive editor with live preview.
"""

import sys
import argparse


def main():
    """Main entry point for the editor."""
    parser = argparse.ArgumentParser(
        description="ASCII Art Interactive Editor",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Interactive TUI Editor Features:
  • Live preview with multiple layers
  • Mouse and keyboard support
  • Undo/Redo functionality
  • Preset styles and effects
  • Save/Load projects
  • Export to multiple formats
  • Clipboard integration

Keyboard Shortcuts:
  H / F1      - Help
  N           - New layer
  T           - Add text layer
  F           - Change font
  E           - Apply effect
  P           - Apply preset
  S           - Save project
  O           - Open project
  C           - Copy to clipboard
  X           - Export menu
  L           - Toggle layers
  Ctrl+Z      - Undo
  Ctrl+Y      - Redo
  Arrow Keys  - Move layer
  Q           - Quit

Examples:
  %(prog)s                    # Launch editor
  %(prog)s --load project.aap # Open existing project
        """
    )
    
    parser.add_argument('--load', type=str, metavar='FILE',
                       help='Load project file on startup')
    parser.add_argument('--width', type=int, default=80,
                       help='Canvas width (default: 80)')
    parser.add_argument('--height', type=int, default=30,
                       help='Canvas height (default: 30)')
    parser.add_argument('--demo', action='store_true',
                       help='Launch with demo content')
    
    args = parser.parse_args()
    
    try:
        from editors.tui_editor import InteractiveTUIEditor
        
        # Create editor
        editor = InteractiveTUIEditor()
        editor.canvas_width = args.width
        editor.canvas_height = args.height
        
        # Load project if specified
        if args.load:
            try:
                import json
                with open(args.load, 'r') as f:
                    project_data = json.load(f)
                
                # Load layers
                from editors.tui_editor import Layer
                editor.layers = []
                for layer_data in project_data['layers']:
                    layer = Layer(**layer_data)
                    editor.layers.append(layer)
                
                if editor.layers:
                    editor.current_layer_id = editor.layers[0].id
                    editor.next_layer_id = max(l.id for l in editor.layers) + 1
                
                print(f"Loaded project: {args.load}")
            
            except Exception as e:
                print(f"Error loading project: {e}")
                sys.exit(1)
        
        # Add demo content if requested
        if args.demo:
            from generators.text_art import TextArtGenerator
            from utils.config import Config
            
            config = Config()
            gen = TextArtGenerator(config)
            
            # Create demo layers
            demo_text = gen.generate("DEMO", font='banner')
            demo_layer = Layer(
                id=editor.next_layer_id,
                name="Demo Layer",
                content=demo_text,
                x=10,
                y=5,
                z_index=0
            )
            editor.layers.append(demo_layer)
            editor.current_layer_id = demo_layer.id
            editor.next_layer_id += 1
        
        # Launch editor
        print("\nLaunching ASCII Art Editor...")
        print("Press H for help, Q to quit\n")
        
        editor.run()
        
        print("\nEditor closed. Thank you for using ASCII Art Editor!")
    
    except ImportError as e:
        print(f"Error: Missing dependency - {e}")
        print("\nThe TUI editor requires curses (built-in on Linux/Mac)")
        print("On Windows, install: pip install windows-curses")
        sys.exit(1)
    
    except KeyboardInterrupt:
        print("\n\nEditor interrupted.")
        sys.exit(0)
    
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

