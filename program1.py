
# Initialize memory
memory = {100: 12, 104: 8}

# Initialize registers
registers = {"R1": 0, "R2": 0, "R3": 0}

# Execute instructions
instructions = [
    ("LOAD R1, 100", lambda: registers.update(R1=memory[100])),
    ("LOAD R2, 104", lambda: registers.update(R2=memory[104])),
    ("ADD R3, R1, R2",
     lambda: registers.update(R3=registers["R1"] + registers["R2"])),
    ("STORE R3, 108",
     lambda: memory.update({108: registers["R3"]}))
]

for step, (instruction, execute) in enumerate(instructions, start=1):
    print(f"Step {step}: {instruction}")
    execute()

    print(f"Registers: R1 = {registers['R1']}, "
          f"R2 = {registers['R2']}, R3 = {registers['R3']}")

    if instruction.startswith("STORE"):
        print(f"Memory[108] = {memory[108]}")

    print()

print("Final memory location 108 =", memory[108])
