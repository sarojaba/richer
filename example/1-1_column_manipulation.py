from dataclasses import dataclass
from datetime import datetime

from rich.console import Console
from richer.table import Column, ListTable


@dataclass
class Project:
    name: str
    star_count: int
    start_date: datetime


items = [
    Project('Vue', 156110, datetime.fromisoformat('2013-07-29T00:00:00')),
    Project('React', 142857, datetime.fromisoformat('2013-05-25T00:00:00')),
    Project('Angular', 57004, datetime.fromisoformat('2014-09-19T00:00:00'))
]

table = ListTable(
    items,
    columns=[
        Column(name='star_count', order='asc', justify='right'),
        Column(name='start_date', visible=False)
    ]
)

console = Console()
console.print(table)
