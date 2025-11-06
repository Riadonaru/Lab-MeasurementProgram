import serial
import time
import logging


class Laser():
    
    def __init__(self):
        self._active = False

    def __enter__(self):
        self._active = True
        self.port = 'COM1'
        self.baudrate = 115200
        self.timeout = 2        # Timeout in seconds
        self.terminator = '\n'  # Set the terminator to newline, or change it according to your device
        self.ser = serial.Serial(port=self.port, baudrate=self.baudrate, timeout=self.timeout)
        
        # Set feedback from device to be active
        res = self.send_command("Set, Interface, 0, Echo, On")
        logging.info(f"Laser feedback: {res}")
        
        if self.ser.is_open:
            print(f"Connected to {self.port} at {self.baudrate} baud.")
            
        return self

    # Function to close the serial connection
    def __exit__(self, exc_type, exc_value, traceback):
        self._active = False
        if self.status:
            self.off()
            
        self.ser.close()
        print("Connection closed.")
        
    def __check_active(self):
        if not self._active:
            raise RuntimeError("The use of 'Laser' class is only premitted with 'with' context manager!")
        
        
    # Function to send a command to the device
    def send_command(self, command: str):
        """Send a command to the device and capture the response

        Args:
            command (str): This will be sent to the device

        Raises:
            RuntimeError: If there was an error with communication

        Returns:
            str: The answer to the query
        """
        try:
            self.ser.write(command.encode() + self.terminator.encode())  # Send the command with terminator

            res =  [bin.decode().strip() for bin in self.ser.readlines()]
            if len(res) == 0 or res[0] != command:
                raise RuntimeError("Invalid command syntax - check manual for list of commands")
            
            if len(res) < 2:
                return "ok"
            
            return res[1]
        except Exception as e:
            logging.error("Error communicating with laser: {command}")
            return f"{command}: err"
    
    @property
    def status(self) -> bool:
        """
        Reads sensor data from laser to update status in real time

        Raises:
            ValueError: if there is a problem with the response.

        Returns:
            bool: True if the laser is on and false if off
        """
        res = self.send_command("Get, SensorHead, 0, Laser")
        self._status = bool(int(res))
        return self._status

    def on(self) -> None:
        """
        Turns the laser on.

        Raises:
            ValueError: If there was a communication problem
        """
        self.__check_active()
        self.send_command("Set, SensorHead, 0, Laser, 1")
        if self.status:
            return
        
        raise ValueError("The laser did not turn on! Check command syntax")
    
    def off(self) -> None:
        """
        Turns the laser off

        Raises:
            ValueError: If there was a communication problem
        """
        self.send_command("Set, SensorHead, 0, Laser, 0")
        if not self.status:
            return
        
        raise ValueError("The laser did not turn off! Check command syntax")