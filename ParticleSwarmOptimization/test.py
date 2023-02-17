from main import particleSwarmOptimization
import unittest

# Functie obiectiv
def f(x):
    sum = 0
    for elem in x:
        sum += elem * elem
    return sum

precision = 1e-4

succes = []
failed = []
count = 0

def test(w, c1, c2, noParticles, iterationMax, precision):

    global count

    straux = ""
    iterationMaxStr = ""
    if iterationMax // 100 != 0:
        iterationMaxStr = str(iterationMax)
    else:
        iterationMaxStr = " " + str(iterationMax)

    sol = particleSwarmOptimization(f, iterationMax, noParticles, w, c1, c2)[1]
    try:
        assert sol < precision
        straux = "Succes: "

        straux = straux + f" w={w} \tc1={c1} \tc2={c2} \tnoParticles={noParticles} \titerationMax={iterationMaxStr}\tcalc = {str(round(sol, 25))}"
        succes.append(straux)
        count = count + 1
    except:
        straux = "Failed: "
        straux = straux + f" w={w} \tc1={c1} \tc2={c2} \tnoParticles={noParticles} \titerationMax={iterationMaxStr}\tcalc = {str(round(sol,5))}"
        failed.append(straux)

class Data:
    def __init__(self, iterationMax, noParticles, c1, c2, w):
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.noParticles = noParticles
        self.iterationMax = iterationMax
        self.precision = precision


data_array = [Data(30, 10,1,1,0.4),
              Data(50, 20,2,2,0.6),
              Data(80, 30,4,4,0.7),
              Data(100,40,6,6,0.9),
              Data(200,60,5,5,0.5)]

default = Data(100,30,1,2,0.4)

for data in data_array:
    test(data.w, default.c1, default.c2, default.noParticles, default.iterationMax, precision)
    test(default.w, data.c1, default.c2, default.noParticles, default.iterationMax, precision)
    test(default.w, default.c1, data.c2, default.noParticles, default.iterationMax, precision)
    test(default.w, default.c1, default.c2, data.noParticles, default.iterationMax, precision)
    test(default.w, default.c1, default.c2, default.noParticles, data.iterationMax, precision)

for strx in succes:
    print(strx)

for strx in failed:
    print(strx)

print("-" * 60)
print("Successful tests: " + str(count) + " / " + str(len(data_array) * 5))