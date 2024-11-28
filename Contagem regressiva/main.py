import time

contagem = int(input("Quantos segundo deseja: "))

print("iniciando Timer...")

for c in range(contagem, 0, -1):
    print(c)
    time.sleep(1)

print("Timer Finalizado!")