from dataclasses import dataclass

@dataclass
class Node:
    id: str
    x: float
    y: float
    node_type: str  # "factory", "store", "hub", "road"...etc