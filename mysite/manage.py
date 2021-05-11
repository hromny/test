import time
 
def timeslong(func):
    start = time.time()
    print("It's time starting ! ")
    func()
    print("It's time ending ! ")
    end = time.time()
    return "It's used : %s ." % (end - start)
