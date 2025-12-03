"""TUI-based color picker for creating custom color palettes."""

import curses
from typing import Tuple, Optional, List
from utils.color_art import ColorMapper


class ColorPicker:
    """TUI color picker using curses."""
    
    def __init__(self):
        """Initialize color picker."""
        self.color_mapper = ColorMapper()
        self.r = 255
        self.g = 255
        self.b = 255
        self.mode = 'rgb'  # 'rgb' or 'hsv'
    
    def pick_color(self, stdscr, initial_color: Optional[Tuple[int, int, int]] = None) -> Optional[Tuple[int, int, int]]:
        """Interactive color picker.
        
        Args:
            stdscr: Curses standard screen
            initial_color: Optional initial RGB color
            
        Returns:
            Selected RGB color tuple or None if cancelled
        """
        if initial_color:
            self.r, self.g, self.b = initial_color
        
        curses.curs_set(0)
        curses.start_color()
        
        # Create color picker window
        height, width = stdscr.getmaxyx()
        picker_height = 15
        picker_width = 60
        y = (height - picker_height) // 2
        x = (width - picker_width) // 2
        
        picker_win = curses.newwin(picker_height, picker_width, y, x)
        
        selected_field = 0  # 0=R, 1=G, 2=B
        confirmed = False
        cancelled = False
        
        while not confirmed and not cancelled:
            picker_win.clear()
            picker_win.box()
            
            try:
                picker_win.addstr(0, 2, " Color Picker ", curses.A_BOLD)
            except curses.error:
                pass
            
            # Display RGB values
            r_str = f"R: {self.r:3d}"
            g_str = f"G: {self.g:3d}"
            b_str = f"B: {self.b:3d}"
            
            # Highlight selected field
            attr_r = curses.A_REVERSE if selected_field == 0 else curses.A_NORMAL
            attr_g = curses.A_REVERSE if selected_field == 1 else curses.A_NORMAL
            attr_b = curses.A_REVERSE if selected_field == 2 else curses.A_NORMAL
            
            try:
                picker_win.addstr(2, 5, r_str, attr_r)
                picker_win.addstr(2, 20, g_str, attr_g)
                picker_win.addstr(2, 35, b_str, attr_b)
            except curses.error:
                pass
            
            # Color preview
            preview_text = "████████████████████"
            color_code = self.color_mapper.ansi_fg_color(self.r, self.g, self.b)
            reset_code = self.color_mapper.reset()
            
            try:
                picker_win.addstr(4, 5, "Preview:")
                # Note: curses may not support truecolor, so we'll use a simple representation
                picker_win.addstr(5, 5, preview_text)
            except curses.error:
                pass
            
            # RGB sliders (visual representation)
            try:
                picker_win.addstr(7, 5, "R: " + "█" * (self.r // 12) + "░" * (21 - self.r // 12))
                picker_win.addstr(8, 5, "G: " + "█" * (self.g // 12) + "░" * (21 - self.g // 12))
                picker_win.addstr(9, 5, "B: " + "█" * (self.b // 12) + "░" * (21 - self.b // 12))
            except curses.error:
                pass
            
            # Instructions
            try:
                picker_win.addstr(11, 2, "[↑↓] Change field  [←→] Adjust value")
                picker_win.addstr(12, 2, "[Enter] Confirm    [Esc] Cancel")
            except curses.error:
                pass
            
            picker_win.refresh()
            
            # Get input
            key = stdscr.getch()
            
            if key == curses.KEY_UP:
                selected_field = (selected_field - 1) % 3
            elif key == curses.KEY_DOWN:
                selected_field = (selected_field + 1) % 3
            elif key == curses.KEY_LEFT:
                if selected_field == 0:
                    self.r = max(0, self.r - 10)
                elif selected_field == 1:
                    self.g = max(0, self.g - 10)
                elif selected_field == 2:
                    self.b = max(0, self.b - 10)
            elif key == curses.KEY_RIGHT:
                if selected_field == 0:
                    self.r = min(255, self.r + 10)
                elif selected_field == 1:
                    self.g = min(255, self.g + 10)
                elif selected_field == 2:
                    self.b = min(255, self.b + 10)
            elif key == ord('\n') or key == curses.KEY_ENTER or key == 10:
                confirmed = True
            elif key == 27:  # Escape
                cancelled = True
            elif key >= ord('0') and key <= ord('9'):
                # Direct number input for selected field
                digit = key - ord('0')
                if selected_field == 0:
                    self.r = min(255, self.r * 10 + digit)
                elif selected_field == 1:
                    self.g = min(255, self.g * 10 + digit)
                elif selected_field == 2:
                    self.b = min(255, self.b * 10 + digit)
            elif key == ord('r') or key == ord('R'):
                selected_field = 0
            elif key == ord('g') or key == ord('G'):
                selected_field = 1
            elif key == ord('b') or key == ord('B'):
                selected_field = 2
        
        if confirmed:
            return (self.r, self.g, self.b)
        return None
    
    def pick_color_simple(self, initial_color: Optional[Tuple[int, int, int]] = None) -> Optional[Tuple[int, int, int]]:
        """Simple color picker wrapper.
        
        Args:
            initial_color: Optional initial RGB color
            
        Returns:
            Selected RGB color tuple or None if cancelled
        """
        return curses.wrapper(self.pick_color, initial_color)


class GradientBuilder:
    """Multi-color gradient builder."""
    
    def __init__(self):
        """Initialize gradient builder."""
        self.colors: List[Tuple[int, int, int]] = []
        self.color_picker = ColorPicker()
    
    def build_gradient(self, stdscr) -> Optional[List[Tuple[int, int, int]]]:
        """Build gradient interactively.
        
        Args:
            stdscr: Curses standard screen
            
        Returns:
            List of RGB colors or None if cancelled
        """
        curses.curs_set(0)
        
        height, width = stdscr.getmaxyx()
        builder_height = 20
        builder_width = 70
        y = (height - builder_height) // 2
        x = (width - builder_width) // 2
        
        builder_win = curses.newwin(builder_height, builder_width, y, x)
        
        selected_index = -1
        confirmed = False
        cancelled = False
        
        while not confirmed and not cancelled:
            builder_win.clear()
            builder_win.box()
            
            try:
                builder_win.addstr(0, 2, " Gradient Builder ", curses.A_BOLD)
            except curses.error:
                pass
            
            # Display current colors
            try:
                builder_win.addstr(2, 5, f"Colors in gradient: {len(self.colors)}")
            except curses.error:
                pass
            
            # List colors
            for i, color in enumerate(self.colors):
                r, g, b = color
                color_str = f"  {i+1}. RGB({r:3d}, {g:3d}, {b:3d})"
                
                attr = curses.A_REVERSE if i == selected_index else curses.A_NORMAL
                try:
                    builder_win.addstr(4 + i, 5, color_str[:builder_width - 10], attr)
                except curses.error:
                    break
            
            # Instructions
            try:
                builder_win.addstr(builder_height - 6, 2, "[A] Add color  [D] Delete selected  [E] Edit selected")
                builder_win.addstr(builder_height - 5, 2, "[Enter] Confirm  [Esc] Cancel")
                builder_win.addstr(builder_height - 4, 2, f"Minimum 2 colors required. Current: {len(self.colors)}")
            except curses.error:
                pass
            
            builder_win.refresh()
            
            # Get input
            key = stdscr.getch()
            
            if key == ord('a') or key == ord('A'):
                # Add new color
                new_color = self.color_picker.pick_color(stdscr)
                if new_color:
                    self.colors.append(new_color)
                    selected_index = len(self.colors) - 1
            
            elif key == ord('d') or key == ord('D'):
                # Delete selected color
                if 0 <= selected_index < len(self.colors) and len(self.colors) > 2:
                    self.colors.pop(selected_index)
                    if selected_index >= len(self.colors):
                        selected_index = len(self.colors) - 1
            
            elif key == ord('e') or key == ord('E'):
                # Edit selected color
                if 0 <= selected_index < len(self.colors):
                    edited_color = self.color_picker.pick_color(stdscr, self.colors[selected_index])
                    if edited_color:
                        self.colors[selected_index] = edited_color
            
            elif key == curses.KEY_UP:
                if selected_index > 0:
                    selected_index -= 1
                elif len(self.colors) > 0:
                    selected_index = len(self.colors) - 1
            
            elif key == curses.KEY_DOWN:
                if selected_index < len(self.colors) - 1:
                    selected_index += 1
                else:
                    selected_index = 0
            
            elif key == ord('\n') or key == curses.KEY_ENTER or key == 10:
                if len(self.colors) >= 2:
                    confirmed = True
                else:
                    # Show error
                    try:
                        builder_win.addstr(builder_height - 3, 2, "Error: Need at least 2 colors!", curses.A_BOLD)
                        builder_win.refresh()
                        curses.napms(1000)
                    except curses.error:
                        pass
            
            elif key == 27:  # Escape
                cancelled = True
        
        if confirmed and len(self.colors) >= 2:
            return self.colors.copy()
        return None
    
    def build_gradient_simple(self) -> Optional[List[Tuple[int, int, int]]]:
        """Simple gradient builder wrapper.
        
        Returns:
            List of RGB colors or None if cancelled
        """
        return curses.wrapper(self.build_gradient)

