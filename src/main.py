from setup.logger_setup import set_logger
from setup.wave import generate_waveform

def main() -> None:
    # logger setup
    set_logger()
    
    # load experiment settings
    generate_waveform(plot=True)
    
    # connect & setup external instruments
    # run experiment
    return

main()