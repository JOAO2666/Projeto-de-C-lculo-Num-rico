"""
Projeto 1 - Calculo Numerico (UNIVASF)
Simulador de Propagacao de Erros Numericos

Equipe:
- Joao Emanuel Almeida Ramos
- Eduardo dos Santos Ferreira Sousa
- Julio Cesar Mendes do Nascimento
"""

import math


# =====================================================================
# 1. PARTE: Normalizacao e Precisao Numérica (Joao Emanuel)
# =====================================================================

def normalizar(valor: float) -> tuple[float, int]:
    """
    Normaliza o numero para a notacao cientifica: 0.d1d2... * 10^e
    Exemplo: 123.45 -> mantissa = 0.12345, expoente = 3
    """
    if valor == 0.0:
        return 0.0, 0
    # TODO: implementar calculo da mantissa e expoente
    pass


def truncar(valor: float, n_digitos: int) -> float:
    """
    Descarta digitos apos a n-esima casa significativa.
    Exemplo: 1.13572 com 4 digitos -> 1.1357
    """
    if valor == 0.0:
        return 0.0
    # TODO: implementar truncamento
    pass


def arredondar(valor: float, n_digitos: int) -> float:
    """
    Arredonda o numero mantendo n digitos significativos.
    Exemplo: 0.76545 com 4 digitos -> 0.7655
    """
    if valor == 0.0:
        return 0.0
    # TODO: implementar arredondamento
    pass


def ajustar_precisao(valor: float, n_digitos: int, metodo: str = "arredondamento") -> float:
    """Chama truncar ou arredondar conforme a escolha."""
    metodo = metodo.lower().strip()
    if metodo in ["truncamento", "truncar"]:
        return truncar(valor, n_digitos)
    return arredondar(valor, n_digitos)


# =====================================================================
# 2. PARTE: Operacoes Aritmeticas e Metricas de Erro (Eduardo)
# =====================================================================

def calcular_erros(valor_exato: float, valor_aprox: float) -> tuple[float, float | None]:
    """
    Calcula:
    - Erro Absoluto: Ea = |Valor Exato - Valor Aprox|
    - Erro Relativo: Er = Ea / |Valor Aprox| (se Valor Aprox != 0)
    """
    # TODO: implementar calculo de Ea e Er
    pass


def calcular_operacao(x: float, y: float, op: str, n_digitos: int, metodo: str = "arredondamento") -> dict:
    """
    Executa a operacao com precisao controlada e calcula os erros.
    """
    # TODO: implementar operacao na maquina finita
    pass


def sequencia_somas(termo: float, repeticoes: int = 10, n_digitos: int = 4, metodo: str = "truncamento") -> list:
    """
    Simula somas consecutivas acumulando o erro a cada passo (Exemplo 3).
    """
    # TODO: implementar loop de somas sucessivas
    pass


# =====================================================================
# 3. PARTE: Interface de Usuario e Menu (Julio Cesar)
# =====================================================================

def ler_numero(mensagem):
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("Valor invalido. Digite um numero real (ex: 2.5).")

def ler_operacao():
    operacoes_validas = ["+", "-", "*", "/"]

    while True:
        operacao = input("Digite a operação (+, -, * ou /): ").strip()

        if operacao in operacoes_validas:
            return operacao

        print("Operação inválida. Tente novamente")

def ler_digitos(mensagem, padrao = 4):
    while True:
        entrada = input(f"{mensagem} [{padrao}]: ").strip()
        if entrada == "":
            return padrao
        if entrada.isdigit() and int(entrada) > 0:
            return int(entrada)
        print("Digite um numero inteiro maior que zero.")

def escolher_metodo():
    while True:
        print("\nMetodo de ajuste:")
        print("1 - Arredondamento")
        print("2 - Truncamento")
        opcao = input("Escolha (1 ou 2) [1]: ").strip()
        if opcao in ["1", ""]:
            return "arredondamento"
        elif opcao == "2":
            return "truncamento"
        print("Opcao invalida. Digite 1 ou 2.")

def exibir_resultado(resultado):
    print("\n--- Resultado ---")
    print(f"Valor exato: {resultado['valor_exato']}")
    print(f"Valor aproximado: {resultado['valor_aproximado']}")
    print(f"Erro absoluto: {resultado['erro_absoluto']}")

    erro_relativo = resultado["erro_relativo"]
    if erro_relativo is None:
        print("Erro relativo: não definido")
    else:
        print(f"Erro relativo: {erro_relativo}")

    
def exibir_menu():
    print("\n" + "=" * 50)
    print("   SIMULADOR DE PROPAGACAO DE ERROS NUMERICOS")
    print("   UNIVASF - Calculo Numerico")
    print("   Equipe: Joao Emanuel | Eduardo | Julio Cesar")
    print("=" * 50)
    print("1 - Fazer novo calculo (+, -, *, /)")
    print("2 - Rodar Exemplo 1 do PDF (Soma simples)")
    print("3 - Rodar Exemplo 2 do PDF (Cancelamento Subtrativo)")
    print("4 - Rodar Exemplo 3 do PDF (Somas Sucessivas)")
    print("0 - Sair")


def main():
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opcao: ").strip()

        if opcao == "1":
            x = ler_numero("Digite o primeiro número (x): ")
            y = ler_numero("Digite o segundo número (y): ")
            operacao = ler_operacao()
            n_digitos = ler_digitos("Número de dígitos significativos")
            metodo = escolher_metodo()
            print(f"Precisão: {n_digitos} dígitos; método: {metodo}")
            resultado_teste = {
                "valor_exato": 7.123,
                "valor_aproximado": 7.12,
                "erro_absoluto": 0.003,
                "erro_relativo": 0.00042
            }
            exibir_resultado(resultado_teste)
        elif opcao == "2":
            # TODO: rodar exemplo 1
            print("\n[Exemplo 1] Em desenvolvimento...")
        elif opcao == "3":
            # TODO: rodar exemplo 2
            print("\n[Exemplo 2] Em desenvolvimento...")
        elif opcao == "4":
            # TODO: rodar exemplo 3
            print("\n[Exemplo 3] Em desenvolvimento...")
        elif opcao == "0":
            print("\nEncerrando o simulador.")
            break
        else:
            print("\nOpcao invalida. Tente novamente.")


if __name__ == "__main__":
    main()
