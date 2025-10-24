import numpy as np
import matplotlib.pyplot as plt
import os
import logging

from config import SETTINGS


def generate_waveform(plot: bool = False) -> np.ndarray:
    """Generate and plot a Gaussian pulse waveform based on settings."""
    wave = SETTINGS['parameters']['wave']
    A = wave['amplitude']
    f = wave['frequency']
    phi = wave['phase']
    t0 = wave['offset']
    sigma = wave['width']

    x = np.linspace(-5, 5, 500)
    y = A * np.exp(-((x - t0)**2) / (2 * sigma**2)) * np.cos(2 * np.pi * f * x + phi)
    
    logging.info(f"Generated gaussian pulse with parameters: Amplitude: {A} Frequency: {f} Phase: {phi} Offset: {t0} Width: {sigma}")
    
    if plot:
        plt.plot(x, y)
        plt.title('Gaussian Pulse Waveform')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.grid(True)  
        plt.show()

    return y


