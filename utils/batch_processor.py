"""Batch processing utilities for multiple files and operations."""

import os
import glob
from typing import List, Callable, Dict, Any, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
import time


@dataclass
class BatchResult:
    """Result of a batch operation."""
    
    input_file: str
    output_file: str
    success: bool
    error: Optional[str] = None
    processing_time: float = 0.0


class BatchProcessor:
    """Process multiple files in batch."""
    
    def __init__(self, max_workers: int = 4):
        """Initialize batch processor.
        
        Args:
            max_workers: Maximum number of parallel workers
        """
        self.max_workers = max_workers
        self.results: List[BatchResult] = []
    
    def process_files(self, input_pattern: str, output_dir: str,
                     processor_func: Callable, **kwargs) -> List[BatchResult]:
        """Process multiple files matching a pattern.
        
        Args:
            input_pattern: Glob pattern for input files
            output_dir: Output directory
            processor_func: Function to process each file
            **kwargs: Additional arguments for processor function
            
        Returns:
            List of batch results
        """
        # Find matching files
        input_files = glob.glob(input_pattern)
        
        if not input_files:
            print(f"No files found matching pattern: {input_pattern}")
            return []
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Process files in parallel
        self.results = []
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {}
            
            for input_file in input_files:
                # Generate output filename
                basename = os.path.basename(input_file)
                name, ext = os.path.splitext(basename)
                output_file = os.path.join(output_dir, f"{name}_processed{ext}")
                
                # Submit task
                future = executor.submit(
                    self._process_single_file,
                    input_file,
                    output_file,
                    processor_func,
                    **kwargs
                )
                futures[future] = (input_file, output_file)
            
            # Collect results
            for future in as_completed(futures):
                input_file, output_file = futures[future]
                try:
                    result = future.result()
                    self.results.append(result)
                    
                    if result.success:
                        print(f"✓ Processed: {input_file} -> {output_file}")
                    else:
                        print(f"✗ Failed: {input_file} - {result.error}")
                
                except Exception as e:
                    result = BatchResult(
                        input_file=input_file,
                        output_file=output_file,
                        success=False,
                        error=str(e)
                    )
                    self.results.append(result)
                    print(f"✗ Error: {input_file} - {e}")
        
        return self.results
    
    def _process_single_file(self, input_file: str, output_file: str,
                            processor_func: Callable, **kwargs) -> BatchResult:
        """Process a single file.
        
        Args:
            input_file: Input file path
            output_file: Output file path
            processor_func: Processing function
            **kwargs: Additional arguments
            
        Returns:
            Batch result
        """
        start_time = time.time()
        
        try:
            # Call processor function
            processor_func(input_file, output_file, **kwargs)
            
            processing_time = time.time() - start_time
            
            return BatchResult(
                input_file=input_file,
                output_file=output_file,
                success=True,
                processing_time=processing_time
            )
        
        except Exception as e:
            processing_time = time.time() - start_time
            
            return BatchResult(
                input_file=input_file,
                output_file=output_file,
                success=False,
                error=str(e),
                processing_time=processing_time
            )
    
    def get_summary(self) -> Dict[str, Any]:
        """Get processing summary.
        
        Returns:
            Summary dictionary
        """
        total = len(self.results)
        successful = sum(1 for r in self.results if r.success)
        failed = total - successful
        total_time = sum(r.processing_time for r in self.results)
        avg_time = total_time / total if total > 0 else 0
        
        return {
            'total_files': total,
            'successful': successful,
            'failed': failed,
            'success_rate': (successful / total * 100) if total > 0 else 0,
            'total_time': total_time,
            'average_time': avg_time
        }
    
    def print_summary(self):
        """Print processing summary."""
        summary = self.get_summary()
        
        print("\n" + "=" * 60)
        print("BATCH PROCESSING SUMMARY")
        print("=" * 60)
        print(f"Total files:     {summary['total_files']}")
        print(f"Successful:      {summary['successful']}")
        print(f"Failed:          {summary['failed']}")
        print(f"Success rate:    {summary['success_rate']:.1f}%")
        print(f"Total time:      {summary['total_time']:.2f}s")
        print(f"Average time:    {summary['average_time']:.2f}s")
        print("=" * 60)


class BatchImageConverter:
    """Batch convert images to ASCII art."""
    
    def __init__(self, width: int = 80, charset: str = 'standard'):
        """Initialize batch image converter.
        
        Args:
            width: Output width
            charset: Character set to use
        """
        self.width = width
        self.charset = charset
    
    def convert(self, input_file: str, output_file: str, **kwargs):
        """Convert single image to ASCII.
        
        Args:
            input_file: Input image path
            output_file: Output text file path
            **kwargs: Additional arguments
        """
        from generators.image_art import ImageArtGenerator
        from utils.config import Config
        
        config = Config()
        generator = ImageArtGenerator(config)
        
        # Generate ASCII art
        ascii_art = generator.generate(input_file, width=self.width, charset=self.charset)
        
        # Save to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(ascii_art)


class BatchTextGenerator:
    """Batch generate text art from list."""
    
    def __init__(self, font: str = 'standard', effect: str = None):
        """Initialize batch text generator.
        
        Args:
            font: Font to use
            effect: Effect to apply
        """
        self.font = font
        self.effect = effect
    
    def generate_from_list(self, text_list: List[str], output_dir: str) -> List[BatchResult]:
        """Generate ASCII art for list of texts.
        
        Args:
            text_list: List of texts to convert
            output_dir: Output directory
            
        Returns:
            List of batch results
        """
        from generators.text_art import TextArtGenerator
        from generators.text_effects import TextEffects
        from utils.config import Config
        
        os.makedirs(output_dir, exist_ok=True)
        
        config = Config()
        generator = TextArtGenerator(config)
        effects = TextEffects() if self.effect else None
        
        results = []
        
        for i, text in enumerate(text_list):
            start_time = time.time()
            
            try:
                # Generate art
                art = generator.generate(text, font=self.font)
                
                # Apply effect
                if effects and self.effect:
                    if self.effect == 'shadow':
                        art = effects.add_shadow(art)
                    elif self.effect == '3d':
                        art = effects.add_3d_effect(art)
                    elif self.effect == 'outline':
                        art = effects.add_outline(art)
                
                # Save
                output_file = os.path.join(output_dir, f"text_{i:03d}_{text[:20]}.txt")
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(art)
                
                processing_time = time.time() - start_time
                
                results.append(BatchResult(
                    input_file=text,
                    output_file=output_file,
                    success=True,
                    processing_time=processing_time
                ))
                
                print(f"✓ Generated: {text}")
            
            except Exception as e:
                processing_time = time.time() - start_time
                
                results.append(BatchResult(
                    input_file=text,
                    output_file="",
                    success=False,
                    error=str(e),
                    processing_time=processing_time
                ))
                
                print(f"✗ Failed: {text} - {e}")
        
        return results


class BatchExporter:
    """Batch export ASCII art to multiple formats."""
    
    def __init__(self, formats: List[str] = None):
        """Initialize batch exporter.
        
        Args:
            formats: List of export formats
        """
        self.formats = formats or ['html', 'svg', 'markdown']
    
    def export_multiple_formats(self, ascii_art: str, base_output_path: str,
                               title: str = "ASCII Art") -> List[BatchResult]:
        """Export ASCII art to multiple formats.
        
        Args:
            ascii_art: ASCII art content
            base_output_path: Base output path (without extension)
            title: Title for exports
            
        Returns:
            List of batch results
        """
        from exporters.formats import HTMLExporter, SVGExporter, MarkdownExporter
        
        results = []
        
        for fmt in self.formats:
            start_time = time.time()
            output_file = f"{base_output_path}.{fmt}"
            
            try:
                if fmt == 'html':
                    exporter = HTMLExporter()
                    content = exporter.export(ascii_art, title=title)
                elif fmt == 'svg':
                    exporter = SVGExporter()
                    content = exporter.export(ascii_art, title=title)
                elif fmt == 'markdown':
                    exporter = MarkdownExporter()
                    content = exporter.export(ascii_art, title=title)
                else:
                    raise ValueError(f"Unknown format: {fmt}")
                
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                processing_time = time.time() - start_time
                
                results.append(BatchResult(
                    input_file=fmt,
                    output_file=output_file,
                    success=True,
                    processing_time=processing_time
                ))
                
                print(f"✓ Exported: {output_file}")
            
            except Exception as e:
                processing_time = time.time() - start_time
                
                results.append(BatchResult(
                    input_file=fmt,
                    output_file=output_file,
                    success=False,
                    error=str(e),
                    processing_time=processing_time
                ))
                
                print(f"✗ Failed: {fmt} - {e}")
        
        return results

