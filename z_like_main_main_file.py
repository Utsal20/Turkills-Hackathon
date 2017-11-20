from Turckeys import startscreen
from turkeykiller import playgame
from Scores import scorescreen

x = 7

while x==7:
    startscreen(False)
    
    playgame()
    print('done')
    
    x = scorescreen()
