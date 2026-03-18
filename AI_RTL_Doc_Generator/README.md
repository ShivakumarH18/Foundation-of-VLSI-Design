AI RTL Documentation Generator Project


# AI RTL Documentation Generator

## Overview
This project is a Python-based tool that automatically generates documentation from Verilog RTL modules.

## Features
- Parses RTL modules
- Extracts:
  - Module name
  - Port names
  - Direction
  - Bus width
- Generates:
  - Overview
  - Block Description
  - Port Table
- Converts Markdown to PDF using Pandoc

## Project Structure
AI_RTL_Doc_Generator/
│
├── src/              # Python script
├── examples/         # RTL files
├── generated_docs/   # Output documentation
└── README.md

## Usage

Run the tool:

```bash
python src/doc_generator.py

**=========================================================================================**
##Example: INPUT 
module full_adder (
    input a, b, cin,
    output sum, cout
);
assign sum = a ^ b ^ cin;
assign cout = (a & b) | (b & cin) | (a & cin);
endmodule

OUTPUT: **Markdown file/format**
# full_adder Module

## Overview
This module implements the full_adder hardware module.

## Block Description
The module processes input signals and produces outputs according to the RTL logic defined in the design.

## Port Table

| No. | Port Name | Direction | Width (bits) | Description |
|-----|-----------|-----------|--------------|-------------|
| 1   | a         | Input     | 1            | General purpose signal                        |
| 2   | b         | Input     | 1            | General purpose signal                        |
| 3   | cin       | Input     | 1            | General purpose signal                        |
| 4   | sum       | Output    | 1            | General purpose signal                        |
| 5   | cout      | Output    | 1            | General purpose signal                        |


**PDF Format**

<img width="715" height="541" alt="image" src="https://github.com/user-attachments/assets/061484eb-63df-4afc-a903-6937c811146e" />

**===========================================================================================**
