#This Python program aims at building an automatic email slicer that provides the username and the domain name of any email address.

#Get an email address
email=input("Enter an email address:")

#Create a function that slices the email address into two parts using the '@' symbol as a separator.
def email_slicer(email):

#Choose the separator    
    x=email.find("@")
#Get back  the username    
    username=email[0:x]
#Get back the domain name    
    domain=email[x+1:]
#Print out the username & the domain name of the email address
    return print("The username is: %s \nThe domain name is: %s" %(username,domain)) 

#Call the function
email_slicer(email)












