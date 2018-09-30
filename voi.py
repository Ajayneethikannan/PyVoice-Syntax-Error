import os
import speech_recognition as sr
import regexify
import delete
import time
from websocket import create_connection
import json




ws = create_connection("ws://127.0.0.1:8000/ws/route/")

def create(FILE):
    cmd="touch "+FILE
    os.system(cmd)

class Converter:
    songFileName="test.wav"
    
    
    def record(self):
        command=("arecord %s --duration=5")%(self.songFileName)
        os.system(command)
    def convert(self):
        r = sr.Recognizer()
        sound = sr.AudioFile(self.songFileName)
        with sound as source:
            audio = r.record(source)
            line=(r.recognize_google(audio))
        return line
 


is_over=False
code=""
converter_object = Converter()
indent=0
long_sentence_flag=False
long_sentence=""
write=False


while(not is_over):
    arr = {'type':'insert', 'data':''}
   
    converter_object.record()
    try:
        line=converter_object.convert()
    except sr.UnknownValueError:
        print("Sorry that wasn\'t caught on the microphone.Repeat yourself")
        continue
    line=line.lower()
    if("end code" in line):
        is_over=True
        continue

    if("cancel line"  in line):
        continue
    if(line[0:4] == 'undo'):
        arr['type'] = 'undo'

    if('snap' in line):
        freq = line.count('snap')
        line = line.replace('snap', '')
        arr['type'] = 'snap'

    if("enter" in line):indent+=1
    elif("exit" in line):indent-=1
    if(indent>0):line="    "*indent+line 


    line=regexify.code_creator(line)
    arr['data'] = line + ' '
    print(line)

    ws.send(json.dumps(arr))



