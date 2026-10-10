"""
PROJETO DE CÁLCULO NUMÉRICO - UNIDADE 1 (ERROS) - 2026.2
UNIVERSIDADE FEDERAL DO VALE DO SÃO FRANCISCO (UNIVASF)

SIMULADOR DE PROPAGAÇÃO DE ERROS NUMÉRICOS

Divisão de Tarefas:
1ª PARTE: João Emanuel Almeida Ramos  -> Normalização, Precisão Numérica e POO
2ª PARTE: Eduardo dos Santos Ferreira  -> Operações Aritméticas e Métricas de Erro
3ª PARTE: Júlio César Mendes          -> Interface de Usuário e Menu Interativo
"""

import math
from src.precisao import MaquinaHipotetica


# ==============================================================================
# 1ª PARTE: NORMALIZAÇÃO E PRECISÃO NUMÉRICA (João Emanuel)
# ==============================================================================

def normalizar(valor: float):
    """Converte o número para a forma canônica: mantissa * 10^expoente."""
    maquina = MaquinaHipotetica()
    return maquina.normalizar(valor)

def truncar(mantissa: float, digitos: int) -> float:
    """Descarta os dígitos além da precisão especificada."""
    maquina = MaquinaHipotetica(digitos=digitos)
    return maquina.truncar(mantissa)

def arredondar(mantissa: float, digitos: int) -> float:
    """Arredonda para a quantidade de dígitos especificada."""
    maquina = MaquinaHipotetica(digitos=digitos)
    return maquina.arredondar(mantissa)

def ajustar_precisao(valor: float, n_digitos: int, metodo: str) -> float:
    """Aplica o ajuste de precisão na máquina hipotética."""
    maquina = MaquinaHipotetica(digitos=n_digitos, metodo=metodo)
    return maquina.ajustar(valor)


# ==============================================================================
# 2ª PARTE: OPERAÇÕES ARITMÉTICAS E MÉTRICAS DE ERRO (Eduardo dos Santos)
# ==============================================================================

def calcular_erros(valor_exato: float, valor_aproximado: float) -> tuple:
    """
    Calcula o Erro Absoluto e o Erro Relativo conforme a especificação do PDF:
    Ea = |Valor Exato - Valor Aproximado|
    Er = |Valor Exato - Valor Aproximado| / |Valor Aproximado|
    """
    erro_absoluto = abs(valor_exato - valor_aproximado)
    if valor_aproximado != 0.0:
        erro_relativo = erro_absoluto / abs(valor_aproximado)
    else:
        erro_relativo = None
    return erro_absoluto, erro_relativo

def calcular_operacao(x: float, y: float, op: str, n_digitos: int, metodo: str = "arredondamento") -> dict:
    """
    Executa a operação exata e a operação na máquina com precisão controlada.
    """
    # 1. Operação Exata (precisão da linguagem)
    if op == '+':
        valor_exato = x + y
    elif op == '-':
        valor_exato = x - y
    elif op == '*':
        valor_exato = x * y
    elif op == '/':
        if y == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        valor_exato = x / y
    else:
        raise ValueError(f"Operação '{op}' inválida.")

    # 2. Operação na Máquina Hipotética
    x_rep = ajustar_precisao(x, n_digitos, metodo)
    y_rep = ajustar_precisao(y, n_digitos, metodo)

    if op == '+':
        res_bruto = x_rep + y_rep
    elif op == '-':
        res_bruto = x_rep - y_rep
    elif op == '*':
        res_bruto = x_rep * y_rep
    elif op == '/':
        if y_rep == 0:
            raise ZeroDivisionError("Divisão por zero na máquina hipotética.")
        res_bruto = x_rep / y_rep

    valor_aproximado = ajustar_precisao(res_bruto, n_digitos, metodo)
    erro_absoluto, erro_relativo = calcular_erros(valor_exato, valor_aproximado)

    return {
        "x_norm": x_rep,
        "y_norm": y_rep,
        "operacao": op,
        "valor_exato": valor_exato,
        "valor_aproximado": valor_aproximado,
        "erro_absoluto": erro_absoluto,
        "erro_relativo": erro_relativo
    }

def sequencia_somas(termo: float, repeticoes: int = 10, n_digitos: int = 4, metodo: str = "truncamento") -> list:
    """
    Simula o acúmulo e propagação de erros em somas sucessivas (Exemplo 3 do PDF).
    """
    valor_exato = termo * repeticoes
    acumulador_aproximado = 0.0
    resultados = []
    termo_ajustado = ajustar_precisao(termo, n_digitos, metodo)

    print(f"\n--- PROPAGAÇÃO DE ERROS EM SOMAS SUCESSIVAS ({metodo.upper()}, k={n_digitos}) ---")
    for i in range(1, repeticoes + 1):
        acumulador_aproximado = ajustar_precisao(acumulador_aproximado + termo_ajustado, n_digitos, metodo)
        ea_passo, er_passo = calcular_erros(termo * i, acumulador_aproximado)
        resultados.append({
            "passo": i,
            "acumulado": acumulador_aproximado,
            "erro_absoluto": ea_passo,
            "erro_relativo": er_passo
        })
        print(f"Soma {i:2d}: {acumulador_aproximado:.6f} | Ea = {ea_passo:.6f}")

    ea_total, er_total = calcular_erros(valor_exato, acumulador_aproximado)
    print(f"\nValor Exato Total:          {valor_exato}")
    print(f"Resultado Final na Máquina: {acumulador_aproximado}")
    print(f"Erro Absoluto Total:        {ea_total:.6f}")
    if er_total is not None:
        print(f"Erro Relativo Total:        {er_total * 100:.4f}%")
    return resultados


# ==============================================================================
# 3ª PARTE: INTERFACE DE USUÁRIO E MENU INTERATIVO (Júlio César)
# ==============================================================================

def ler_numero(mensagem: str) -> float:
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("Entrada inválida. Digite um número real válido.")

def ler_operacao() -> str:
    operacoes_validas = ["+", "-", "*", "/"]
    while True:
        op = input("Escolha a operação (+, -, *, /): ").strip()
        if op in operacoes_validas:
            return op
        print("Operação inválida. Escolha entre: +, -, * ou /")

def ler_digitos(mensagem: str = "Número de dígitos significativos", padrao: int = 4) -> int:
    while True:
        entrada = input(f"{mensagem} [{padrao}]: ").strip()
        if entrada == "":
            return padrao
        try:
            n = int(entrada)
            if n > 0:
                return n
            print("O número de dígitos deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def escolher_metodo() -> str:
    while True:
        print("\nMétodo de ajuste:")
        print("1 - Arredondamento (padrão)")
        print("2 - Truncamento")
        opcao = input("Escolha uma opção [1]: ").strip()
        if opcao in ["", "1"]:
            return "arredondamento"
        if opcao == "2":
            return "truncamento"
        print("Opção inválida. Digite 1 ou 2.")

def exibir_resultado(resultado: dict):
    print("\n" + "=" * 50)
    print("               RESULTADO DA OPERAÇÃO")
    print("=" * 50)
    print(f"Operação Realizada: {resultado.get('operacao', '')}")
    print(f"Valor Exato:        {resultado['valor_exato']:.8g}")
    print(f"Valor Aproximado:   {resultado['valor_aproximado']:.8g}")
    print(f"Erro Absoluto (Ea): {resultado['erro_absoluto']:.8g}")
    if resultado['erro_relativo'] is not None:
        print(f"Erro Relativo (Er): {resultado['erro_relativo']:.8g} ({resultado['erro_relativo'] * 100:.4f}%)")
    else:
        print("Erro Relativo (Er): Não definido (divisão por zero)")
    print("=" * 50 + "\n")

def executar_casos_pdf():
    print("\n" + "-" * 50)
    print("       CASOS DE TESTE OFICIAIS DO PDF")
    print("-" * 50)
    print("1 - Exemplo 2: Cancelamento Subtrativo (x=0.76545, y=0.76541, k=4)")
    print("2 - Exemplo 3: Propagação de Erros (Somar 0.56786 dez vezes, k=4)")
    opcao = input("Escolha o teste [1]: ").strip()

    if opcao in ["", "1"]:
        print("\n[EXEMPLO 2 - CANCELAMENTO SUBTRATIVO]")
        res = calcular_operacao(0.76545, 0.76541, "-", 4, "arredondamento")
        exibir_resultado(res)
    elif opcao == "2":
        sequencia_somas(0.56786, 10, 4, "truncamento")

def exibir_menu():
    print("\n" + "=" * 50)
    print("    SIMULADOR DE PROPAGAÇÃO DE ERROS NUMÉRICOS")
    print("=" * 50)
    print("1 - Realizar Nova Operação (Entrada Livre)")
    print("2 - Executar Casos de Teste do PDF (Exemplos 2 e 3)")
    print("3 - Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            x = ler_numero("Digite o primeiro número (x): ")
            y = ler_numero("Digite o segundo número (y): ")
            op = ler_operacao()
            n_digitos = ler_digitos("Número de dígitos significativos")
            metodo = escolher_metodo()

            try:
                resultado = calcular_operacao(x, y, op, n_digitos, metodo)
                exibir_resultado(resultado)
            except ZeroDivisionError as e:
                print(f"\nErro de cálculo: {e}\n")

        elif opcao == "2":
            executar_casos_pdf()

        elif opcao == "3":
            print("\nEncerrando o simulador. Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()
