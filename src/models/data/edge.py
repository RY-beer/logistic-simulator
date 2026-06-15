from dataclasses import dataclass

@dataclass
class Edge:
    id: str
    from_node: str
    to_node: str
    distance: float
    base_speed: float = 1.0
    congestion: float = 0.0  # 0~1