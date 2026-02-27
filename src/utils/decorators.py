import functools
from src.utils.helpers import capture_screenshot


def capture_screenshot_on_fail(func):

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception:
            capture_screenshot(self.driver, func.__name__)
            raise

    return wrapper