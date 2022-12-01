## import das bibliotecas
import speech_recognition as sr
import pyttsx3
import pyaudio 
import datetime 
import wikipedia
import pywhatkit
import googlesearch

## definicao dos objetos
au = sr.Recognizer()
maquina = pyttsx3.init()

## metodo que executa comando de voz
def executa_comando():
    try:
        #configura som, faz o print ouvindo..,
        with sr.Microphone() as source:
            print('ouvindo...')
            voz = au.listen(source)
            comando = au.recognize_google(voz, language='pt-Br')
            comando = comando.lower()
            #comando remove o sexta feira na hora de analisar o que escuta
            if 'Sexta-feira' in comando:
                comando = comando.replace('Sexta-Feira', '')
                maquina.say ('comando') 
                maquina.runAndWait
    except:
        #printa caso microfone esteja com problema
        print('Microfone não está ok')
    return comando

def comando_voz_usuario():
    comando = executa_comando()
    ## informa a hora
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say ('Agora são' + hora)
        maquina.runAndWait()
    #comando "procure por" que pucha informação da wikipédia
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    #comando que aciona biblioteca do google
    elif 'pesquise por' in comando:
        pesquisar = comando.replace('pesquise por', '')
        resultado = googlesearch.search(pesquisar, lang="pt-br", num_results=10)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
     ## toca musca atraves do youtube
    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando Música')
        maquina.runAndWait()
    
    
# executa as funcao base de comando de voz do usuario
comando_voz_usuario()
#https://python-googlesearch.readthedocs.io/en/latest/index.html#googlesearch.search
#https://python-googlesearch.readthedocs.io/en/latest/