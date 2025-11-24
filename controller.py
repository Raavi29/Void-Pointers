# controller.py
import time
from config import EXTEND_THRESHOLD, EXTEND_SECONDS, DEFAULT_GREEN, MAX_GREEN

class LogicEngine:
    def _init_(self):
        self.green_time_remaining = DEFAULT_GREEN

    def decide(self, vehicle_count):
        """
        Returns a dict describing what the system decided:
        - 'action': EXTEND or NORMAL
        - 'duration': seconds of green
        """
        if vehicle_count > EXTEND_THRESHOLD:
            self.green_time_remaining = min(
                MAX_GREEN,
                self.green_time_remaining + EXTEND_SECONDS
            )
            return {"action": "EXTEND", "duration": EXTEND_SECONDS}

        return {"action": "NORMAL", "duration": DEFAULT_GREEN}