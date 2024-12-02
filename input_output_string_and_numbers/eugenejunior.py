# Program that interacts with the user in a conversational manner by asking questions and responding appropriately. 
# Name: Natasha Mazibuko
# Date: 16 April 2024

def main():
 
 print("Hello, I am Eugene Junior.")
 name = input("What is your first name?\n")
 last_name = input("What is your last name?\n")
 title = input("And what is your preferred title?\n")
 print("Hi" , title , name[0] + "." , last_name + "!")
 
 course = input("What is the course code of your current course?\n")
 print("So, what does '" + course[0:3] + "' stand for?")  #slice first 3 letters
 course_full = input()
 print(course_full + " sounds interesting.")
 
 weight = input("What weight are you in kilograms?\n")
 pounds = eval(weight) * 2.20462262
 ounces = (pounds - int(pounds)) * 16   #want the decimal point values
 print("That's" , int(pounds), "lbs and", round(ounces), "ounces in the US!")
 
 date = input("What's today's date (dd/mm/yy)?\n")
 
 current_year = eval("20" + date[6] + date[7])    #write the current year as an int to do calculation
 year_born = input("And what year were you born?\n")
 age = current_year - eval(year_born)
 print("Okay, so you're" , age, "this year.\nNice talking to you, bye!")
 
 
 
main() 