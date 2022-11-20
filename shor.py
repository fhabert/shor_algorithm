import math
import numpy as np
import matplotlib.pyplot as plt
import time
import random

def euclid(N, a):
    N_factors = []
    for i in range(N):
        if i != 0 and i != 1 and N % i == 0:
            N_factors.append(i)
    a_factors = []
    for i in range(a):
        if i != 0 and i != 1 and a % i == 0:
            a_factors.append(i)
    for i in range(len(N_factors)):
        for j in range(len(a_factors)):
            if N_factors[i] == a_factors[j]:
                return True
    return False

def get_gcd(N, num):
    N_factors = []
    for i in range(N):
        if i != 0 and i != 1 and N % i == 0:
            N_factors.append(i)
    a_factors = []
    for i in range(num):
        if i != 0 and i != 1 and num % i == 0:
            a_factors.append(i)
    common_factors = []
    for i in range(len(N_factors)):
        for j in range(len(a_factors)):
            if N_factors[i] == a_factors[j]:
                common_factors.append(N_factors[i])
    if len(common_factors) != 0:
        return np.max(common_factors)
    return None

def finding_period(N, a):
    for i in range(N):
        result = a**i 
        if i != 0 and result % N == 1:
            return i
    return None

def get_factors(nb_to_factor):
    start_time = time.time()
    not_coprime = True
    period = 1
    counter = 2
    while counter <= nb_to_factor and not_coprime and period != None and period % 2 != 0:
        not_coprime = euclid(nb_to_factor, counter)
        if not not_coprime:
            period = finding_period(nb_to_factor, counter)
        counter += 1
    print("period", period)
    p_f, q_f = int(counter**(period/2) - 1), int(counter**(period/2) + 1)
    p, q = get_gcd(nb_to_factor, p_f), get_gcd(nb_to_factor, q_f)
    end_time = time.time()
    duration = end_time - start_time
    return p, q, duration


def get_y_output(Ns, nb_t=None):
    y_output = []
    if nb_t:
        x = [i for i in range(nb_t)]
        for _ in range(nb_t):
            _, _, duration = get_factors(Ns[0])
            y_output.append(duration)
    else:
        x = [item for item in Ns]
        for item in Ns:
            _, _, duration = get_factors(item)
            y_output.append(duration)
    print(y_output)
    return x, y_output


def visualize(Ns, durations, title, bar=False):
    if bar:
        plt.bar(Ns, durations, color="b", alpha=0.5)
    else:
        plt.plot(Ns, durations, color="b", alpha=0.5)
        plt.scatter(Ns, durations, color="r", marker="x", alpha=0.7)
    plt.xlabel("Number tested")
    plt.ylabel("Time elapsed (s)")
    plt.title(f"{title}")
    plt.show()
    pass

test = [15, 35, 77]
nb_test = None
title = "Time required for Shor's algorithm to be executed on a \n classical computer for N = 35"
title2 = "Time required for Shor's algorithm to be executed on a \n classical computer for different N values"
x, y = get_y_output(test)
bar = False
visualize(x, y, title2, bar)
# print(x, y)
# N_35 = [0.01, 1.7801356315612793, 0.21999907493591309, 0.0993967056274414]
# trials = [0.0, 0.020, 1.0252, 1.70329]


