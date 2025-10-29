import pyvisa
from devices.device import Device

class LecroyOscilloscope(Device):
    
    def __init__(self, id: str):
        super().__init__(id)
        self.rm = pyvisa.ResourceManager()
        self.scope: pyvisa.resources.Resource = self.rm.open_resource(self.id)
        self.scope.write("TIME_DIV 1E-3")   # Set time/div to 1 ms
        self.scope.write("C1:TRACE ON")     # Turn on channel 1
        self.scope.write("C2:TRACE ON")     # Turn on channel 2

    def identify(self):
        return self.scope.query("*IDN?")

    def arm_trigger(self):
        self.scope.write("ARM")
        
    def fetch_waveform(self, channel: int = 1):
        return self.scope.query_binary_values(f"C{channel}:WAVEFORM? DAT1", datatype='B', container=bytes)
 