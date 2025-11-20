"""Template management system for pre-made ASCII art designs."""

import json
import os
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict


@dataclass
class Template:
    """Represents an ASCII art template."""
    
    name: str
    category: str
    content: str
    description: str
    author: str = "ASCII Art Generator"
    tags: List[str] = None
    variables: Dict[str, str] = None
    
    def __post_init__(self):
        """Initialize default values."""
        if self.tags is None:
            self.tags = []
        if self.variables is None:
            self.variables = {}
    
    def render(self, **kwargs) -> str:
        """Render template with variables.
        
        Args:
            **kwargs: Variable values to substitute
            
        Returns:
            Rendered template
        """
        result = self.content
        
        # Substitute variables
        for key, value in kwargs.items():
            placeholder = f"{{{key}}}"
            if placeholder in result:
                result = result.replace(placeholder, str(value))
        
        # Fill remaining variables with defaults
        for key, default_value in self.variables.items():
            placeholder = f"{{{key}}}"
            if placeholder in result:
                result = result.replace(placeholder, default_value)
        
        return result


class TemplateManager:
    """Manage ASCII art templates."""
    
    def __init__(self, template_dir: str = None):
        """Initialize template manager.
        
        Args:
            template_dir: Directory containing templates
        """
        self.template_dir = template_dir or self._get_default_template_dir()
        self.templates: Dict[str, Template] = {}
        self._load_builtin_templates()
        self._load_custom_templates()
    
    def _get_default_template_dir(self) -> str:
        """Get default template directory.
        
        Returns:
            Path to template directory
        """
        return os.path.join(os.path.dirname(__file__), 'library')
    
    def _load_builtin_templates(self):
        """Load built-in templates."""
        
        # Banners
        self.templates['welcome_banner'] = Template(
            name='welcome_banner',
            category='banners',
            content='''
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║                     {title}                                   ║
║                                                               ║
║                     {subtitle}                                ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
'''.strip(),
            description='Welcome banner with title and subtitle',
            tags=['banner', 'welcome', 'header'],
            variables={'title': 'WELCOME', 'subtitle': 'to ASCII Art'}
        )
        
        self.templates['simple_banner'] = Template(
            name='simple_banner',
            category='banners',
            content='''
┌─────────────────────────────────────────────────────────────┐
│  {text}                                                      │
└─────────────────────────────────────────────────────────────┘
'''.strip(),
            description='Simple single-line banner',
            tags=['banner', 'simple'],
            variables={'text': 'Your text here'}
        )
        
        # Frames
        self.templates['photo_frame'] = Template(
            name='photo_frame',
            category='frames',
            content='''
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║  {content}                                                    ║
║                                                               ║
║  Caption: {caption}                                           ║
╚═══════════════════════════════════════════════════════════════╝
'''.strip(),
            description='Frame for ASCII art with caption',
            tags=['frame', 'photo', 'caption'],
            variables={'content': '[ASCII Art Here]', 'caption': 'My Art'}
        )
        
        # Dividers
        self.templates['section_divider'] = Template(
            name='section_divider',
            category='dividers',
            content='''
════════════════════════════════════════════════════════════════
                          {section_name}
════════════════════════════════════════════════════════════════
'''.strip(),
            description='Section divider with name',
            tags=['divider', 'section'],
            variables={'section_name': 'SECTION'}
        )
        
        # Headers
        self.templates['readme_header'] = Template(
            name='readme_header',
            category='headers',
            content='''
# {project_name}

> {tagline}

[![Version](https://img.shields.io/badge/version-{version}-blue.svg)]()
[![License](https://img.shields.io/badge/license-{license}-green.svg)]()

## Description

{description}
'''.strip(),
            description='README header template',
            tags=['readme', 'header', 'markdown'],
            variables={
                'project_name': 'My Project',
                'tagline': 'A cool project',
                'version': '1.0.0',
                'license': 'MIT',
                'description': 'Project description here'
            }
        )
        
        # Loading screens
        self.templates['loading_screen'] = Template(
            name='loading_screen',
            category='loading',
            content='''
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║                      {app_name}                               ║
║                                                               ║
║                      Loading...                               ║
║                      [{progress}]                             ║
║                                                               ║
║                      {status}                                 ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
'''.strip(),
            description='Loading screen template',
            tags=['loading', 'progress', 'screen'],
            variables={
                'app_name': 'Application',
                'progress': '████████░░░░░░░░░░░░',
                'status': 'Initializing...'
            }
        )
        
        # Menus
        self.templates['menu'] = Template(
            name='menu',
            category='menus',
            content='''
┌─────────────────────────────────────────────────────────────┐
│                         {title}                              │
├─────────────────────────────────────────────────────────────┤
│  {option1}                                                   │
│  {option2}                                                   │
│  {option3}                                                   │
│  {option4}                                                   │
│  0. Exit                                                     │
└─────────────────────────────────────────────────────────────┘
'''.strip(),
            description='Menu template',
            tags=['menu', 'interface'],
            variables={
                'title': 'MAIN MENU',
                'option1': '1. Option One',
                'option2': '2. Option Two',
                'option3': '3. Option Three',
                'option4': '4. Option Four'
            }
        )
        
        # Status boxes
        self.templates['status_box'] = Template(
            name='status_box',
            category='status',
            content='''
┌─────────────────────────────────────────────────────────────┐
│ Status: {status}                                             │
│ Time: {time}                                                 │
│ User: {user}                                                 │
│ Message: {message}                                           │
└─────────────────────────────────────────────────────────────┘
'''.strip(),
            description='Status information box',
            tags=['status', 'info', 'box'],
            variables={
                'status': 'Active',
                'time': '00:00:00',
                'user': 'Guest',
                'message': 'System ready'
            }
        )
        
        # Code blocks
        self.templates['code_block'] = Template(
            name='code_block',
            category='code',
            content='''
┌─ {filename} ─────────────────────────────────────────────────┐
│                                                               │
│  {code}                                                       │
│                                                               │
└───────────────────────────────────────────────────────────────┘
'''.strip(),
            description='Code block with filename',
            tags=['code', 'block', 'file'],
            variables={
                'filename': 'example.py',
                'code': 'print("Hello, World!")'
            }
        )
        
        # Quotes
        self.templates['quote_box'] = Template(
            name='quote_box',
            category='quotes',
            content='''
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║  "{quote}"                                                    ║
║                                                               ║
║                                          - {author}           ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
'''.strip(),
            description='Quote box with author',
            tags=['quote', 'citation'],
            variables={
                'quote': 'Your quote here',
                'author': 'Author Name'
            }
        )
        
        # Alerts
        self.templates['alert_success'] = Template(
            name='alert_success',
            category='alerts',
            content='''
┌─────────────────────────────────────────────────────────────┐
│ ✓ SUCCESS                                                    │
│                                                              │
│   {message}                                                  │
└─────────────────────────────────────────────────────────────┘
'''.strip(),
            description='Success alert',
            tags=['alert', 'success', 'notification'],
            variables={'message': 'Operation completed successfully!'}
        )
        
        self.templates['alert_error'] = Template(
            name='alert_error',
            category='alerts',
            content='''
┌─────────────────────────────────────────────────────────────┐
│ ✗ ERROR                                                      │
│                                                              │
│   {message}                                                  │
└─────────────────────────────────────────────────────────────┘
'''.strip(),
            description='Error alert',
            tags=['alert', 'error', 'notification'],
            variables={'message': 'An error occurred!'}
        )
        
        # Tables
        self.templates['data_table'] = Template(
            name='data_table',
            category='tables',
            content='''
┌─────────────┬─────────────┬─────────────┬─────────────┐
│ {col1}      │ {col2}      │ {col3}      │ {col4}      │
├─────────────┼─────────────┼─────────────┼─────────────┤
│ {row1_c1}   │ {row1_c2}   │ {row1_c3}   │ {row1_c4}   │
│ {row2_c1}   │ {row2_c2}   │ {row2_c3}   │ {row2_c4}   │
│ {row3_c1}   │ {row3_c2}   │ {row3_c3}   │ {row3_c4}   │
└─────────────┴─────────────┴─────────────┴─────────────┘
'''.strip(),
            description='Data table with 4 columns',
            tags=['table', 'data', 'grid'],
            variables={
                'col1': 'Column 1', 'col2': 'Column 2', 'col3': 'Column 3', 'col4': 'Column 4',
                'row1_c1': 'Data', 'row1_c2': 'Data', 'row1_c3': 'Data', 'row1_c4': 'Data',
                'row2_c1': 'Data', 'row2_c2': 'Data', 'row2_c3': 'Data', 'row2_c4': 'Data',
                'row3_c1': 'Data', 'row3_c2': 'Data', 'row3_c3': 'Data', 'row3_c4': 'Data',
            }
        )
    
    def _load_custom_templates(self):
        """Load custom templates from directory."""
        if not os.path.exists(self.template_dir):
            return
        
        for filename in os.listdir(self.template_dir):
            if filename.endswith('.json'):
                filepath = os.path.join(self.template_dir, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        template = Template(**data)
                        self.templates[template.name] = template
                except Exception as e:
                    print(f"Error loading template {filename}: {e}")
    
    def get_template(self, name: str) -> Optional[Template]:
        """Get template by name.
        
        Args:
            name: Template name
            
        Returns:
            Template or None
        """
        return self.templates.get(name)
    
    def list_templates(self, category: str = None) -> List[Template]:
        """List available templates.
        
        Args:
            category: Filter by category (optional)
            
        Returns:
            List of templates
        """
        templates = list(self.templates.values())
        
        if category:
            templates = [t for t in templates if t.category == category]
        
        return templates
    
    def list_categories(self) -> List[str]:
        """Get list of template categories.
        
        Returns:
            List of category names
        """
        categories = set(t.category for t in self.templates.values())
        return sorted(categories)
    
    def search_templates(self, query: str) -> List[Template]:
        """Search templates by name, description, or tags.
        
        Args:
            query: Search query
            
        Returns:
            List of matching templates
        """
        query = query.lower()
        results = []
        
        for template in self.templates.values():
            if (query in template.name.lower() or
                query in template.description.lower() or
                any(query in tag.lower() for tag in template.tags)):
                results.append(template)
        
        return results
    
    def save_template(self, template: Template, filename: str = None):
        """Save template to file.
        
        Args:
            template: Template to save
            filename: Output filename (optional)
        """
        if filename is None:
            filename = f"{template.name}.json"
        
        os.makedirs(self.template_dir, exist_ok=True)
        filepath = os.path.join(self.template_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(asdict(template), f, indent=2)
    
    def create_template(self, name: str, category: str, content: str,
                       description: str, **kwargs) -> Template:
        """Create a new template.
        
        Args:
            name: Template name
            category: Category
            content: Template content
            description: Description
            **kwargs: Additional template attributes
            
        Returns:
            Created template
        """
        template = Template(
            name=name,
            category=category,
            content=content,
            description=description,
            **kwargs
        )
        
        self.templates[name] = template
        return template

