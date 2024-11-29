# tak się tworzy komentarze w kodzie
# typy danych w pythonie:
x=5 # typ integer (piczba całkowita)
y=5.1 # typ float (liczba zmienna przecinkowa)
z="Tomeczek" # typ str (string - tekst)
typ_danych_logicznych = True # (0 lub 1) typ bool (boolean)
typ_list = [ x, y, z ]
typ_dict = {
    "silnik": "diesel",
    "rok produkcji": 1972
} #typ "słownikowy"
print(typ_list[0])
print(typ_dict["silnik"])
if not typ_danych_logicznych:
    print("jestem w if'ie")
else:
    print("jestem w elsie")

if x>5:
    print("x>5")
elif x==5:
    print("x=5")
else:
    print("x<5")

for i in range(5):
    print(i)

for a in typ_list:
    print(a)

x = 0
while x<5:
    print(x)
    x += 1
