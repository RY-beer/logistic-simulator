from dataclasses import dataclass

from models.data.cargo import Cargo

@dataclass
class Order:
    id: int
    pickup_location_id: str
    delivery_location_id: str
    cargo_type: Cargo
    amount: int
    deadline_tick: int
    reward: float
    penalty_per_tick: float
    status: str = "pending"