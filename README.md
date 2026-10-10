# Simulador de Propagação de Erros Numéricos

Trabalho prático da 1ª unidade da disciplina de **Cálculo Numérico** (Universidade Federal do Vale do São Francisco (UNIVASF), 2026.2).

Calculadora de precisão finita que simula uma máquina hipotética decimal com `k` dígitos significativos, com truncamento ou arredondamento, e calcula **Erro Absoluto (Ea)** e **Erro Relativo (Er)** de cada operação.

> Este README é apenas guia de instalação e uso. **Nenhum código do projeto foi alterado.**

## 1. Equipe e divisão de autoria

| Parte | Responsável | Responsabilidade | Onde está no código |
|---|---|---|---|
| 1ª PARTE | **João Emanuel Almeida Ramos** | Normalização, precisão numérica e POO | `src/precisao.py` → classe `MaquinaHipotetica` (`normalizar`, `truncar`, `arredondar`, `ajustar`) |
| 2ª PARTE | **Eduardo dos Santos Ferreira Sousa** | Operações aritméticas e métricas de erro | `main.py` → `calcular_operacao`, `calcular_erros`, `sequencia_somas` |
| 3ª PARTE | **Júlio César Mendes do Nascimento** | Interface CLI e menus | `main.py` → `ler_numero`, `ler_operacao`, `ler_digitos`, `escolher_metodo`, `exibir_resultado`, `exibir_menu`, `main` |

Preserve essa divisão na apresentação. O professor avalia autoria individual.

## 2. O que o programa faz

1. Representa números na forma normalizada base 10: `x = ± m × 10^e`, com `0.1 ≤ |m| < 1.0`.
2. Ajusta cada entrada e cada resultado para `k` dígitos significativos:
   2.1. **Truncamento:** descarta dígitos além de `k`.
   2.2. **Arredondamento:** se o dígito `k+1 ≥ 5`, soma 1 no último dígito.
3. Executa `+`, `-`, `*`, `/` em duas vias: **exata** (Python) e **aproximada** (máquina hipotética).
4. Calcula:
   4.1. `Ea = |Valor Exato − Valor Aproximado|`
   4.2. `Er = Ea / |Valor Aproximado|` (indefinido se aproximado = 0).
5. Demonstra fenômenos clássicos: **cancelamento subtrativo** e **propagação cumulativa de erro**.

## 3. Estrutura do repositório

```
Projeto-de-C-lculo-Num-rico/
├── main.py                 # Ponto de entrada ( junta as 3 partes )
├── src/
│   ├── __init__.py         # (pode estar vazio, só marca o pacote)
│   └── precisao.py         # Classe MaquinaHipotetica (Parte 1)
├── 1-projeto-1-erros.pdf   # Enunciado oficial
└── README.md               # Este arquivo
```

Dependências: **nenhuma externa**. Só biblioteca padrão do Python (`math`). Funciona em qualquer Python 3.8+.

## 4. Pré-requisitos

1. **Python 3.8 ou superior.** Recomendado 3.10+. Verifique com:
   ```bash
   python --version
   ```
2. **Git** (opcional, só se for clonar). Alternativa: baixar ZIP do GitHub.
3. Windows, Linux ou macOS. Exemplos abaixo são para **Windows (PowerShell)**.

## 5. Instalação: passo a passo (Windows)

### Opção A: Clonar com Git (recomendado)

```powershell
# 1. Clonar
git clone https://github.com/JOAO2666/Projeto-de-C-lculo-Num-rico.git

# 2. Entrar na pasta
cd Projeto-de-C-lculo-Num-rico

# 3. Confirmar Python
python --version

# 4. Executar
python main.py
```

### Opção B: sem Git (baixar ZIP)

1. Acesse `https://github.com/JOAO2666/Projeto-de-C-lculo-Num-rico`
2. Clique em **Code → Download ZIP**.
3. Extraia o ZIP.
4. Abra PowerShell **dentro da pasta extraída** (Shift + botão direito → Abrir no Terminal).
5. Rode:
   ```powershell
   python main.py
   ```

> Se `python` não for reconhecido: reinstale o Python marcando **Add python.exe to PATH** na primeira tela do instalador. Depois feche e reabra o terminal. Alternativa: tente `py main.py`.

> Não precisa `pip install`. Não há `requirements.txt` porque o projeto não usa pacotes externos.

## 6. Como usar (menu)

Ao rodar `python main.py` você vê:

```
==================================================
    SIMULADOR DE PROPAGAÇÃO DE ERROS NUMÉRICOS
==================================================
1 - Realizar Nova Operação (Entrada Livre)
2 - Executar Casos de Teste do PDF (Exemplos 2 e 3)
3 - Sair
```

1. **Opção 1:** digite `x`, `y`, operação (`+ - * /`), `k` (padrão 4) e método (1 = arredondamento, 2 = truncamento). Aceita vírgula ou ponto como decimal.
2. **Opção 2:** roda os casos oficiais do enunciado (cancelamento subtrativo e somas sucessivas).
3. **Opção 3:** sai.

## 7. Roteiro de demonstração para nota máxima (5 min)

Faça exatamente nesta ordem na frente do professor:

**Demo 1: Soma simples, k=4 (Exemplo 1):**
1. Opção 1 → `x=1.23456`, `y=2.34567`, `+`, `k=4`, arredondamento.
2. Esperado: Exato `3.58023` → Aprox `3.581` → `Ea=0.00077` → `Er≈0.0215%`.
3. Repita com truncamento: Aprox `3.579` → `Ea=0.00123` → `Er≈0.0344%`.
4. Fale: "o arredondamento erra menos que o truncamento aqui".

**Demo 2: Cancelamento subtrativo (Exemplo 2):**
1. Opção 1 → `x=0.76545`, `y=0.76541`, `-`, `k=4`, arredondamento.
2. Valor exato `0.00004`. Mostre que pequenas diferenças nas entradas geram erro relativo enorme (teoria prevê ~60%).
3. Se aparecer `Aprox=0` com `Er indefinido`, explique: "é a anulação total (perda de dígitos significativos do truncamento). Isso também é conteúdo avaliado."

**Demo 3: Somas sucessivas (Exemplo 3):**
1. Opção 2 → escolha `2` (somar `0.56786` dez vezes, `k=4`, truncamento).
2. Esperado teórico: exato `5.6786` vs máquina `≈5.6710`, `Ea≈0.0076`.
3. Fale: "o erro se acumula a cada passo porque truncamos o acumulador toda vez".

Esse roteiro cobre os 3 critérios que o professor colocou no PDF.

## 8. Validação rápida (checklist antes de entregar)

1. `python main.py` abre o menu sem erro.
2. Opção 1 com `1.23456 + 2.34567`, `k=4`, arredondamento → `3.581`.
3. Divisão por zero mostra mensagem de erro, não quebra (`y=0` com `/`).
4. `0` como entrada funciona (`m=0.0`, `e=0`).
5. `src/precisao.py` existe e `main.py` importa `from src.precisao import MaquinaHipotetica`.
6. Repositório no GitHub está público e com os 3 nomes na Equipe.

## 9. Problemas comuns (FAQ)

| Sintoma | Causa | Solução |
|---|---|---|
| `'python' não é reconhecido` | Python sem PATH | Reinstale marcando Add to PATH, ou use `py main.py` |
| `ModuleNotFoundError: src` | Rodou de dentro de `src/` | Volte para a raiz: `cd ..` e rode `python main.py` |
| Acentos quebrados (`Propaga??o`) | Code page do PowerShell | Normal no Windows, não tira ponto. Opcional: `chcp 65001` antes de rodar |
| `Er: Não definido` | Aproximado deu zero | Comportamento correto pela fórmula (divisão por zero). Explique como anulação total |
| `ZeroDivisionError` na máquina | `y_rep` zerou após ajuste | Tratado pelo programa com mensagem. Teste com `y` muito pequeno e `k` pequeno |

## 10. Como entregar

1. Suba este README para o repo (sem mexer em `main.py` ou `src/`).
2. Deixe o repo **público**.
3. Entregue o link + PDF do enunciado + nomes dos 3 membros.
4. Na apresentação, cada membro explica sua parte (tabela do item 1).

Bons estudos e boa apresentação.
