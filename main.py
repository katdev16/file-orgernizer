
from FileManger import FileManager

from Speech import Speech


manager = FileManager()
mic = Speech()
mic.speech_to_text_from_microphone()
txt = mic.text
input = txt.split(" ")


while txt.lower()!="exit":


    if input[0]=="create":
        print(input)
        manager.create_folder(input[2])
       
        mic = Speech()
        mic.speech_to_text_from_microphone()
        txt = mic.text
        input = txt.split(" ")

    if input[0]=="exit":
        # print(input)
        print("program exited")
        break



    if input[0]=="delete":
        print(input)
        manager.delete_folder(input[2])

        mic = Speech()
        mic.speech_to_text_from_microphone()
        txt = mic.text
        input = txt.split(" ")



    if input[0]=="move":
        src_file = manager.current_directory.join(input[1])
        dest_file = manager.current_directory.join(input[3])

        print(input)
        manager.move_file(src_file,dest_file)

        mic = Speech()
        mic.speech_to_text_from_microphone()
        txt = mic.text
        input = txt.split(" ")

    if input[0].lower()=="new":
        mic = Speech()
        mic.speech_to_text_from_microphone()
        txt = mic.text
        manager.new_file(input[2],txt)

        print("file")


    else:
        print(input)
        print("Not availble command")

        mic = Speech()
        mic.speech_to_text_from_microphone()
        txt = mic.text
        input = txt.split(" ")