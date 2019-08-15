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

