#kon banega crorpatti(*WarisHayat)---->list,tuple(exercise)

question=["Q1:Who is the Prime Minister of pakistan?","Q2:which fruit is the national fruit in pakistan?","Q3:Highest Mountain in tha Pakistan?","Capital of paistan is?"]
answer=("imran_khan","mango","k2","islamabad")
CorrectAnswer=0  
prizeperquestion=300000
prize=1200000

print("*************Welcome to Kon banyga cror pati show*************")
print()
name=input("Enter you name:")
print(f"********Welcome ! to kon banyga crorpatti show:{name}*********")
print()

def round1(name):
    print()
print()

print(question[0])
choose1=input("""
Note:Type the right answer only without spaces.(Question worht 3 lac)
1: Nawaz_Shareef
2: Asif_Ali_zardari
3: Imran_Khan(wthout_space)
4: Shahbaz_Shareef
""")

if choose1.lower()== answer[0]:
    print()
    print("Your answer is correct")
    CorrectAnswer+=1 
else:
    print("Incorrect Answer")
    print("Correct Aanswer is=",answer[0])
    
#now for question 2:
print()
print()
print(question[1])
choose2=input("""
Note:write down the name thorugh keyboard without spaces.(Question worht 3 lac):
1: Banana
2: Mango
3: watemelon
4: avacado
""")

if choose2.lower()==answer[1]:
    print()
    print("your answer is correct:")
    CorrectAnswer+=1
else:
    print("Incorrect Answer.")
    print("Correct Answer is=",answer[1])
print()
print()
#now for question3:
print(question[2])
choose3=input("""
Note:write down the name thorugh keyboard (Question worht 3 lac):
1: Nanga_parbat
2: k2
3: ganga_choti
4: fairy_medows
""")

if choose3.lower()==answer[2]:
    
    print()
    print("Your answer is correct")
    CorrectAnswer+=1
else:
    print("Incorrect Answer.")
    print("Correct Aanswer is=",answer[2])
print()
print()
#now for question4:
print(question[3])
choose4=input("""
Note:write down the capital of pakistan only (Question worht 3 lac):
1: karachi
2: lahor
3: islamabad
4: Multan
""")

if choose4.lower()==answer[3]:
    
    print()
    print("Correct Your answer is right")
    CorrectAnswer+=1
    
else:
    print("Incorrect Answer.")
    print("The correct Answer is ",answer[3])

if CorrectAnswer==4:
    CorrectAnswer=1200000
elif CorrectAnswer==3:
    prizeperquestion=prizeperquestion*3
elif CorrectAnswer==2:
    prizeperquestion=prizeperquestion*2
elif CorrectAnswer==1:
    prizeperquestion=prizeperquestion*1
else:
    prizeperquestion=0

print()
print()
print()
print()
print("************Match Results baord******************")
print("The match is finish now:")
print("The match total prize was:",prize)
print("Your total correct anser are:",CorrectAnswer)
print("Your total wining amount is:",prizeperquestion)



round1(name)