countrys = {'Qatar': 'asia', 'Belgium': 'Europe', 'Nigeria':'Africa', 'Canada':'America'}
points = 0

qatar = input('In  which continent is Qatar? :')
if qatar.lower() == 'asia':
    print('Great!')
    points+=1
else:
    print('Bettre next time:)')
Belgium = input('In  which continent is Belgium? :')
if Belgium.lower() == 'europe':
    print('Great!')
    points+=1
else:
    print('Bettre next time:)')
nigeria = input('In  which continent is Nigeria? :')
if nigeria.lower() == 'africa':
    print('Great!')
    points+=1
else:
    print('Bettre next time:)')
canada = input('In  which continent is Canada? :')
if canada.lower() == 'america':
    print('Great!')
    points+=1
else:
    print('Never give up!')
    
print(points)