from dataclasses import dataclass
from datetime import datetime
from typing import List

from rich.console import Console
from richer.table import PropertyTable


@dataclass
class Tag:
    name: str
    commit: str


@dataclass
class Project:
    name: str
    star_count: int
    start_date: datetime
    tags: List[Tag]

tags = [
    Tag('v17.0.0', '89b6109'),
    Tag('v16.0.0', '5c6ef40')
]


item = Project(
    'React',
    142857,
    datetime.fromisoformat('2013-05-25T00:00:00'),
    tags
)

console = Console()
console.print(PropertyTable(item))
