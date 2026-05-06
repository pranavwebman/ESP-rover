Here's a professional README.md file for your ESP-Rover project:

```markdown
# ESP-Rover 🤖

A remote-controlled rover powered by ESP32 with Android control application.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Installation Guide](#installation-guide)
  - [Linux Setup](#linux-setup)
  - [ESP32 Firmware Upload](#esp32-firmware-upload)
  - [Android Application](#android-application)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## 🚀 Overview

ESP-Rover is a WiFi-controlled rover built on the ESP32 platform. The project includes:
- MicroPython firmware for ESP32 (`boot.py`, `main.py`)
- Android control application (`roverapp.apk`)
- Automated setup script for Thonny IDE on Linux

## ✨ Features

- **WiFi Control** - Control the rover wirelessly via ESP32's WiFi capability
- **Android Interface** - Dedicated mobile app for rover control
- **Easy Setup** - Automated installation script for Linux environments
- **Real-time Response** - Low-latency control mechanism

## 🔧 Hardware Requirements

| Component | Specification |
|-----------|---------------|
| Microcontroller | ESP32 (any variant) |
| Motor Driver | L298N or similar |
| Motors | DC Motors (x2 or x4) |
| Power Supply | 7.4V-12V battery pack |
| Chassis | Rover/robot chassis |
| Wheels | 2-4 wheels with appropriate mounts |

## 💻 Software Requirements

- **Operating System**: Ubuntu 20.04+ / Debian-based Linux distributions
- **Python**: 3.6 or higher
- **Thonny IDE**: For ESP32 firmware upload
- **Android**: 8.0 (Oreo) or higher for control app

## 📥 Installation Guide

### Linux Setup

#### 1. Install Thonny IDE

Run the automated installation script:

```bash
chmod +x thonny_install.sh
./thonny_install.sh
```

The script will:
- Update system packages
- Install Thonny and required dependencies
- Configure Thonny for ESP32 MicroPython support

#### 2. Manual Thonny Installation (Alternative)

```bash
sudo apt update
sudo apt install thonny -y
```

### ESP32 Firmware Upload

#### Using Thonny IDE:

1. **Connect ESP32** to your computer via USB cable
2. **Launch Thonny**:
   ```bash
   thonny
   ```
3. **Configure Interpreter**:
   - Go to `Tools → Options → Interpreter`
   - Select `MicroPython (ESP32)`
   - Choose the correct COM port (usually `/dev/ttyUSB0` or `/dev/ttyACM0`)

4. **Upload Firmware Files**:
   - Open `boot.py` in Thonny
   - Click `File → Save As → MicroPython device`
   - Save as `boot.py`
   - Repeat for `main.py`

5. **Reset ESP32** - Press the reset button on your ESP32 board

### Android Application

#### Install Rover Control App:

**Method 1: Direct Installation**
```bash
# Copy APK to Android device
adb install roverapp.apk
```

**Method 2: Manual Installation**
1. Transfer `roverapp.apk` to your Android device
2. Enable "Install from unknown sources" in Settings
3. Open the APK file and follow installation prompts

## 📁 Project Structure

```
ESP-Rover/
├── README.md              # Project documentation
├── boot.py                # ESP32 boot initialization script
├── main.py                # ESP32 main rover control logic
├── roverapp.apk           # Android control application
└── thonny_install.sh      # Linux installation script for Thonny
```

## 🎮 Usage

### Starting the Rover:

1. **Power on the ESP32** rover
2. **Connect to WiFi** (credentials configured in `boot.py`)
3. **Launch the Rover App** on your Android device
4. **Connect to ESP32** using the IP address shown in serial monitor
5. **Control the rover** using on-screen joystick/buttons

### Default WiFi Configuration:

Edit `boot.py` to set your WiFi credentials:

```python
ssid = 'Your_WiFi_SSID'
password = 'Your_WiFi_Password'
```

## 🔍 Troubleshooting

| Issue | Solution |
|-------|----------|
| ESP32 not detected | Check USB cable and install drivers: `sudo apt install python3-serial` |
| Permission denied (USB port) | Run: `sudo usermod -a -G dialout $USER` and reboot |
| Thonny can't find MicroPython | Flash MicroPython firmware to ESP32 first |
| Android app won't install | Enable "Unknown sources" in Android settings |
| Connection timeout | Ensure device and ESP32 are on same WiFi network |

### Common Commands

```bash
# Check if ESP32 is connected
ls -l /dev/ttyUSB* /dev/ttyACM*

# Give serial port permissions
sudo chmod 666 /dev/ttyUSB0

# Monitor ESP32 serial output (baud rate 115200)
screen /dev/ttyUSB0 115200
```

## 📝 License

This project is licensed under the MIT License - see below:

```
MIT License

Copyright (c) 2024 Pranav Webman

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

## 👥 Contributors

- **Pranav Webman** - *Initial work*

## 📧 Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Contact: [Your Email]

---

**⭐ Star this repository if you found it helpful!**
``
