from dataclasses import dataclass


@dataclass
class Token:
    text: str
    attr: str = '0'
    row: int = 0
    col: int = 0


def parse(ansi_color_text, escape_code=None):
    import re

    tokens = []
    row = 0
    col = 0

    if escape_code is None:
        if '\x1b' in ansi_color_text:
            escape_code = '\x1b'
        else:
            escape_code = '\^\['

    while ansi_color_text:

        # Find ANSI escape sequence
        regex = re.compile(
            f'({escape_code}\[(\d+(;\d+)*)m(.*?){escape_code}\[0m)')
        found = regex.search(ansi_color_text)
        if found is None:
            for l in ansi_color_text.splitlines(True):
                tokens.append(Token(text=l, row=row, col=col))
                if '\n' in l:
                    row += 1
                    col = 0
                else:
                    col += len(l)
            return tokens

        start, end = found.span()

        # Head
        head_text = ansi_color_text[:start]
        if head_text:
            for l in head_text.splitlines(True):
                tokens.append(Token(text=l, row=row, col=col))
                if '\n' in l:
                    row += 1
                    col = 0
                else:
                    col += len(l)

        # Body
        text = found.group(1)
        attr = found.group(2)
        inner_text = found.group(4)
        if inner_text:
            tokens.append(Token(text=inner_text, attr=attr, row=row, col=col))
            col += len(inner_text)

        # Tail
        ansi_color_text = ansi_color_text[end:]

    return tokens
