def initials_generator(personsName):


    personsInitials = ""
    seperate_names = personsName.split()
    personsInitials = ".".join([names[0] for names in seperate_names]) + '.'
    
    return personsInitials.strip()

personsName = input('Enter the users first, middle, and last name:')

initials = initials_generator(personsName)

print(initials)

# Program #1, Donovan Thompson 3/21/2025
