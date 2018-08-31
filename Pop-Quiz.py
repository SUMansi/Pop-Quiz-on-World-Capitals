#Import the required packages
import os, csv, random

#To change the current working directory as mentioned
os.chdir("M:/Programming for Business Analytics/Python")

def capitalQuiz(fileName, noQuestions):
    
    #read countries, capitals from file
    InFile = csv.reader(open(fileName, 'r'))
    #To store the data into a list
    Data = list(InFile)
    
    
    #Dictionary for storing capitals keyed by countries. 
    capitals = {}
    for a in Data:
        capitals[a[0]] = a[1]
    
    Correct = 0
    Wrong = 0
    
    #Loop over the number of questions
    for questionNum in range(0,noQuestions):
        
        #Randomly select countries for the question 
        Country = ''.join(random.sample(list(capitals.keys()),1))
        
        #Print the Quiz Question
        print("Question" + str(questionNum + 1) + " : What is the capital of " + Country + "?" )
        
        #Remove the correct answer from the list
        L = list(capitals.values())
        L.remove(capitals[Country])
        
        #Randomly select 3 wrong answers and the correct answer
        Options = (random.sample(L,3)) + [capitals[Country]]
        
        #Shuffle the order of answer options
        random.shuffle(Options)
        
        #Print the answer options
        print("\n" + "1: " + Options[0] + "\n" + "2: " + Options[1] +"\n" + "3: " + Options[2] + "\n" + "4: " + Options[3] )
        
        #Take Input from user
        while True:
            Answer = raw_input("Please enter correct answer (number only). ")
            if str(Answer).isalpha():
                print("Invalid Value! Please enter number only")
                continue
            elif int(Answer) not in [1,2,3,4]:
                print("Please enter the choice between 1 & 4")
                continue
            else:
                Answer = int(Answer)
                break
         
         
        #Condition to match the answer choice with correct answer
        if Options[Answer-1] == capitals[Country]:
            print ("Correct!")
            Correct = Correct + 1
        else:
            print ("Correct Answer is " + capitals[Country])
            Wrong = Wrong + 1
         
    #Return the result of the quiz   
    results = {'Correct' : Correct , 'Wrong' : Wrong}
    return results

#The main function for the script    
def main():
    fileName = input("Enter the FileName (in brackets): ") #'capitals.csv'
    
    while True:
            noQuestions = raw_input("Number of Quiz Question: ")
            if str(noQuestions).isalpha():
                print("Invalid Value! Please enter number only")
            elif int(noQuestions) not in range(1,202):
                print("Please enter the number of questions between 1 & 201")
                continue
            else:
                noQuestions = int(noQuestions)
                break
                    
    results = capitalQuiz(fileName,noQuestions)
    print results

#Program Execution
main()


        
    

    
    


   


