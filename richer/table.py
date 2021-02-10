from datetime import datetime
from dataclasses import dataclass, is_dataclass, Field, field, fields
from typing import Any, List

from rich import box
from rich.table import Table


@dataclass
class Column:
    name: str
    justify: str = None
    order: str = None


def column(field: Field) -> Column:
    if field.type == int:
        justify = 'right'
    else:
        justify = 'left'

    return Column(field.name, justify)


def style(text: str):
    return f"[bold]{text.upper().replace('_', ' ')}[/bold]"


def cell(value):
    if value is None:
        return '-'
    elif isinstance(value, str):
        if not value:
            return '-'
        return value
    elif isinstance(value, int):
        return f'{value:,}'  # ex) 9,999
    elif isinstance(value, datetime):
        return value.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(value, Table):
        return value
    elif isinstance(value, List):
        return ListRenderer(value, inner=True)
    elif is_dataclass(value):
        return PropertyRenderer(value, inner=True)
    else:
        return value


@dataclass
class ListTable:
    items: List
    index: bool = False
    inner: bool = False
    columns: List[Column] = field(default_factory=list)

    def __rich__(self) -> Table:
        show_edge = not self.inner
        __table = Table(box=box.SQUARE, show_edge=show_edge, show_lines=False)

        # Sort
        sorted_items = self.items[:]
        for c in self.columns[::-1]:  # Rewind
            if c.order is not None:
                def key(it): return getattr(it, c.name)
                reverse = c.order == 'desc'
                sorted_items.sort(key=key, reverse=reverse)

        columns = [column(f) for f in fields(self.items[0])]
        column_names = [c.name for c in columns]

        orders = {c.name: c.order for c in self.columns}
        justifies = {c.name: c.justify for c in self.columns}

        # Index Column
        if self.index:
            __table.add_column('INDEX', justify='right')

        for c in columns:
            order = orders.get(c.name)
            if order:
                # Colum headers
                reverse = c.order == 'desc'
                arrow = '🢓' if reverse else '🢑'
                max_length = max([len(cell(getattr(it, c.name)))
                                  for it in sorted_items])
                blank_length = max(
                    max_length - (len(c.name) + len(arrow)), 1)
                column_name = c.name + (' ' * blank_length) + arrow
            else:
                column_name = c.name

            __table.add_column(style(column_name),
                               justify=justifies.get(c.name, c.justify))

        # Rows
        for i, it in enumerate(sorted_items):
            values = [cell(getattr(it, cn)) for cn in column_names]
            if self.index:
                __table.add_row(str(i), *values)
            else:
                __table.add_row(*values)

        return __table


@dataclass
class PropertyTable:
    item: Any
    inner: bool = False

    def __rich__(self) -> Table:
        show_edge = not self.inner
        __table = Table(box=box.SQUARE, show_edge=show_edge,
                        show_header=False, show_lines=True)

        for f in fields(self.item):
            __table.add_row(style(f.name), cell(getattr(self.item, f.name)))

        return __table
