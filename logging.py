import ucolorama

logging_level = 0

blacklist = []

def debug(section: str, text: str):
    if not section in blacklist:
        if logging_level <= 0:
            print(f"{ucolorama.Fore.BLACK_BRIGHT}{section:<10} - DEBUG - {text}{ucolorama.Style.from_raw(ucolorama.Style.RAW_RESET)}")
def info(section: str, text: str):
    if not section in blacklist:
        if logging_level <= 1:
            print(f"{ucolorama.Fore.BLUE_BRIGHT}{section:<10} - INFO  - {text}{ucolorama.Style.from_raw(ucolorama.Style.RAW_RESET)}")
def warn(section: str, text: str):
    if not section in blacklist:
        if logging_level <= 2:
            print(f"{ucolorama.Fore.YELLOW}{section:<10} - WARN  - {text}{ucolorama.Style.from_raw(ucolorama.Style.RAW_RESET)}")
def error(section: str, text: str):
    if not section in blacklist:
        if logging_level <= 3:
            print(f"{ucolorama.Fore.RED}{section:<10} - ERROR - {text}{ucolorama.Style.from_raw(ucolorama.Style.RAW_RESET)}")
def fatal(section: str, text: str):
    if not section in blacklist:
        if logging_level <= 4:
            print(f"{ucolorama.Fore.WHITE}{ucolorama.Back.RED}{ucolorama.Style.from_raw(ucolorama.Style.RAW_BOLD)}{section: <10} - FATAL - {text}{ucolorama.Style.from_raw(ucolorama.Style.RAW_RESET)}")