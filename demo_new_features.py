#!/usr/bin/env python3
"""
Demo script showcasing the new features:
1. Preset Style Library
2. ASCII Emoji Collection
3. Quick Templates
4. Clipboard Integration
"""

from styles.preset_library import PresetStyleLibrary
from assets.emoji_library import EmojiLibrary
from templates.quick_templates import QuickTemplates
from utils.clipboard import ClipboardManager, ClipboardHelper


def demo_preset_library():
    """Demonstrate preset style library."""
    print("\n" + "=" * 80)
    print("FEATURE 1: PRESET STYLE LIBRARY".center(80))
    print("=" * 80)
    
    library = PresetStyleLibrary()
    
    print(f"\n✓ Loaded {len(library.presets)} professional style presets")
    print(f"✓ Categories: {', '.join(library.list_categories())}")
    
    # Show presets by category
    print("\n📚 Available Presets by Category:\n")
    
    for category in library.list_categories():
        presets = library.list_presets(category)
        print(f"  {category.upper()}:")
        for preset in presets:
            print(f"    • {preset.name}: {preset.description}")
    
    # Apply a preset
    print("\n🎨 Applying 'tech_modern' preset to 'DEMO':\n")
    art = library.apply_preset('DEMO', 'tech_modern', apply_colors=False)
    print(art)
    
    # Show recommendations
    print("\n💡 Recommendations for 'logo' context:")
    recommendations = library.get_recommendations('logo')
    for preset in recommendations[:3]:
        print(f"  • {preset.name}: {preset.description}")
    
    input("\n[Press Enter to continue...]")


def demo_emoji_library():
    """Demonstrate ASCII emoji collection."""
    print("\n" + "=" * 80)
    print("FEATURE 2: ASCII EMOJI COLLECTION".center(80))
    print("=" * 80)
    
    library = EmojiLibrary()
    
    print(f"\n✓ Loaded {len(library.emojis)} emojis")
    print(f"✓ Loaded {len(library.icons)} icons")
    print(f"✓ Loaded {len(library.symbols)} symbols")
    print(f"✓ Loaded {len(library.decorations)} decorations")
    
    # Show emoji categories
    print("\n😊 Sample Emojis:")
    emoji_samples = ['smile', 'heart', 'thumbs_up', 'rocket', 'fire', 'party', 'star']
    for name in emoji_samples:
        emoji = library.get(name)
        print(f"  {name.ljust(15)}: {emoji}")
    
    print("\n🔧 Sample Icons:")
    icon_samples = ['check', 'cross', 'warning', 'info', 'arrow_right', 'star', 'code']
    for name in icon_samples:
        icon = library.get(name, 'icon')
        print(f"  {name.ljust(15)}: {icon}")
    
    print("\n➕ Sample Symbols:")
    symbol_samples = ['plus', 'infinity', 'pi', 'heart', 'star', 'bullet']
    for name in symbol_samples:
        symbol = library.get(name, 'symbol')
        print(f"  {name.ljust(15)}: {symbol}")
    
    # Search functionality
    print("\n🔍 Search for 'arrow':")
    results = library.search('arrow')
    for name, symbol in list(results.items())[:6]:
        print(f"  {name.ljust(15)}: {symbol}")
    
    # Create emoji art
    print("\n🎨 Creating emoji art:")
    emoji_art = f"""
{library.get('star')} {library.get('star')} {library.get('star')} ASCII ART GENERATOR {library.get('star')} {library.get('star')} {library.get('star')}

{library.get('rocket')} Fast Generation
{library.get('fire')} Amazing Results  
{library.get('heart')} Made with Love
{library.get('thumbs_up')} Easy to Use
"""
    print(emoji_art)
    
    input("\n[Press Enter to continue...]")


def demo_quick_templates():
    """Demonstrate quick templates."""
    print("\n" + "=" * 80)
    print("FEATURE 3: QUICK TEMPLATES".center(80))
    print("=" * 80)
    
    quick = QuickTemplates()
    
    print(f"\n✓ Loaded {len(quick.list_templates())} quick templates")
    print(f"✓ Templates: {', '.join(quick.list_templates())}")
    
    # Demo various templates
    print("\n📋 Template Examples:\n")
    
    print("1. Header:")
    print(quick.header('ASCII ART GENERATOR'))
    print()
    
    print("2. Banner:")
    print(quick.banner('WELCOME', 'Version 4.0'))
    print()
    
    print("3. Success Alert:")
    print(quick.success('All tests passed!'))
    print()
    
    print("4. Error Alert:")
    print(quick.error('Connection failed'))
    print()
    
    print("5. Progress Bar:")
    print(quick.progress('Processing', 65, 100))
    print()
    
    print("6. Menu:")
    print(quick.menu('MAIN MENU', ['Start Application', 'Settings', 'Help']))
    print()
    
    print("7. Divider:")
    print(quick.divider('SECTION 1'))
    print()
    
    print("8. Timestamp:")
    print(quick.timestamp('Generated'))
    
    input("\n[Press Enter to continue...]")


def demo_clipboard():
    """Demonstrate clipboard integration."""
    print("\n" + "=" * 80)
    print("FEATURE 4: CLIPBOARD INTEGRATION".center(80))
    print("=" * 80)
    
    clipboard = ClipboardManager()
    helper = ClipboardHelper()
    
    # Show clipboard info
    info = clipboard.get_clipboard_info()
    
    print("\n📋 Clipboard System Information:")
    print(f"  Platform: {info['platform']}")
    print(f"  Tool: {info['tool']}")
    print(f"  Available: {'✓ Yes' if info['available'] else '✗ No'}")
    
    if not info['available']:
        print("\n⚠ Clipboard not available")
        print(clipboard.install_instructions())
        return
    
    # Demo copy functionality
    print("\n✂ Copy Functionality:")
    
    # Generate some art
    from templates.quick_templates import QuickTemplates
    quick = QuickTemplates()
    art = quick.banner('COPIED!', 'To Clipboard')
    
    print("\nGenerating ASCII art:")
    print(art)
    
    # Copy to clipboard
    print("\n📋 Copying to clipboard...")
    success = clipboard.copy(art)
    
    if success:
        print("✓ Successfully copied to clipboard!")
        print("  You can now paste it anywhere with Ctrl+V (or Cmd+V on Mac)")
    else:
        print("✗ Failed to copy to clipboard")
    
    # Demo helper functions
    print("\n🔧 Helper Functions:")
    
    test_art = quick.success('Feature complete!')
    print("\nTest art:")
    print(test_art)
    
    print("\n📋 Using quick_copy with preview:")
    helper.quick_copy(test_art, show_preview=True, preview_lines=3)
    
    input("\n[Press Enter to continue...]")


def demo_combined():
    """Demonstrate combining all features."""
    print("\n" + "=" * 80)
    print("COMBINED DEMO: ALL FEATURES TOGETHER".center(80))
    print("=" * 80)
    
    from styles.preset_library import PresetStyleLibrary
    from assets.emoji_library import EmojiLibrary
    from templates.quick_templates import QuickTemplates
    from utils.clipboard import ClipboardHelper
    
    library = PresetStyleLibrary()
    emoji = EmojiLibrary()
    quick = QuickTemplates()
    clipboard = ClipboardHelper()
    
    print("\n🎨 Creating a complete project banner...\n")
    
    # 1. Generate styled title with preset
    print("Step 1: Applying 'tech_modern' preset...")
    title = library.apply_preset('PROJECT', 'tech_modern', apply_colors=False)
    
    # 2. Add quick template elements
    print("Step 2: Adding quick template elements...")
    subtitle = quick.subtitle('Version 2.0 - Production Ready')
    
    # 3. Add emojis
    print("Step 3: Adding emojis and icons...")
    features = f"""
{emoji.get('rocket')} Fast Performance
{emoji.get('fire')} Amazing Features
{emoji.get('check')} Production Ready
{emoji.get('heart')} Community Driven
"""
    
    # 4. Combine everything
    print("Step 4: Combining elements...")
    complete = f"""
{title}

{subtitle}

{quick.divider('FEATURES')}

{features}

{quick.divider()}

{quick.timestamp('Generated')}
"""
    
    print("\n📄 Final Result:\n")
    print(complete)
    
    # 5. Copy to clipboard
    print("\n📋 Copying to clipboard...")
    clipboard.quick_copy(complete, show_preview=False)
    
    print("\n✨ All features demonstrated successfully!")


def main():
    """Main demo function."""
    print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║              ASCII ART GENERATOR - NEW FEATURES DEMO                      ║
║                                                                           ║
║                            Version 4.0                                    ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
""")
    
    print("This demo showcases 4 powerful new features:\n")
    print("  1. 📚 Preset Style Library (20 professional presets)")
    print("  2. 😊 ASCII Emoji Collection (185+ emojis, icons, symbols)")
    print("  3. ⚡ Quick Templates (16 instant templates)")
    print("  4. 📋 Clipboard Integration (cross-platform copy/paste)")
    
    input("\n[Press Enter to start demo...]")
    
    try:
        demo_preset_library()
        demo_emoji_library()
        demo_quick_templates()
        demo_clipboard()
        demo_combined()
        
        print("\n" + "=" * 80)
        print("DEMO COMPLETE!".center(80))
        print("=" * 80)
        print("\n🎉 All features are working perfectly!")
        print("\n📚 For more information:")
        print("  • API Reference: docs/API_REFERENCE.md")
        print("  • Tutorials: docs/TUTORIALS.md")
        print("  • Best Practices: docs/BEST_PRACTICES.md")
        
    except KeyboardInterrupt:
        print("\n\nDemo interrupted.")
    except Exception as e:
        print(f"\n\nError during demo: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()

