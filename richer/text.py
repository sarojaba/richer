from dataclasses import dataclass, field
from typing import List


@dataclass
class Token:
    text: str
    attr: str = '0'
    row: int = 0
    col: int = 0


class AnsiEscapeText:
    tokens: List[Token]

    def __init__(self, text, escape_code=None):
        import re

        if escape_code is None:
            if '\x1b' in text:
                escape_code = '\x1b'
            else:
                escape_code = '\^\['

        regex = re.compile(
            f'({escape_code}\[(\d+(;\d+)*)m(.*?){escape_code}\[0m)')

        self.tokens = []
        row = 0
        col = 0

        while text:

            # Find ANSI escape sequence
            found = regex.search(text)
            if found is None:
                for l in text.splitlines(True):
                    self.tokens.append(Token(text=l, row=row, col=col))
                    if '\n' in l:
                        row += 1
                        col = 0
                    else:
                        col += len(l)
                return

            start, end = found.span()

            # Head
            head_text = text[:start]
            if head_text:
                for l in head_text.splitlines(True):
                    self.tokens.append(Token(text=l, row=row, col=col))
                    if '\n' in l:
                        row += 1
                        col = 0
                    else:
                        col += len(l)

            # Body
            attr = found.group(2)
            inner_text = found.group(4)
            if inner_text:
                self.tokens.append(
                    Token(text=inner_text, attr=attr, row=row, col=col))
                col += len(inner_text)

            # Tail
            text = text[end:]

    def __rich__(self) -> str:
        ret = ''
        for t in self.tokens:
            if t.attr == '0':
                ret += t.text
            else:
                switch = {
                    '1': 'bold',
                    '31': 'red',
                    '32': 'green'
                }
                bbcode = ' '.join([switch[a] for a in t.attr.split(';')])
                ret += f'[{bbcode}]{t.text}[/]'

        return ret
