from dataclasses import dataclass
from typing import List

@dataclass
class Cargo:
    id: int
    cargo_type: str
    size: int
    attributes: List[str]