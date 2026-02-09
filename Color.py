"""
    This is a library, made with ChatGPT. I did not write any of this
"""
from __future__ import annotations


class Color:
    """
    Terminal ANSI color + style codes for easy f-string usage.

    Example:
        print(f"{color.green}Hello{color.clear}")
        print(f"{color.bold}{color.red}ERROR{color.clear}")
        print(f"{color.bg_blue}{color.white} NICE {color.clear}")

    Supports:
    - Basic colors
    - Bright colors
    - Background colors
    - Formatting (bold, underline, etc.)
    - 256-color and Truecolor helpers
    """

    ESC = "\033["

    def __init__(self) -> None:
        # reset / clear
        self.clear = f"{self.ESC}0m"
        self.reset = self.clear

        # styles
        self.bold = f"{self.ESC}1m"
        self.dim = f"{self.ESC}2m"
        self.italic = f"{self.ESC}3m"
        self.underline = f"{self.ESC}4m"
        self.blink = f"{self.ESC}5m"
        self.reverse = f"{self.ESC}7m"
        self.hidden = f"{self.ESC}8m"
        self.strike = f"{self.ESC}9m"

        # normal foreground colors
        self.black = f"{self.ESC}30m"
        self.red = f"{self.ESC}31m"
        self.green = f"{self.ESC}32m"
        self.yellow = f"{self.ESC}33m"
        self.blue = f"{self.ESC}34m"
        self.magenta = f"{self.ESC}35m"
        self.cyan = f"{self.ESC}36m"
        self.white = f"{self.ESC}37m"

        # bright foreground colors
        self.bright_black = f"{self.ESC}90m"
        self.bright_red = f"{self.ESC}91m"
        self.bright_green = f"{self.ESC}92m"
        self.bright_yellow = f"{self.ESC}93m"
        self.bright_blue = f"{self.ESC}94m"
        self.bright_magenta = f"{self.ESC}95m"
        self.bright_cyan = f"{self.ESC}96m"
        self.bright_white = f"{self.ESC}97m"

        # aliases
        self.gray = self.bright_black
        self.grey = self.bright_black

        # normal background colors
        self.bg_black = f"{self.ESC}40m"
        self.bg_red = f"{self.ESC}41m"
        self.bg_green = f"{self.ESC}42m"
        self.bg_yellow = f"{self.ESC}43m"
        self.bg_blue = f"{self.ESC}44m"
        self.bg_magenta = f"{self.ESC}45m"
        self.bg_cyan = f"{self.ESC}46m"
        self.bg_white = f"{self.ESC}47m"

        # bright background colors
        self.bg_bright_black = f"{self.ESC}100m"
        self.bg_bright_red = f"{self.ESC}101m"
        self.bg_bright_green = f"{self.ESC}102m"
        self.bg_bright_yellow = f"{self.ESC}103m"
        self.bg_bright_blue = f"{self.ESC}104m"
        self.bg_bright_magenta = f"{self.ESC}105m"
        self.bg_bright_cyan = f"{self.ESC}106m"
        self.bg_bright_white = f"{self.ESC}107m"

    # ------------------- advanced color helpers -------------------

    def fg256(self, n: int) -> str:
        """256-color foreground. n must be 0..255"""
        if not (0 <= n <= 255):
            raise ValueError("fg256 color must be between 0 and 255")
        return f"{self.ESC}38;5;{n}m"

    def bg256(self, n: int) -> str:
        """256-color background. n must be 0..255"""
        if not (0 <= n <= 255):
            raise ValueError("bg256 color must be between 0 and 255")
        return f"{self.ESC}48;5;{n}m"

    def rgb(self, r: int, g: int, b: int) -> str:
        """Truecolor foreground (24-bit RGB)."""
        if not all(0 <= v <= 255 for v in (r, g, b)):
            raise ValueError("rgb values must be 0..255")
        return f"{self.ESC}38;2;{r};{g};{b}m"

    def bgrgb(self, r: int, g: int, b: int) -> str:
        """Truecolor background (24-bit RGB)."""
        if not all(0 <= v <= 255 for v in (r, g, b)):
            raise ValueError("bgrgb values must be 0..255")
        return f"{self.ESC}48;2;{r};{g};{b}m"


color = Color()
