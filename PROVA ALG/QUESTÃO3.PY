popuA1 = int(15000)
popuA2 = int(15000)
popuB = int(45000)
popuC = int(65000)
anos1 = int(0)
anos2 = int(0)

popuC = popuC + (popuC * 2.5) / 100 

while popuA1 < popuB:
    popuA1 = popuA1 + (popuA1 * 10) / 100
    popuB = popuB + (popuB * 5) / 100
    anos1 = anos1 + 1

print('Sâo ', + int(anos1) ,' para a população A passar a população B')

while popuA2 <= popuC:
    popuA2 = popuA2 + (popuA2 * 10) / 100
    popuC = popuC + (popuC * 2.5) / 100
    anos2 = anos2 + 1

print('Sâo ', + int(anos2) ,' para a população A passar a população C em 23%')