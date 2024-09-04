#!/usr/bin/python3
import dis  # Module for analyzing Python bytecode

if __name__ == "__main__":
    with open("/tmp/hidden_4.pyc", "rb") as f:
        # Read the bytecode from the .pyc file
        code = f.read()

    # Disassemble the bytecode to extract names
    instructions = dis.get_instructions(code)
    names = [instr.argval for instr in instructions if instr.opname == "LOAD_NAME"]

    # Filter out names starting with "__" and sort alphabetically
    filtered_names = sorted(name for name in names if not name.startswith("__"))

    # Print the filtered names, one per line
    for name in filtered_names:
        print(name)
