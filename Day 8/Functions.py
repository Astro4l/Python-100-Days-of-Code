#Simple Functions

def greet():
    print("Hello")
    print("This is a simple function")
    print("Goodbye")

greet()


#Function that allows for input

def greet_with_name(name):
    print (f"Hello {name}")
    print (f"How are you doing {name}")

greet_with_name("Astro")


#Functions with more than one input - first with positional arguments

def greet_with_twoinputs(name, location):
    print (f"Hello {name}")
    print (f"How is it like in {location}")

greet_with_twoinputs("Astro", "Dublin")


#Functions with keyword arguments

def greet_with_keyword(name, location, weather):
    print (f"Hello {name}")
    print (f"Welcome to {location}")
    print (f"Today is very {weather}")

greet_with_keyword(name="Astro", location="Dublin",weather="cloudy")