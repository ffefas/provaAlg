popuA1 = int(15000)
popuA2 = int(15000)
popuB = int(45000)
popuC = int(65000)
anos1 = int(0)
anos2 = int(0)

popuC = popuC + (popuC * 0.23)

while popuA1 < popuB:
    popuA1 = popuA1 + (popuA1 * 0.10)
    popuB = popuB + (popuB * 0.05) 
    anos1 = anos1 + 1

print('Serão ', + int(anos1) ,'anos para a população A passar a população B')

while popuA2 <= popuC:
    popuA2 = popuA2 + (popuA2 * 0.10)
    popuC = popuC + (popuC * 0.025) 
    anos2 = anos2 + 1

print('Serão ', + int(anos2) ,'anos para a população A passar a população C em 23%')