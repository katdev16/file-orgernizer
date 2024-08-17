


from FileManger import FileManager

from Speech import Speech





manager = FileManager()


# print("enter command:")
# UserInput = input()




mic = Speech()

mic.speech_to_text_from_microphone()

txt = mic.text

input = txt.split(" ")
print(input)


if input[0]=="create":
  
    manager.create_folder(input[1])

