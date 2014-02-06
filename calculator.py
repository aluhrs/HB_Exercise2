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

    if len(tokens) > 2 and not tokens[1].isdigit():
        print "Please enter a number."

    if len(tokens) > 2 and not tokens[2].isdigit():
        print "Please enter a number."

    if len(tokens) < 3 and tokens[0] != "square": # "cube"):
        print """Please enter one of the following options:
            Addition: + num num,
            Subtraction: - num num, 
            Multiplication: * num num,
            Division: / num num, 
            Square: square num,
            Cube: cube num, 
            Modulo: mod num num or 
            Power: pow num num."""         
   
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
        if len(tokens) == 1:
            print """Please enter one of the following options:
            Addition: + num num,
            Subtraction: - num num, 
            Multiplication: * num num,
            Division: / num num, 
            Square: square num,
            Cube: cube num, 
            Modulo: mod num num or 
            Power: pow num num."""
        else:
            print """Please enter one of the following options:
            Addition: + num num,
            Subtraction: - num num, 
            Multiplication: * num num,
            Division: / num num, 
            Square: square num,
            Cube: cube num, 
            Modulo: mod num num or 
            Power: pow num num."""          

