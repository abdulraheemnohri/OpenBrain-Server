class NodeRegistry:
    """Manages connected devices in the AI Mesh Network."""
    def __init__(self):
        self.nodes = {}

    def register_node(self, node_id: str, expert_type: str, url: str):
        self.nodes[node_id] = {
            "expert_type": expert_type,
            "url": url,
            "status": "online"
        }
        print(f"[MESH] Registered node {node_id} as {expert_type} expert.")

    def get_nodes_by_expert(self, expert_type: str):
        return [node for node in self.nodes.values() if node["expert_type"] == expert_type and node["status"] == "online"]

_registry = None

def get_node_registry():
    global _registry
    if _registry is None:
        _registry = NodeRegistry()
    return _registry
