#!/usr/bin/env python3
"""
Create a blank JSON template for new workflows
"""
import json, sys
def create_workflow(name):
    workflow = {"name": name, "nodes": [], "connections": {}}
    with open(f"{name}.json", "w") as f:
        json.dump(workflow, f, indent=2)
    print(f"Created {name}.json")
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_workflow.py new-workflow-name")
    else:
        create_workflow(sys.argv[1])
