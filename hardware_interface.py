# hardware_interface.py

class HardwareInterface:
    def _init_(self):
        # no hardware now
        pass

    def send_command(self, cmd):
        # For now do nothing
        print(f"[HARDWARE SIMULATION] Command = {cmd}")