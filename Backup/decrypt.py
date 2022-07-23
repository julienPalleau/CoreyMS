alphabet = "abcdefghijklmnopqrstuvwxyz 0123456789"
longueur = len(alphabet)
dictionnaire = {}
print('nombre de caracteres :', longueur)
table = ""
print("table de substitution")
for i in range(longueur):
    caractere = alphabet[i]  # recuperer le caractere correspondant a i dans la chaine 'alphabet'
    code = ord(caractere)
    cle = str(code) + " = " + caractere + " ; "  # cle de decryptage
    table = table + cle  # mise a jour table
print(table)

message_crypte = "99101115115101122321081013210210111732973249493297109321081013249493210011 732109111105115324949"
longueur_message_crypte = len(message_crypte)
dictionnaire.update({'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 103, 'i': 105,
                     'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114,
                     's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122})
nombre = ''
result = []
i = 0
j = 0
k = 0
for i in message_crypte:
    print(f"i: {i}")
    if i not in dictionnaire.values():
        k = str(j) + str(i)
        j = i
        print(f"k : {k}")
    if int(k) < 97 or int(k) > 122:
        pass
    else:
        for z, val in dictionnaire.items():
            print(f"val: {val}, k: {int(k)}")
            if int(k) == val:
                print(f"test : {k}")
                result.append(k)

print(result)