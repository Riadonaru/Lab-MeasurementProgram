from setup.logger_setup import set_logger
from setup.wave import generate_waveform
import measurement.backup as backup

def main() -> None:
    # logger setup
    set_logger()
           
    # load experiment settings
    generate_waveform(plot=True)
    
    # connect & setup external instruments
    # run experiment
    return


if __name__ == "__main__":
    main()