#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("./Input/Letters/starting_letter.txt") as file:
    content = file.readlines()


with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
    print(names)


def change_first_line(name):
    return f"Dear {name},\n"


def write_letter(file_name):
    with open(f"./Output/ReadyToSend/{file_name}_letter.txt", 'w') as write:
        content[0] = change_first_line(file_name)
        for a in content:
            write.write(a)


for name in names:
    write_letter(name[:-1])
