import json
from getpass import getpass
import random
from datetime import datetime
from datetime import timedelta

# Open "data.txt" in write mode and write the data to it in JSON format.
def saveChanges(dataList):
    f = open('data.txt', 'w')
    json.dump(dataList, f, indent=4)
    f.close()
def updateScores():
    f = open('scores.txt','a')
    f.write('\n'+name+" "+str(score)+" "+str(totalq))
    f.close()
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
try: 
    f = open('data.txt', 'r')
    data = json.load(f)
    f.close()
except (FileNotFoundError, ValueError):
    data = []

time_check = 0                  ## For timer

print('Welcome to the CLI based Quiz Appliaction')

while True:
    print('Choose [a]dmin, [p]layer or [q]uit')
    choice = input('>> ')
    if choice == 'a':
        print('Enter Your User Name')
        #Create new item and prompt for values
        user = input('User: ')
        password = getpass()
        if((user == 'a' and password == "b") or (user == 'c' and password == "d")): ## To add more users change here
            print("Welcome")
            while True:
                print("Choose [d]isplay, [a]dd or [b]ack to main menu")
                item = {}
                choice = input('>> ')
                if choice == 'a':
                    print("Enter Your Question followed by 4 Options")
                    item['Question'] = input('Enter Question: ')
                    item['A'] = input('Option A: ')
                    item['B'] = input('Option B: ')
                    item['C'] = input('Option C: ')
                    item['D'] = input('Option D: ')
                    item['Correct Answer'] = input('Enter Correct Answer: ')
                    data.append(item)
                    print("Question Added Succesfully")
                    print("Total Questions: "+str(len(data)))
                elif choice == 'b':
                    break;
                elif choice == 'd':
                    for item in data:
                        print("Question: "+ item['Question'])
                        print("Options:: \nA: %s\nB: %s\nC: %s\nD: %s"%(item['A'],item['B'],item['C'],item['D']))
                        print("Correct Answer: "+item['Correct Answer'])
                else:
                    # Print 'invalid choice' message
                    print('Invalid choice.')
                saveChanges(data)
        else:
            print("Invalid Username or Password")
    elif choice == 'p':
        name = input("Enter Your Name : ")
        print("Welcome "+str(name))
        score = 0
        print("How many questions you want to answer ?"+"Enter a number between 5 and "+str(len(data)))
        number = input()
        if(number.isdigit() and int(number) >= 5 and int(number) <= len(data)):
            totalq = int(number)
            totaltime = totalq*10
            randomQ = random.sample(range(0, len(data)), totalq)
            print("You will be given "+str(totaltime)+" seconds to complete the quiz")
            starttime = datetime.now()
            time_check = 0
            count = 1
            for i in randomQ:
                item = data[i]
                print("Question "+str(count)+":"+item['Question'])
                count = count+1
                print("Options:: \nA: %s\nB: %s\nC: %s\nD: %s"%(item['A'],item['B'],item['C'],item['D']))
                rem_time = (timedelta(seconds = totaltime)-(datetime.now()-starttime)).seconds
                print("Time Left "+str(rem_time))
                if rem_time > totaltime:
                    time_check = 1
                    break;
                print("Choose Correct Option: A, B, C, or D")
                selA = input()
                while True:
                    rem_time = (timedelta(seconds = totaltime)-(datetime.now()-starttime)).seconds
                    if selA in ['A','B','C','D']:
                        if(item[selA] == item['Correct Answer']):
                            print("Congrats")
                            rem_time = (timedelta(seconds = totaltime)-(datetime.now()-starttime)).seconds
                            if rem_time > totaltime:
                                time_check = 1
                                break;
                            score = score + 1;
                        else:
                            print("Wrong Answer")
                            print("Correct Answer is "+item['Correct Answer'])
                        break;
                    else:
                        print("Enter a valid input")
                        if rem_time > totaltime:
                            time_check = 1
                            break;
                        print("Time Left "+str(rem_time))
                        selA = input()
                if(time_check):
                    break;
                
            if(time_check):
                print("Times Up")
            print(name+"!!! You have scored "+str(score)+" out of "+str(totalq))
            updateScores()
        else:
            print("Invalid Input")
    elif choice == 'q':
        print('Goodbye!')
        break
    else:
        print('Invalid Choice.')
