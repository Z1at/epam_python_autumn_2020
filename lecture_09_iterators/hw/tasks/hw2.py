"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with supressor(IndexError):
...    [][2]

"""
from contextlib import contextmanager


class ContextManager:
    """Suppresses the received exception.

    Args:
        exception: An exception to be suppressed.

    Attributes:
        exception: An exception to be suppressed.

    """

    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type is self.exception


@contextmanager
def managed_exception(exception: Exception) -> None:
    """Emulates the context manager. Suppresses the received exception.

    Args:
        exception: An exception to be suppressed.

    """
    try:
        yield
    except exception:
        pass
