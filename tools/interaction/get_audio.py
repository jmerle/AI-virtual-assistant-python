
from settings.settings import interaction_setting as it 
from settings.logs import *
from system.screen_text import thoughts_processing
from tools.interaction import speak

def get_audio_text():
    msg = input("(Write Something)-> ")
    return msg


def get_audio_microphone():
    try :
        import speech_recognition as sr
        r = sr.Recognizer()
        logger.info("Ready to listen")
        input('(Press enter to give voice commands...')
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            logger.info('adjusted ambient noise') 
            print('(Say someting) ->',sep=' ')
            audio = r.listen(source,timeout=8, phrase_time_limit=20)   
            said = ""
            logger.info('audio listened')
            thoughts_processing('voice heared, trying to recognize')
            try :
                said = r.recognize_google(audio)
                if said == '':
                    thoughts_processing("Haven't got it sir, please try again")
                    said = get_audio_microphone()
                logger.info(said)
            except Exception as e:
                logger.info("Exception occured "+str(e))
                thoughts_processing("Haven't got it sir, please try again")
                said = get_audio_microphone()
        return said
    except :
        return get_audio_text() 


def get_audio():
    if it['voice_read+voice_reply']:
        return get_audio_microphone()
    elif it['text_read']:
        return get_audio_text()
    else: 
        logger.error('Your mircrophone audio and read text both are disabled, enable them from settings')
        print('Your BOT do not have any listing power, give him the power from settings -_-')
        return 'NONE'



# def get_audio_microphone():
#     prit('Here')
#     try :
#         import speech_recognition as sr
#         r = sr.Recognizer()
#         r.adjust_for_ambient_noise(source)
#         with sr.Microphone() as source:
#             while True :
#                 audio = r.listen(source)
#                 try :
#                     said = r.recognize_google(audio)
#                     logger.info(said)
#                     if  'jarvis' in said:
#                         speak('Listening sir.')
#                         try :
#                             audio = r.listen(source)
#                             said = r.recognize_google(audio)
#                             return said
#                             break
#                         except :
#                             said =  'Have not got it sir, please try again'
#                     else :
#                         continue
#                 except Exception as e:
#                     logger.info(str(e))
#         return said
#     except :
#         return get_audio_text() 
