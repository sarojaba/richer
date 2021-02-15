from dataclasses import dataclass

from richer.console import InteractiveConsole


@dataclass
class Row:
    id: int

items = [Row(r) for r in range(0, 100)]

console = InteractiveConsole(items)
console.print()
