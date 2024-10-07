# Giovana Simões Franco	    RA: 10417646
# Julia Santos Oliveira		RA: 10417672
# Larissa Yuri Sato		    RA: 10418318
# Marina Haru Marcoulakis	RA: 10417370 

def multiplicacaoMatriz(A, B):
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    if len(B) != n:
        return "Operação impossível"
    C = []
    for i in range(m):
        C.append([])
        for j in range(p):
            soma = 0
            for k in range(n):
                soma += A[i][k] * B[k][j]
            C[i].append(soma)
    return C


def entradaMatriz(nome):
    m = int(input("Digite o número de linhas da matriz" + nome + " : "))
    n = int(input("Digite o número de colunas da matriz " + nome + " : "))
    matriz = []
    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(float(input(f"Digite o elemento ({i+1},{j+1}): ")))
        matriz.append(linha)
    return matriz

def imprimirMatriz(matriz):
    for linha in matriz:
        print(linha)

def arquivoMatriz(nome):
    matriz = []
    with open(nome, "r") as arquivo:
        for linha in arquivo:
            matriz.append([float(x) for x in linha.split()])
    return matriz

def pwd():
    import os
    print(os.getcwd())

def main():
    opcao = 0
    
    while(opcao!= 3):
        print("1 - Entrada de dados")
        print("2 - Arquivo de dados")
        print("3 - Sair")
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            MatrizA = entradaMatriz("A")
            MatrizB = entradaMatriz("B")
            resultado = multiplicacaoMatriz(MatrizA, MatrizB)

            print("\n")
            if resultado == "Operação impossível":
                print("Operação impossível")
            else:
                imprimirMatriz(resultado)
        elif opcao == 2:
            pwd()
            MatrizA = arquivoMatriz("./matrizA.txt")
            MatrizB = arquivoMatriz("./matrizB.txt")
            resultado = multiplicacaoMatriz(MatrizA, MatrizB)

            print("\n")
            if resultado == "Operação impossível":
                print("Operação impossível")
            else:
                imprimirMatriz(resultado)
        else:
            if opcao == 3:
                print("\nSaindo...")
            else:
                print("Opção inválida")

if __name__ == "__main__":
    main()

