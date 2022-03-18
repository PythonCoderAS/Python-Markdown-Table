from dataclasses import dataclass, field
from typing import Iterable


@dataclass
class Table:
    headers: list[str] = field(default_factory=list)
    rows: list[Iterable[str]] = field(default_factory=list, init=False)

    def add_row(self, row: Iterable[str]):
        self.rows.append(row)

    def set_headers(self, headers: list[str]):
        self.headers = headers

    def get_table(self) -> str:
        header_row = "|" + "|".join(self.headers) + "|"
        separator_row = "|" + "|".join(["-"] * len(self.headers)) + "|"
        body_rows = [f"|{'|'.join(row)}|" for row in self.rows]
        return "\n".join([header_row, separator_row] + body_rows)
