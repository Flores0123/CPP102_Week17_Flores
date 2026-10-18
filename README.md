# Simulated Device Monitoring and Alert System
 
**Student Name:** (Adrian S. Flores)
**Student Number:** (2601293)
**Section:** (1 CpE - B)
 
## Project Description
This Python program simulates a device monitoring system that stores temperature readings. It classifies each reading as NORMAL, WARNING, or CRITICAL based on the given temperature limits. It also calculates a summary of the readings and displays an overall system status.
 
## Features
- View all stored temperature readings
- Add a new reading (whole numbers from 0 to 100 only)
- Classify every reading
- Generate a numerical summary and overall status
- Reject invalid menu choices and invalid readings
 
## Requirements
- Python 3 (no external packages)
 
## How to Run
1. Open a terminal inside the Week17 folder.
2. Type: python device_monitor.py
   (On macOS or Linux, type: python3 device_monitor.py)
 
## Sample Output
SIMULATED DEVICE MONITORING SYSTEM
----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit
Enter choice: 1

CURRENT READINGS
----------------
Reading 1 : 28 °C
Reading 2 : 31 °C
Reading 3 : 35 °C
Reading 4 : 37 °C
Reading 5 : 29 °C

## Test Cases
I performed 10 tests. __ passed and __ failed.
Full details are in test_cases.md.
 
## Known Limitations
- Readings are stored only while the program is running. They are lost when the program closes.
- Only whole-number readings from 0 to 100 are accepted.
 
## Reflection
When I discovered this final project, I practiced using lists, loops, selection statements, functions, parameters, and return values in one program. I learned how to classify readings using conditions and calculate a summary using loops. One important part was validating user input so invalid readings would not be added to the list. I would improve the project in the future by allowing readings to be saved between program sessions and by connecting it to a real device.