def towersOfHanoi(numberOfDisks, startPeg=1, endPeg=3):
    if numberOfDisks:
        towersOfHanoi(numberOfDisks-1, startPeg, 6-startPeg-endPeg)
        print("Move disk %d from peg %d to peg %d" %(numberOfDisks, startPeg, endPeg))
        towersOfHanoi(numberOfDisks-1, 6-startPeg-endPeg, endPeg)

towersOfHanoi(numberOfDisks=3)