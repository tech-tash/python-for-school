# Program tthat will be used to log the results of an athletics long jump contest
# Name: Natasha Mazibuko
# Date: 29 July 2024

def main():
     print("***** Long Jump Information System *****")
     competitors = {}
     Names = []
     num = 1
     print("Please enter the names of competitors. (Press return when done.)")

     while True:
    
          print("Competitor no. {}:".format(num))
          name = input()   
    
          if not name:
               break
          
          Names.append(name)
    
          num = num + 1
     
     print("Please enter the distances for each competitor.")  
     
     for key in Names:
          num2 = 1
          print("Competitor {}:".format(key))
          
          print("Attempt {}:".format(num2))
          distance1 = input()
          
          num2 += 1
          print("Attempt {}:".format(num2))
          distance2 = input()  
          
          num2 += 1
          print("Attempt {}:".format(num2))
          distance3 = input()  
          
          bool1, bool2, bool3 = False, False, False
          
          if not distance1.isalpha():
               bool1 = True
          if not distance2.isalpha():
               bool2 = True
          if not distance3.isalpha():
               bool3 = True
          
          if bool1 and bool2 and bool3:
               max_distance = max(eval(distance1), eval(distance2), eval(distance3))
               competitors[key] = max_distance
          
          elif not bool1 and bool2 and bool3:
               max_distance = max(eval(distance2), eval(distance3))
               competitors[key] = max_distance              
          
          elif bool1 and not bool2 and bool3:
               max_distance = max(eval(distance1), eval(distance3))
               competitors[key] = max_distance
               
          elif bool1 and bool2 and not bool3:     
               max_distance = max(eval(distance1), eval(distance2))
               competitors[key] = max_distance
               
          elif not bool1 and not bool2 and bool3:     
               competitors[key] = eval(distance3)
               
          elif not bool1 and bool2 and not bool3:     
               competitors[key] = eval(distance2)
               
          elif bool1 and not bool2 and not bool3:     
               competitors[key] = eval(distance1)            
          
          else:
               competitors[key] = "No jump"
               
     print()          
     word1 = "Competitor"          
     word2 = "Longest Distance"
     print("{:<25}{}".format(word1, word2))   
     
     for key, value in competitors.items():
          
          if isinstance(value, float):
               print("{:<25}{:.2f}".format(key, value))
               
          else:
               print("{:<25}{}".format(key, value))
               
     winner = None
     max_distance =-1
     
     for key, value in competitors.items():
          if isinstance(value, float) and value > max_distance:
               max_distance = value
               winner = key
               
     if winner:
          print()
          print("The winner is {} with a jump of {:.2f}.".format(winner, max_distance))
     
     
main()