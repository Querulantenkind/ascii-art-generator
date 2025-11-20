"""ASCII video generation from video files."""

import os
import subprocess
from typing import Optional, Callable
import time


class VideoToASCII:
    """Convert video files to ASCII art animation."""
    
    def __init__(self, width: int = 80, charset: str = 'standard',
                 fps: int = 10):
        """Initialize video converter.
        
        Args:
            width: Width of ASCII output
            charset: Character set to use
            fps: Frames per second to extract
        """
        self.width = width
        self.charset = charset
        self.fps = fps
    
    def convert_video(self, video_path: str, output_dir: str,
                     progress_callback: Optional[Callable] = None) -> bool:
        """Convert video to ASCII art frames.
        
        Args:
            video_path: Path to input video
            output_dir: Directory for output frames
            progress_callback: Optional progress callback function
            
        Returns:
            True if successful
        """
        try:
            from PIL import Image
        except ImportError:
            print("Error: Pillow library required for video conversion")
            return False
        
        if not os.path.exists(video_path):
            print(f"Error: Video file not found: {video_path}")
            return False
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Extract frames using ffmpeg (if available)
        frames_dir = os.path.join(output_dir, 'frames_temp')
        os.makedirs(frames_dir, exist_ok=True)
        
        try:
            # Try to use ffmpeg
            self._extract_frames_ffmpeg(video_path, frames_dir)
        except Exception as e:
            print(f"FFmpeg not available or error: {e}")
            print("Attempting alternative method...")
            return self._convert_with_opencv(video_path, output_dir, progress_callback)
        
        # Convert frames to ASCII
        from generators.image_art import ImageArtGenerator
        from utils.config import Config
        
        config = Config()
        generator = ImageArtGenerator(config)
        
        # Get list of extracted frames
        frame_files = sorted([f for f in os.listdir(frames_dir) if f.endswith(('.png', '.jpg'))])
        
        print(f"Converting {len(frame_files)} frames to ASCII...")
        
        for i, frame_file in enumerate(frame_files):
            frame_path = os.path.join(frames_dir, frame_file)
            
            # Convert to ASCII
            ascii_art = generator.generate(frame_path, width=self.width, charset=self.charset)
            
            # Save ASCII frame
            output_file = os.path.join(output_dir, f"frame_{i:05d}.txt")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(ascii_art)
            
            if progress_callback:
                progress = (i + 1) / len(frame_files) * 100
                progress_callback(progress, i + 1, len(frame_files))
            
            if (i + 1) % 10 == 0:
                print(f"Processed {i + 1}/{len(frame_files)} frames")
        
        # Clean up temporary frames
        import shutil
        shutil.rmtree(frames_dir)
        
        print(f"✓ Video conversion complete! Frames saved to: {output_dir}")
        return True
    
    def _extract_frames_ffmpeg(self, video_path: str, output_dir: str):
        """Extract frames using ffmpeg.
        
        Args:
            video_path: Input video path
            output_dir: Output directory for frames
        """
        output_pattern = os.path.join(output_dir, 'frame_%05d.png')
        
        cmd = [
            'ffmpeg',
            '-i', video_path,
            '-vf', f'fps={self.fps}',
            '-q:v', '2',
            output_pattern
        ]
        
        subprocess.run(cmd, check=True, capture_output=True)
    
    def _convert_with_opencv(self, video_path: str, output_dir: str,
                            progress_callback: Optional[Callable] = None) -> bool:
        """Convert video using OpenCV (fallback method).
        
        Args:
            video_path: Input video path
            output_dir: Output directory
            progress_callback: Progress callback
            
        Returns:
            True if successful
        """
        try:
            import cv2
        except ImportError:
            print("Error: Neither ffmpeg nor OpenCV available")
            print("Please install: pip install opencv-python")
            return False
        
        from generators.image_art import ImageArtGenerator
        from utils.config import Config
        from PIL import Image
        import numpy as np
        
        config = Config()
        generator = ImageArtGenerator(config)
        
        # Open video
        cap = cv2.VideoCapture(video_path)
        
        if not cap.isOpened():
            print(f"Error: Could not open video: {video_path}")
            return False
        
        # Get video properties
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        video_fps = cap.get(cv2.CAP_PROP_FPS)
        frame_interval = max(1, int(video_fps / self.fps))
        
        print(f"Processing video: {total_frames} frames at {video_fps} FPS")
        print(f"Extracting every {frame_interval} frames ({self.fps} FPS)")
        
        frame_count = 0
        saved_count = 0
        
        while True:
            ret, frame = cap.read()
            
            if not ret:
                break
            
            # Process only at specified intervals
            if frame_count % frame_interval == 0:
                # Convert OpenCV frame to PIL Image
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                pil_image = Image.fromarray(frame_rgb)
                
                # Save temporary image
                temp_path = os.path.join(output_dir, 'temp_frame.png')
                pil_image.save(temp_path)
                
                # Convert to ASCII
                ascii_art = generator.generate(temp_path, width=self.width, charset=self.charset)
                
                # Save ASCII frame
                output_file = os.path.join(output_dir, f"frame_{saved_count:05d}.txt")
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(ascii_art)
                
                saved_count += 1
                
                if progress_callback:
                    progress = frame_count / total_frames * 100
                    progress_callback(progress, saved_count, total_frames // frame_interval)
                
                if saved_count % 10 == 0:
                    print(f"Processed {saved_count} frames")
            
            frame_count += 1
        
        cap.release()
        
        # Clean up temp file
        temp_path = os.path.join(output_dir, 'temp_frame.png')
        if os.path.exists(temp_path):
            os.remove(temp_path)
        
        print(f"✓ Extracted and converted {saved_count} frames")
        return True
    
    def play_ascii_video(self, frames_dir: str, fps: int = None, loop: bool = False):
        """Play ASCII video in terminal.
        
        Args:
            frames_dir: Directory containing ASCII frames
            fps: Playback FPS (default: use conversion FPS)
            loop: Whether to loop playback
        """
        if fps is None:
            fps = self.fps
        
        frame_delay = 1.0 / fps
        
        # Get sorted list of frame files
        frame_files = sorted([f for f in os.listdir(frames_dir) if f.endswith('.txt')])
        
        if not frame_files:
            print(f"No frames found in {frames_dir}")
            return
        
        print(f"Playing {len(frame_files)} frames at {fps} FPS")
        print("Press Ctrl+C to stop")
        
        try:
            while True:
                for frame_file in frame_files:
                    # Clear screen
                    print('\033[2J\033[H', end='')
                    
                    # Read and display frame
                    frame_path = os.path.join(frames_dir, frame_file)
                    with open(frame_path, 'r', encoding='utf-8') as f:
                        print(f.read())
                    
                    time.sleep(frame_delay)
                
                if not loop:
                    break
        
        except KeyboardInterrupt:
            print("\n\nPlayback stopped.")
    
    def create_ascii_video_file(self, frames_dir: str, output_file: str,
                                fps: int = None):
        """Create a video file from ASCII frames (requires ffmpeg).
        
        Args:
            frames_dir: Directory containing ASCII frames
            output_file: Output video file path
            fps: Frames per second
        """
        if fps is None:
            fps = self.fps
        
        print("Creating video from ASCII frames...")
        print("Note: This creates a video of the ASCII text rendered as images")
        
        # First, convert ASCII frames to images
        from exporters.formats import ImageExporter
        
        images_dir = os.path.join(frames_dir, 'images_temp')
        os.makedirs(images_dir, exist_ok=True)
        
        exporter = ImageExporter()
        frame_files = sorted([f for f in os.listdir(frames_dir) if f.endswith('.txt')])
        
        print(f"Converting {len(frame_files)} ASCII frames to images...")
        
        for i, frame_file in enumerate(frame_files):
            frame_path = os.path.join(frames_dir, frame_file)
            
            with open(frame_path, 'r', encoding='utf-8') as f:
                ascii_art = f.read()
            
            image_path = os.path.join(images_dir, f"frame_{i:05d}.png")
            exporter.export_to_png(ascii_art, image_path)
            
            if (i + 1) % 10 == 0:
                print(f"Converted {i + 1}/{len(frame_files)} frames")
        
        # Use ffmpeg to create video
        try:
            input_pattern = os.path.join(images_dir, 'frame_%05d.png')
            
            cmd = [
                'ffmpeg',
                '-framerate', str(fps),
                '-i', input_pattern,
                '-c:v', 'libx264',
                '-pix_fmt', 'yuv420p',
                '-y',  # Overwrite output file
                output_file
            ]
            
            subprocess.run(cmd, check=True)
            
            print(f"✓ Video created: {output_file}")
            
            # Clean up temporary images
            import shutil
            shutil.rmtree(images_dir)
        
        except subprocess.CalledProcessError as e:
            print(f"Error creating video: {e}")
            print("Make sure ffmpeg is installed")
        except FileNotFoundError:
            print("Error: ffmpeg not found")
            print("Install ffmpeg to create video files")

