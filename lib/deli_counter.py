# Initialize an empty list to represent the queue
katz_deli = []

def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        # Create a formatted string to display the current line
        current_line = "The line is currently:"
        for i, person in enumerate(katz_deli, start=1):
            current_line += f" {i}. {person}"
        print(current_line)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        next_person = katz_deli.pop(0)
        print(f"Now serving {next_person}.")

# test
line(katz_deli)  
take_a_number(katz_deli, "Clive")  
take_a_number(katz_deli, "David")  
line(katz_deli)  
now_serving(katz_deli) 
line(katz_deli)  
