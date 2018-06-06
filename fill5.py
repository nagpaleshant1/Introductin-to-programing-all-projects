def quiz(x):
    return xinput(x)


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
        while user_answer != user_answers[i]:
            user_answer = quiz`("user ans is: "+ spaces[i])
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


easy = ["Procedural _ing_verb_ involves creating _adverb_ clear and unambigous \n" +
                "_plural_noun_ for a _noun_ to follow. It may be easy to tell a person how to \n" +
                " _verb_ a deck of cards, but getting a _noun_ to do that requires more thought.\n" +
                " But once you've learned to think this way you'll find that computers can do it much faster.\n",
                ["_ing_verb_", "_adverb_", "_plural_noun_", "_noun_", "_verb_"],
                ["thinking", "perfectly", "instructions", "computer", "sort"]]

medium = ["Abstract _ing_verb_ means finding similarity, or as _plural_noun_  would say,\n " +
                "generality among seemingly different things. In this Nanodegree you will _verb1_ hundreds of Udacity web pages.\n" +
                " It would be _adjective_ for a programmer to specifically program each of these pages individually. \n " +
                " The Udacity programmers used the power of what's called _noun_ to _verb2_ unnecessary repetition of work. \n",
                ["_ing_verb_", "_plural_noun_","_verb1_", "_adjective_", "_noun_", "_verb2_"],
                ["thinking", "programmers", "visit", "impractical", "abstraction", "avoid"]]




a=0

while a==0:
    imp=input('chosse your level easy or medium')
    a=z(str.lower(imp))
    
my_first_game(z)





