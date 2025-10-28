import numpy as np

import nidaqmx
from nidaqmx.constants import AcquisitionType
from setup.wave import generate_waveform

def write_to_device(waveform: np.ndarray):
    device_name = "PXI1Slot2"

    # Create a new task
    with nidaqmx.Task() as task:
        task.ao_channels.add_ao_voltage_chan(f"{device_name}/ao0")

        # Generate Wave
        sample_rate = 10000 # 10 kHz
        
        # Write waveform to the channel
        task.timing.cfg_samp_clk_timing(sample_rate, sample_mode=AcquisitionType.FINITE)
        task.write(waveform, auto_start=True)

        task.wait_until_done()
        task.stop()