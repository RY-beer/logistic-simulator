from dataclasses import dataclass, field
from typing import List, Optional

from models.data.cargo import Cargo
from models.data.order import Order

@dataclass
class Vehicle:
    id: int
    capacity: int
    speed: int
    loaded_cargo: List[Cargo] = field(default_factory=list)
    assigned_orders: Order
    x: int
    y: int
    
    current_edge: Optional[str] = None
    allowed_attributes: List[str]
    progress: float = 0.0  # 0~1 on edge