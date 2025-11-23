# ASCII Art Generator - Plugin System Guide

## Overview

The ASCII Art Generator now supports a plugin system that allows you to extend the functionality of the tool by adding custom generators. Plugins are Python modules that inherit from the `BaseGenerator` class.

## Creating a Plugin

1. Create a new Python file in the `plugins/` directory (e.g., `my_plugin.py`).
2. Import `BaseGenerator` from `generators.base`.
3. Create a class that inherits from `BaseGenerator`.
4. Implement the `generate` method.

### Example Plugin

```python
# plugins/my_plugin.py
from generators.base import BaseGenerator

class MyPlugin(BaseGenerator):
    def __init__(self, config=None):
        super().__init__(config)
        self._name = "My Plugin"
        self._description = "A custom plugin description"
        self._author = "Your Name"
        self._version = "1.0.0"

    def generate(self, **kwargs):
        return "Hello from My Plugin!"
```

## Using Plugins

The `PluginManager` automatically discovers and loads plugins from the `plugins/` directory.

### In Python Code

```python
from utils.plugin_manager import PluginManager

# Initialize manager
manager = PluginManager()

# Discover plugins
manager.discover_plugins('plugins')

# Get plugin instance
plugin = manager.get_plugin_instance('MyPlugin')

# Generate content
if plugin:
    print(plugin.generate())
```

### Verification

Run the `demo_plugins.py` script to see all installed plugins in action:

```bash
python demo_plugins.py
```

