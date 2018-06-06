
def quiz(x):
    return input(x)


def wrong_ans():
    print "ans is incrrect!"


def my_first_game(z):
    sentance=z[0]
    space=z[1]
    user_answers=z[2]
    count=len(space)
    for i in range(count):
        print sentence
        user_answer=""
        while user_answer!= user_answers[i]:
            user_answer=quiz`("user ans is: "+ spaces[i])
        if user_answer != user_answer[i]:
            wrong_ans()
        sentence=sentence.replace(space[i],user_answers[i])
        print "This is a correct answer"+ user_answers[i]
    print sentence


def chosse_level(imp):
    if imp == 'easy':
        return easy
    else if imp == 'medium':
        return medium
    else:
        return 0

easy='''What is full form of html __1___? What is full form of css ____2____
what is use of html ____3___'''
['Hypertext Markup Language','Cascading Style Sheets','Webpage Making']


medium='''Which of the following is a way to associate styles with your __1__ document
In HTML we have ___2__ heading tags for writing heading.
In HTML we have __3__ tag for typing paragraphs ?
'''
['HTML','Six','Three']



a=0

while a==0:
    imp=input('chosse your level easy or medium')
    a=z(str.lower(imp))
    
my_first_game(z)





