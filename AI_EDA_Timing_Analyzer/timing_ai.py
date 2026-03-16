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