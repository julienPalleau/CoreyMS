def main():
    # creation d'une variable username ayant pour valeur julien
    username = "Julien"
    # creation d'une variable age ayant pour valeur 45
    age = 45
    # affiche le username et l'age
    print(username, age)
    # change la valeur age
    age = 25
    # affiche la nouvelle valeur age
    print(age)
    age = age * age
    print(age)

    print("Salut " + username + ", vous avez " + str(age) + " ans")


if __name__ == '__main__':
    main()
