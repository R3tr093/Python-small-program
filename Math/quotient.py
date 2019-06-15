def MyQuotient (param,param2):
    
        
    try:
        int(param)
        
        
        
    except ValueError:
        
        print("Le premier paramètre est incorrect ! ")
    
    try:
        
        int(param2)
        
        
        
    except ValueError:
        
        print("Le second paramètre est incorrect ! ")
    
    i = 0
    
    while i <= param2:
        print(str(i) + " x " + str(param) + " = " + str(i * param))
        i = i + 1
    