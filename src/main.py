from setup import generate_waveform, set_logger


def main() -> None:
    # logger setup
    set_logger()
    
    # load experiment settings
    generate_waveform(plot=True)
    
    # connect & setup external instruments
    # run experiment
    return

main()