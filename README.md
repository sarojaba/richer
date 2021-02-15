# Richer

Table renderer for dataclass using [Rich](https://github.com/willmcgugan/rich)

## Features

### List Table

Display table from dataclasses

[1_list_table.py](example/1_list_table.py)

```python3
from rich.console import Console
from richer.table import ListTable

@dataclass
class Project:
    name: str
    star_count: int
    start_date: datetime

items = [
    Project('Vue', 156110, datetime.fromisoformat('2013-07-29T00:00:00')),
    Project('React', 142857, datetime.fromisoformat('2013-05-25T00:00:00'))
]

console = Console()
console.print(ListTable(items))
```

```
┌───────┬────────────┬─────────────────────┐
│ NAME  │ STAR COUNT │ START DATE          │
├───────┼────────────┼─────────────────────┤
│ Vue   │    156,110 │ 2013-07-29 00:00:00 │
│ React │    142,857 │ 2013-05-25 00:00:00 │
└───────┴────────────┴─────────────────────┘
```

### Property Table

Display table from a dataclass

[2_property_table.py](example/2_property_table.py)

```python3
from rich.console import Console
from richer.table import PropertyTable

console = Console()
console.print(PropertyTable(item[0]))
```

```
┌────────────┬─────────────────────┐
│ NAME       │ Vue                 │
├────────────┼─────────────────────┤
│ STAR COUNT │ 156,110             │
├────────────┼─────────────────────┤
│ START DATE │ 2013-07-29 00:00:00 │
└────────────┴─────────────────────┘
```

### Inner Table

Display inner table from a nested dataclass

[3_inner_table.py](example/3_inner_table.py)

```python3
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
```

```
┌────────────┬─────────────────────┐
│ NAME       │ React               │
├────────────┼─────────────────────┤
│ STAR COUNT │ 142,857             │
├────────────┼─────────────────────┤
│ START DATE │ 2013-05-25 00:00:00 │
├────────────┼─────────────────────┤
│ TAGS       │  NAME    │ COMMIT   │
│            │ ─────────┼───────── │
│            │  v17.0.0 │ 89b6109  │
│            │  v16.0.0 │ 5c6ef40  │
└────────────┴─────────────────────┘
```

### Pagination a table

Paginate a table using curses

- Press 'q' key to exit from interactive console.
- Press 'right' key or 'page down' key to go to next page.
- Press 'left' key or 'page up' key to go to previous page.

[4_pagination.py](example/4_pagination.py)

```python3
from richer.console import InteractiveConsole

@dataclass
class Row:
    id: int

items = [Row(r) for r in range(0, 100)]

console = InteractiveConsole(items)
console.print()
```

```
┌────┐
│ ID │
├────┤
│  0 │
│  1 │
│  2 │
│  3 │
│  4 │
│  5 │
│  6 │
│  7 │
│  8 │
│  9 │
│ 10 │
└────┘
```

### ANSI Escape Text

Display ANSI Escape Text

It is useful to use rich by redirecting stdout and stderr

[5_ansi_escape_text.py](example/5_ansi_escape_text.py)

```python3
from richer.text import AnsiEscapeText

console = Console()
text = '\x1b[1;32mSuccess\x1b[0m\n\x1b[1;31mFailure\x1b[0m'
console.print(AnsiEscapeText(text))
```

<div class="blockquote"><span style="color:green;">Success</span><br/><span style="color:red;">Failure</span></div>
