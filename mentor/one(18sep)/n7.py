# Question -  Accept any city from the user and display monument of that city  
#  city      Monument 
#  Delhi       Red fort       
#  Agra        Taj mahal   
#  Jaipur      Jal mahal      
# Get the user's input for the city
city = input("Please enter a city: ")

city = city.lower()

if city == "delhi":
    print("The monument in Delhi is Red Fort.")
elif city == "agra":
    print("The monument in Agra is Taj Mahal.")
elif city == "jaipur":
    print("The monument in Jaipur is Jal Mahal.")
else:
    print(f"Sorry, we don't have information about a monument in {city}.")
