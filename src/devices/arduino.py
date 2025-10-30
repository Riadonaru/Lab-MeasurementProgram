import serial
import time

# --- Adjust this port and baud rate for your setup ---
PORT = 'COM5'
BAUD = 115200
    
# --- Connect to GRBL ---
grbl = serial.Serial(PORT, BAUD)
time.sleep(2)  # Wait for GRBL to initialize

# --- Initialize GRBL and XY plane ---
init_commands = [
    '$X',   # Unlock GRBL
    'G17',  # Select XY plane
    'G21',  # Set units to millimeters
    'G90',  # Absolute coordinates
    'G54'
]

for cmd in init_commands:
    grbl.write((cmd + '\n').encode())
    time.sleep(0.2)

print("✅ GRBL initialized for XY motion")    
    
# --- Define function to move to a point ---
def move_to(x, y, feed_rate=500):
    """
    Move the GRBL-controlled machine to (x, y) in mm.
    feed_rate is in mm/min.
    """
    gcode = f"G01 X{x:.3f} Y{y:.3f} F{feed_rate}"
    print(f"→ Sending: {gcode}")
    grbl.write((gcode + '\n').encode())
    time.sleep(0.1)
    
    # Read and print GRBL response
    while grbl.in_waiting:
        response = grbl.readline().decode().strip()
        print(f"← {response}")

# --- Example usage ---
move_to(0, 0)     # Return to origin
time.sleep(20)

# --- Close connection when done ---
grbl.close()
print("🔌 Connection closed.")
