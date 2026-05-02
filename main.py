import speech_recognition as sr
import os

# Nếu dùng Raspberry Pi thật, bạn có thể dùng RPi.GPIO
# import RPi.GPIO as GPIO

# GPIO setup (demo)
LIGHT_PIN = 17

def setup_gpio():
    print("GPIO setup complete")
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setup(LIGHT_PIN, GPIO.OUT)

def turn_on_light():
    print("Light ON")
    # GPIO.output(LIGHT_PIN, GPIO.HIGH)

def turn_off_light():
    print("Light OFF")
    # GPIO.output(LIGHT_PIN, GPIO.LOW)

def process_command(command):
    command = command.lower()
    print(f"Command: {command}")

    if "turn on light" in command:
        turn_on_light()
    elif "turn off light" in command:
        turn_off_light()
    else:
        print("Command not recognized")

def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        return command
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError:
        print("API error")

    return ""

def main():
    setup_gpio()

    while True:
        command = listen()
        if command:
            process_command(command)

if __name__ == "__main__":
    main()
