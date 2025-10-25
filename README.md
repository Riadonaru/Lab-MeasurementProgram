# 🧪 Lab Measurement Program

A modular Python-based control system for laboratory experiments — integrating PXIe devices, oscilloscopes, Arduino boards, and laser meters.

---

## 🚀 Getting Started

### 1️⃣ Requirements
- **Python 3.10+** installed  
- (Optional) **NI-DAQmx** drivers for PXIe devices  
- (Optional) **VISA** drivers for instruments (e.g., LeCroy scopes)

---

### 2️⃣ Installation

Run the setup script once to create a virtual environment and install dependencies:

```bash
.\setup.bat
```

---

### 3️⃣ Configuration

Edit your experimental parameters in:  
experiment.json

This file defines all the runtime parameters for your experiment (device configuration, waveform settings, timing, etc.).

---

### 4️⃣ Running the Program
Start the measurement program using:

```bash
.\run.bat
```

#### The software will:  
- Load configuration  
- Initialize connected instruments  
- Execute the measurement loop  
- Log data and save results automatically  

---

### 📁 Project Structure  
|Folder  |  Description                                             |
|--------|----------------------------------------------------------|
|logs/	 |   Stores program log files                               |
|res/	   |   Stores experiment results (measurements, plots, etc.)  |
|src/	   |   Contains all Python source code                        |
|tmp/	   |   Backup checkpoints and temporary data                  |
|venv/	 |   Python virtual environment and interpreter             |

---

### ⚙️ Scripts
Script  Purpose  
setup.bat	 - Creates virtual environment and installs all dependencies  
run.bat	   - Runs the experiment using the configured environment  

---

### 🧩 Configuration File: experiment.json

This file defines the experimental setup, such as:

- Measurement parameters  
- Device channels and sampling rates  
- Waveform definitions  
- Output and logging preferences  
(Detailed documentation for each field will be added here later.)

---

### 🧰 Tech Overview

Language: Python  
Core Libraries: nidaqmx, numpy, matplotlib, pyvisa, pyserial  
Logging: Built-in Python logging (file + console)  
Structure: Modular, expandable architecture for hardware and software simulation  
