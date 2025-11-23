"""Plugin manager for dynamically loading and accessing generators."""

import os
import importlib.util
import inspect
import sys
from typing import Dict, Type, List, Optional
from generators.base import BaseGenerator


class PluginManager:
    """Manages the discovery and registration of ASCII art generator plugins."""
    
    def __init__(self):
        """Initialize the plugin manager."""
        self._plugins: Dict[str, Type[BaseGenerator]] = {}
        self._loaded_modules = []

    def discover_plugins(self, directory: str) -> List[str]:
        """Discover and load plugins from a directory.
        
        Args:
            directory: Path to the directory containing plugins.
            
        Returns:
            List of names of discovered plugins.
        """
        if not os.path.isdir(directory):
            print(f"Warning: Plugin directory '{directory}' not found.")
            return []
            
        discovered = []
        
        # Add directory to sys.path to allow imports if needed
        if directory not in sys.path:
            sys.path.append(directory)

        for filename in os.listdir(directory):
            if filename.endswith(".py") and not filename.startswith("__"):
                plugin_path = os.path.join(directory, filename)
                module_name = filename[:-3]
                
                try:
                    self._load_plugin_from_file(plugin_path, module_name)
                    discovered.append(module_name)
                except Exception as e:
                    print(f"Error loading plugin '{filename}': {e}")
                    
        return discovered

    def _load_plugin_from_file(self, path: str, module_name: str):
        """Load a plugin module from a file path.
        
        Args:
            path: Full path to the python file.
            module_name: Name to give the module.
        """
        spec = importlib.util.spec_from_file_location(module_name, path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
            self._loaded_modules.append(module)
            
            # Find classes inheriting from BaseGenerator
            for name, obj in inspect.getmembers(module):
                if (inspect.isclass(obj) and 
                    issubclass(obj, BaseGenerator) and 
                    obj is not BaseGenerator):
                    
                    # Instantiate to get the name property if possible, 
                    # or just use the class name if we want to be lazy.
                    # But better to just register the class.
                    # We can use the class name as the default key.
                    
                    # Check if the class has a default name in __init__? 
                    # We can't easily instantiate without config.
                    # Let's verify it has the required structure.
                    
                    self.register_plugin(name, obj)

    def register_plugin(self, name: str, plugin_class: Type[BaseGenerator]):
        """Register a plugin class.
        
        Args:
            name: Identifier for the plugin.
            plugin_class: The class of the plugin.
        """
        self._plugins[name] = plugin_class
        # print(f"Registered plugin: {name}")

    def get_plugin(self, name: str) -> Optional[Type[BaseGenerator]]:
        """Get a plugin class by name.
        
        Args:
            name: Plugin identifier.
            
        Returns:
            Plugin class or None if not found.
        """
        return self._plugins.get(name)

    def list_plugins(self) -> List[str]:
        """List all registered plugins.
        
        Returns:
            List of plugin names.
        """
        return list(self._plugins.keys())

    def get_plugin_instance(self, name: str, config=None) -> Optional[BaseGenerator]:
        """Get an instance of a plugin.
        
        Args:
            name: Plugin identifier.
            config: Configuration object passed to constructor.
            
        Returns:
            Instance of the plugin or None.
        """
        plugin_class = self.get_plugin(name)
        if plugin_class:
            return plugin_class(config)
        return None

