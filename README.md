# Microsoft_Python_U2
Create get_names() Function to collect input of 5 unique element names
The function accepts no arguments and returns a list of 5 input strings (element names)
define a list to hold the input
collect input of a element name
if input it is not already in the list add the input to the list
don't allow empty strings as input
once 5 unique inputs return the list
Create the Program flow
import the file into the Jupyter Notebook environment
use !curl to download https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt" as elements1_20.txt
open the file with the first 20 elements
read one line at a time to get element names, remove any whitespace (spaces, newlines) and save each element name, as lowercase, into a list
Call the get_names() function
the return value will be the quiz responses list
check if responses are in the list of elements
Iterate through 5 responses

compare each response to the list of 20 elements
any response that is in the list of 20 elements is correct and should be added to a list of correct responses
if not in the list of 20 elements then add to a list of incorrect responses
calculate the % correct
find the the number of items in the correct responses and divide by 5, this will result in answers like 1.0, .8, .6,...
to get the % multiple the calculated answer above by 100, this will result in answers like 100, 80, 60...
hint: instead of dividing by 5 and then multiplying by 100, the number of correct responses can be multiplied by 20
Print output
print the Score % right
print each of the correct responses
print each of the incorrect responses
create Element_Quiz then paste code on edX submission page
# [] create Element_Quiz
# [] copy and paste in edX assignment page
print("list any 5 of the first 20 elements in the Period table")
def get_names():
    elements = []
    while len(elements)<5:
        user_inp = input("Enter the name of an element: ").lower()
        if user_inp != "":
            if user_inp not in elements:
                elements.append(user_inp)
            else:
                print(user_inp,"was already entered")
    return elements
! curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt
elements1_20 = open('elements1_20.txt','r')
elements1_20.seek(0)
elem_list = []
elem_names = elements1_20.readline().strip()
while elem_names:
    elem_list.append(elem_names.lower())
    elem_names = elements1_20.readline().strip()
input_list = get_names()
correct = 0
correct_answers = ''
wrong_answers = ''
for answer in input_list:
    if answer in elem_list:
        correct += 1
        correct_answers += answer.title() + ' '
    else:
        wrong_answers += answer.title() + ' '
print (correct*20, "% correct")
print ("Found:", correct_answers)
print ("Not Found:", wrong_answers)
elements1_20.close()


# [] create Element_Quiz
