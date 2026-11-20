percenta = int(input('Koľko si dostal percent z písomky? (0%-100%) '))
# zatial ešte neviem ako spravit tak aby som tam mohol pouzit aj %, takze to bude len celé čislo

if percenta >= 90:
    znamka = 1
elif percenta >= 75:
    znamka = 2
elif percenta >= 50:
    znamka = 3
elif percenta >= 30:
    znamka = 4
else:
    znamka = 5

print('Vychádza ti: ', znamka)