import os

def process_command(command):
    command = command.lower()

    if "turn on light" in command:
        print("Light ON")
        # GPIO control here
    elif "turn off light" in command:
        print("Light OFF")
    else:
        print("Command not recognized")

while True:
    command = input("Say something: ")
    process_command(command)
