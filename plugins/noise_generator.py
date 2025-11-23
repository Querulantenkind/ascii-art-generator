"""Sample plugin that generates random noise."""

import random
from generators.base import BaseGenerator


class NoiseGenerator(BaseGenerator):
    """Generates ASCII noise patterns."""
    
    def __init__(self, config=None):
        super().__init__(config)
        self._name = "Static Noise"
        self._description = "Generates random static noise patterns"
        self._author = "ASCII Art Team"
        self._version = "1.0.0"
        
    def generate(self, width: int = 80, height: int = 20, density: float = 0.5, **kwargs) -> str:
        """Generate random noise.
        
        Args:
            width: Width of the output.
            height: Height of the output.
            density: Probability of a character being filled (0.0 to 1.0).
            
        Returns:
            String containing the noise pattern.
        """
        chars = self.config.get_charset('standard')
        result = []
        
        for _ in range(height):
            line = ""
            for _ in range(width):
                if random.random() < density:
                    line += random.choice(chars)
                else:
                    line += " "
            result.append(line)
            
        return "\n".join(result)

