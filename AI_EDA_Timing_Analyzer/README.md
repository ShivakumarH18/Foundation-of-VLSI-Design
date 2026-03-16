# AI EDA Timing Analyzer
CLI Python tool that analyzes EDA timing reports and detects timing violations.


// EDA Tool Timing Report

            Startpoint: FF1
            Endpoint: FF2
            Slack: -0.30

            Startpoint: FF3
            Endpoint: FF4
            Slack: 0.12

            Startpoint: FF5
            Endpoint: FF6
            Slack: -0.10

**===========================================================================================**
            
// CLI Interface Python Code 

import re

print("EDA Timing Analyzer CLI Tool")
print("--------------------------------")

# Read timing report
with open("report.txt", "r") as file:
    report = file.read()

# Extract timing paths
paths = re.findall(
    r"Startpoint:\s*(.*?)\s*Endpoint:\s*(.*?)\s*Slack:\s*(-?\d+\.\d+)",
    report,
    re.S,
)

# Convert slack to float
paths = [(s, e, float(sl)) for s, e, sl in paths]

slacks = [p[2] for p in paths]

worst_slack = min(slacks)

print("Timing report loaded successfully!")

while True:

    print("\nAvailable commands:")
    print(" summary")
    print(" show paths")
    print(" worst slack")
    print(" count violations")
    print(" explain")
    print(" fix")
    print(" exit")

    cmd = input("\nEnter command: ").lower()

    if cmd == "exit":
        print("Exiting tool...")
        break

    elif cmd == "summary":

        violations = [s for s in slacks if s < 0]

        print("\nTiming Summary")
        print("----------------")
        print("Total Paths:", len(paths))
        print("Worst Slack:", worst_slack)
        print("Timing Violations:", len(violations))

    elif cmd == "show paths":

        print("\nTiming Paths")
        print("----------------")

        for p in paths:
            print(f"Startpoint: {p[0]} → Endpoint: {p[1]} | Slack: {p[2]}")

    elif cmd == "worst slack":

        print("\nCritical Path Slack:", worst_slack)

    elif cmd == "count violations":

        violations = [s for s in slacks if s < 0]
        print("\nNumber of Timing Violations:", len(violations))

    elif cmd == "explain":

        if worst_slack < 0:
            print("\nExplanation:")
            print("Negative slack means the signal arrives later than required.")
            print("This creates a setup timing violation in the circuit.")
            print("The circuit may fail at the target clock frequency.")

        else:
            print("No timing violations detected.")

    elif cmd == "fix":

        print("\nSuggested Fixes:")
        print("- Reduce combinational logic delay")
        print("- Add pipeline registers")
        print("- Optimize synthesis")
        print("- Adjust clock period")

    else:
        print("Unknown command.")


**===================================================================================================**


# AI EDA Timing Analyzer

## Project Overview
This project implements a command line tool that analyzes EDA timing reports.

EDA tools generate large timing reports during chip design.  
It is often difficult for engineers to quickly understand these reports.

This tool reads a timing report file, extracts important timing information,
and helps the user identify timing violations.

The tool also explains timing issues and suggests possible fixes.



## Goal of the Project

The goal of this project is to build a simple prototype that can:

- Read EDA timing reports
- Detect timing violations
- Identify worst slack in the design
- Explain timing problems
- Suggest optimization fixes

This tool demonstrates how software and AI can assist engineers in analyzing
EDA tool outputs.



## Technologies Used

- Python
- Regular expressions (for parsing reports)
- Command Line Interface (CLI)



## Project Structure

AI_EDA_Timing_Analyzer
│
├── timing_analyzer.py
├── report.txt
└── README.md


### File Description

**timing_analyzer.py**
Main Python program that analyzes timing reports.

**report.txt**
Sample timing report used for testing the tool.

**README.md**
Documentation explaining the project.


## How the Tool Works

1. The program reads a timing report file.
2. It extracts important information such as:

- Startpoint
- Endpoint
- Slack value

3. The tool analyzes this data and calculates:

- Worst slack
- Total timing paths
- Timing violations

4. The user can interact with the tool using CLI commands.


## How to Run the Program

Open a terminal in the project folder and run:


python timing_analyzer.py report.txt


## Available Commands

After running the program, the following commands can be used:

summary
show paths
worst slack
count violations
explain
fix
exit


### Command Explanation

**summary**

Displays a summary of the timing report including:

- Total paths
- Worst slack
- Number of timing violations

**show paths**
Shows all timing paths extracted from the report.

**worst slack**
Displays the most critical slack value in the design.

**count violations**
Counts how many timing paths have negative slack.

**explain**
Explains the meaning of negative slack and timing violations.

**fix**
Provides suggestions to improve timing performance.

**exit**
Closes the program.


## Example Timing Report

Example input report:

Startpoint: U1
Endpoint: U10
Slack: -0.25

Startpoint: U2
Endpoint: U8
Slack: 0.10


Example output:

Timing Summary
Total Paths: 2
Worst Slack: -0.25
Timing Violations: 1


## Example Usage

python timing_analyzer.py report.txt

Enter command: summary
Enter command: show paths
Enter command: explain


## Suggested Fixes for Timing Violations

The tool suggests several possible fixes:

- Reduce combinational logic delay
- Add pipeline registers
- Optimize synthesis
- Adjust clock period


## Future Improvements

This project can be improved further by:

- Integrating AI models to explain reports automatically
- Supporting multiple EDA report formats
- Adding graphical visualization
- Integrating with open-source EDA tools


**===================================================================================================================**


        
