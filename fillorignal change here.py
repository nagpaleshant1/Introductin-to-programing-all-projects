def my_python_project(mission):
# the main roll of this function is to check the answer from the user and the answer given by the admin is correct if yess then loop go again for second question
#It also helps in getting the ans value by replacing space[i] with given_answers[i]
#If ans is right it will print ans is right if not then invalid ans.
# also replacing the value in the qusetion with the answer value if it is true.
    line = mission[0]
    space = mission[1]
    given_answers = mission[2]
    count_length = len(space)
    for i in range(count_length):
        print line
        ans = ""
        while ans != given_answers[i]:
            ans = ques("What is your ans: " + space[i] + ": ")
# it helps in checking answer
            if ans != given_answers[i]:
                print "The ans is invalid"
        line = line.replace(space[i], given_answers[i])
        print "You are right! The Answer is:" + given_answers[i] + "' !\n"
    print line
    
easy = ["What is full form of HTML ___1___\n" +
        "What is full form of css ___2___ \n" +
        " What is full form of js ___3___\n" +
        " What is python called____4___\n",
        ["___1___", "___2___", "___3___", "____4___"],
        ["hypertext markup language", "cascading style sheets", "javascript", "programing language"]]

medium = ["For what purpose css is used ___1___\n " +
         "what purpose is html used:___2___\n" +
         " What you would prefer css or html for design :___3___" +
         " What is p tag used for : ___4____",
         ["___1___", "","___2___", "", "___3___", "___4____"],
         ["design", "framing", "css", "paragraph"]]


def chosse_level(level):
# It helps in checking that it is matching or not. == means check that it is equal or not if yes thn return statement will work if not then it moves to next statement.
    if level == "easy":
        return easy
    
    elif level == "medium":
        return medium
    
    else:
        return 0





def ques(ques1):
    return raw_input(ques1)



mission = 0

while mission == 0:
    level = raw_input("Select a level Easy or Medium: ")
    mission = chosse_level(str.lower(level))

#Calling this function to start this according to the level chossen
my_python_project(mission)
