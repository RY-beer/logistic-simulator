from dataclasses import dataclass, field
from typing import List

from models.data.order import Order
from models.data.vehicle import Vehicle

@dataclass
class Company:
    capital: int
    cash: int
    profit_per_day: int
    order_ids: set[int]