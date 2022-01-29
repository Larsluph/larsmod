"""
basic python chronometer (support laps)
"""

from time import perf_counter
from collections import namedtuple


class Chrono:
    """
    Stores the start and stop time to compute the time passed between these two
    """

    time_tuple = namedtuple("chrono_time", "days,hours,minutes,seconds,ms")

    def __init__(self):
        self._begin = 0

    def start(self) -> None:
        """
        Start/Reset the chronometer
        """
        self._begin = perf_counter()  # stores the begin time
        return None

    def lap(self) -> time_tuple:
        """
        Return elapsed time since last start
        """

        lap = perf_counter() - self._begin  # compute time delta in seconds

        # compute all time units from lap
        ms = round(lap % 1 * 1000)
        seconds = round(lap)
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        # return a named tuple
        return self.time_tuple(days, hours, minutes, seconds, ms)
