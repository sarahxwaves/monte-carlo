## import random
import numpy as np

frequencia_intervalos = {
        "N4": 0,
        "N7": 0,
        "N8": 0,
        "N13": 0,
        "N14": 0
    }

intervalos = {
        "N4": (0, 149),
        "N7": (150, 299),
        "N8": (300, 679),
        "N13": (680, 929),
        "N14": (930, 999)
    }  
# cria matriz 100x100 de 10 dígitos
def getTable():
    table = np.random.randint(10**9, 10**10, size=(100, 100), dtype=np.int64)
    return table

def contar_frequencia_intervalos(number):
    for intervalo, (inicio, fim) in intervalos.items():
        if inicio <= number <= fim:
         frequencia_intervalos[intervalo] += 1

    return frequencia_intervalos
    
#calcula média dos dígitos escolhidos
def monte_carlo(table, iterations, positionOne, positionTwo, positionThree):
    line = 0
    col = 0
    sumValues = 0
    for i in range(iterations):
     cellNumber = table[line][col]
     str_number = str(cellNumber)
     #print(str_numero)
     number1 = str_number[positionOne - 1]
     number2 = str_number[positionTwo - 1]
     number3 = str_number[positionThree - 1]
     number = number1 + number2 + number3
     sumValues += int(number)
     frequencia = contar_frequencia_intervalos(int(number))
     print(frequencia)
    # print(f"Soma {sumValues}")
     if line == 99:
      line = 0
      if col == 99:
       col = 0
      else:
       col +=1
     else:
      line +=1
    average = (sumValues/iterations)
    return average
    

def main():
    table = getTable()
    iterations = int(input("Número de iterações: "))
    
    positionOne = int(input(f"Posição 1: "))
    positionTwo = int(input(f"Posição 2: "))
    positionThree = int(input(f"Posição 3: "))
    
    averageMonteCarlo = monte_carlo(table, iterations, positionOne, positionTwo, positionThree)
    print(f"Média: {averageMonteCarlo}")

if __name__ == "__main__":
    main()