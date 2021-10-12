from openpyxl.cell.cell import Cell
from openpyxl.worksheet._write_only import WriteOnlyWorksheet
from openpyxl.worksheet.worksheet import Worksheet
from typing import (
    Any,
    Iterator,
    List,
    Optional,
    Tuple,
    Union,
)

def create_temporary_file(suffix: str = ...) -> str: ...

class WorksheetWriter:
    def __init__(
        self, ws: Union[Worksheet, WriteOnlyWorksheet], out: None = ...
    ) -> None: ...
    def cleanup(self) -> None: ...
    def close(self) -> None: ...
    def get_stream(self) -> Iterator[None]: ...
    def read(self) -> bytes: ...
    def rows(
        self,
    ) -> Union[
        List[Union[Tuple[int, List[Any]], Tuple[int, List[Cell]]]],
        List[Tuple[int, List[Cell]]],
    ]: ...
    def write(self) -> None: ...
    def write_breaks(self) -> None: ...
    def write_cols(self) -> None: ...
    def write_dimensions(self) -> None: ...
    def write_drawings(self) -> None: ...
    def write_filter(self) -> None: ...
    def write_format(self) -> None: ...
    def write_formatting(self) -> None: ...
    def write_header(self) -> None: ...
    def write_hyperlinks(self) -> None: ...
    def write_legacy(self) -> None: ...
    def write_margins(self) -> None: ...
    def write_merged_cells(self) -> None: ...
    def write_page(self) -> None: ...
    def write_print(self) -> None: ...
    def write_properties(self) -> None: ...
    def write_protection(self) -> None: ...
    def write_rows(self) -> None: ...
    def write_scenarios(self) -> None: ...
    def write_sort(self) -> None: ...
    def write_tables(self) -> None: ...
    def write_tail(self) -> None: ...
    def write_top(self) -> None: ...
    def write_validations(self) -> None: ...
    def write_views(self) -> None: ...
