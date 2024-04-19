katz_deli = []

def line(katz_deli):
    if(katz_deli == []):
        print("The line is currently empty.")
    else:
        names_list = [str(katz_deli.index(person) + 1) + ". " + person for person in katz_deli]
        names_str = " ".join(names_list)
        print(f'The line is currently: {names_str}')

def take_a_number(katz_deli, name):
    position = len(katz_deli) + 1
    katz_deli.append(name)
    print(f'Welcome, {name}. You are number {position} in line.')

def now_serving(katz_deli):
    if(katz_deli == []):
        print("There is nobody waiting to be served!")
    else:
        next_person = katz_deli.pop(0)
        print(f'Currently serving {next_person}.')