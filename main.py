ism = 'Ahad'
familiya = 'Qayum'
print(ism ,familiya)


ism = "James"
familiya = 'Bond'
print(f"Salom, mening ismim {familiya}. {ism} {familiya}!")

ism = "Ahad"
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif)


ism = (input('Kim u ?'))
familiya = 'Rizayeva'
print(ism)
if ism == "Shahzoda?" or ism == "Shahzoda":
    print(f'yes {ism} is her name.')
else:
    print(f'no {ism} is not her name.')


name = 'Abdurazzoq'

name2 = ["O'rik", "Shaftoli", "Uzum"]

for raqam, a in enumerate(name2, start=1):
    print(str(raqam) + ". " + a)


name2 = ["O'rik", "Shaftoli", "Uzum"]

for a in enumerate(name2, 1):
    print(a)

for a in range(1,11):
    print(a)