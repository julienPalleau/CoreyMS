#cryptage d'un message base sur le code ASCII
#nom programme: ascii.py
message_clair = input("tapez un message a crypter : ")
message_crypte = ""
longueur = len(message_clair)
for i in range(longueur):
    letter = message_clair[i]
    codage = str(ord(letter))
    message_crypte = message_crypte + codage
print("message crypte a envoyer")
print(message_crypte)