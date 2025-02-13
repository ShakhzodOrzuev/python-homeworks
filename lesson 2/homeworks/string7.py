text = str(input("matnni kiriting: "))
word = str(input("matndagi almashtiriladigan so'zni kiriting: "))
replacewith = str(input("alternative so'zni kiriting: "))
a = text.find(word)
yangi = text[:a] + replacewith + text[a +len(word):]
if a != -1: print(yangi)
else: print("kiritilgan so'z yuqoridagi matn tarkibida mavjud emas!")