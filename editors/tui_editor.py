"""Real-time interactive TUI editor with mouse support and live preview."""

import curses
import sys
from typing import List, Optional, Tuple, Dict
from dataclasses import dataclass, field
from datetime import datetime
import json


@dataclass
class Layer:
    """Represents a layer in the editor."""
    
    id: int
    name: str
    content: str
    visible: bool = True
    x: int = 0
    y: int = 0
    z_index: int = 0


@dataclass
class EditorState:
    """Editor state for undo/redo."""
    
    layers: List[Layer]
    current_layer_id: int
    timestamp: datetime = field(default_factory=datetime.now)


class UndoRedoManager:
    """Manage undo/redo history."""
    
    def __init__(self, max_history: int = 50):
        """Initialize undo/redo manager.
        
        Args:
            max_history: Maximum history size
        """
        self.history: List[EditorState] = []
        self.current_index = -1
        self.max_history = max_history
    
    def save_state(self, state: EditorState):
        """Save current state.
        
        Args:
            state: State to save
        """
        # Remove any states after current index
        self.history = self.history[:self.current_index + 1]
        
        # Add new state
        self.history.append(state)
        
        # Limit history size
        if len(self.history) > self.max_history:
            self.history = self.history[-self.max_history:]
        
        self.current_index = len(self.history) - 1
    
    def undo(self) -> Optional[EditorState]:
        """Undo to previous state.
        
        Returns:
            Previous state or None
        """
        if self.current_index > 0:
            self.current_index -= 1
            return self.history[self.current_index]
        return None
    
    def redo(self) -> Optional[EditorState]:
        """Redo to next state.
        
        Returns:
            Next state or None
        """
        if self.current_index < len(self.history) - 1:
            self.current_index += 1
            return self.history[self.current_index]
        return None
    
    def can_undo(self) -> bool:
        """Check if undo is available."""
        return self.current_index > 0
    
    def can_redo(self) -> bool:
        """Check if redo is available."""
        return self.current_index < len(self.history) - 1


class InteractiveTUIEditor:
    """Real-time terminal UI editor for ASCII art."""
    
    def __init__(self):
        """Initialize TUI editor."""
        self.layers: List[Layer] = []
        self.current_layer_id = 0
        self.next_layer_id = 1
        self.history = UndoRedoManager()
        
        # Editor settings
        self.canvas_width = 80
        self.canvas_height = 30
        self.preview_mode = True
        self.show_help = False
        self.current_font = 'standard'
        self.current_effect = None
        self.current_preset = None
        
        # UI windows
        self.preview_win = None
        self.toolbar_win = None
        self.layers_win = None
        self.status_win = None
        self.help_win = None
        
        # Input buffer
        self.input_buffer = ""
        self.input_mode = False
    
    def run(self):
        """Launch the interactive editor."""
        try:
            curses.wrapper(self._main_loop)
        except KeyboardInterrupt:
            pass
    
    def _main_loop(self, stdscr):
        """Main editor loop.
        
        Args:
            stdscr: Curses standard screen
        """
        # Initialize curses
        curses.curs_set(0)
        curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
        
        # Initialize colors if available
        if curses.has_colors():
            curses.start_color()
            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Selected
            curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Success
            curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)    # Error
            curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)   # Info
            curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK) # Warning
        
        # Get screen dimensions
        max_y, max_x = stdscr.getmaxyx()
        
        # Create windows
        self._create_windows(max_y, max_x)
        
        # Initial render
        self._render_all()
        
        # Main event loop
        running = True
        while running:
            try:
                # Get input
                key = stdscr.getch()
                
                # Handle input
                if key == ord('q') or key == ord('Q'):
                    if self._confirm_quit():
                        running = False
                
                elif key == ord('n') or key == ord('N'):
                    self._new_layer()
                
                elif key == ord('t') or key == ord('T'):
                    self._add_text_layer()
                
                elif key == ord('e') or key == ord('E'):
                    self._toggle_effect_menu()
                
                elif key == ord('f') or key == ord('F'):
                    self._change_font()
                
                elif key == ord('p') or key == ord('P'):
                    self._apply_preset()
                
                elif key == ord('s') or key == ord('S'):
                    self._save_project()
                
                elif key == ord('o') or key == ord('O'):
                    self._open_project()
                
                elif key == ord('c') or key == ord('C'):
                    self._copy_to_clipboard()
                
                elif key == ord('x') or key == ord('X'):
                    self._export_menu()
                
                elif key == ord('l') or key == ord('L'):
                    self._toggle_layers_panel()
                
                elif key == ord('h') or key == ord('H') or key == curses.KEY_F1:
                    self._toggle_help()
                
                elif key == 26:  # Ctrl+Z
                    self._undo()
                
                elif key == 25:  # Ctrl+Y
                    self._redo()
                
                elif key == curses.KEY_UP:
                    self._move_layer(0, -1)
                
                elif key == curses.KEY_DOWN:
                    self._move_layer(0, 1)
                
                elif key == curses.KEY_LEFT:
                    self._move_layer(-1, 0)
                
                elif key == curses.KEY_RIGHT:
                    self._move_layer(1, 0)
                
                elif key == curses.KEY_MOUSE:
                    self._handle_mouse()
                
                elif key == curses.KEY_RESIZE:
                    self._handle_resize()
                
                # Update display
                self._render_all()
                
            except Exception as e:
                self._show_error(str(e))
    
    def _create_windows(self, max_y: int, max_x: int):
        """Create UI windows.
        
        Args:
            max_y: Screen height
            max_x: Screen width
        """
        # Preview window (main area)
        preview_height = max_y - 8
        preview_width = max_x - 25
        self.preview_win = curses.newwin(preview_height, preview_width, 0, 0)
        
        # Layers panel (right side)
        self.layers_win = curses.newwin(preview_height, 24, 0, preview_width + 1)
        
        # Toolbar (top)
        self.toolbar_win = curses.newwin(2, max_x, 0, 0)
        
        # Status bar (bottom)
        self.status_win = curses.newwin(3, max_x, max_y - 3, 0)
        
        # Help window (overlay)
        help_height = min(30, max_y - 4)
        help_width = min(70, max_x - 4)
        help_y = (max_y - help_height) // 2
        help_x = (max_x - help_width) // 2
        self.help_win = curses.newwin(help_height, help_width, help_y, help_x)
    
    def _render_all(self):
        """Render all windows."""
        self._render_toolbar()
        self._render_preview()
        self._render_layers()
        self._render_status()
        
        if self.show_help:
            self._render_help()
        
        curses.doupdate()
    
    def _render_toolbar(self):
        """Render toolbar."""
        if not self.toolbar_win:
            return
        
        self.toolbar_win.clear()
        self.toolbar_win.box()
        
        toolbar_text = " [N]ew [T]ext [E]ffect [F]ont [P]reset [S]ave [O]pen [C]opy e[X]port [H]elp [Q]uit "
        
        try:
            self.toolbar_win.addstr(0, 2, toolbar_text[:self.toolbar_win.getmaxyx()[1] - 4])
        except curses.error:
            pass
        
        self.toolbar_win.noutrefresh()
    
    def _render_preview(self):
        """Render preview window with composed layers."""
        if not self.preview_win:
            return
        
        self.preview_win.clear()
        self.preview_win.box()
        
        # Add title
        try:
            self.preview_win.addstr(0, 2, " Preview ", curses.A_BOLD)
        except curses.error:
            pass
        
        # Render layers
        height, width = self.preview_win.getmaxyx()
        
        # Sort layers by z-index
        sorted_layers = sorted(
            [l for l in self.layers if l.visible],
            key=lambda l: l.z_index
        )
        
        for layer in sorted_layers:
            lines = layer.content.split('\n')
            
            for i, line in enumerate(lines):
                y = layer.y + i + 1  # +1 for border
                x = layer.x + 1      # +1 for border
                
                if 1 <= y < height - 1 and x < width - 1:
                    try:
                        # Highlight current layer
                        if layer.id == self.current_layer_id:
                            self.preview_win.addstr(y, x, line[:width - x - 1], curses.A_REVERSE)
                        else:
                            self.preview_win.addstr(y, x, line[:width - x - 1])
                    except curses.error:
                        pass
        
        self.preview_win.noutrefresh()
    
    def _render_layers(self):
        """Render layers panel."""
        if not self.layers_win:
            return
        
        self.layers_win.clear()
        self.layers_win.box()
        
        try:
            self.layers_win.addstr(0, 2, " Layers ", curses.A_BOLD)
        except curses.error:
            pass
        
        height, width = self.layers_win.getmaxyx()
        
        # List layers
        for i, layer in enumerate(self.layers):
            if i + 2 < height - 1:
                # Layer indicator
                indicator = "●" if layer.visible else "○"
                selected = ">" if layer.id == self.current_layer_id else " "
                
                layer_text = f"{selected}{indicator} {layer.name[:width-6]}"
                
                try:
                    if layer.id == self.current_layer_id:
                        self.layers_win.addstr(i + 2, 1, layer_text, curses.A_REVERSE)
                    else:
                        self.layers_win.addstr(i + 2, 1, layer_text)
                except curses.error:
                    pass
        
        # Add controls hint
        try:
            self.layers_win.addstr(height - 2, 1, "[L] Toggle panel", curses.A_DIM)
        except curses.error:
            pass
        
        self.layers_win.noutrefresh()
    
    def _render_status(self):
        """Render status bar."""
        if not self.status_win:
            return
        
        self.status_win.clear()
        self.status_win.box()
        
        # Status info
        layer_count = len(self.layers)
        current_layer = self._get_current_layer()
        layer_name = current_layer.name if current_layer else "None"
        
        status_text = f" Layers: {layer_count} | Current: {layer_name} | Font: {self.current_font}"
        
        if self.current_effect:
            status_text += f" | Effect: {self.current_effect}"
        
        if self.current_preset:
            status_text += f" | Preset: {self.current_preset}"
        
        try:
            self.status_win.addstr(1, 2, status_text[:self.status_win.getmaxyx()[1] - 4])
        except curses.error:
            pass
        
        # Undo/Redo status
        undo_status = "Undo: " + ("✓" if self.history.can_undo() else "✗")
        redo_status = "Redo: " + ("✓" if self.history.can_redo() else "✗")
        
        try:
            self.status_win.addstr(2, 2, f"{undo_status} | {redo_status}")
        except curses.error:
            pass
        
        self.status_win.noutrefresh()
    
    def _render_help(self):
        """Render help overlay."""
        if not self.help_win:
            return
        
        self.help_win.clear()
        self.help_win.box()
        
        try:
            self.help_win.addstr(0, 2, " HELP - Keyboard Shortcuts ", curses.A_BOLD)
        except curses.error:
            pass
        
        help_text = [
            "",
            "  GENERAL:",
            "    H / F1      - Toggle this help",
            "    Q           - Quit editor",
            "    Ctrl+Z      - Undo",
            "    Ctrl+Y      - Redo",
            "",
            "  LAYERS:",
            "    N           - New empty layer",
            "    T           - Add text layer",
            "    L           - Toggle layers panel",
            "    Arrow Keys  - Move current layer",
            "",
            "  STYLING:",
            "    F           - Change font",
            "    E           - Apply effect",
            "    P           - Apply preset style",
            "",
            "  FILE OPERATIONS:",
            "    S           - Save project",
            "    O           - Open project",
            "    C           - Copy to clipboard",
            "    X           - Export menu",
            "",
            "  Press any key to close help...",
        ]
        
        for i, line in enumerate(help_text):
            if i + 1 < self.help_win.getmaxyx()[0] - 1:
                try:
                    self.help_win.addstr(i + 1, 1, line)
                except curses.error:
                    pass
        
        self.help_win.noutrefresh()
        curses.doupdate()
        
        # Wait for key
        self.help_win.getch()
        self.show_help = False
    
    def _toggle_help(self):
        """Toggle help display."""
        self.show_help = not self.show_help
    
    def _new_layer(self):
        """Create new empty layer."""
        layer = Layer(
            id=self.next_layer_id,
            name=f"Layer {self.next_layer_id}",
            content="",
            z_index=len(self.layers)
        )
        
        self.layers.append(layer)
        self.current_layer_id = layer.id
        self.next_layer_id += 1
        
        self._save_history()
        self._show_message("New layer created")
    
    def _add_text_layer(self):
        """Add text layer with input."""
        # Get text input
        text = self._get_text_input("Enter text: ")
        
        if not text:
            return
        
        # Generate ASCII art
        from generators.text_art import TextArtGenerator
        from utils.config import Config
        
        config = Config()
        gen = TextArtGenerator(config)
        
        try:
            art = gen.generate(text, font=self.current_font)
            
            # Create layer
            layer = Layer(
                id=self.next_layer_id,
                name=f"Text: {text[:10]}",
                content=art,
                z_index=len(self.layers)
            )
            
            self.layers.append(layer)
            self.current_layer_id = layer.id
            self.next_layer_id += 1
            
            self._save_history()
            self._show_message(f"Text layer added: {text}")
        
        except Exception as e:
            self._show_error(f"Error: {e}")
    
    def _toggle_effect_menu(self):
        """Show effect selection menu."""
        effects = ['shadow', '3d', 'outline', 'glow', 'mirror', 'neon', 'none']
        
        selected = self._show_menu("Select Effect", effects)
        
        if selected and selected != 'none':
            self._apply_effect_to_current_layer(selected)
    
    def _apply_effect_to_current_layer(self, effect: str):
        """Apply effect to current layer.
        
        Args:
            effect: Effect name
        """
        current_layer = self._get_current_layer()
        
        if not current_layer:
            self._show_error("No layer selected")
            return
        
        from generators.text_effects import TextEffects
        
        effects = TextEffects()
        
        try:
            if effect == 'shadow':
                current_layer.content = effects.add_shadow(current_layer.content)
            elif effect == '3d':
                current_layer.content = effects.add_3d_effect(current_layer.content)
            elif effect == 'outline':
                current_layer.content = effects.add_outline(current_layer.content)
            elif effect == 'glow':
                current_layer.content = effects.add_glow(current_layer.content)
            elif effect == 'mirror':
                current_layer.content = effects.add_mirror(current_layer.content)
            elif effect == 'neon':
                current_layer.content = effects.add_neon(current_layer.content)
            
            self.current_effect = effect
            self._save_history()
            self._show_message(f"Applied effect: {effect}")
        
        except Exception as e:
            self._show_error(f"Error applying effect: {e}")
    
    def _change_font(self):
        """Change current font."""
        fonts = ['standard', 'banner', 'block', 'slant', 'small', 'bubble']
        
        selected = self._show_menu("Select Font", fonts)
        
        if selected:
            self.current_font = selected
            self._show_message(f"Font changed to: {selected}")
    
    def _apply_preset(self):
        """Apply preset style."""
        from styles.preset_library import PresetStyleLibrary
        
        library = PresetStyleLibrary()
        presets = [p.name for p in library.list_presets()]
        
        selected = self._show_menu("Select Preset", presets[:10])  # Show first 10
        
        if selected:
            current_layer = self._get_current_layer()
            
            if current_layer:
                # Extract text from current layer (simplified)
                text = current_layer.name.replace("Text: ", "")
                
                try:
                    art = library.apply_preset(text, selected, apply_colors=False)
                    current_layer.content = art
                    self.current_preset = selected
                    self._save_history()
                    self._show_message(f"Applied preset: {selected}")
                except Exception as e:
                    self._show_error(f"Error: {e}")
    
    def _save_project(self):
        """Save current project."""
        filename = self._get_text_input("Save as: ", default="project.aap")
        
        if not filename:
            return
        
        try:
            project_data = {
                'version': '1.0',
                'layers': [
                    {
                        'id': layer.id,
                        'name': layer.name,
                        'content': layer.content,
                        'visible': layer.visible,
                        'x': layer.x,
                        'y': layer.y,
                        'z_index': layer.z_index
                    }
                    for layer in self.layers
                ],
                'settings': {
                    'font': self.current_font,
                    'effect': self.current_effect,
                    'preset': self.current_preset
                },
                'metadata': {
                    'created': datetime.now().isoformat(),
                    'layer_count': len(self.layers)
                }
            }
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(project_data, f, indent=2)
            
            self._show_message(f"Project saved: {filename}")
        
        except Exception as e:
            self._show_error(f"Save failed: {e}")
    
    def _open_project(self):
        """Open project file."""
        filename = self._get_text_input("Open file: ", default="project.aap")
        
        if not filename:
            return
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                project_data = json.load(f)
            
            # Load layers
            self.layers = []
            for layer_data in project_data['layers']:
                layer = Layer(**layer_data)
                self.layers.append(layer)
            
            # Load settings
            settings = project_data.get('settings', {})
            self.current_font = settings.get('font', 'standard')
            self.current_effect = settings.get('effect')
            self.current_preset = settings.get('preset')
            
            if self.layers:
                self.current_layer_id = self.layers[0].id
                self.next_layer_id = max(l.id for l in self.layers) + 1
            
            self._save_history()
            self._show_message(f"Project loaded: {filename}")
        
        except Exception as e:
            self._show_error(f"Load failed: {e}")
    
    def _copy_to_clipboard(self):
        """Copy current composition to clipboard."""
        from utils.clipboard import ClipboardManager
        
        # Compose all layers
        composed = self._compose_layers()
        
        clipboard = ClipboardManager()
        
        if clipboard.copy(composed):
            self._show_message("✓ Copied to clipboard!")
        else:
            self._show_error("✗ Clipboard copy failed")
    
    def _export_menu(self):
        """Show export menu."""
        formats = ['text', 'html', 'svg', 'markdown', 'png']
        
        selected = self._show_menu("Export Format", formats)
        
        if selected:
            filename = self._get_text_input(f"Export as {selected}: ", default=f"output.{selected}")
            
            if filename:
                self._export_to_format(filename, selected)
    
    def _export_to_format(self, filename: str, format: str):
        """Export to specified format.
        
        Args:
            filename: Output filename
            format: Export format
        """
        composed = self._compose_layers()
        
        try:
            if format == 'text':
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(composed)
            
            elif format == 'html':
                from exporters.formats import HTMLExporter
                exporter = HTMLExporter()
                html = exporter.export(composed, title="ASCII Art")
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(html)
            
            elif format == 'svg':
                from exporters.formats import SVGExporter
                exporter = SVGExporter()
                svg = exporter.export(composed, title="ASCII Art")
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(svg)
            
            elif format == 'markdown':
                from exporters.formats import MarkdownExporter
                exporter = MarkdownExporter()
                md = exporter.export(composed, title="ASCII Art")
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(md)
            
            elif format == 'png':
                from exporters.formats import ImageExporter
                exporter = ImageExporter()
                exporter.export_to_png(composed, filename)
            
            self._show_message(f"Exported to: {filename}")
        
        except Exception as e:
            self._show_error(f"Export failed: {e}")
    
    def _compose_layers(self) -> str:
        """Compose all visible layers.
        
        Returns:
            Composed ASCII art
        """
        # Create canvas
        canvas = [[' ' for _ in range(self.canvas_width)] 
                  for _ in range(self.canvas_height)]
        
        # Sort layers by z-index
        sorted_layers = sorted(
            [l for l in self.layers if l.visible],
            key=lambda l: l.z_index
        )
        
        # Render each layer
        for layer in sorted_layers:
            lines = layer.content.split('\n')
            
            for i, line in enumerate(lines):
                y = layer.y + i
                
                if 0 <= y < self.canvas_height:
                    for j, char in enumerate(line):
                        x = layer.x + j
                        
                        if 0 <= x < self.canvas_width and char != ' ':
                            canvas[y][x] = char
        
        return '\n'.join([''.join(row).rstrip() for row in canvas])
    
    def _move_layer(self, dx: int, dy: int):
        """Move current layer.
        
        Args:
            dx: X offset
            dy: Y offset
        """
        current_layer = self._get_current_layer()
        
        if current_layer:
            current_layer.x += dx
            current_layer.y += dy
            self._save_history()
    
    def _get_current_layer(self) -> Optional[Layer]:
        """Get current layer.
        
        Returns:
            Current layer or None
        """
        for layer in self.layers:
            if layer.id == self.current_layer_id:
                return layer
        return None
    
    def _toggle_layers_panel(self):
        """Toggle layers panel visibility."""
        # Cycle through layers
        if self.layers:
            current_index = next((i for i, l in enumerate(self.layers) 
                                if l.id == self.current_layer_id), -1)
            next_index = (current_index + 1) % len(self.layers)
            self.current_layer_id = self.layers[next_index].id
    
    def _undo(self):
        """Undo last action."""
        state = self.history.undo()
        
        if state:
            self._restore_state(state)
            self._show_message("Undo")
        else:
            self._show_message("Nothing to undo")
    
    def _redo(self):
        """Redo last undone action."""
        state = self.history.redo()
        
        if state:
            self._restore_state(state)
            self._show_message("Redo")
        else:
            self._show_message("Nothing to redo")
    
    def _save_history(self):
        """Save current state to history."""
        state = EditorState(
            layers=[Layer(**vars(l)) for l in self.layers],
            current_layer_id=self.current_layer_id
        )
        self.history.save_state(state)
    
    def _restore_state(self, state: EditorState):
        """Restore editor state.
        
        Args:
            state: State to restore
        """
        self.layers = [Layer(**vars(l)) for l in state.layers]
        self.current_layer_id = state.current_layer_id
    
    def _handle_mouse(self):
        """Handle mouse events."""
        try:
            _, x, y, _, button = curses.getmouse()
            
            # Check if click is in preview window
            if self.preview_win:
                py, px = self.preview_win.getbegyx()
                ph, pw = self.preview_win.getmaxyx()
                
                if py <= y < py + ph and px <= x < px + pw:
                    # Click in preview - could select layer at position
                    pass
        
        except curses.error:
            pass
    
    def _handle_resize(self):
        """Handle terminal resize."""
        curses.endwin()
        curses.initscr()
        max_y, max_x = curses.LINES, curses.COLS
        self._create_windows(max_y, max_x)
    
    def _get_text_input(self, prompt: str, default: str = "") -> str:
        """Get text input from user.
        
        Args:
            prompt: Input prompt
            default: Default value
            
        Returns:
            User input
        """
        if not self.status_win:
            return default
        
        curses.curs_set(1)
        curses.echo()
        
        self.status_win.clear()
        self.status_win.box()
        
        try:
            self.status_win.addstr(1, 2, prompt)
            self.status_win.refresh()
            
            # Get input
            input_str = self.status_win.getstr(1, 2 + len(prompt), 50).decode('utf-8')
        except:
            input_str = default
        
        curses.noecho()
        curses.curs_set(0)
        
        return input_str or default
    
    def _show_menu(self, title: str, options: List[str]) -> Optional[str]:
        """Show selection menu.
        
        Args:
            title: Menu title
            options: List of options
            
        Returns:
            Selected option or None
        """
        if not self.help_win:
            return None
        
        current_selection = 0
        
        while True:
            self.help_win.clear()
            self.help_win.box()
            
            try:
                self.help_win.addstr(0, 2, f" {title} ", curses.A_BOLD)
            except curses.error:
                pass
            
            # Show options
            for i, option in enumerate(options):
                if i + 2 < self.help_win.getmaxyx()[0] - 2:
                    try:
                        if i == current_selection:
                            self.help_win.addstr(i + 2, 2, f"> {option}", curses.A_REVERSE)
                        else:
                            self.help_win.addstr(i + 2, 2, f"  {option}")
                    except curses.error:
                        pass
            
            try:
                self.help_win.addstr(self.help_win.getmaxyx()[0] - 2, 2, 
                                    "[↑↓] Navigate [Enter] Select [Esc] Cancel")
            except curses.error:
                pass
            
            self.help_win.refresh()
            
            # Get input
            key = self.help_win.getch()
            
            if key == curses.KEY_UP and current_selection > 0:
                current_selection -= 1
            elif key == curses.KEY_DOWN and current_selection < len(options) - 1:
                current_selection += 1
            elif key == ord('\n') or key == curses.KEY_ENTER or key == 10:
                return options[current_selection]
            elif key == 27:  # Escape
                return None
    
    def _show_message(self, message: str):
        """Show status message.
        
        Args:
            message: Message to show
        """
        if self.status_win:
            try:
                self.status_win.addstr(2, 2, f"ℹ {message}"[:self.status_win.getmaxyx()[1] - 4], 
                                      curses.color_pair(4))
                self.status_win.refresh()
            except curses.error:
                pass
    
    def _show_error(self, message: str):
        """Show error message.
        
        Args:
            message: Error message
        """
        if self.status_win:
            try:
                self.status_win.addstr(2, 2, f"✗ {message}"[:self.status_win.getmaxyx()[1] - 4], 
                                      curses.color_pair(3))
                self.status_win.refresh()
            except curses.error:
                pass
    
    def _confirm_quit(self) -> bool:
        """Confirm quit action.
        
        Returns:
            True if user confirms
        """
        response = self._get_text_input("Quit without saving? (y/n): ", default="n")
        return response.lower() == 'y'


def launch_editor():
    """Launch the interactive TUI editor."""
    editor = InteractiveTUIEditor()
    editor.run()


if __name__ == '__main__':
    launch_editor()

