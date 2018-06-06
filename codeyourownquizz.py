
def game_ask_question(question):
    # This procedure is needed for correctly working of the procedure gameplay(levels).
    return raw_input(question)

def game_incorrect_answer():
    # This procedure is used to show the user that his/her answer is not correct.
    print "Incorrect! Please try again!"

def gameplay(level):
    # This procedure takes the nested list from procedure levels(dificulty), depending on what level of difficulty
    #  the user has choosen - easy,medium or hard.Then runs a for loop in certain range, ask a question for the user
    #  and evaluate the answer.If the asnwear is correct its replacing it in the text by using replace function.
    text = level[0]
    blanks = level[1]
    answers = level[2]
    questions_count = len(blanks)
    for i in range(questions_count):
        # print text
        print text
        # ask question
        answer = ""
        while answer != answers[i]:
            answer = game_ask_question("What should go in blank " + blanks[i] + ": ")
        # evaluate answer
            if answer != answers[i]:
                game_incorrect_answer()
        text = text.replace(blanks[i], answers[i])
        print "That's correct! Answer is '" + answers[i] + "' !\n"
    # print final text
    print text

def levels(difficulty):
    # This procedure is determining which one of the nested list are going to be used to play the game.
    # Each one of the lists are representing a level of difficulty.
    if difficulty == "easy":
        return procedural_thinking
    
    elif difficulty == "medium":
        return abstract_thinking
    
    elif difficulty == "hard":
        return technological_empathy
    
    else:
        return 0

# MAIN

procedural_thinking = ["Procedural _ing_verb_ involves creating _adverb_ clear and unambigous \n" +
                "_plural_noun_ for a _noun_ to follow. It may be easy to tell a person how to \n" +
                " _verb_ a deck of cards, but getting a _noun_ to do that requires more thought.\n" +
                " But once you've learned to think this way you'll find that computers can do it much faster.\n",
                ["_ing_verb_", "_adverb_", "_plural_noun_", "_noun_", "_verb_"],
                ["thinking", "perfectly", "instructions", "computer", "sort"]]

abstract_thinking = ["Abstract _ing_verb_ means finding similarity, or as _plural_noun_  would say,\n " +
                "generality among seemingly different things. In this Nanodegree you will _verb1_ hundreds of Udacity web pages.\n" +
                " It would be _adjective_ for a programmer to specifically program each of these pages individually. \n " +
                " The Udacity programmers used the power of what's called _noun_ to _verb2_ unnecessary repetition of work. \n",
                ["_ing_verb_", "_plural_noun_","_verb1_", "_adjective_", "_noun_", "_verb2_"],
                ["thinking", "programmers", "visit", "impractical", "abstraction", "avoid"]]

technological_empathy = ["'Technological Empathy' _plural_verb_ in many forms.\n" +
                " For example, _noun1_ empathy is the ability to _verb1_ what a _noun2_ is, \n " +
                " how it works, and what it's good and bad at doing. A _noun3_ is a tool, \n " +
                " as are the _plural_noun_1_ we use and the programming _plural_noun_2_ used to _verb2_ them. \n " +
                " It's almost _adjective_ to program anything substantial without a basic undearstanding of how these tools work. \n",
                ["_plural_verb_", "_noun1_", "_verb1_", "_noun2_", "_noun3_", "_plural_noun_1_", "_plural_noun_2_", "_verb2_", "_adjective_" ],
                ["comes", "computer", "undearstand", "computer", "computer", "programs", "languages", "write", "impossible"]]
# Ask user to select his/her level
level = 0

while level == 0:
    difficulty = raw_input("Please select level of difficulty - Easy, Medium or Hard: ")
    # Choosing text according to the selected level
    level = levels(str.lower(difficulty))

# Start gameplay with the chosen text
gameplay(level)


