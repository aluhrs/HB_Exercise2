import arithmetic
# repeat forever
while True:
    # read input
    token = raw_input("> ")
    # tokenize input
    tokens = token.split(" ")   
    #print tokens

    if tokens[0] == "q":
        break
    #if tokens[1].isdigit() and tokens[2].isdigit():
     #   int(tokens)

    #addition
    if tokens[0] == "+":    
        add = arithmetic.add(int(tokens[1]), int(tokens[2]))
        print add
    break

