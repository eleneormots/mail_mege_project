#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def main():
    path_starting_letter="C:/Users/user/Desktop/100 day challange/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt"
    path_invited_names="C:/Users/user/Desktop/100 day challange/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt"
    with open(path_invited_names) as invited_names:
        names=invited_names.readlines()
        for name in names:
            name=name.strip()
            result_path = "C:/Users/user/Desktop/100 day challange/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend"
            with open(path_starting_letter, mode="r") as starting_letter:
                lines=starting_letter.readlines()
                result_path+=f"/letter to {name}"
                with open(result_path,mode="x") as new_letter:
                    for line in lines:
                        new_letter.write(line.replace("[name]", name))
if __name__ == "__main__":
    main()