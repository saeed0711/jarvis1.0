import datetime 

# voices = engine.getProperty('voices')        # getting details of current voice
#                                              # changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)    # changing index, changes voices. 1 for female


# volume=engine.getProperty('volume')
# #volume=engine.setProperty('volume',0)
# volume1=engine.getProperty('volume')
# print(volume)
# print(volume1)
# print(voices)

import pyttsx3
# engine = pyttsx3.init()                      #initialising engine in loop otherwise it will not talk back continously

# engine = pyttsx3.init()                      #initialising engine in loop otherwise it will not talk back continously
def speak(audio):          #defining function
    engine = pyttsx3.init()                      #initialising engine in loop otherwise it will not talk back continously
    # print("from speak")
    # engine = pyttsx3.init(driverName='sapi5')  #explicitly defining sound driver name 
    engine.setProperty('rate', 200)
    # voices=engine.getProperty('voices')        #getting voices in array 0 for male 1 for female
    # engine.setProperty('voice', voices[index].id)  #changing to female
    engine.say(audio)       #4 white space called indentation to group a functon or loops 
    engine.runAndWait() 
   
def voiceSetting(ind): 
    # print("from setting")
    if ind== 1:
       indx=0 
       str='jarvis' 
    if index== 2:
       indx=1; 
       str='friday' 
    t=time()
    speak(f"hello i am {str} 1.0 ",indx)
    speak("right now time is ",indx)
    speak(t,indx)
    

def time():
    
    time=datetime.datetime.now().strftime("%H:%M:%S")
#    print(time)
    speak("current  time is ")
    speak(time)
#    return time
#    speak(time)

def date():
    year=str(datetime.datetime.now().year)
    # print(  type(year))
    month=datetime.datetime.now().strftime("%B")
    # print(  type(month))

    day=str(datetime.datetime.now().day)
    # print(  type(day))

    speak("the current date is")
    speak(year)
    speak(month)
    speak(day)
    
    
def greet():
    # speak("hello")
    hour = datetime.datetime.now().hour
    print(  type(hour))
    if hour >=6 and hour < 12:
        speak("good morning !")
    elif hour >=12 and hour < 18:
        speak("good afternoon !")
    elif hour >=18 and hour < 24:
        speak("good evening !")
    else:
        speak("Good Night !")
def wishme():
    speak("welcome back sir!")  
    greet()
    # date()
    time()
    speak("jarvis at your service , please tell me how can i help you!")

# wishme()
# while True:
#     index = int( input("enter 1 for jarvis voice \nenter 2 for friday voice \n"))
#     # if audio.strip().lower() =="exit":
#     #     #   if audio.strip().lower() == "exit":
#     #     break
#     voiceSetting(index)


# print("Spoken.")    it will not print coz above loop is infinite 


def takeCommandCMD():
    query= input("please tell me how can i help you?\n")
    return query

if __name__=="__main__":
    # date()
    wishme()
    while True:

        query=takeCommandCMD().lower()

        if "time" in query:
            time()

        elif "date" in query:
            date()


