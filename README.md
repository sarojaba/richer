# Richer

Table renderer for dataclass

## Example

```python3
from datetime import datetime
from dataclasses import dataclass
from typing import List

from richer.richer import PropertyRenderer, ListRenderer, Sort


@dataclass
class Inner:
    id: int
    name: str


@dataclass
class Row:
    id: int
    name: str
    price: int
    desc: str
    now: datetime
    inners: List[Inner]
    inner: Inner


if __name__ == '__main__':
    from rich.console import Console

    item0 = Row(9999, 'bear', 300,
                'abcdeabcdeabcdeabcdeabcde',
                datetime.today(),
                [Inner(0, 'white'), Inner(1, 'black')],
                Inner(0, 'white'))

    item1 = Row(1, 'apple', 200,
                '',
                datetime.today(),
                [Inner(0, 'white'), Inner(1, 'black')],
                Inner(0, 'white'))

    items = [item0, item1]

    console = Console()
    console.print(PropertyRenderer(item0))
    console.print(ListRenderer(items, Sort('name', 'desc')))
```

sarojaba@gmail.com