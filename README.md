# Microsoft-Math-OCR
This script perform an OCR on the screenshot and return a LATEX equation to your clipboard.

## Usage with screenshot
Simply run equationOCR.py in the terminal, it will start an OCR on "screenshot_temp.png" under the same directory.

The script post an HTTP request to Microsoft Bing, using the same API as the mobile APP Microsoft Math Solver.

## Usage with BetterTouchTool
1. Add a _Keyboard Shortcut_ for _All Apps_, record a shortcut you would like to use.
2. Assign an _Action_ to the trigger. Choose "Capture Screenshot (Configuration)" from the list.
3. Configure screenshot action.
  - Path: Choose <your_path> where the script file is
  - File name: screenshot_temp
  - Format: PNG
  - After capture: Run terminal command
    - Terminal command: cd <your_path>; <your_python_path> equationOCR.py

## How to find <your_python_path>
If you are not using a default python from the operating system, then type "which python" in your terminal.
