def dict_interdiff(d1, d2):
    result1 = {}    
    result2 = {}
    for key in d1.keys():
        if key in d2.keys():
           result1[key] =  f(d1[key], d2[key])
        else:
            result2[key] = d1[key]
    for key in d2.keys():
        if key not in d1.keys():
            result2[key] = d2[key]
    return result1, result2