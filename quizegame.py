#python quize game]


questions = (("toady date? :  ",
 " today vara? : ",
  " today breakfast? :  ",
   " today snana? :"))
options = (("a .26 ", "b .27" , "c .28" , "d .29"),
    ("a .mon ", "b .sun" , "c .wed" , "d .thu"),
     ("a .no ", "b .yes" , "c .idk" , "d .may be"),
      ("a .no ", "b .yes" , "c .ithi" , "d .not"))
guessess = []
answers = ("d","b","a", "a")
question_num=0

for question in questions:
            print(question)
            print("_____________________")
            for option in options[question_num]:
                print(option)           
            
            guess = input("enter your guess :  ")
            guessess.append(guess)
            if guess == answers[question_num]:
                print("correct")
            else:
                print("incorrect")
                
            question_num+=1
            
print("answer : ",end = "")
for answer in answers:
    print(answer,end="   ")
    print()    
    
print("guess: ",end="")
for guess in guessess:
    print(guess,end="   ")
    print()
    