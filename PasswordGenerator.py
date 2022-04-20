import random
from symtable import Symbol

a=input("Şifreniz kaç karakter olsun?")
length_for_pass=int(a)
lower_case="abcdefghijklmopqrstuvwyz"
upper_case=lower_case.upper()
number="1234567890"
symbol="@#'^%&/?!"
Use_for=lower_case+upper_case+number+symbol
password="".join(random.sample(Use_for,length_for_pass))
print(password)