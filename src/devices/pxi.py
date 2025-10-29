import numpy as np

import nidaqmx
from nidaqmx.constants import AcquisitionType
from setup.wave import generate_waveform
from devices.device import Device

class Pxi(Device):

    def __init__(self, id):
        super().__init__(id)
        
    def write_waveform(self, waveform: np.ndarray) -> None:
        with nidaqmx.Task() as task:
            task.ao_channels.add_ao_voltage_chan(f"{self.id}/ao0")
            sample_rate = 10000 # 10 kHz
            
            # Write waveform to the channel
            task.timing.cfg_samp_clk_timing(sample_rate, sample_mode=AcquisitionType.FINITE)
            task.write(waveform, auto_start=True)

            task.wait_until_done()
            task.stop()