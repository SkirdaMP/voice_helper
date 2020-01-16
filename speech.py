import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print('search yandex')
        print('speak now!')
        audio = r3.listen(source)
    try:
        if 'старт' in r2.recognize_google(audio, language='ru-RU'):
            r2 = sr.Recognizer()
            url = 'https://yandex.ru/search/?text='
            with sr.Microphone() as source:
                print('search your query')
                audio = r2.listen(source)

                try:
                    get = r2.recognize_google(audio, language='ru-RU')
                    print(get)
                    # wb.get().open_new(url+get)
                except (sr.UnknownValueError, sr.RequestError) as e:
                    print('error: {}'.format(e))
        elif 'стоп' in r2.recognize_google(audio, language='ru-RU'):
            break
    except (sr.UnknownValueError, sr.RequestError) as e:
        print('error: {}'.format(e))

