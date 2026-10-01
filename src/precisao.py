import math

class MaquinaHipotetica:
    # Isso aqui vai representar uma máquina para fazer os controles
    # de dígitos significativos e o método de corte.

    def __init__(self, digitos: int = 4, metodo: str = "arredondamento"):
        self.digitos = digitos
        self.metodo = metodo.strip().lower()

    def normalizar(self, valor: float):
        # Essa função vai servir para converter da escrita normal para mantissa e expoente:
        # 0.1 <= |mantissa| < 1.0. Serve para isolar as casas decimais significativas.
        if valor == 0.0:
            return 0.0, 0

        expoente = math.floor(math.log10(abs(valor))) + 1
        mantissa = valor / (10 ** expoente)
        return mantissa, expoente

    def truncar(self, mantissa: float) -> float:
        # Corta os dígitos além de self.digitos
        fator = 10 ** self.digitos
        return math.trunc(mantissa * fator) / fator

    def arredondar(self, mantissa: float) -> float:
        # Arredonda para self.digitos observando o próximo dígito
        fator = 10 ** self.digitos
        return round(mantissa * fator) / fator

    def ajustar(self, valor: float) -> float:
        # Aplica a normalização e o ajuste configurado na máquina
        if valor == 0.0:
            return 0.0

        mantissa, expoente = self.normalizar(valor)

        if self.metodo == "truncamento":
            mantissa_ajustada = self.truncar(mantissa)
        elif self.metodo == "arredondamento":
            mantissa_ajustada = self.arredondar(mantissa)
        else:
            raise ValueError(f"Método '{self.metodo}' não reconhecido.")

        return mantissa_ajustada * (10 ** expoente)
