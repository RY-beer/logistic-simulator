from dataclasses import dataclass
from typing import List
from bisect import bisect_left

import game_config
from models.data.order import Order
from models.data.vehicle import Vehicle

@dataclass
class Company:
    capital: int
    cash: int
    profit_per_day: int
    order_ids: set[int]

    def get_level(self) -> int:
        index = bisect_left(game_config.LEVELS, self.profit_per_day)
        return index+1 ## level start from 1, not 0