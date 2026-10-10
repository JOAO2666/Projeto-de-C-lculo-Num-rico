# Simulador de Propagação de Erros Numéricos

Trabalho prático da 1ª unidade da disciplina de **Cálculo Numérico** (Universidade Federal do Vale do São Francisco (UNIVASF), 2026.2).

Calculadora de precisão finita que simula uma máquina hipotética decimal com `k` dígitos significativos, com truncamento ou arredondamento, e calcula **Erro Absoluto (Ea)** e **Erro Relativo (Er)** de cada operação.

> Este README é apenas guia de instalação e uso. 

## Equipe e divisão de autoria

| Parte | Responsável | Responsabilidade | Onde está no código |
|---|---|---|---|
| 1ª PARTE | **João Emanuel Almeida Ramos** | Normalização, precisão numérica e POO | `src/precisao.py` → classe `MaquinaHipotetica` (`normalizar`, `truncar`, `arredondar`, `ajustar`) |
| 2ª PARTE | **Eduardo dos Santos Ferreira Sousa** | Operações aritméticas e métricas de erro | `main.py` → `calcular_operacao`, `calcular_erros`, `sequencia_somas` |
| 3ª PARTE | **Júlio César Mendes do Nascimento** | Interface CLI e menus | `main.py` → `ler_numero`, `ler_operacao`, `ler_digitos`, `escolher_metodo`, `exibir_resultado`, `exibir_menu`, `main` |

Preserve essa divisão na apresentação. O professor avalia autoria individual.

##  O que o programa faz

 Representa números na forma normalizada base 10: `x = ± m × 10^e`, com `0.1 ≤ |m| < 1.0`.
 Ajusta cada entrada e cada resultado para `k` dígitos significativos:
    **Truncamento:** descarta dígitos além de `k`.
    **Arredondamento:** se o dígito `k+1 ≥ 5`, soma 1 no último dígito.
 Executa `+`, `-`, `*`, `/` em duas vias: **exata** (Python) e **aproximada** (máquina hipotética).
 Calcula:
    `Ea = |Valor Exato − Valor Aproximado|`
    `Er = Ea / |Valor Aproximado|` (indefinido se aproximado = 0).
 Demonstra fenômenos clássicos: **cancelamento subtrativo** e **propagação cumulativa de erro**.

## Estrutura do repositório

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

## Pré-requisitos

**Python 3.8 ou superior.** Recomendado 3.10+. Verifique com:
   ```bash
   python --version
   ```
 **Git** (opcional, só se for clonar). Alternativa: baixar ZIP do GitHub.
 Windows, Linux ou macOS. Exemplos abaixo são para **Windows (PowerShell)**.

## Instalação: passo a passo (Windows)

### Opção A: Clonar com Git (recomendado)

```powershell
# Clonar
git clone https://github.com/JOAO2666/Projeto-de-C-lculo-Num-rico.git

#  Entrar na pasta
cd Projeto-de-C-lculo-Num-rico

#  Confirmar Python
python --version

#  Executar
python main.py
```

### Opção B: sem Git (baixar ZIP)

 Acesse `https://github.com/JOAO2666/Projeto-de-C-lculo-Num-rico`
 Clique em **Code → Download ZIP**.
 Extraia o ZIP.
 Abra PowerShell **dentro da pasta extraída** (Shift + botão direito → Abrir no Terminal).
 Rode:
   ```powershell
   python main.py
   ```

> Se `python` não for reconhecido: reinstale o Python marcando **Add python.exe to PATH** na primeira tela do instalador. Depois feche e reabra o terminal. Alternativa: tente `py main.py`.

> Não precisa `pip install`. Não há `requirements.txt` porque o projeto não usa pacotes externos.

##  Como usar (menu)

Ao rodar `python main.py` você vê:

```
==================================================
    SIMULADOR DE PROPAGAÇÃO DE ERROS NUMÉRICOS
==================================================
1 - Realizar Nova Operação (Entrada Livre)
2 - Executar Casos de Teste do PDF (Exemplos 2 e 3)
3 - Sair
```

 **Opção 1:** digite `x`, `y`, operação (`+ - * /`), `k` (padrão 4) e método (1 = arredondamento, 2 = truncamento). Aceita vírgula ou ponto como decimal.
 **Opção 2:** roda os casos oficiais do enunciado (cancelamento subtrativo e somas sucessivas).
 **Opção 3:** sai.

## Roteiro de demonstração para nota máxima (5 min)

Faça exatamente nesta ordem na frente do professor:

**Demo 1: Soma simples, k=4 (Exemplo 1):**
 Opção 1 → `x=1.23456`, `y=2.34567`, `+`, `k=4`, arredondamento.
 Esperado: Exato `3.58023` → Aprox `3.581` → `Ea=0.00077` → `Er≈0.0215%`.
 Repita com truncamento: Aprox `3.579` → `Ea=0.00123` → `Er≈0.0344%`.
 Fale: "o arredondamento erra menos que o truncamento aqui".

**Demo 2: Cancelamento subtrativo (Exemplo 2):**
 Opção 1 → `x=0.76545`, `y=0.76541`, `-`, `k=4`, arredondamento.
 Valor exato `0.00004`. Mostre que pequenas diferenças nas entradas geram erro relativo enorme (teoria prevê ~60%).
 Se aparecer `Aprox=0` com `Er indefinido`, explique: "é a anulação total (perda de dígitos significativos do truncamento). Isso também é conteúdo avaliado."

**Demo 3: Somas sucessivas (Exemplo 3):**
 Opção 2 → escolha `2` (somar `0.56786` dez vezes, `k=4`, truncamento).
 Esperado teórico: exato `5.6786` vs máquina `≈5.6710`, `Ea≈0.0076`.
 Fale: "o erro se acumula a cada passo porque truncamos o acumulador toda vez".

Esse roteiro cobre os 3 critérios que o professor colocou no PDF.

## Validação rápida (checklist antes de entregar)

 `python main.py` abre o menu sem erro.
 Opção 1 com `1.23456 + 2.34567`, `k=4`, arredondamento → `3.581`.
 Divisão por zero mostra mensagem de erro, não quebra (`y=0` com `/`).
 `0` como entrada funciona (`m=0.0`, `e=0`).
 `src/precisao.py` existe e `main.py` importa `from src.precisao import MaquinaHipotetica`.
 Repositório no GitHub está público e com os 3 nomes na Equipe.

##  Problemas comuns (FAQ)

| Sintoma | Causa | Solução |
|---|---|---|
| `'python' não é reconhecido` | Python sem PATH | Reinstale marcando Add to PATH, ou use `py main.py` |
| `ModuleNotFoundError: src` | Rodou de dentro de `src/` | Volte para a raiz: `cd ..` e rode `python main.py` |
| Acentos quebrados (`Propaga??o`) | Code page do PowerShell | Normal no Windows, não tira ponto. Opcional: `chcp 65001` antes de rodar |
| `Er: Não definido` | Aproximado deu zero | Comportamento correto pela fórmula (divisão por zero). Explique como anulação total |
| `ZeroDivisionError` na máquina | `y_rep` zerou após ajuste | Tratado pelo programa com mensagem. Teste com `y` muito pequeno e `k` pequeno |

