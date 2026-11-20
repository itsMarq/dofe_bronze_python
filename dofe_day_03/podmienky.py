# Jednoducha aplikacia na naucenie s podmienkami - Aplikacia určí či je číslo kladné, záporné alebo sa rovná nule.
cislo = int(input('Zadaj číslo: '))

if cislo > 0:
    print('Kladné')
elif cislo < 0:
    print('Záporné')
else:
    print('Nula')
