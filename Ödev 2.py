# Task 1: Examine the data structures below

x = 8
print(type (x))
y = 3.2
print(type (y))
z = 8j + 18
print(type (z))
a = "Hello World"
print(type (a))
b = True
print(type (b))
c = 23 > 22
print(type (c))
d = {"Name": "Jake",
     "Age": 27,
    "Address": "Downtown"}
print(type(d))
l = [1,2,3,4]
print(type (l))
t= ("Machine Learning","Data Science")
print(type(t))
s = {"Python", "Machine Learning", "Data Science"}
print(type(s))


data_types=[x,y,z,a,b,c,l,d,t,s]
print([type(i) for i in data_types])

# Task 2: Convert all the letters of the string below to capital letters

text = ("The goal is to turn data into information, and information into insight.")

text=text.upper().replace("," , " ").replace("." , " ").split()
print(text)

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
print(len(lst))
print(lst[0],lst[10])

lst1 = lst[0:4]
print(lst1)

lst.pop(8)

lst1.append("Y")
print(lst1)

lst.insert(8,"N")
print(lst)

dict = {'Christian': ["America", 18],
        'Daisy' : ["England", 12],
        'Antonio' : ["Spain", 22],
        'Dante': ["Italy", 25]}
print(type(dict))

print(dict.keys())
print(dict.values())

dict['Daisy'][1] = 22
print(dict)
dict["Ahmet"] = ["Turkey", 22]
print(dict)
dict["Omar"] = ["Jordan", 31]
print(dict)
del dict['Antonio']
dict.items()
dict["Antonio"] = ["Spain", 22]
print(dict)

removedvalue = dict.pop('Antonio')
print(removedvalue)
dict.keys()
dict.values()
dict["Daisy"][1] = 32
print(dict)


l = [2,13,18,93,22]
print(l)

def func(list):
    even_list=[]
    odd_list=[]
    for t in l:
         if t % 2 == 0:
             even_list.append(t)
         else:
             odd_list.append(t)
    return even_list,odd_list
even_list,odd_list = func(list)
print(even_list)
print(odd_list)


ogrenciler= ["Ali","Veli", "Ayse","Talat","Zeynep", "Ece"]

muhendislik_fakultesi = ogrenciler[:3]
tip_fakultesi = ogrenciler[3:]
for index, ogrenci in enumerate(muhendislik_fakultesi, start=1):
    print(f"Mühendislik Fakültesi {index}. ögrenci: {ogrenci}")
for index, ogrenci in enumerate(tip_fakultesi, start=1):
    print(f"Tip Fakültesi {index}. ögrenci: {ogrenci}")

ogrenciler= ["Ali","Veli", "Ayse","Talat","Zeynep", "Ece"]
for index, o in enumerate (ogrenciler, start=1):
    if index < 4:
        print ("Mühendislik Fakültesi", index, ".", "ögrenci:", o)
    else:
        print("Tip Fakültesi", index -3, ".", "ögrenci:", o)

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2004"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

list(zip(ders_kodu,kredi,kontenjan))

for kod, kred, kont in zip(ders_kodu, kredi, kontenjan):
    print(f"Kredisi {kred} olan {kod} kodlu dersin kontenjani {kont} kisidir")

kume1 = set(["data","python"])
kume2 = set(["data","function","qcut","lambda", "python","miuul"])

def kapsiyorsa(kume1,kume2):
    if kume1.issuperset(kume2):
        print(kume1.intersection(kume2))
    else:
        print(kume2.difference(kume1))

kapsiyorsa(kume1,kume2)