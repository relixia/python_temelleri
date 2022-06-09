# key - value

sehirler = ["kocaeli", "istanbul"]
plakalar = [41, 34]

print(plakalar[sehirler.index("kocaeli")]) #cevap 41 gelecek

plakalar = { "kocaeli" : 41, "istanbul" : 34}
print(plakalar["kocaeli"]) #cevap 41 gelecek

plakalar["ankara"] = 6
print(plakalar) #ankara : 6 bilgisi eklenmiş oldu



users = {
    "bugracayir": {
        "age": 18,
        "roles": ["user"],
        "email": "bugra@hotmail.com",
        "address": "Erzurum",
        "phone": "124523"
    },
    "busecayir": {
        "age": 7,
        "roles": ["admin", "user"],
        "email": "buse@hotmail.com",
        "address": "Erzurum",
        "phone": "733423"
    }
}

print(users["busecayir"])
print(users["busecayir"]["age"])
print(users["busecayir"]["email"])
print(users["busecayir"]["roles"][0])