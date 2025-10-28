from setup.logger_setup import set_logger
from setup.wave import generate_waveform
from devices.pxi import write_to_device

import measurement.backup as backup

def main() -> None:
    # logger setup
    set_logger()
           
    # Project a wave
    write_to_device(generate_waveform())
    
    # connect & setup external instruments
    # run experiment
    return


if __name__ == "__main__":
    main()