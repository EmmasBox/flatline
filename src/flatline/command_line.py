
from datetime import datetime

from textual.app import ComposeResult

from textual.suggester import SuggestFromList
from textual import on
from textual.events import ScreenResume
from textual.widgets import Input, Log, Label, Select
from textual.containers import HorizontalGroup,Container
from textual.screen import Screen

try:
    from zoautil_py import mvscmd, opercmd # type: ignore
    zoau_enabled = True
except:
    print("##GHOST_ERROR_1 Warning: could not find ZOAU, entering lockdown mode")    
    zoau_enabled = False

def generate_command_meta_header(command):
    now = datetime.now() # current date and time
    date_time = now.strftime("date: %m/%d/%Y time: %H:%M:%S")
    local_now = now.astimezone()
    local_tz = local_now.tzinfo
    local_tzname = local_tz.tzname(local_now)
    
    return f"""
    --------------------------------------------------------------------------------------------------
    Command '{command}' 
    executed on {date_time} {local_tzname}
    --------------------------------------------------------------------------------------------------
    \n
    """

class CommandLine(HorizontalGroup):
    def compose(self) -> ComposeResult:
        yield Select(options=[("TSO", "TSO"),("MVS", "MVS"),("OPER", "OPER")],value="TSO",id="command_mode")
        yield Input(id="cli",max_length=250,placeholder="Submit a command...",classes="command-field",tooltip="Use this command field to submit commands. You can view the output in the command history panel")