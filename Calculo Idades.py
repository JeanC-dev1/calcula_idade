def calcular_soma_produto(idades_homens, idades_mulheres):
    # Identifica o homem mais velho e mais novo
    homem_mais_velho = max(idades_homens)
    homem_mais_novo = min(idades_homens)
    
    # Identifica a mulher mais velha e mais nova
    mulher_mais_velha = max(idades_mulheres)
    mulher_mais_nova = min(idades_mulheres)
    
    # Cálculo da soma e do produto
    soma = homem_mais_velho + mulher_mais_nova
    produto = homem_mais_novo * mulher_mais_velha
    
    return soma, produto

def validar_idade(idade):
    if not isinstance(idade, int) or idade < 0:
        raise ValueError("A idade deve ser um número inteiro positivo.")

def main():
    try:
        # Leitura das idades de cada um
        idade_homem_1 = int(input("Digite a idade do Homem 1: "))
        validar_idade(idade_homem_1)
        
        idade_homem_2 = int(input("Digite a idade do Homem 2: "))
        validar_idade(idade_homem_2)
        
        idade_mulher_1 = int(input("Digite a idade da Mulher 1: "))
        validar_idade(idade_mulher_1)
        
        idade_mulher_2 = int(input("Digite a idade da Mulher 2: "))
        validar_idade(idade_mulher_2)
        
        # Lista das idades
        idades_homens = [idade_homem_1, idade_homem_2]
        idades_mulheres = [idade_mulher_1, idade_mulher_2]

        # Cálculo da soma e do produto
        soma, produto = calcular_soma_produto(idades_homens, idades_mulheres)
        
        print(f"Soma da idade do homem mais velho com a mulher mais nova: {soma}")
        print(f"Produto da idade do homem mais novo com a mulher mais velha: {produto}")

    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
def calcular_soma_produto(idades_homens, idades_mulheres):
    # Identifica o homem mais velho e mais novo
    homem_mais_velho = max(idades_homens)
    homem_mais_novo = min(idades_homens)
    
    # Identifica a mulher mais velha e mais nova
    mulher_mais_velha = max(idades_mulheres)
    mulher_mais_nova = min(idades_mulheres)
    
    # Cálculo da soma e do produto
    soma = homem_mais_velho + mulher_mais_nova
    produto = homem_mais_novo * mulher_mais_velha
    
    return soma, produto

def validar_idade(idade):
    if not isinstance(idade, int) or idade < 0:
        raise ValueError("A idade deve ser um número inteiro positivo. Por gentileza meu jovem!!")

def main():
    try:
        # Leitura das idades
        idade_homem_1 = int(input("Digite a idade do Homem 1: "))
        validar_idade(idade_homem_1)
        
        idade_homem_2 = int(input("Digite a idade do Homem 2: "))
        validar_idade(idade_homem_2)
        
        idade_mulher_1 = int(input("Digite a idade da Mulher 1: "))
        validar_idade(idade_mulher_1)
        q
        idade_mulher_2 = int(input("Digite a idade da Mulher 2: "))
        validar_idade(idade_mulher_2)
        
        # Lista de idades
        idades_homens = [idade_homem_1, idade_homem_2]
        idades_mulheres = [idade_mulher_1, idade_mulher_2]

        # Cálculo da soma e do produto
        soma, produto = calcular_soma_produto(idades_homens, idades_mulheres)
        
        print(f"Soma da idade do homem mais velho com a mulher mais nova: {soma}")
        print(f"Produto da idade do homem mais novo com a mulher mais velha: {produto}")

    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()