import random
import matplotlib.pyplot as plt

def evaluate(individual):
    """
    Recebe um indivíduo (lista de inteiros) e retorna o número de ataques
    entre rainhas na configuração especificada pelo indivíduo.
    Por exemplo, no individuo [2,2,4,8,1,6,3,4], o número de ataques é 10.

    :param individual:list
    :return:int numero de ataques entre rainhas no individuo recebido
    """

    colisions = 0
    index = 0
    for queen in individual:

        #Line colisions
        colisions += individual.count(queen) - 1

        #Right diagonal colisions
        for step in range(1, 8 - index):
            if(queen + step == individual[index + step]):
                colisions += 1
            if(queen - step == individual[index + step]):
                colisions += 1
            
        #Left diagonal colisions
        for step in range(1, index + 1):
            if(queen + step == individual[index - step]):
                colisions += 1
            if(queen - step == individual[index - step]):
                colisions += 1
            
        index += 1
   
    return int(colisions / 2)

def tournament(participants):
    """
    Recebe uma lista com vários indivíduos e retorna o melhor deles, com relação
    ao numero de conflitos
    :param participants:list - lista de individuos
    :return:list melhor individuo da lista recebida
    """

    best_individual = participants[0]
    best_colisions = evaluate(participants[0])

    colisions = 0
    for individual in participants:
        colisions = evaluate(individual)

        if(colisions < best_colisions):
            best_colisions = colisions
            best_individual = individual
    
    return best_individual

def crossover(parent1, parent2, index):
    """
    Realiza o crossover de um ponto: recebe dois indivíduos e o ponto de
    cruzamento (indice) a partir do qual os genes serão trocados. Retorna os
    dois indivíduos com o material genético trocado.
    Por exemplo, a chamada: crossover([2,4,7,4,8,5,5,2], [3,2,7,5,2,4,1,1], 3)
    deve retornar [2,4,7,5,2,4,1,1], [3,2,7,4,8,5,5,2].
    A ordem dos dois indivíduos retornados não é importante
    (o retorno [3,2,7,4,8,5,5,2], [2,4,7,5,2,4,1,1] também está correto).
    :param parent1:list
    :param parent2:list
    :param index:int
    :return:list,list
    """

    return (parent1[0:index] + parent2[index:8], parent2[0:index] + parent1[index:8])


def mutate(individual, m):
    """
    Recebe um indivíduo e a probabilidade de mutação (m).
    Caso random() < m, sorteia uma posição aleatória do indivíduo e
    coloca nela um número aleatório entre 1 e 8 (inclusive).
    :param individual:list
    :param m:int - probabilidade de mutacao
    :return:list - individuo apos mutacao (ou intacto, caso a prob. de mutacao nao seja satisfeita)
    """

    mutation_probability = random.random()

    if(mutation_probability < m):
        individual[random.randint(0,7)] = random.randint(1,8)
    
    return individual

def generate_individual():
    individual = []
    for i in range(0,8):
        individual.append(random.randint(1,8))
    
    return individual

def run_ga(g, n, k, m, e):
    """
    Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
    :param g:int - numero de gerações
    :param n:int - numero de individuos
    :param k:int - numero de participantes do torneio
    :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
    :param e:int - número de indivíduos no elitismo
    :return:list - melhor individuo encontrado
    """

    population = []
    for i in range(0, n):
        population.append(generate_individual())

    for i in range(0, g):
        new_population = []

        #Elitism
        for i in range(0, e):
            new_population.append(tournament(population))

        while len(new_population) < n:

            #Selection
            participants1 = []
            participants2 = []

            for i in range(0, k):
                randnum1 = random.randint(0, n-1)
                participants1.append(population[randnum1])
                randnum2 = random.randint(0, n-1)
                participants2.append(population[randnum2])
            
            individual1 = tournament(participants1)
            individual2 = tournament(participants2)

            #Crossover
            individual1, individual2 = crossover(individual1, individual2, random.randint(0,7))

            #Mutation
            individual1 = mutate(individual1, m)
            individual2 = mutate(individual2, m)

            new_population.append(individual1)
            new_population.append(individual2)

        population = new_population
        
        data_collect(population, j)
    
    return tournament(population)

def data_collect(population, j):
    generation.append(j)

    best = 1000
    average = 0
    worst = 0
    for individual in population:
        fitness = evaluate(individual)
        if(fitness > worst):
            worst = fitness
        if(fitness < best):
            best = fitness
        average += fitness
    average /= len(population)

    best_fitness.append(best)
    average_fitness.append(average)
    worst_fitness.append(worst)

generation = []
best_fitness = []
average_fitness = []
worst_fitness = []

#Run the algorithm
run_ga(100, 64, 16, 0.4, 2)

#Graph plotting
plt.plot(generation, best_fitness, color='green',label='Best Fitness')
plt.plot(generation, average_fitness, color='blue', label='Average Fitness')
plt.plot(generation, worst_fitness, color='red', label='Worst Fitness')

plt.title("Genetic Algorithm")
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.legend(loc='upper right', fontsize='large', frameon=True, shadow=True)
plt.show()
