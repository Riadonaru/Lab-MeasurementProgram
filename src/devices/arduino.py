import serial
import time

# Adjust these for your setup
PORT = 'COM5'   # e.g., 'COM3' on Windows or '/dev/ttyUSB0' on Linux
BAUD = 115200

# Open serial connection
grbl = serial.Serial(PORT, BAUD, timeout=1)

# Give GRBL time to initialize
time.sleep(2)

# Flush startup text in buffer
grbl.reset_input_buffer()

print("Connected to GRBL on", PORT)
print("Type G-code commands, or 'exit' to quit.")

try:
    while True:
        cmd = input(">>> ").strip()
        if cmd.lower() in ['exit', 'quit']:
            break

        # Send command with newline
        grbl.write((cmd + '\n').encode())

        # Read GRBL response(s)
        while True:
            line = grbl.readline().decode().strip()
            if not line:
                break
            print("<--", line)

except KeyboardInterrupt:
    pass
finally:
    grbl.close()
    print("Connection closed.")
