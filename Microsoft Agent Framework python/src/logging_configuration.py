import logging
from rich.logging import RichHandler


def setup_logging():
    handler = RichHandler(show_path=False, rich_tracebacks=True, show_level=False)
    logging.basicConfig(level=logging.WARNING, handlers=[handler], force=True, format="%(message)s")
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)