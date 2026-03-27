import random
from .node_registry import get_node_registry

class LoadBalancer:
    """Distributes AI tasks among available nodes in the Mesh Network."""
    def __init__(self):
        self.registry = get_node_registry()

    def select_node(self, expert_type: str):
        """Selects a healthy node for the given expert type using basic random balancing."""
        available_nodes = self.registry.get_nodes_by_expert(expert_type)
        if available_nodes:
            return random.choice(available_nodes)
        return None

_balancer = None

def get_load_balancer():
    global _balancer
    if _balancer is None:
        _balancer = LoadBalancer()
    return _balancer
