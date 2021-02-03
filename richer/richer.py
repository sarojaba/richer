from datetime import datetime
from dataclasses import dataclass, is_dataclass, Field, fields
from typing import Any, List

from rich import box
from rich.table import Table


def style(text: str):
    return f'[bold]{text.upper()}[/bold]'


@dataclass
class Column:
    name: str
    justify: str


def column(field: Field) -> Column:
    if field.type == int:
        justify = 'right'
    else:
        justify = 'left'

    return Column(field.name, justify)


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
class Sort:
    key: str
    order: str


@dataclass
class ListRenderer:
    items: List
    sort: Sort = None
    inner: bool = False

    def __rich__(self) -> Table:
        show_edge = not self.inner
        __table = Table(box=box.SQUARE, show_edge=show_edge, show_lines=True)

        colums = [column(f) for f in fields(self.items[0])]
        colum_names = [c.name for c in colums]

        if self.sort:
            # Sort
            if self.sort.key in colum_names:
                def key(it): return getattr(it, self.sort.key)
                reverse = self.sort.order == 'desc'
                sorted_items = sorted(self.items, key=key, reverse=reverse)
            else:
                sorted_items = self.items

            # Colum headers
            for c in colums:
                if self.sort.key == c.name:
                    arrow = '🢓' if reverse else '🢑'
                    max_length = max([len(cell(getattr(it, self.sort.key)))
                                      for it in sorted_items])
                    blank_length = max(
                        max_length - (len(c.name) + len(arrow)), 1)
                    column_name = c.name + (' ' * blank_length) + arrow
                else:
                    column_name = c.name

                __table.add_column(style(column_name), justify=c.justify)
        else:
            sorted_items = self.items

            # Colum headers
            for c in colums:
                column_name = c.name
                __table.add_column(style(column_name), justify=c.justify)

        # Rows
        for it in sorted_items:
            values = [cell(getattr(it, cn)) for cn in colum_names]
            __table.add_row(*values)

        return __table


@dataclass
class PropertyRenderer:
    item: Any
    inner: bool = False

    def __rich__(self) -> Table:
        show_edge = not self.inner
        __table = Table(box=box.SQUARE, show_edge=show_edge, show_header=False, show_lines=True)

        for f in fields(self.item):
            __table.add_row(style(f.name), cell(getattr(self.item, f.name)))

        return __table
