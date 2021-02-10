from dataclasses import dataclass
from datetime import datetime

from rich.console import Console
from richer.table import PropertyTable


@dataclass
class Project:
    name: str
    star_count: int
    start_date: datetime


item = Project('Vue', 156110, datetime.fromisoformat('2013-07-29T00:00:00'))

console = Console()
console.print(PropertyTable(item))
