'''
Napisz program który prosi użytkownika o promien okregu i oblicza jego pole. Przyklad:

jaki promien ma twoj okrag?
> 5
Twój okrąg ma pole 75.39
'''

promien = input("Jaki promień ma twój okrąg?\n")
promien = int(promien)
pole = 3.14*promien*promien
print("Twój okrąg ma pole", pole)