oldDist = 16637000000
speedperhour = 38241
speedperday = speedperhour*24

print('The Voyager 1 spacecraft launched Septemeber 15, 1977.')
print('The NASA update page on Septemeber 25, 2009, reported the spacecraft as') 
print('being roughly 16,637,000,000 miles from the sun.')
print('The spacecraft is flying away from the sun at '+str(speedperday)+' per day.')
print('')
print('With this information I can estimate how far away from the sun the spacecraft will')
print('be with a given number of days from the last report in 2009.')
print('How many days after the last report do you want me to estimate?')
askTime = int(input('-->:'))

estimateDistMi = oldDist+(speedperday*askTime)
estimateDistKm = estimateDistMi*1.609344
estimateDistAu = estimateDistMi/929558876

comSpeed = 57760.111
comTime = (estimateDistMi/comSpeed)*60*60

print('')
print('The distance from the sun in miles is '+str(estimateDistMi)+'.')
print('The distance from the sun in kilometers is '+str(estimateDistKm)+'.')
print('The distance from the sun in astronimical units is '+str(estimateDistAu)+'.')
print('It would take radio comminications '+str(comTime*2)+' hours for a round trip.')