nom=input('votre nom: ')
prenom=input('votre prénom: ')
age=int(input('votre age: '))
print(nom,prenom,age)
if age < 9 :
    ('tout petit')
elif age ==9 or age==10:
    print('poussin')
elif age ==11 or age==12:
    print('benjamin')
elif age ==13 or age==14:
    print('minime')
elif age ==15 or age==16:
    print('cadet')
elif age ==17 or age==18:
    print('junior')
elif age <=19 or age>=34:
    print('senior')
else :
    print('vétéran')