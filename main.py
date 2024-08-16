


from FileManger import FileManager


manager = FileManager()


print("enter command:")
UserInput = input()




input = UserInput.split(" ")

if input[0].lower()=="command":
    if input[1]=="create":
        if input[2]=="name":
            manager.create_folder("name")

