#HCD 10/2/18
def keep_track(x,y,z):
    for i in range(y):
        x-=z
    return(x)


print(keep_track(1000,5,-5))
      
