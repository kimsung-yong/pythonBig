import logging
import traceback

pi = 3.1141592


class Math:
    try:
        def solv(self, r):
            return pi * (r ** 2)
    except BaseException:
        traceback.format_exc()
        pass
