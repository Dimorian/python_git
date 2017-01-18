

Answers = ['ASS', 'Bayer', '20','yes'
           ,'codeine', 'dripping', 'FUCK','25'
           ,'opioid', 'potent', 'MJ','propofol']


Levels = ["The acronym of Aspirin is __1__. It was developed by the __2__AG in the early __3__th century. Is aspirin an anti-inflammatory product?__4__",
          "Listen to the song loud from the rap artis Mac Miller and tell what he has in his cup:__1__. And what are the __2__ bitches trying to do?__3__! Last but not least, tell me the age of Mr. Mac Miller:__4__",
          "Sufentanil is a synthetic __1__. It is the most __2__ painkiller that mankind knows. Do you remember Michael Jackson aka __3__? He died to the abbusive use of __4__. :("]

#Start of Function
def getAnswer( i , Level):

    print 'Blank Nr.', count+1
    Answer = raw_input("Your answer is: ")
    print("Your answer is " + Answer)
    if Answer == Answers[(Level-1)*4+ i]:
        print("That's right")
        return True
    else:
        print("Nope. Try again")
        return False
#End of Function
                          
print("choose your level of pain: easy, medium, or hard!")

b = True 
while(b):
    b = False 
    Enter = raw_input("At which difficulty do you like to win at?")
    if Enter == ("easy"):
        Level = 1;
    elif Enter == ("medium"):
        Level = 2;
    elif Enter == ("hard"):
        Level = 3;
    else:
        b = True



    
print("Well, i'd hope you don't suffer that much " + str(Level) )

print(Levels[Level-1])
count = 0
while (count < 4):                         
   b = getAnswer(count, Level)
   if b == True:
       count = count + 1
