import pyttsx3
import speech_recognition as sr
import sys


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали " + task)
    except (sr.UnknownValueError, sr.RequestError):
        print('Не понятно, повторите')
        task = command()
    return task


def sayText(task):
    if "стоп" in task:
        sys.exit(0)
    else:
        print(task)

def main():
    while True:
        sayText(command())

if __name__ == "__main__":
    main()