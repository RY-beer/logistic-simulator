from dataclasses import dataclass

from models.data.cargo import Cargo

@dataclass
class Node:
    id: int
    x: float
    y: float
    node_type: str  # "factory", "store", "hub", "road"...etc
    active_cargo: Cargo
    demand_rate: int = 0

    FACTORY = "factory"
    STORE = "store"
    HUB = "hub"
    JUNCTION = "junction"