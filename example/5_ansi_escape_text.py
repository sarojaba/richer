from dataclasses import dataclass

from rich.console import Console

from richer.text import AnsiEscapeText

console = Console()
text = '\x1b[1;32mSuccess\x1b[0m\n\x1b[1;31mFailure\x1b[0m'
console.print(AnsiEscapeText(text))
