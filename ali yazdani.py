heads=35
legs = 94

for i in range(94):
    if (legs)/(heads*2) == 1:
        print('there are '+str( heads)+ " chickens and " + str((35-heads))+' cows')
        
        break
    else:
        legs = legs -4
        heads = heads -1

