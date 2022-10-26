"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:

my_file = open('questions.txt', 'r')

full_operations = [line.strip() for line in my_file]
operations = [ops.split('=') for ops in full_operations]
my_file.close()
result = open('result.txt', 'w')
true_answer = wrong_answer = 0
for ops in operations:
    while True:
        try:
            resultat = int(input(f"Donner le resultat de l'operation {ops[0]} :"))
            break
        except ValueError:
            print("Veuillez saisir un entier!")

    print(f"Debug {ops[1]}")
    if resultat == int(ops[1]):
        print('Bravo !')
        result.write(f'Votre reponse a la question {ops[0]} est {resultat}. Bravo bonne reponse !.\n')
        true_answer += 1
    else:
        print('Ca ira mieux avec la prochaine operation: ')
        result.write(f'Votre reponse a la question {ops[0]} est {resultat}. Oh non ! La reponse etait: {int(ops[1])} '
                     f'ca ira mieux avec la prochaine operation: \n')
        wrong_answer += 1

result.close()
print(f"Your final socre is {true_answer}/{true_answer + wrong_answer}")

