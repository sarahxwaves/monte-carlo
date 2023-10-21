## import random
import numpy as np

# cria matriz 100x100 de 10 dígitos
def getTable():
    table = np.random.randint(10**9, 10**10, size=(100, 100), dtype=np.int64)
    return table

#calcula frequencia dos intervalos
    
#calcula média dos dígitos escolhidos
def monte_carlo(table, iterations, positionOne, positionTwo, positionThree):
    ranges = {}
    num_ranges = {}
    ranges[000] = 149
    ranges[150] = 299
    ranges[300] = 679
    ranges[680] = 929
    ranges[930] = 999
    frequencia = {}
    line = 0
    col = 0
    sumValues = 0
    for i in range(iterations):
        cellNumber = table[line][col]
        str_number = str(cellNumber)
        number1 = str_number[positionOne - 1]
        number2 = str_number[positionTwo - 1]
        number3 = str_number[positionThree - 1]
        number = number1 + number2 + number3
        print(number)
        sumValues += int(number)
        # Adiciona o número à tabela de frequência
        frequencia[int(number)] = frequencia.get(int(number), 0) + 1
        #print(frequence)
        # print(f"Soma {sumValues}")
        # Cria um dicionário para armazenar os valores agrupados
        if line == 99:
            line = 0
            if col == 99:
               col = 0
            else:
                col +=1
        else:
         line +=1
    for inicio, fim in ranges.items():
     num_ranges[f"{inicio}-{fim}"] = 0

    for num, freq in frequencia.items():
        for inicio, fim in ranges.items():
            if inicio <= num  <= fim:
             num_ranges[f"{inicio}-{fim}"] += freq

    for x, y in num_ranges.items():
        print(f"range:{x} numero_aparicoes: {y} Frequencia:{y/iterations}")

    for num, freq in frequencia.items():
        for inicio, fim in ranges.items():
            if (num >= inicio) and  (num <= fim):
                num_ranges[f"{inicio}-{fim}"] += freq

  
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