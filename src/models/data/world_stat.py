from dataclasses import dataclass
from typing import Dict
from xml.dom import Node

from models.data.order import Order
from models.data.vehicle import Vehicle
from models.data.edge import Edge

@dataclass
class WorldState:
    tick: int
    nodes: Dict[str, Node]
    edges: Dict[str, Edge]
    vehicles: Dict[str, Vehicle]
    orders: Dict[str, Order]