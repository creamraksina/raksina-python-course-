"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("", 0, "", "")  # name, age, city, country
    hobbies = []
    
    # Your code here
    name = input("What is your name? : ")
    age = int(input("How old are you? : "))
    city = input("Where do you live in city? : ")
    

if __name__ == "__main__":
    personal_info_manager()
