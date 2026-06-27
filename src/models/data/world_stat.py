from dataclasses import dataclass
from typing import Dict
from xml.dom import Node

from models.data.order import Order
from models.data.vehicle import Vehicle

@dataclass
class WorldState:
    tick: int
    nodes: Dict[int, Node]
    vehicles: Dict[int, Vehicle]
    orders: Dict[int, Order]
    current_size_index: int = 0