print('The current population in the US is '+307357870)
print('I calculate how much that population will change in a given number of years')
print('Please enter a number of years')

numYrs = input('-->:')
numBrnYrl = 4505142.857
numDieYrl = 2425846.154
numImgYrl = 901028.5714
numGanYrl = (numBrnYrl+numImgYrl)-numDieYrl
newPop = numYrs*numGanYrl

print('The population in '+str(numYrs)+' will be '+str(newPop))