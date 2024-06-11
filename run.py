import multiprocessing

# To run evo
def startEvo():
    print("Process 1 is running...")
    from main import start
    start()

# To run hotword
def listenHotword():
    print("Process 2 is running...")
    from evo_back.features import hotword
    hotword()
    
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=startEvo)
    p2 = multiprocessing.Process(target=listenHotword)
    p1.start()
    p2.start()
    p1.join()
    
    if p2.is_alive():
        p2.terminate
        p2.join()
        
    print("system stop")
