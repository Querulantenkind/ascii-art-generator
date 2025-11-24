#!/usr/bin/env python3
"""
Demo script for Enhanced Diagram Generators.
Showcases Gantt Charts and Entity Relationship Diagrams (ERD).
"""

from generators.diagrams import GanttChartGenerator, ERDGenerator


def demo_gantt_chart():
    """Demonstrate Gantt chart generation."""
    print("\n" + "=" * 80)
    print("GANTT CHART DEMO - Software Development Project")
    print("=" * 80 + "\n")
    
    gantt = GanttChartGenerator()
    
    # Add tasks for a software project
    gantt.add_task("Requirements Analysis", start_day=0, duration=5, progress=100)
    gantt.add_task("System Design", start_day=5, duration=7, progress=100)
    gantt.add_task("Database Setup", start_day=12, duration=3, progress=100)
    gantt.add_task("Backend Development", start_day=15, duration=15, progress=75)
    gantt.add_task("Frontend Development", start_day=20, duration=12, progress=60)
    gantt.add_task("API Integration", start_day=30, duration=5, progress=40)
    gantt.add_task("Testing & QA", start_day=35, duration=7, progress=20)
    gantt.add_task("Documentation", start_day=40, duration=5, progress=10)
    gantt.add_task("Deployment", start_day=45, duration=3, progress=0)
    
    chart = gantt.generate(width=100, show_progress=True)
    print(chart)
    print("\n")


def demo_erd():
    """Demonstrate Entity Relationship Diagram generation."""
    print("\n" + "=" * 80)
    print("ENTITY RELATIONSHIP DIAGRAM DEMO - E-Commerce Database")
    print("=" * 80 + "\n")
    
    erd = ERDGenerator()
    
    # Define entities
    erd.add_entity("Users", [
        {'name': 'user_id', 'type': 'INT', 'key': 'PK'},
        {'name': 'username', 'type': 'VARCHAR(50)'},
        {'name': 'email', 'type': 'VARCHAR(100)'},
        {'name': 'password_hash', 'type': 'VARCHAR(255)'},
        {'name': 'created_at', 'type': 'TIMESTAMP'}
    ])
    
    erd.add_entity("Products", [
        {'name': 'product_id', 'type': 'INT', 'key': 'PK'},
        {'name': 'name', 'type': 'VARCHAR(100)'},
        {'name': 'description', 'type': 'TEXT'},
        {'name': 'price', 'type': 'DECIMAL(10,2)'},
        {'name': 'stock', 'type': 'INT'},
        {'name': 'category_id', 'type': 'INT', 'key': 'FK'}
    ])
    
    erd.add_entity("Orders", [
        {'name': 'order_id', 'type': 'INT', 'key': 'PK'},
        {'name': 'user_id', 'type': 'INT', 'key': 'FK'},
        {'name': 'order_date', 'type': 'TIMESTAMP'},
        {'name': 'total_amount', 'type': 'DECIMAL(10,2)'},
        {'name': 'status', 'type': 'VARCHAR(20)'}
    ])
    
    erd.add_entity("OrderItems", [
        {'name': 'order_item_id', 'type': 'INT', 'key': 'PK'},
        {'name': 'order_id', 'type': 'INT', 'key': 'FK'},
        {'name': 'product_id', 'type': 'INT', 'key': 'FK'},
        {'name': 'quantity', 'type': 'INT'},
        {'name': 'price', 'type': 'DECIMAL(10,2)'}
    ])
    
    erd.add_entity("Categories", [
        {'name': 'category_id', 'type': 'INT', 'key': 'PK'},
        {'name': 'name', 'type': 'VARCHAR(50)'},
        {'name': 'description', 'type': 'TEXT'}
    ])
    
    # Define relationships
    erd.add_relationship("Users", "Orders", "1:N", "places")
    erd.add_relationship("Orders", "OrderItems", "1:N", "contains")
    erd.add_relationship("Products", "OrderItems", "1:N", "included in")
    erd.add_relationship("Categories", "Products", "1:N", "categorizes")
    
    diagram = erd.generate()
    print(diagram)
    print("\n")


def demo_simple_gantt():
    """Demonstrate simple Gantt chart."""
    print("\n" + "=" * 80)
    print("SIMPLE GANTT CHART - Weekly Sprint")
    print("=" * 80 + "\n")
    
    gantt = GanttChartGenerator()
    
    # Simple sprint tasks
    gantt.add_task("Sprint Planning", start_day=0, duration=1, progress=100)
    gantt.add_task("Feature A Development", start_day=1, duration=3, progress=100)
    gantt.add_task("Feature B Development", start_day=1, duration=4, progress=75)
    gantt.add_task("Code Review", start_day=4, duration=1, progress=50)
    gantt.add_task("Sprint Demo", start_day=5, duration=1, progress=0)
    
    chart = gantt.generate(width=80, show_progress=True)
    print(chart)
    print("\n")


def main():
    """Run all demos."""
    print("\n")
    print("╔═══════════════════════════════════════════════════════════════════════════╗")
    print("║                                                                           ║")
    print("║               ENHANCED DIAGRAM GENERATORS DEMONSTRATION                   ║")
    print("║                                                                           ║")
    print("╚═══════════════════════════════════════════════════════════════════════════╝")
    
    # Run demos
    demo_gantt_chart()
    
    input("Press Enter to continue to ERD demo...")
    
    demo_erd()
    
    input("Press Enter to continue to simple Gantt demo...")
    
    demo_simple_gantt()
    
    print("\n" + "=" * 80)
    print("DEMO COMPLETE")
    print("=" * 80)
    print("\nThese diagrams can be used in:")
    print("  - Project documentation")
    print("  - Database schema documentation")
    print("  - Project management reports")
    print("  - Technical specifications")
    print("\nTry creating your own diagrams using the GanttChartGenerator and ERDGenerator classes!")
    print("\n")


if __name__ == "__main__":
    main()

