from typing import Callable
from .models import Meter


class BinaryMeterNavigator:
    """
    Navigates time-labeled patterns according to rules.
    """

    def __init__(self, pattern_store):
        self.pattern_store = pattern_store

    def build_meter(self, label, start_time, end_time, step_mode="time", **params):
        return Meter(
            label=label,
            start_time=start_time,
            end_time=end_time,
            step_mode=step_mode,
            params=params
        )

    def traverse(self, meter: Meter, callback: Callable):
        if meter.step_mode == "time":
            patterns = self.pattern_store.get_patterns_between(
                meter.start_time, meter.end_time
            )
            for p in patterns:
                callback(p["pattern_sig"], p["time_label"])
