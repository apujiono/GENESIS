import json
import os

def generate_plugin(plugin_name):
    plugin_path = f"plugins/{plugin_name}"
    os.makedirs(plugin_path, exist_ok=True)
    with open(f"{plugin_path}/prompt.py", 'w') as f:
        f.write(f"""
def get_prompt(data):
    return "Generated prompt for {plugin_name}: " + str(data)
""")
    return f"Plugin {plugin_name} generated"
