
from textual.app import App
from textual.widgets import Header, Footer, Label
from textual.containers import Container

from flatline.command_line import CommandLine
from flatline.tabs import TabSystem

try:
    from zoautil_py import zsystem # type: ignore
    zoau_enabled = True
except:
    zoau_enabled = False

#system information
if zoau_enabled:
    zsystem_info = json.loads(zsystem.zinfo()) # type: ignore
    system_name = zsystem_info["sys_info"]["sys_name"]
    lpar_name = zsystem_info["sys_info"]["lpar_name"]

class Flatline(App):
    #Import css
    CSS_PATH = "UI.css"

    def on_mount(self) -> None:
        self.title = "Flatline"
        self.sub_title = "System Administration"

    #UI elements
    def compose(self):
        #display system and LPAR name
        if zoau_enabled:
            yield Label(f"You are working on the {system_name} mainframe system in LPAR {lpar_name}")
        yield Header()
        yield CommandLine()
        with Container():
            yield TabSystem()
        yield Footer()