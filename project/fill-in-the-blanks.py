# -*- coding: utf-8 -*-
# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!



# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

Answers = ['lvl1eins', 'lvl1zwei', 'lvl1drei'
           ,'lvl2eins', 'lvl2zwei', 'lvl2drei',
           'lvl3eins', 'lvl3zwei', 'lvl3drei']


Levels = ["Das ist ist Level 1. da kommen die lücken: __1__ __2__ __3__",
          "Das ist ist Level 2. da kommen die lücken: __1__ __2__ __3__",
          "Das ist ist Level 3. da kommen die lücken: __1__ __2__ __3__"]

#Start of Function
def getAnswer( i , Level):

    print 'Question Nr.', count+1
    Antwort = raw_input("Your answer is: ")
    print("Your answer is " + Antwort)
    if Antwort == Answers[(Level-1)*3+ i]:
        print("Du bist der King, das war richtig")
        return True
    else:
        print("nope.")
        return False
#End of Function
                          
print("Choose Level 1, 2, or 3!")
Level = input("Welches Level?")
print("Well, Level " + str(Level) )

print(Levels[Level-1])
count = 0
while (count < 3):                         
   b = getAnswer(count, Level)
   if b == True:
       count = count + 1
