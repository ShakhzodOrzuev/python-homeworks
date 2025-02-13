
matn = str(input("so'zni kiriting: "))
b = len(matn)
a = matn.count("a")
e = matn.count("e")
i = matn.count("i")
o = matn.count("o")
u = matn.count("u")
o_ = matn.count("o'")
unlilar = a + e + i + o + u + o_
undoshlar = b - unlilar
print("so'zdagi unlilar soni: ", unlilar)
print("so'zdagi undoshlar soni: ", undoshlar)