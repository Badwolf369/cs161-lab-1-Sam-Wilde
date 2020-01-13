#set starting values
usArea = 3119884.69**2
lakeVolume = 22810**3
depth = lakeVolume/usArea

#dialogue; str() converts set values to strings; round() makes calculations look prettier
print('The Great Lakes are huge. They contain roughly 22% of all the freshwater in the world.')
print('If the 48 US states had a giant wall placed around them and all the water in the lakes was placed inside, the water would be '+str(round(depth, 2))+' feet deep!')
print('Thats a lot of water!')