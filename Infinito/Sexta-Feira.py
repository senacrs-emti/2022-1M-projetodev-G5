from email.mime import audio
import speech_recognition as sr
import pyttsx3
import pyaudio 
import datetime 
import wikipedia
import pywhatkit
import googlesearch
import google 


audio = sr.Recognizer()
maquina = pyttsx3.init()




def executa_comando():

    try:
        with sr.Microphone() as source:
            print('ouvindo...')

            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-Br')
            comando = comando.lower()
            if 'Sexta-feira' in comando:
                comando = comando.replace('Sexta-Feira', '')
                maquina.say ('comando') 
                maquina.runAndWait

    except:
        print('Microfone não está ok')


    return comando



def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say ('Agora são' + hora)
        maquina.runAndWait()
    elif 'procure por' in comando:
        procurar = comando.replace(' procure por', '')
        wikipedia.set_lang('pt-br')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'pesquise por' in comando:
        pesquisar = comando.replace(' pesquise por', '')
        googlesearch.set_lang('pt-br')
        resultado = googlesearch.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comando:
        # 
        musica = comando.replace('toque', '')
        #
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando Música')
        maquina.runAndWait()
    
    

comando_voz_usuario()