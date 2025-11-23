#!/usr/bin/env python3
"""
Demo script for the Plugin System.
Shows how to load and use dynamic plugins.
"""

import os
import sys
from utils.plugin_manager import PluginManager
from utils.config import Config


def main():
    print("ASCII Art Generator - Plugin System Demo")
    print("========================================")
    
    # Initialize components
    config = Config()
    manager = PluginManager()
    
    # Path to plugins directory
    plugins_dir = os.path.join(os.path.dirname(__file__), 'plugins')
    
    # Discover plugins
    print(f"\nScanning for plugins in: {plugins_dir}")
    discovered = manager.discover_plugins(plugins_dir)
    print(f"Found {len(discovered)} plugin modules: {', '.join(discovered)}")
    
    # List registered plugins
    registered = manager.list_plugins()
    print(f"Registered plugins: {', '.join(registered)}")
    
    # Use the 'NoiseGenerator' plugin
    plugin_name = 'NoiseGenerator'
    if plugin_name in registered:
        print(f"\nLoading plugin: {plugin_name}...")
        generator = manager.get_plugin_instance(plugin_name, config)
        
        if generator:
            print(f"Plugin Info: {generator.name} v{generator.version} by {generator.author}")
            print(f"Description: {generator.description}")
            
            print("\nGenerating Art (80x10, density=0.3):")
            print("-" * 80)
            art = generator.generate(width=80, height=10, density=0.3)
            print(art)
            print("-" * 80)
        else:
            print("Failed to instantiate plugin.")
    else:
        print(f"Plugin '{plugin_name}' not found.")
        
    print("\nDemo complete.")


if __name__ == "__main__":
    main()

