class Fore:
    def from_id256(id256: int):
        return f"\033[38;5;{id256}m"
    def from_id16(id16: int):
        return f"\033[{id16}m"
    def from_rgb(rgb: tuple[int, int, int]):
        return f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m"
    def from_raw(raw_code):
        return f"\033[{raw_code}m"
    RAW_BLACK = 30
    RAW_RED = 31
    RAW_GREEN = 32
    RAW_YELLOW = 33
    RAW_BLUE = 34
    RAW_MAGENTA = 35
    RAW_CYAN = 36
    RAW_WHITE = 37
    RAW_BLACK_BRIGHT = 90
    RAW_RED_BRIGHT = 91
    RAW_GREEN_BRIGHT = 92
    RAW_YELLOW_BRIGHT = 93
    RAW_BLUE_BRIGHT = 94
    RAW_MAGENTA_BRIGHT = 95
    RAW_CYAN_BRIGHT = 96
    RAW_WHITE_BRIGHT = 97
    BLACK = f"\033[{RAW_BLACK}m"
    RED = f"\033[{RAW_RED}m"
    GREEN = f"\033[{RAW_GREEN}m"
    YELLOW = f"\033[{RAW_YELLOW}m"
    BLUE = f"\033[{RAW_BLUE}m"
    MAGENTA = f"\033[{RAW_MAGENTA}m"
    CYAN = f"\033[{RAW_CYAN}m"
    WHITE = f"\033[{RAW_WHITE}m"
    BLACK_BRIGHT = f"\033[{RAW_BLACK_BRIGHT}m"
    RED_BRIGHT = f"\033[{RAW_RED_BRIGHT}m"
    GREEN_BRIGHT = f"\033[{RAW_GREEN_BRIGHT}m"
    YELLOW_BRIGHT = f"\033[{RAW_YELLOW_BRIGHT}m"
    BLUE_BRIGHT = f"\033[{RAW_BLUE_BRIGHT}m"
    MAGENTA_BRIGHT = f"\033[{RAW_MAGENTA_BRIGHT}m"
    CYAN_BRIGHT = f"\033[{RAW_CYAN_BRIGHT}m"
    WHITE_BRIGHT = f"\033[{RAW_WHITE_BRIGHT}m"
class Back:
    def from_id256(id256: int):
        return f"\033[48;5;{id256}m"
    def from_id16(id16: int):
        return f"\033[{id256}m"
    def from_rgb(rgb: tuple[int, int, int]):
        return f"\033[48;2;{rgb[0]};{rgb[1]};{rgb[2]}m"
    def from_raw(raw_code):
        return f"\033[{raw_code}m"
    RAW_BLACK = 40
    RAW_RED = 41
    RAW_GREEN = 42
    RAW_YELLOW = 43
    RAW_BLUE = 44
    RAW_MAGENTA = 45
    RAW_CYAN = 46
    RAW_WHITE = 47
    RAW_BLACK_BRIGHT = 100
    RAW_RED_BRIGHT = 101
    RAW_GREEN_BRIGHT = 102
    RAW_YELLOW_BRIGHT = 103
    RAW_BLUE_BRIGHT = 104
    RAW_MAGENTA_BRIGHT = 105
    RAW_CYAN_BRIGHT = 106
    RAW_WHITE_BRIGHT = 107
    BLACK = f"\033[{RAW_BLACK}m"
    RED = f"\033[{RAW_RED}m"
    GREEN = f"\033[{RAW_GREEN}m"
    YELLOW = f"\033[{RAW_YELLOW}m"
    BLUE = f"\033[{RAW_BLUE}m"
    MAGENTA = f"\033[{RAW_MAGENTA}m"
    CYAN = f"\033[{RAW_CYAN}m"
    WHITE = f"\033[{RAW_WHITE}m"
    BLACK_BRIGHT = f"\033[{RAW_BLACK_BRIGHT}m"
    RED_BRIGHT = f"\033[{RAW_RED_BRIGHT}m"
    GREEN_BRIGHT = f"\033[{RAW_GREEN_BRIGHT}m"
    YELLOW_BRIGHT = f"\033[{RAW_YELLOW_BRIGHT}m"
    BLUE_BRIGHT = f"\033[{RAW_BLUE_BRIGHT}m"
    MAGENTA_BRIGHT = f"\033[{RAW_MAGENTA_BRIGHT}m"
    CYAN_BRIGHT = f"\033[{RAW_CYAN_BRIGHT}m"
    WHITE_BRIGHT = f"\033[{RAW_WHITE_BRIGHT}m"
class Style:
    def from_raw(raw_code):
        return f"\033[{raw_code}m"
    RAW_RESET = 0
    RAW_BOLD = 1
    RAW_FAINT = 2
    RAW_ITALIC = 3
    RAW_UNDERLINE = 4
    RAW_BLINK = 5
    RAW_BLINK_QUICK = 6
    RAW_REVERSE = 7
    RAW_CONCEAL = 8
    RAW_CROSSED_OUT = 9
    RAW_FONT_DEFAULT = 10
    RAW_FONT_0 = 11
    RAW_FONT_1 = 12
    RAW_FONT_2 = 13
    RAW_FONT_3 = 14
    RAW_FONT_4 = 15
    RAW_FONT_5 = 16
    RAW_FONT_6 = 17
    RAW_FONT_7 = 18
    RAW_FONT_8 = 19
    RAW_FRAKTUR = 20
    RAW_BOLD_OFF = 21
    RAW_NORMAL_COLOR = 22
    RAW_ITALIC_FRAKTUR_OFF = 23
    RAW_UNDERLINE_OFF = 24
    RAW_BLINK_OFF = 25
    #??? = 26
    RAW_REVERSE_OFF = 27
    RAW_CONCEAL_OFF = 28
    RAW_CROSSED_OUT_OFF = 29
    #SET_FORE_COLOR 30-37
    #SET_FORE_COLOR_CUSTOM 38
    #DEFAULT_FORE_COLOR 39
    #SET_BACK_COLOR 40-47
    #SET_BACK_COLOR_CUSTOM 48
    #DEFAULT_BACK_COLOR 49
    #??? = 50
    RAW_FRAMED = 51
    RAW_ENCIRCLED = 52
    RAW_OVERLINED = 53
    RAW_FRAMED_ENCIRCLED_OFF = 54
    RAW_OVERLINED_OFF = 55
    RAW_UNDERLINE_IDEOGRAM = 60
    RAW_UNDERLINE_DOUBLE_IDEOGRAM = 61
    RAW_OVERLINE_IDEOGRAM = 62
    RAW_OVERLINE_DOUBLE_IDEOGRAM = 63
    RAW_STRESS_MARKING_IDEOGRAM = 64
    RAW_IDEOGRAM_OFF = 65
    #??? 66-72
    RAW_SUPERSCRIPT = 73
    RAW_SUBSCRIPT = 74
    RAW_SUPERSCRIPT_SUBSCRIPT_OFF = 75
    #??? 76-89
    #SET_BRIGHT_FORE_COLOR 90-97
    #??? 98-99
    #SET_BRIGHT_BACK_COLOR 100-107
class Special:
    NULL = "\x00"
    START_OF_HEADING = "\x01"
    START_OF_TEXT = "\x02"
    END_OF_TEXT = "\x03"
    END_OF_TRANSMISSION = "\x04"
    ENQUIRY = "\x05"
    ACKNOWLEDGE = "\x06"
    BELL = "\x07"
    BACKSPACE = "\x08"
    TAB = "\x09"
    LINE_FEED = "\x0A"
    VERTICAL_TAB = "\x0B"
    FORM_FEED = "\x0C"
    CARRIAGE_RETURN = "\x0D"
    SHIFT_OUT = "\x0E"
    SHIFT_IN = "\x0F"
    DATA_LINK_ESCAPE = "\x10"
    DEVICE_CONTROL_ONE = "\x11"
    DEVICE_CONTROL_TWO = "\x12"
    DEVICE_CONTROL_THREE = "\x13"
    DEVICE_CONTROL_FOUR = "\x14"
    NEGATIVE_ACKNOWLEDGE = "\x15"
    SYNCHRONOUS_IDLE = "\x16"
    END_OF_TRANSMISSION_BLOCK = "\x17"
    CANCEL = "\x18"
    SUBSTITUTE = "\x1A"
    ESCAPE = "\x1B"
    FILE_SEPARATOR = "\x1C"
    GROUP_SEPARATOR = "\x1D"
    RECORD_SEPARATOR = "\x1E"
    UNIT_SEPARATOR = "\x1F"
    SPACE = "\x20"
    DELETE = "\x7F"
class Escapes:
    def from_raw(raw_code):
        return f"\033{raw_code}"
    def use(raw_code, content, terminator):
        return f"{from_raw(raw_code)}{content}"
    PADDING_CHARACTER = "@"
    HIGH_OCTET_PRESET = "A"
    BREAK_PERMITTED_HERE = "B"
    NO_BREAK_HERE = "C"
    INDEX = "D"
    NEXT_LINE = "E"
    START_OF_SELECTED_AREA = "F"
    END_OF_SELECTED_AREA = "G"
    CHAR_TAB_SET = "H"
    CHAR_TAB_SET_WITH_JUSTIFICATION = "I"
    LINE_TAB_SET = "J"
    PARTIAL_LINE_FORWARD = "K"
    PARTIAL_LINE_BACKWARD = "L"
    REVERSE_LINE_FEED = "M"
    SINGLE_SHIFT_TWO = "N"
    SINGLE_SHIFT_THREE = "O"
    DEVICE_CONTROL_STRING = "P"
    CONTROL_SEQUENCE_INTRODUCER = "["
    STRING_TERMINATOR = "\\"
    OPERATING_SYSTEM_COMMAND = "]"
    START_OF_STRING = "X"
    PRIVACY_MESSAGE = "^"
    APPLICATION_PROGRAM_COMMAND = "_"
class Cursor:
    def CURSOR_UP(times):
        return f"\033[{times}A"
    def CURSOR_DOWN(times):
        return f"\033[{times}B"
    def CURSOR_FORWARD(times):
        return f"\033[{times}C"
    def CURSOR_BACK(times):
        return f"\033[{times}D"
    def CURSOR_NEXT_LINE(times):
        return f"\033[{times}E"
    def CURSOR_PREVIOUS_LINE(times):
        return f"\033[{times}F"
    def CURSOR_HORIZONTAL_ABSOLUTE(column):
        return f"\033[{column}G"
    def CURSOR_POSITION(row, column):
        return f"\033[{row};{column}H"
    CLEAR_SCREEN_FROM_CURSOR_TO_END = "\033[0J"
    CLEAR_SCREEN_FROM_CURSOR_TO_BEGINNING = "\033[1J"
    CLEAR_SCREEN_FROM_BEGINNING_TO_END = "\033[2J"
    CLEAR_SCREEN_FROM_BEGINNING_TO_END_DELETE_SCROLLBACK = "\033[3J"
    CLEAR_LINE_FROM_CURSOR_TO_END = "\033[0K"
    CLEAR_LINE_FROM_CURSOR_TO_BEGINNING = "\033[1K"
    CLEAR_LINE_FROM_BEGINNING_TO_END = "\033[2K"
    def SCROLL_UP(times):
        return f"\033[{times}S"
    def SCROLL_DOWN(times):
        return f"\033[{times}T"
    def HORIZONTAL_VERTICAL_POSITION(row, column):
        return f"\033[{row};{column}f"
    DEVICE_STATUS_REPORT = "\0336n"
class Other:
    AUX_PORT_OFF = "\0334i"
    AUX_PORT_ON = "\0335i"