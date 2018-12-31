def standard_while(i):
    while i < 5:
        print(i)
        i+= 1

#########################################################
# do while replacement
#########################################################

def kind_of_do_while(i):
    while True:
        print(i)
        if i>=5:
            break

#########################################################
# while not 
#########################################################
def name_entry():
    min_length = 2
    name = input("Please enter your name: ")

    while not(len(name) >= min_length and name.isprintable() and name.isalpha()):
        name = input("Please enter your name: ")

    print("Hello, {0}".format(name))

''' It is not a good idea to ask something twice. For instance,
in the function name_entry(), we have name = ... twice.
We can use the infinite loop (do while replacement) to adjust that
as such:'''

def clean_name_entry():
    min_length = 2

    while True:
        name = input("Please enter your name: ")
        if len(name) >= min_length and name.isprintable() and name.isalpha():

            print("Hello, {0}".format(name))
    
#########################################################
# continue statement 
#########################################################
def continue_use(i):
    while i < 10:
        i += 1
        if i % 2 == 0: 
            continue
        print(i)

#########################################################
# adding else to a while loop
#########################################################
def while_if_ifnot(value):
    l = [1, 2, 3]
    val = value

    found = False
    idx = 0
    while idx < len(l):
        if l[idx] == val:
            found = True
            break
        idx += 1

    if not found:
        l.append(val)

    print(l)

def while_if_else(value):
    l = [1, 2, 3]
    val = value 
    idx = 0
    while idx < len(l):
        if l[idx] == val:
            break
        idx += 1
    else:
        l.append(val)

    print(l)
