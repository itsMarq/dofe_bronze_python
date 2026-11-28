password = 'velmitajneheslo'
attempt = ''

while attempt != password: # Loop ktory sa opakuje, pokym sa nezada spravne heslo
    attempt = input('Zadajte heslo: ')
    if attempt != password:
        print('Nesprávne heslo, skúste to znova.')

print('Prihlásenie prebehlo úspešne. Vitajte!')