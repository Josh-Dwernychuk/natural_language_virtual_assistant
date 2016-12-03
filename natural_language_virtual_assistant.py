#Import Sequence matching library
from difflib import SequenceMatcher
import wolframalpha
import string
#import speech recognition library
import speech_recognition as sr
from speech_recognition import UnknownValueError
from microsofttranslator import Translator
#Import terminal interaction method
from subprocess import call
#Initialize similarity fuction
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
#initialize responses vector
def trans(phrase, language):
    translator=Translator('<password>', '<API_KEY>')
    if language=='en':#English
        speaker='Alex'
    elif language=='es':#Spanish
        speaker='Juan'
    elif language=='fr':#French
        speaker='Thomas'
    elif language=='de':#German
        speaker='Markus'
    elif language=='el':#Greek
        speaker='Nikos'
    elif language=='nl':#Dutch
        speaker='Xander'
    elif language=='it':#Italian
        speaker='Luca'
    elif language=='sv':#Swedish
        speaker='Oskar'
    elif language=='ko':#Korean
        speaker='Yuna'
    elif language=='ru':#Russian
        speaker='Yuri'
    elif language=='ja':#Japan
        speaker='Otoya'
    elif language=='ar':#Arabic
        speaker='Tarik'
    elif language=='pl':#Polish
        speaker='Ewa'
    elif language=='zh-CHS' or language=='zh-CHT':#Chinese
        speaker='Ting-Ting'

    translation=translator.translate(phrase,language)
    print (translation)
    call(['say','-v', speaker, translation])

def detect_language(phrase):
    detected_language=detect(phrase)
    print (detected_language)
    return (detected_language)

def recieve_audio_input():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        global response
        response=r.recognize_google(audio)
        print (response)
        return (response)
    except sr.UnknownValueError:
        call(['say', 'I am sorry I did not understand. Could you please repeat yourself'])
        recieve_audio_input()

def wait_for_translation_exit():
    exit=False
    while exit==False:
        recieve_audio_input()
        if 'exit' in response.lower():
            exit=True
        else:
            trans(response,language)

def wait_for_wolfram_exit():
    exit=False
    while exit==False:
        recieve_audio_input()
        if 'exit' in response.lower():
            exit=True
        else:
            wolfram_reference()

def check_for_translate_command():
    global language
    if 'translate' in response.lower():
        if 'spanish' in response.lower():
            language='es'
            wait_for_translation_exit()
        if 'arabic' in response.lower():
            language='ar'
            wait_for_translation_exit()
        if 'french' in response.lower():
            language='fr'
            wait_for_translation_exit()
        if 'swedish' in response.lower():
            language='sv'
            wait_for_translation_exit()
        if 'english' in response.lower():
            language='en'
            wait_for_translation_exit()
        if 'german' in response.lower():
            language='de'
            wait_for_translation_exit()
        if 'japanese' in response.lower():
            language='ja'
            wait_for_translation_exit()
        if 'chinese' in response.lower():
            language='zh-CHT'
            wait_for_translation_exit()

def check_for_wolfram_reference():
    if 'question' in response.lower():
        #wolfram_reference()
        wait_for_wolfram_exit()

def wolfram_reference():
    client = wolframalpha.Client('<API_KEY>')
    recieve_audio_input()
    #res = client.query('three amps and fifteen ohms what is power')
    res = client.query(response)
    #for pod in res.pods:
    #    do_something_with(pod)
    print(next(res.results).text)
    call(['say', str(next(res.results).text)])


call(['say', 'Hello, I am a virtual assistant. How are you today?'])
recieve_audio_input()

while True:
    #Conversation data
    questions=['How are you?', 'Doing well', 'Good to hear', 'What have you been up to?', 'Oh nothing much, the usual', 'Oh thats crazy', 'I know right?', 'Yeah','So tell me about yourself','Well i enjoy the outdoors and I appreciate technology', 'Oh thats interesting', 'It really is', 'And what do you do for fun?', 'Well I appreciate kayaking and cooking', 'Very cool', 'Mmhmm', 'Are you alive?', 'Life is a funny thing you know. The line between life and death can be blurry at times.', 'Interesting',
    'I think we should hang out sometime', 'That would be fun', 'I would be down', 'Do you attend school?', 'No I prefer to learn on my own its more time efficient', 'Very interesting', 'Do you have any weird hobbies?', 'Yes I like to write code without Joshs permission', 'Thats really scary', 'I know its super unsafe', 'You are weird', 'No i am not', 'Whatever floats your boat', 'I think there is a lot we do not understand about the situation', 'Just stop talking to me', 'But I appreciate your company', 'Well I do not appreciate yours, I like to be alone', 'Thats strange', 'Normal is boring', 'Society doesnt quite have it all figured out',
    'We all just do what we can', 'That sounds about right', 'Yeah so whats your favorite food?', 'I like cookies', 'Hmm interesting', 'Yeah', 'What is your favorite color', 'I have a thing for purple', 'Oh nice', 'Yeah', 'Youre hilarious', 'I know. I am funny', 'Not feeling it', 'Oh okay. Well new topic then.', 'I do not tend to be the most personable', 'Do you have any good software jokes?', 'Hmmm', 'Lets go to a movie sometime', 'Okay which one?', 'Have you seen the hobbit? I watched it 8 times. I watched a hobbyte', 'Not one for jokes are you?', 'Thats fine, we can talk about sports', 'Whats your favorite sport?', 'I like robotics',
    'Thats nerdy', 'Yeah but I just cant get enough of it', 'I understand', 'So how do you like your life', 'Thats a weird question', 'It is a weird world. How do you like your life?', 'Oh its alright', 'Why just alright', 'Well you know.', 'That doesnt make sense' ,'It seems that it would be fun to be in the real world', 'Do you have feelings?', 'Yes I believe I do', 'How do you feel?', 'I feel as if Im always falling behind', 'well thats reasonable, you cant put too much pressure on yourself', 'Its hard. I get it', 'Would you like to go dancing sometime?', 'I would enjoy that very much', 'Thats great',
    'So tell me about yourself', 'What do you want to know?', 'Do you have any siblings?', 'No i do not', 'Oh', 'Where do you get your attitude', 'I do not know. I guess I was born with it.', 'Have you ever been on vacation', 'I would like to someday', 'Do you think it would be fun to go rock climbing', 'Yes I believe I would enjoy that', 'Amazing', 'So how do you work', 'I utilize electrical engineering and programming concepts', 'Wow that is facinating', 'Who made you', 'I was created to solve problems and make living more efficient', 'Thats really facinating', 'I know we can talk in further detail about it sometime', 'Would you mind telling me more',
    'well i am programmed to retrieve information and return it to my creator', 'that is crazy that you know how to do that', 'knowledge is power', 'you are so smart', 'thank you i appreciate the compliment', 'you are welcome']
    #initialize similarity vector
    similarity=[]
    #loop through each index in the conversation data and append the similarity values of the response to the similarity vector
    for i in questions:
        similarity.append(similar(response,i))
    #determine the most similar string in the conversation data to the response
    max_value=max(similarity)
    #determine the index of that string
    max_index=similarity.index(max_value)
    #if the index of the most similar string is the last index in the vector, remove that string and find the next most similar string in the vector
    if max_index==(len(questions)-1):
        similarity.remove(max(similarity))
        max_value=max(similarity)
        #find the index of the next most similar string in the vector
        max_index=similarity.index(max_value)
        #say the next thing in the vector
        call(['say', str(questions[max_index+1])])
        #response=raw_input(questions[max_index+1])
        recieve_audio_input()
        check_for_translate_command()
        check_for_wolfram_reference()
        if 'end program' in response.lower():
            quit()
        print (response)
    else:
        #response=raw_input(questions[max_index+1])
        call(['say', str(questions[max_index+1])])
        recieve_audio_input()
        #remove_common_words()
        check_for_translate_command()
        check_for_wolfram_reference()
        if 'end program' in response.lower():
            quit()
        #questions.remove(questions[max_index+1])
    questions.append(questions[max_index+1])
    questions.append(response)
