def displayFloat(value):

    if type(value) is not float:
        
        raise TypeError("\n Error :: >>> Le paramètre attendu doit être un flottant.")

    value = str(value)

    integerFragment, floatFragment = value.split(".")

    result = ",".join([integerFragment, floatFragment[:3]])

    print(result)

displayFloat(3.99999999999998)
