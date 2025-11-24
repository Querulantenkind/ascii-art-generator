"""ASCII diagram generators for flowcharts, UML, and network diagrams."""

from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class Node:
    """Represents a node in a diagram."""
    id: str
    label: str
    type: str  # 'process', 'decision', 'start', 'end', 'data'
    x: int = 0
    y: int = 0


@dataclass
class Edge:
    """Represents an edge/connection in a diagram."""
    from_node: str
    to_node: str
    label: str = ""


class FlowchartGenerator:
    """Generate flowchart diagrams in ASCII."""
    
    def __init__(self):
        """Initialize flowchart generator."""
        self.nodes: Dict[str, Node] = {}
        self.edges: List[Edge] = []
        self.box_chars = {
            'tl': '┌', 'tr': '┐', 'bl': '└', 'br': '┘',
            'h': '─', 'v': '│'
        }
    
    def add_node(self, node_id: str, label: str, node_type: str = 'process'):
        """Add a node to the flowchart.
        
        Args:
            node_id: Unique node identifier
            label: Node label text
            node_type: Type of node
        """
        self.nodes[node_id] = Node(node_id, label, node_type)
    
    def add_edge(self, from_node: str, to_node: str, label: str = ""):
        """Add an edge between nodes.
        
        Args:
            from_node: Source node ID
            to_node: Target node ID
            label: Edge label (optional)
        """
        self.edges.append(Edge(from_node, to_node, label))
    
    def generate(self) -> str:
        """Generate the flowchart.
        
        Returns:
            ASCII flowchart
        """
        if not self.nodes:
            return "Empty flowchart"
        
        # Auto-layout nodes
        self._auto_layout()
        
        # Create canvas
        max_x = max(node.x for node in self.nodes.values()) + 20
        max_y = max(node.y for node in self.nodes.values()) + 10
        
        canvas = [[' ' for _ in range(max_x)] for _ in range(max_y)]
        
        # Draw edges first
        for edge in self.edges:
            self._draw_edge(canvas, edge)
        
        # Draw nodes on top
        for node in self.nodes.values():
            self._draw_node(canvas, node)
        
        # Convert to string
        return '\n'.join([''.join(row).rstrip() for row in canvas])
    
    def _auto_layout(self):
        """Automatically layout nodes."""
        # Simple vertical layout
        y = 0
        for node in self.nodes.values():
            node.x = 20
            node.y = y
            y += 5
    
    def _draw_node(self, canvas: List[List[str]], node: Node):
        """Draw a node on the canvas.
        
        Args:
            canvas: Canvas to draw on
            node: Node to draw
        """
        label = node.label
        width = len(label) + 4
        
        if node.type == 'start' or node.type == 'end':
            # Rounded box
            self._draw_rounded_box(canvas, node.x, node.y, width, 3, label)
        elif node.type == 'decision':
            # Diamond
            self._draw_diamond(canvas, node.x, node.y, label)
        else:
            # Rectangle
            self._draw_rectangle(canvas, node.x, node.y, width, 3, label)
    
    def _draw_rectangle(self, canvas: List[List[str]], x: int, y: int,
                       width: int, height: int, label: str):
        """Draw a rectangle.
        
        Args:
            canvas: Canvas to draw on
            x, y: Top-left position
            width, height: Dimensions
            label: Text label
        """
        # Top border
        self._put_char(canvas, x, y, self.box_chars['tl'])
        for i in range(1, width - 1):
            self._put_char(canvas, x + i, y, self.box_chars['h'])
        self._put_char(canvas, x + width - 1, y, self.box_chars['tr'])
        
        # Middle (with label)
        for j in range(1, height - 1):
            self._put_char(canvas, x, y + j, self.box_chars['v'])
            if j == height // 2:
                # Center label
                label_x = x + (width - len(label)) // 2
                for i, char in enumerate(label):
                    self._put_char(canvas, label_x + i, y + j, char)
            self._put_char(canvas, x + width - 1, y + j, self.box_chars['v'])
        
        # Bottom border
        self._put_char(canvas, x, y + height - 1, self.box_chars['bl'])
        for i in range(1, width - 1):
            self._put_char(canvas, x + i, y + height - 1, self.box_chars['h'])
        self._put_char(canvas, x + width - 1, y + height - 1, self.box_chars['br'])
    
    def _draw_rounded_box(self, canvas: List[List[str]], x: int, y: int,
                         width: int, height: int, label: str):
        """Draw a rounded box (for start/end).
        
        Args:
            canvas: Canvas to draw on
            x, y: Position
            width, height: Dimensions
            label: Text label
        """
        # Use parentheses for rounded effect
        self._put_char(canvas, x, y, '(')
        for i in range(1, width - 1):
            self._put_char(canvas, x + i, y, '─')
        self._put_char(canvas, x + width - 1, y, ')')
        
        for j in range(1, height - 1):
            self._put_char(canvas, x, y + j, '(')
            if j == height // 2:
                label_x = x + (width - len(label)) // 2
                for i, char in enumerate(label):
                    self._put_char(canvas, label_x + i, y + j, char)
            self._put_char(canvas, x + width - 1, y + j, ')')
        
        self._put_char(canvas, x, y + height - 1, '(')
        for i in range(1, width - 1):
            self._put_char(canvas, x + i, y + height - 1, '─')
        self._put_char(canvas, x + width - 1, y + height - 1, ')')
    
    def _draw_diamond(self, canvas: List[List[str]], x: int, y: int, label: str):
        """Draw a diamond shape (for decisions).
        
        Args:
            canvas: Canvas to draw on
            x, y: Center position
            label: Text label
        """
        size = max(len(label) // 2 + 2, 3)
        
        # Top half
        for i in range(size):
            self._put_char(canvas, x - i, y + i, '/')
            self._put_char(canvas, x + i, y + i, '\\')
        
        # Bottom half
        for i in range(size):
            self._put_char(canvas, x - size + i + 1, y + size + i, '\\')
            self._put_char(canvas, x + size - i - 1, y + size + i, '/')
        
        # Label in center
        label_y = y + size
        label_x = x - len(label) // 2
        for i, char in enumerate(label):
            self._put_char(canvas, label_x + i, label_y, char)
    
    def _draw_edge(self, canvas: List[List[str]], edge: Edge):
        """Draw an edge between nodes.
        
        Args:
            canvas: Canvas to draw on
            edge: Edge to draw
        """
        from_node = self.nodes.get(edge.from_node)
        to_node = self.nodes.get(edge.to_node)
        
        if not from_node or not to_node:
            return
        
        # Simple vertical line
        start_y = from_node.y + 3
        end_y = to_node.y
        x = from_node.x + 10
        
        for y in range(start_y, end_y):
            self._put_char(canvas, x, y, '│')
        
        # Arrow
        self._put_char(canvas, x, end_y - 1, '▼')
    
    def _put_char(self, canvas: List[List[str]], x: int, y: int, char: str):
        """Put a character on the canvas.
        
        Args:
            canvas: Canvas
            x, y: Position
            char: Character to place
        """
        if 0 <= y < len(canvas) and 0 <= x < len(canvas[0]):
            canvas[y][x] = char
    
    def from_description(self, description: str) -> str:
        """Generate flowchart from text description.
        
        Args:
            description: Text description of flowchart
            
        Returns:
            ASCII flowchart
        """
        # Simple parser for format: "A -> B -> C"
        lines = description.strip().split('\n')
        
        for line in lines:
            if '->' in line:
                parts = [p.strip() for p in line.split('->')]
                for i, part in enumerate(parts):
                    node_id = f"node_{i}"
                    node_type = 'start' if i == 0 else 'end' if i == len(parts) - 1 else 'process'
                    
                    if '?' in part:
                        node_type = 'decision'
                        part = part.replace('?', '')
                    
                    self.add_node(node_id, part, node_type)
                    
                    if i > 0:
                        self.add_edge(f"node_{i-1}", node_id)
        
        return self.generate()


class UMLGenerator:
    """Generate UML diagrams in ASCII."""
    
    def __init__(self):
        """Initialize UML generator."""
        pass
    
    def class_diagram(self, classes: Dict[str, Dict]) -> str:
        """Generate UML class diagram.
        
        Args:
            classes: Dictionary of class definitions
            
        Returns:
            ASCII UML diagram
        """
        result = []
        
        for class_name, definition in classes.items():
            box = self._create_class_box(
                class_name,
                definition.get('attributes', []),
                definition.get('methods', [])
            )
            result.append(box)
            
            # Show inheritance
            if 'inherits' in definition:
                parent = definition['inherits']
                result.append(f"       │")
                result.append(f"       ▲")
                result.append(f"       │")
                result.append(f"  (inherits from {parent})")
            
            result.append("")
        
        return '\n'.join(result)
    
    def _create_class_box(self, name: str, attributes: List[str],
                         methods: List[str]) -> str:
        """Create a class box.
        
        Args:
            name: Class name
            attributes: List of attributes
            methods: List of methods
            
        Returns:
            ASCII class box
        """
        width = max(
            len(name) + 4,
            max([len(a) for a in attributes] + [0]) + 4,
            max([len(m) for m in methods] + [0]) + 4,
            20
        )
        
        lines = []
        
        # Top border
        lines.append('┌' + '─' * (width - 2) + '┐')
        
        # Class name
        lines.append('│ ' + name.center(width - 4) + ' │')
        
        # Separator
        lines.append('├' + '─' * (width - 2) + '┤')
        
        # Attributes
        for attr in attributes:
            lines.append('│ ' + attr.ljust(width - 4) + ' │')
        
        # Separator
        lines.append('├' + '─' * (width - 2) + '┤')
        
        # Methods
        for method in methods:
            lines.append('│ ' + method.ljust(width - 4) + ' │')
        
        # Bottom border
        lines.append('└' + '─' * (width - 2) + '┘')
        
        return '\n'.join(lines)


class NetworkDiagram:
    """Generate network topology diagrams."""
    
    def __init__(self):
        """Initialize network diagram generator."""
        self.device_icons = {
            'router': '╔═══╗\n║ R ║\n╚═══╝',
            'switch': '┌───┐\n│ S │\n└───┘',
            'server': '┌───┐\n│▓▓▓│\n└───┘',
            'pc': '┌─┐\n│█│\n└─┘',
            'cloud': ' ☁ '
        }
    
    def generate(self, topology: Dict[str, Dict]) -> str:
        """Generate network topology diagram.
        
        Args:
            topology: Network topology definition
            
        Returns:
            ASCII network diagram
        """
        result = []
        
        for device, config in topology.items():
            device_type = config.get('type', 'pc')
            icon = self.device_icons.get(device_type, '[ ]')
            
            result.append(f"{device}:")
            result.append(icon)
            
            if 'connects_to' in config:
                for connection in config['connects_to']:
                    result.append(f"  │")
                    result.append(f"  ├──> {connection}")
            
            result.append("")
        
        return '\n'.join(result)


class SequenceDiagram:
    """Generate UML sequence diagrams."""
    
    def __init__(self):
        """Initialize sequence diagram generator."""
        pass
    
    def generate(self, actors: List[str], interactions: List[Tuple[str, str, str]]) -> str:
        """Generate sequence diagram.
        
        Args:
            actors: List of actors/objects
            interactions: List of (from, to, message) tuples
            
        Returns:
            ASCII sequence diagram
        """
        # Calculate positions
        spacing = 20
        positions = {actor: i * spacing for i, actor in enumerate(actors)}
        
        result = []
        
        # Actor headers
        header = ""
        for actor in actors:
            pos = positions[actor]
            header += " " * (pos - len(header)) + actor
        result.append(header)
        
        # Lifelines
        lifeline = ""
        for actor in actors:
            pos = positions[actor] + len(actor) // 2
            lifeline += " " * (pos - len(lifeline)) + "│"
        
        # Interactions
        for from_actor, to_actor, message in interactions:
            result.append(lifeline)
            
            from_pos = positions[from_actor] + len(from_actor) // 2
            to_pos = positions[to_actor] + len(to_actor) // 2
            
            # Draw arrow
            arrow_line = " " * min(from_pos, to_pos)
            arrow_length = abs(to_pos - from_pos)
            
            if from_pos < to_pos:
                arrow_line += "─" * arrow_length + ">"
            else:
                arrow_line += "<" + "─" * arrow_length
            
            result.append(arrow_line)
            
            # Message label
            msg_pos = (from_pos + to_pos) // 2 - len(message) // 2
            msg_line = " " * msg_pos + message
            result.append(msg_line)
        
        result.append(lifeline)
        
        return '\n'.join(result)


class GanttChartGenerator:
    """Generate Gantt charts for project management."""
    
    def __init__(self):
        """Initialize Gantt chart generator."""
        self.tasks = []
    
    def add_task(self, name: str, start_day: int, duration: int, 
                 progress: int = 0, dependencies: Optional[List[str]] = None):
        """Add a task to the Gantt chart.
        
        Args:
            name: Task name
            start_day: Start day (0-indexed)
            duration: Duration in days
            progress: Progress percentage (0-100)
            dependencies: List of task names this depends on
        """
        self.tasks.append({
            'name': name,
            'start': start_day,
            'duration': duration,
            'progress': progress,
            'dependencies': dependencies or []
        })
    
    def generate(self, width: int = 80, show_progress: bool = True) -> str:
        """Generate Gantt chart.
        
        Args:
            width: Width of the chart
            show_progress: Whether to show progress percentages
            
        Returns:
            ASCII Gantt chart
        """
        if not self.tasks:
            return "No tasks defined"
        
        # Calculate timeline
        max_end = max(task['start'] + task['duration'] for task in self.tasks)
        
        # Calculate column widths
        max_name_len = max(len(task['name']) for task in self.tasks)
        name_col_width = min(max_name_len + 2, 25)
        
        # Progress column
        progress_col_width = 8 if show_progress else 0
        
        # Timeline width
        timeline_width = width - name_col_width - progress_col_width - 5
        days_per_char = max(1, max_end / timeline_width)
        
        result = []
        
        # Header
        result.append("=" * width)
        result.append("Gantt Chart".center(width))
        result.append("=" * width)
        result.append("")
        
        # Timeline header
        header_line = " " * name_col_width + "│"
        if show_progress:
            header_line += " Prog. │"
        
        # Day markers
        timeline_header = ""
        for day in range(0, max_end + 1, max(1, int(days_per_char * 5))):
            pos = int(day / days_per_char)
            if pos < timeline_width:
                label = f"D{day}"
                timeline_header += label + " " * (5 - len(label))
        
        header_line += " " + timeline_header[:timeline_width]
        result.append(header_line)
        
        # Separator
        sep = "─" * name_col_width + "┼"
        if show_progress:
            sep += "───────┼"
        sep += "─" * timeline_width
        result.append(sep)
        
        # Tasks
        for task in self.tasks:
            # Task name
            task_name = task['name'][:name_col_width-1].ljust(name_col_width-1)
            line = task_name + " │"
            
            # Progress
            if show_progress:
                progress_str = f"{task['progress']:3d}%"
                line += f" {progress_str} │"
            
            # Timeline bar
            start_pos = int(task['start'] / days_per_char)
            bar_length = max(1, int(task['duration'] / days_per_char))
            
            timeline = " " * timeline_width
            timeline_list = list(timeline)
            
            # Draw bar
            progress_chars = int(bar_length * task['progress'] / 100)
            for i in range(bar_length):
                pos = start_pos + i
                if 0 <= pos < timeline_width:
                    if i < progress_chars:
                        timeline_list[pos] = '█'
                    else:
                        timeline_list[pos] = '░'
            
            # Add milestone marker at end if 100% complete
            if task['progress'] == 100 and start_pos + bar_length < timeline_width:
                timeline_list[start_pos + bar_length] = '◆'
            
            line += " " + ''.join(timeline_list)
            result.append(line)
        
        result.append("=" * width)
        
        # Legend
        result.append("")
        result.append("Legend: █ Complete  ░ Remaining  ◆ Milestone")
        
        return '\n'.join(result)


class ERDGenerator:
    """Generate Entity Relationship Diagrams for database schemas."""
    
    def __init__(self):
        """Initialize ERD generator."""
        self.entities = {}
        self.relationships = []
    
    def add_entity(self, name: str, attributes: List[Dict[str, str]]):
        """Add an entity (table) to the diagram.
        
        Args:
            name: Entity name
            attributes: List of attribute dicts with 'name', 'type', and optional 'key' (PK/FK)
        """
        self.entities[name] = attributes
    
    def add_relationship(self, from_entity: str, to_entity: str, 
                        relationship_type: str, label: str = ""):
        """Add a relationship between entities.
        
        Args:
            from_entity: Source entity name
            to_entity: Target entity name
            relationship_type: Type ('1:1', '1:N', 'N:M')
            label: Optional relationship label
        """
        self.relationships.append({
            'from': from_entity,
            'to': to_entity,
            'type': relationship_type,
            'label': label
        })
    
    def generate(self) -> str:
        """Generate ERD diagram.
        
        Returns:
            ASCII ERD diagram
        """
        if not self.entities:
            return "No entities defined"
        
        result = []
        
        # Title
        result.append("=" * 80)
        result.append("Entity Relationship Diagram".center(80))
        result.append("=" * 80)
        result.append("")
        
        # Draw each entity
        for entity_name, attributes in self.entities.items():
            entity_box = self._draw_entity(entity_name, attributes)
            result.append(entity_box)
            result.append("")
            
            # Show relationships for this entity
            entity_rels = [r for r in self.relationships if r['from'] == entity_name]
            for rel in entity_rels:
                rel_line = self._draw_relationship(rel)
                result.append(rel_line)
                result.append("")
        
        # Legend
        result.append("=" * 80)
        result.append("Legend:")
        result.append("  PK = Primary Key")
        result.append("  FK = Foreign Key")
        result.append("  1:1 = One-to-One")
        result.append("  1:N = One-to-Many")
        result.append("  N:M = Many-to-Many")
        
        return '\n'.join(result)
    
    def _draw_entity(self, name: str, attributes: List[Dict[str, str]]) -> str:
        """Draw an entity box.
        
        Args:
            name: Entity name
            attributes: List of attributes
            
        Returns:
            ASCII entity box
        """
        # Calculate width
        max_attr_len = max(
            len(f"{attr.get('key', ''):3s} {attr['name']} : {attr['type']}")
            for attr in attributes
        )
        width = max(len(name) + 4, max_attr_len + 4, 30)
        
        lines = []
        
        # Top border
        lines.append('┌' + '─' * (width - 2) + '┐')
        
        # Entity name (centered, bold)
        lines.append('│ ' + name.upper().center(width - 4) + ' │')
        
        # Separator
        lines.append('├' + '─' * (width - 2) + '┤')
        
        # Attributes
        for attr in attributes:
            key_marker = attr.get('key', '')
            if key_marker:
                key_marker = f"[{key_marker}]".ljust(5)
            else:
                key_marker = "     "
            
            attr_line = f"{key_marker}{attr['name']} : {attr['type']}"
            lines.append('│ ' + attr_line.ljust(width - 4) + ' │')
        
        # Bottom border
        lines.append('└' + '─' * (width - 2) + '┘')
        
        return '\n'.join(lines)
    
    def _draw_relationship(self, relationship: Dict) -> str:
        """Draw a relationship line.
        
        Args:
            relationship: Relationship dictionary
            
        Returns:
            ASCII relationship representation
        """
        from_entity = relationship['from']
        to_entity = relationship['to']
        rel_type = relationship['type']
        label = relationship['label']
        
        # Simple text representation
        arrow = {
            '1:1': '───────',
            '1:N': '──────>',
            'N:M': '<─────>'
        }.get(rel_type, '───────')
        
        rel_str = f"  {from_entity} {arrow} {to_entity}"
        if label:
            rel_str += f"  ({label})"
        rel_str += f"  [{rel_type}]"
        
        return rel_str

