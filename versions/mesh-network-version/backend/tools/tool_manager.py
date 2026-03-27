import os
import importlib.util

class ToolManager:
    def __init__(self):
        self.tools = {}
        self.load_plugins()

    def load_plugins(self):
        """Discovers and loads tools from the plugins directory."""
        plugins_dir = "plugins"
        if not os.path.exists(plugins_dir):
            return

        for plugin_name in os.listdir(plugins_dir):
            plugin_path = os.path.join(plugins_dir, plugin_name, "plugin.py")
            if os.path.exists(plugin_path):
                spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                if hasattr(module, "register_tool"):
                    tool_info = module.register_tool()
                    self.tools[tool_info["name"]] = {
                        "description": tool_info["description"],
                        "func": tool_info["func"]
                    }
                    print(f"Loaded tool: {tool_info['name']}")

    def execute_tool(self, name: str, *args, **kwargs):
        """Executes a registered tool by name."""
        if name in self.tools:
            return self.tools[name]["func"](*args, **kwargs)
        return f"Error: Tool '{name}' not found."

    def get_available_tools(self):
        """Returns a list of all loaded tools and their descriptions."""
        return [{"name": name, "description": data["description"]} for name, data in self.tools.items()]

_tool_manager = None

def get_tool_manager():
    global _tool_manager
    if _tool_manager is None:
        _tool_manager = ToolManager()
    return _tool_manager
