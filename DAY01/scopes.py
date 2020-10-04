# LEGB ---> local enclosing global built-ins

# x = "Aashima"

def tryfunction():
    x = "Neeraj"
    def flkd():
        print(x)
    print(x)

tryfunction()
print(x)