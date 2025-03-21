#Enables true colors to be active by default
from os import environ
if "TEXTUAL_COLOR_SYSTEM" not in environ:
    environ["TEXTUAL_COLOR_SYSTEM"] = "truecolor"