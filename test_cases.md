# Test Cases – Simulated Device Monitoring and Alert System

Tested by: Adrian Flores        Date: October 18, 2026

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose 1 | Five readings: 28, 31, 35, 37, 29 | The program displayed all five initial readings: 28 °C, 31 °C, 35 °C, 37 °C, and 29 °C. | Pass |
| TC02 | Choose 2, enter 33 | Reading added successfully | The program displayed "Reading added successfully." The reading 33 was added to the list. | Pass |
| TC03 | Choose 2, enter abc | Rejected; list unchanged | The program displayed "Invalid input. Enter a whole number only." The list remained unchanged. | Pass |
| TC04 | Choose 2, enter -5 | Rejected; list unchanged | The program displayed "Invalid reading. Enter a value from 0 to 100." The list remained unchanged. | Pass |
| TC05 | Choose 2, enter 120 | Rejected; list unchanged | The program displayed "Invalid reading. Enter a value from 0 to 100." The list remained unchanged. | Pass |
| TC06 | Add 30, then choose 3 | 30 °C -> WARNING | The program displayed "Reading added successfully." and classified 30 °C as WARNING. | Pass |
| TC07 | Choose 3 | 35 °C -> WARNING | The program displayed "35 °C -> WARNING." | Pass |
| TC08 | Choose 4 using initial data | Total 160, Avg 32.00, Min 28, Max 37, status ATTENTION REQUIRED | The summary showed 5 readings, total 160, average 32.00 °C, minimum 28 °C, maximum 37 °C, NORMAL 2 (40.00%), WARNING 2 (40.00%), CRITICAL 1 (20.00%), and ATTENTION REQUIRED. | Pass |
| TC09 | Enter 9 | Error message; menu shown again | The program displayed "Invalid choice. Please enter a number from 1 to 5." and showed the menu again. | Pass |
| TC10 | Choose 5 | Exit message; program ends | The program displayed "Thank you for using the Device Monitoring System." and ended. | Pass |

## Bugs Found and Fixed

The hardest test was TC06 because it checks the boundary value of 30 °C. The program correctly classifies 30 °C as WARNING because readings from 30 through 35 are classified as WARNING.