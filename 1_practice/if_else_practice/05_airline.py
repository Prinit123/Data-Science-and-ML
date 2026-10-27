print("Airline reservation System = >")

print("select state destination :->")
print("1.Gujrat")
print("2.mumbai")
print("3.india")

state = int(input("which state to go ,choose  state no : "))
print("choose class Eco,busi,first")
clas = input("chose class : ")
if(state == 1):
           if(clas == 'Eco'):
                      print("ticket price : 10,000 for Economy")
           elif(clas == 'busi'):
                      print("ticket price : 15,000 for Business")
           elif(clas == 'first'):
                      print("ticket price : 20,000 for first")
           else:
                      print("Envalid class selected")
elif(state == 2):
           if(clas == 'Eco'):
                      print("Ticket price : 15,000 for Economy")
           elif(clas == 'busi'):
                      print("ticket price : 20,000 for Business")
           elif(clas == 'first'):
                      print("ticket price : 25,000 for first")
           else:
                      print("Envalid class selected")
elif(state == 3):
           if(clas == 'Eco'):
                      print("Ticket price : 35,000 for Economy")
           elif(clas == 'busi'):
                      print("ticket price : 40,000 for Business")
           elif(clas == 'first'):
                      print("ticket price : 55,000 for first")
           else:
                      print("Envalid class selected")
else:
           print("flight not avialable")
           
           