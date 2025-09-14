states_of_america = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut']

print(states_of_america[1])
print(states_of_america[-1])
print(states_of_america[-3])

states_of_america[1] = "Pencilvania"

print(states_of_america)

states_of_america.append("Hawai")

print(states_of_america)

#Acrescentando mais de 1 item

states_of_america.extend(["Angelaland", "Jack Bauer Land"])

print(states_of_america)


#imprimindo o último item quand não sabemos o tamanho
num_of_states = len(states_of_america)

print(states_of_america[num_of_states - 1])

#Listas dentro de lista - Nested List

fruits = ['Strawberries', 'Nectarines','Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears']
vegetables = ['Tomatoes', 'Celery', 'Potatoes']
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)