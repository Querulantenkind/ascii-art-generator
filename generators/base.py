"""Base class for ASCII art generators."""

from abc import ABC, abstractmethod
from typing import Optional, Any
from utils.config import Config


class BaseGenerator(ABC):
    """Abstract base class for all ASCII art generators.
    
    All plugins must inherit from this class and implement the generate method.
    """
    
    def __init__(self, config: Optional[Config] = None):
        """Initialize the generator.
        
        Args:
            config: Configuration object. If None, a default Config is created.
        """
        self.config = config or Config()
        self._name = "Base Generator"
        self._description = "Base class for generators"
        self._version = "1.0.0"
        self._author = "Unknown"

    @property
    def name(self) -> str:
        """Get the name of the generator."""
        return self._name

    @property
    def description(self) -> str:
        """Get the description of the generator."""
        return self._description
    
    @property
    def version(self) -> str:
        """Get the version of the generator."""
        return self._version
        
    @property
    def author(self) -> str:
        """Get the author of the generator."""
        return self._author

    @abstractmethod
    def generate(self, **kwargs) -> Any:
        """Generate ASCII art.
        
        Args:
            **kwargs: Arbitrary keyword arguments specific to the generator.
            
        Returns:
            Generated ASCII art (usually a string).
        """
        pass

