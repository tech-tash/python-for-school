# Program to allow the user to o enter information about a credit card account, and then produce a formatted output of that information.
# Name: Natasha Mazibuko
# Date: 16 April 2024

def main():
 
 name = input("Enter the card holder's name:\n")
 digit = input("Enter the 16 digit card number (no spaces please):\n")
 date_issue = input("Enter the date of issue (mm:yy):\n")
 date_expiry = input("Enter the expiry date (mm:yy):\n")
 sec_code = input("Enter the 3 digit security code:\n")
 
 credit_lim = float(input("Enter the credit limit (Rand):\n"))
 rounded_cred = "{:.2f}".format(credit_lim)
 credit = rounded_cred + " Rand"
 
 balance1 = float(input("Enter the balance (Rand):\n"))
 rounded_bal = "{:.2f}".format(balance1)
 balance = rounded_bal + " Rand"
 
 available1 = credit_lim - balance1
 rounded_avail = "{:.2f}".format(available1)
 available = rounded_avail + " Rand"
 
 pipe = "|"
 print("\n")
 
 print("+------------- Credit Card Account --------------+")
 print("| Card holder:   " + name + "                 |")  
 print("| Card number:   " + digit[0:4] + " " + digit[4:8] + " " + digit[8:12] + " " + digit[12:15] + digit[15] + "             |")
 print("| Date of issue: " + date_issue[0:2] + "/" + date_issue[3:4] + date_issue[4] + "    Expiry date: " + date_expiry[0:2] + "/" + date_expiry[3:4] + date_expiry[4] + "     |")
 
 
 print("| Security code: " + sec_code + "                             |")
 print("| Credit limit:  {0:31} {1}".format(credit, pipe))                
 print("| Available:     {0:31} {1}".format(available, pipe))                 
 print("| Balance:       {0:31} {1}".format(balance, pipe))         
 print("+------------------------------------------------+")
 
main() 
