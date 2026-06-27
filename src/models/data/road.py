from dataclasses import dataclass
from typing import List

from models.data.node import Node

@dataclass
class Node:
    id: int
    x: float
    y: float
    node_type: str  # "highway", "urban_road", "residential_street"...etc

    nodes: List[Node]