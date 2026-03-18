import os
import re

# Function to describe ports
def describe_port(port):

    name = port.lower()

    if "clk" in name:
        return "Clock signal used for synchronization"

    elif "rst" in name or "reset" in name:
        return "Reset signal used to initialize the module"

    elif "data" in name:
        return "Data bus used for data transfer"

    elif "addr" in name:
        return "Address bus for memory access"

    else:
        return "General purpose signal"


# Parse RTL file
def parse_verilog(file):

    with open(file,'r') as f:
        code = f.read()

    module_match = re.search(r'module\s+(\w+)', code)

    if not module_match:
        print("Skipping file:", file)
        return None, None

    module = module_match.group(1)

    # NEW PORT PARSING (correct place)
    ports = []

    lines = code.splitlines()

    for line in lines:

        line = line.strip()

        if line.startswith("input") or line.startswith("output") or line.startswith("inout"):

            line = line.replace(",", "")

            parts = line.split()

            direction = parts[0]
            width = "1"

            names = []

            for part in parts[1:]:

                if "[" in part:
                    width = part
                else:
                    names.append(part)

            for name in names:
                ports.append((name, direction, width))

    return module, ports
# Generate documentation
def generate_doc(module, ports):

    doc = f"# {module} Module\n\n"

    # Overview
    doc += "## Overview\n"
    doc += f"This module implements the {module} hardware module.\n\n"

    # Block Description
    doc += "## Block Description\n"
    doc += "The module processes input signals and produces outputs according to the RTL logic defined in the design.\n\n"

    # Port Table
    doc += "## Port Table\n\n"
    doc += "| No. | Port Name | Direction | Width (bits) | Description |\n"
    doc += "|-----|-----------|-----------|--------------|-------------|\n"

    count = 1

    for name, direction, width in ports:

        desc = describe_port(name)

        doc += f"| {count:<3} | {name:<9} | {direction.capitalize():<9} | {width:<12} | {desc:<45} |\n"

        count += 1

    return doc

# Scan examples folder
folder="examples"

for file in os.listdir(folder):

    print("Found file:", file)

    if file.lower().endswith(".v"):

        filepath = os.path.join(folder, file)

        module, ports = parse_verilog(filepath)

        if module is None:
            continue

        doc = generate_doc(module, ports)

        os.makedirs("generated_docs", exist_ok=True)

        output = "generated_docs/" + module + "_doc.md"

        with open(output, "w") as f:
            f.write(doc)

        pdf_output = output.replace(".md", ".pdf")
        os.system(f"pandoc {output} -o {pdf_output}")

        print(module, "documentation generated")
