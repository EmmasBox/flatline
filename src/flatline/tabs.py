

from textual.app import ComposeResult
from textual.widgets import TabPane, TabbedContent
from textual.containers import HorizontalGroup

class TabSystem(HorizontalGroup):
    BINDINGS = [

    ]

    def compose(self) -> ComposeResult:
        yield TabbedContent()