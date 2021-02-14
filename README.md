# Richer

Table renderer for dataclass

## Example

### List

```python3
from dataclasses import dataclass
from datetime import datetime

from rich.console import Console
from richer.table import ListTable


@dataclass
class Project:
    name: str
    star_count: int
    start_date: datetime


items = [
    Project('Vue', 156110, datetime.fromisoformat('2013-07-29T00:00:00')),
    Project('React', 142857, datetime.fromisoformat('2013-05-25T00:00:00')),
]

console = Console()
console.print(ListTable(items))
```

| **NAME**  │ **STAR COUNT** │ **START DATE**      │
| --------- | -------------- | ------------------- |
│ Vue       │        156,110 │ 2013-07-29 00:00:00 │
│ React     │        142,857 │ 2013-05-25 00:00:00 │

### Property

```python3
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
```

│ **NAME**       │ Vue                 │
│ **STAR COUNT** │ 156,110             │
│ **START DATE** │ 2013-07-29 00:00:00 │

### Pagination

```python3
from dataclasses import dataclass

from richer.interactive_console import InteractiveConsole


@dataclass
class Row:
    id: int

items = [Row(r) for r in range(0, 100)]

console = InteractiveConsole(items)
console.print()
```
