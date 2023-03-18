#Definiranje datuma

from datetime import date


#Definiranje rijecnika "Kolegij"

kolegij = {
    'ime_kolegija':None,
    'ects_bodovi':None
}


#Upis trazenih podataka od korisnika

kolegij['ime_kolegija']=input('Unesite ime kolegija:')
kolegij['ime_kolegija']=kolegij['ime_kolegija'].strip()
kolegij['ime_kolegija']=kolegij['ime_kolegija'].upper()
kolegij['ects_bodovi']=input('Unesite ECTS bodove za kolegij:')
kolegij['ects_bodovi']=kolegij['ects_bodovi'].strip()


#Definiranje rijecnika "Ispit"

ispit = {
    'kolegij':kolegij['ime_kolegija'],
    'ects_bodovi':kolegij['ects_bodovi'],
    'dan_ispita':None,
    'mjesec_ispita':None,
    'godina_ispita':None,
    'datum':None
}


#Upis trazenih podataka od korisnika

ispit['dan_ispita']=input('Unesite dan ispita:')
ispit['dan_ispita']=ispit['dan_ispita'].strip()
ispit['dan_ispita']=int(ispit['dan_ispita'])

#Provjera ispravnosti upisa
while ispit['dan_ispita'] > 31:
    print('Pogreska unosa, pokusajte ponovo.')
    ispit['dan_ispita'] = input('Unesite dan ispita:')
    ispit['dan_ispita'] = ispit['dan_ispita'].strip()
    ispit['dan_ispita'] = int(ispit['dan_ispita'])
    if ispit['dan_ispita']<=31:
        break

ispit['mjesec_ispita']=input('Unesite mjesec ispita:')
ispit['mjesec_ispita']=ispit['mjesec_ispita'].strip()
ispit['mjesec_ispita']=int(ispit['mjesec_ispita'])

#Provjera ispravnosti upisa
while ispit['mjesec_ispita'] > 12:
    print('Pogreska unosa, pokusajte ponovo.')
    ispit['mjesec_ispita'] = input('Unesite mjesec ispita:')
    ispit['mjesec_ispita'] = ispit['mjesec_ispita'].strip()
    ispit['mjesec_ispita'] = int(ispit['mjesec_ispita'])
    if ispit['mjesec_ispita']<=12:
        break

ispit['godina_ispita']=input('Unesite godinu ispita:')
ispit['godina_ispita']=ispit['godina_ispita'].strip()
ispit['godina_ispita']=int(ispit['godina_ispita'])


#Definiranje datuma od unesenih podataka

ispit['datum']=date(ispit['godina_ispita'],ispit['mjesec_ispita'],ispit['dan_ispita'])


#Definiranje rijecnika "Student"

student = {
    'kolegij': ispit['kolegij'],
    'ects_bodovi':ispit['ects_bodovi'],
    'dan_ispita':ispit['dan_ispita'],
    'mjesec_ispita':ispit['mjesec_ispita'],
    'godina_ispita':ispit['godina_ispita'],
    'datum':ispit['datum'],
    'ime_studenta':None,
    'prezime_studenta':None,
}


#Upis trazenih podataka od korisnika

student['ime_studenta']=input('Unesite ime studenta:')
student['ime_studenta']=student['ime_studenta'].strip()
student['ime_studenta']=student['ime_studenta'].title()
student['prezime_studenta']=input('Unesite prezime studenta:')
student['prezime_studenta']=student['prezime_studenta'].strip()
student['prezime_studenta']=student['prezime_studenta'].title()


#Ispis unesenih podataka

print('Student',student['prezime_studenta'],student['ime_studenta'],'je prijavio ispit')
print('iz kolegij',ispit['kolegij'],'koji nosi',ispit['ects_bodovi'],'ECTS bodova')
print('i odrzat ce se:',ispit['datum'])
