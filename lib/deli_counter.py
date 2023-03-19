def line(line):

    if len(line) > 0:
        i = 0
        positions = []
        for person in line:
            i += 1
            positions.append(f"{i}. {person}")
        positions.insert(0, "The line is currently:")
        print(" ".join(positions))
        
    else:
        print("The line is currently empty.")
        return "The line is currently empty."

def take_a_number(katz_deli, name):

    katz_deli.append(name)
    positions = []
    i = 0
    for person in katz_deli:
        i += 1
        positions.append(f"Welcome, {person}. You are number {i} in line.")
    print(positions[-1])

def now_serving(line):
    
    if len(line) > 0:
        up_next = line.pop(0)
        print(f"Currently serving {up_next}.")
    else:
        print("There is nobody waiting to be served!")

