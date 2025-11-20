"""Animation support for ASCII art with frame generation."""

import time
import math
from typing import List, Callable, Optional
import sys


class AnimationFrame:
    """Represents a single frame of ASCII animation."""
    
    def __init__(self, content: str, duration: float = 0.1):
        """Initialize animation frame.
        
        Args:
            content: ASCII art content
            duration: Frame duration in seconds
        """
        self.content = content
        self.duration = duration


class Animation:
    """ASCII art animation with multiple frames."""
    
    def __init__(self, frames: List[AnimationFrame] = None):
        """Initialize animation.
        
        Args:
            frames: List of animation frames
        """
        self.frames = frames or []
    
    def add_frame(self, content: str, duration: float = 0.1):
        """Add a frame to the animation.
        
        Args:
            content: Frame content
            duration: Frame duration in seconds
        """
        self.frames.append(AnimationFrame(content, duration))
    
    def play(self, loop: bool = False, clear_screen: bool = True):
        """Play the animation in terminal.
        
        Args:
            loop: Whether to loop the animation
            clear_screen: Whether to clear screen between frames
        """
        try:
            while True:
                for frame in self.frames:
                    if clear_screen:
                        # Clear screen
                        print('\033[2J\033[H', end='')
                    
                    print(frame.content)
                    time.sleep(frame.duration)
                
                if not loop:
                    break
        
        except KeyboardInterrupt:
            print("\nAnimation stopped.")
    
    def export_frames(self, output_dir: str, prefix: str = 'frame'):
        """Export frames to files.
        
        Args:
            output_dir: Output directory
            prefix: Filename prefix
        """
        import os
        
        os.makedirs(output_dir, exist_ok=True)
        
        for i, frame in enumerate(self.frames):
            filename = os.path.join(output_dir, f'{prefix}_{i:04d}.txt')
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(frame.content)


class AnimationGenerator:
    """Generate various types of ASCII animations."""
    
    def __init__(self):
        """Initialize animation generator."""
        pass
    
    def spinning_loader(self, frames: int = 8) -> Animation:
        """Generate spinning loader animation.
        
        Args:
            frames: Number of frames
            
        Returns:
            Animation object
        """
        animation = Animation()
        chars = ['|', '/', '-', '\\']
        
        for i in range(frames):
            char = chars[i % len(chars)]
            content = f"Loading {char}"
            animation.add_frame(content, 0.1)
        
        return animation
    
    def bouncing_ball(self, width: int = 40, height: int = 10,
                     frames: int = 20) -> Animation:
        """Generate bouncing ball animation.
        
        Args:
            width: Width of canvas
            height: Height of canvas
            frames: Number of frames
            
        Returns:
            Animation object
        """
        animation = Animation()
        
        for i in range(frames):
            t = i / frames
            
            # Calculate ball position
            x = int((math.sin(t * 2 * math.pi) + 1) / 2 * (width - 1))
            y = int((abs(math.sin(t * 4 * math.pi))) * (height - 1))
            
            # Create frame
            lines = []
            for row in range(height):
                line = ''
                for col in range(width):
                    if row == y and col == x:
                        line += 'O'
                    else:
                        line += ' '
                lines.append(line)
            
            animation.add_frame('\n'.join(lines), 0.05)
        
        return animation
    
    def wave_animation(self, width: int = 60, height: int = 10,
                      frames: int = 30) -> Animation:
        """Generate wave animation.
        
        Args:
            width: Width of canvas
            height: Height of canvas
            frames: Number of frames
            
        Returns:
            Animation object
        """
        animation = Animation()
        
        for frame_num in range(frames):
            lines = []
            phase = frame_num / frames * 2 * math.pi
            
            for y in range(height):
                line = ''
                for x in range(width):
                    # Calculate wave
                    wave_y = int((height / 2) + (height / 4) * 
                               math.sin((x / width) * 4 * math.pi + phase))
                    
                    if y == wave_y:
                        line += '~'
                    else:
                        line += ' '
                
                lines.append(line)
            
            animation.add_frame('\n'.join(lines), 0.05)
        
        return animation
    
    def text_scroll(self, text: str, width: int = 80,
                   frames: int = None) -> Animation:
        """Generate scrolling text animation.
        
        Args:
            text: Text to scroll
            width: Width of viewport
            frames: Number of frames (default: len(text) + width)
            
        Returns:
            Animation object
        """
        animation = Animation()
        
        if frames is None:
            frames = len(text) + width
        
        for i in range(frames):
            # Calculate visible portion
            start = max(0, i - width)
            end = i
            
            visible = ' ' * (width - (i - start)) + text[start:end]
            visible = visible[:width]
            
            animation.add_frame(visible, 0.05)
        
        return animation
    
    def rotating_text(self, text: str, frames: int = 8) -> Animation:
        """Generate rotating text animation (perspective effect).
        
        Args:
            text: Text to rotate
            frames: Number of frames
            
        Returns:
            Animation object
        """
        animation = Animation()
        
        for i in range(frames):
            angle = (i / frames) * 2 * math.pi
            scale = abs(math.cos(angle))
            
            if scale < 0.1:
                content = '|'
            else:
                # Compress text based on angle
                compressed_len = max(1, int(len(text) * scale))
                content = text[:compressed_len]
            
            animation.add_frame(content, 0.1)
        
        return animation
    
    def matrix_rain(self, width: int = 80, height: int = 20,
                   frames: int = 50) -> Animation:
        """Generate Matrix-style falling characters animation.
        
        Args:
            width: Width of canvas
            height: Height of canvas
            frames: Number of frames
            
        Returns:
            Animation object
        """
        import random
        
        animation = Animation()
        
        # Initialize columns
        columns = []
        for _ in range(width):
            columns.append({
                'y': random.randint(-height, 0),
                'speed': random.randint(1, 3),
                'length': random.randint(5, 15)
            })
        
        for frame_num in range(frames):
            lines = [[' ' for _ in range(width)] for _ in range(height)]
            
            # Update and draw columns
            for col_idx, col in enumerate(columns):
                col['y'] += col['speed']
                
                if col['y'] > height + col['length']:
                    col['y'] = -col['length']
                
                # Draw column
                for i in range(col['length']):
                    y = col['y'] - i
                    if 0 <= y < height:
                        char = chr(random.randint(33, 126))
                        lines[y][col_idx] = char
            
            # Convert to string
            frame_content = '\n'.join([''.join(line) for line in lines])
            animation.add_frame(frame_content, 0.05)
        
        return animation
    
    def progress_bar(self, width: int = 50, steps: int = 20) -> Animation:
        """Generate progress bar animation.
        
        Args:
            width: Width of progress bar
            steps: Number of steps
            
        Returns:
            Animation object
        """
        animation = Animation()
        
        for i in range(steps + 1):
            progress = i / steps
            filled = int(width * progress)
            
            bar = '█' * filled + '░' * (width - filled)
            percentage = int(progress * 100)
            content = f'[{bar}] {percentage}%'
            
            animation.add_frame(content, 0.1)
        
        return animation
    
    def typewriter_effect(self, text: str, delay: float = 0.05) -> Animation:
        """Generate typewriter effect animation.
        
        Args:
            text: Text to type out
            delay: Delay between characters
            
        Returns:
            Animation object
        """
        animation = Animation()
        
        lines = text.split('\n')
        current_text = []
        
        for line in lines:
            for i in range(len(line) + 1):
                frame_lines = current_text + [line[:i]]
                content = '\n'.join(frame_lines)
                animation.add_frame(content, delay)
            
            current_text.append(line)
        
        return animation

