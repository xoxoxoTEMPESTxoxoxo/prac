import pickle 

import os
file_path = "example.txt"
if os.path.exists(file_path):
    print(f"The file {file_path} exists.")

    
sum1=0
with open ("sale.dat","rb") as F1:
    #d= {'a': 100, 'b': 200, 'c': 300}
    #pickle.dump(d,F1)
    #x=pickle.load(F1)
    #print(x.keys())
    #print(list(x.keys())[1])
    #print(x.values())
    #print(list(x.values())[0])
    #for i in x:      
      #print (x[i])
    #l=[('a',100),('b',100),('c',100)]  # zip(l1,l2) 
    #pickle.dump(l,F1)
    #print(pickle.load(F1))
    while True:
        try:
            l=pickle.load(F1)
            for i in l : # python goes through keys of dictionary in for loop of Dictionary
                sum1 = sum1 +l[i]

        except:
            break
print (sum1)

def count_word_occurrence(file_path, word_to_count):
try:

with open('file_path, 'r') as file:
          
 text = file.read() # returns string 
# Split the text into words and count occurrences of the target word
 words = text.split()
 word_count = words.count(word_to_count) # counts occurance of word_... in string 
 return word_count

except FileNotFoundError:
 return -1 # Return -1 to indicate that the file was not found
# File path (adjust to your file's location)
file_path = "test.txt"
word_to_count = "the"
# Call the function to count the occurrence of the word "the"
occurrences = count_word_occurrence(file_path, word_to_count)
if occurrences >= 0:
 print(f'The word "{word_to_count}" occurs {occurrences} times in the file.')
else:
 print('File not found.')


def hash_display(file_path):

 try:
    with open(file_path, 'r') as file:
    content = file.read()
    formatted_content = "#".join(content) # join for list,string as well 
    print(formatted_content)
    content = file.read(10)  # Read first 10 characters
    file.seek(0)  # Move the pointer to the beginning
    new_content = file.read(5)  # Read next 5 characters from the start



 except FileNotFoundError:
   print(f"File '{file_path}' not found.")

