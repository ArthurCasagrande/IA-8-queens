import numpy as np


def compute_mse(theta_0, theta_1, data):
    """
    Calcula o erro quadratico medio
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    se = 0
    n = len(data)
    for i in range(n):
        xi = data[i][0]
        yi = data[i][1]
        se += (yi - theta_0 - theta_1*xi)**2
    return se/n

def step_gradient(theta_0, theta_1, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de theta_0 e theta_1.
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de theta_0 e theta_1, respectivamente
    """
    derivative_t0_sum = 0
    derivative_t1_sum = 0
    n = len(data)
    for i in range(n):
        xi = data[i][0]
        yi = data[i][1]
        derivative_t0_sum += (yi - theta_0 - theta_1*xi)
        derivative_t1_sum += (yi - theta_0 - theta_1*xi)*xi        
    derivative_theta_0 = -(2/n)*derivative_t0_sum
    derivative_theta_1 = -(2/n)*derivative_t1_sum
    #direction_grad_descent_t0 = -np.sign(derivative_theta_0)
    #direction_grad_descent_t1 = -np.sign(derivative_theta_1)
    new_theta_0 = theta_0 - alpha*derivative_theta_0
    new_theta_1 = theta_1 - alpha*derivative_theta_1

    return new_theta_0, new_theta_1

def fit(data, theta_0, theta_1, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de theta_0 e theta_1.
    Ao final, retorna duas listas, uma com os theta_0 e outra com os theta_1
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os theta_0 e outra com os theta_1 obtidos ao longo da execução
    """
    theta_0_list = [theta_0]
    theta_1_list = [theta_1]

    for i in range(num_iterations):
        theta_0, theta_1 = step_gradient(theta_0, theta_1, data, alpha)
        theta_0_list.append(theta_0)
        theta_1_list.append(theta_1)
    return theta_0_list, theta_1_list
