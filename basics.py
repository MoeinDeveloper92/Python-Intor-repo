#bellow I want to define a global variable
myName = "moein samani nejad"

print("Hello "+myName)
def myfunction():
    global myName
    myName="Web developer"
    print("Hello " + myName)

myfunction()

print("Hello "+myName)