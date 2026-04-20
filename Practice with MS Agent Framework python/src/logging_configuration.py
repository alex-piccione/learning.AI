import logging
from rich.logging import RichHandler


def setup_logging():
    handler = RichHandler(show_path=False, rich_tracebacks=True, show_level=False)
    logging.basicConfig(level=logging.INFO, handlers=[handler], force=True, format="%(message)s")

def log_tool_call (method:str, params:str):
    logging.info(f"⛏️  {method} {params}")
