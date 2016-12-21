def ram_shuffel(objects,mass):
    import random
    "maintaing two sets number constant and shuffle them"
    randomized_array=[]
    t=0
    x=1
    while x<=len(objects):
        while t<mass[x-1]:       #total number of object a(1)
            randomized_array.append(objects[x-1])
            t=t+1
        t=0
        x=x+1 
    
    #print arr
    random.shuffle(randomized_array)
    
    return randomized_array

print ram_shuffel(["f","s"],[5,6])
