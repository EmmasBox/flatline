
from datetime import datetime

from textual.app import ComposeResult

from textual.suggester import SuggestFromList
from textual import on
from textual.events import ScreenResume
from textual.widgets import Input, Log, Label
from textual.containers import HorizontalGroup
from textual.screen import Screen

try:
    from zoautil_py import mvscmd, opercmd # type: ignore
    zoau_enabled = True
except:
    print("##GHOST_ERROR_1 Warning: could not find ZOAU, entering lockdown mode")    
    zoau_enabled = False

