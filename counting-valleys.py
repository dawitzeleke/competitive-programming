def countingValleys(n, s):
    valley_count=0
    level= 0
    dic= {'U':1,'D':-1}
    for step in s:
        level+=dic[step]
        if level==0 and step=='U':
            valley_count+=1
            
            
    return valley_count
