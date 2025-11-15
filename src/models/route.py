from typing import Any
from dataclasses import dataclass

@dataclass(frozen=True)
class Route:
    route: str
    name: str
    icon: Any
    
