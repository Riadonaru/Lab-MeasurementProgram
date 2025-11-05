import serial
import time


class Laser():
    
    def __init__(self):
        self.port = 'COM1'  # Change this to the correct COM port (e.g., 'COM3', '/dev/ttyUSB0', etc.)
        self.baudrate = 115200
        self.timeout = 2  # Timeout in seconds
        self.terminator = '\n'  # Set the terminator to newline, or change it according to your device

    def __enter__(self):
        self.ser = serial.Serial(port=self.port, baudrate=self.baudrate, timeout=self.timeout)
        if self.ser.is_open:
            print(f"Connected to {self.port} at {self.baudrate} baud.")
            
        return self

    # Function to send a command to the device
    def send_command(self, command: str):
        try:
            # Write the command to the serial port
            self.ser.write(command.encode() + self.terminator.encode())  # Send the command with terminator

            # Read the response from the device
            response = self.ser.readlines()
            print("\nResponse: ")
            for line in response:
                print(f"<--- {line.decode('ascii').strip()}")

        except serial.SerialException as e:
            print(f"Error: {e}")

    # Function to close the serial connection
    def __exit__(self, exc_type, exc_value, traceback):
        self.ser.close()
        print("Connection closed.")

if __name__ == "__main__":
    with Laser() as las:
        cmd = input("---> ")
        while cmd != "exit":
            las.send_command(cmd)
            cmd = input("---> ")


