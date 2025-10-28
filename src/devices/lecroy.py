import pyvisa


# Initialize VISA resource manager
rm = pyvisa.ResourceManager()
scope = rm.open_resource("USB0::0x05FF::0x1023::2816N63242::0::INSTR")

# Identify the instrument
print(scope.query("*IDN?"))

# Example: set timebase and acquire waveform
scope.write("TIME_DIV 1E-3")   # Set time/div to 1 ms
scope.write("C1:TRACE ON")     # Turn on channel 1
scope.write("C2:TRACE ON")     # Turn on channel 2
scope.write("ARM")             # Arm the trigger

# Fetch waveform data
data = scope.query_binary_values("C1:WAVEFORM? DAT1", datatype='B', container=bytes)
print(f"Received {len(data)} bytes of waveform data.")
