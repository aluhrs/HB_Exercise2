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
     
    if not tokens[1].isdigit() or not tokens[2].isdigit():
        print "Please enter a number."

    #addition
    elif tokens[0] == "+":    
        add = arithmetic.add(int(tokens[1]), int(tokens[2]))
        print add
    #subtraction
    elif tokens[0] == "-":    
        subtract = arithmetic.subtract(int(tokens[1]), int(tokens[2]))
        print subtract

    #multiplication
    elif tokens[0] == "*":    
        multiply = arithmetic.multiply(int(tokens[1]), int(tokens[2]))
        print multiply    

    #division
    elif tokens[0] == "/":    
        divide = arithmetic.divide(int(tokens[1]), int(tokens[2]))
        print divide

    #square
    elif tokens[0] == "square":    
        square = arithmetic.square(int(tokens[1]))
        print square

    #cube
    elif tokens[0] == "cube":    
        cube = arithmetic.cube(int(tokens[1]))
        print cube       

    #power
    elif tokens[0] == "pow":    
        power = arithmetic.power(int(tokens[1]), int(tokens[2]))
        print power  

    #mod
    elif tokens[0] == "mod":    
        mod = arithmetic.mod(int(tokens[1]), int(tokens[2]))
        print mod

    else:
            print "Please enter +, -, *, /, square, cube, mod, or pow."     

