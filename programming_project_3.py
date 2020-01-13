print('Hello!')
print('I calculate gasoline usage and amount conversions.')
print('Please enter an amount of gasoline in gallons.')
galGas = float(input('-->:'))

litrGas = galGas*3.785
barlOil = galGas/19.5
co2Prod = galGas*20
btueGas = galGas*115000
btueEth = btueGas/75700
monyGas = galGas*3

print('You entered '+str()+' gallons')
print('-That much gasoline in liters is '+str(round(litrGas, 2))+' liters')
print('-It would take '+str(round(barlOil, 2))+' barrels to make that much gasoline')
print('-If you burned all that gasoline it would produce '+str(co2Prod)+' pounds of CO2')
print('-It would require '+str(round(btueEth, 2))+' gallons of ethanol to produce the\n same amount of energy as that much gas')
print('-That much gasoline costs about $'+str(round(monyGas, 2)))