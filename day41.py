#there ser two type of programming
# 1: procedural programming
# 2: Object oriented programming

#procedural programming is simple logic and function like:

def calculate_sum(x,y):
    print("The sum is:",x+y)

calculate_sum(2,4) #this is simple procedural programming 



#But have diifrent concept of classes objects constructor and many more things.
#Object oriented programming 
#classes and objects

class airticket:
    airlane_name="PIA"
    plain_no='2A314'
    airport="islamabad"
    flight_time="1:00"

    def info(self): #self is the paramenter to the current instance of the class(wo object jis par method call hora h)
     
        print(f"flight name is={self.airlane_name}, plain no is={self.plain_no}, airport location is={self.airport}, and timing of flight is={self.flight_time} ")

a=airticket()
a.airport="karachi"
a.airlane_name="air sial"
a.info()
print()
b=airticket()
b.airport="german munich"
b.airlane_name="Emirates"
b.info()