from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, tipo: str, id: str, tempo_entrada: int):
        self.__id = id
        self.__tempo_entrada = tempo_entrada
        self.__tipo = tipo
    
    def getId(self):
        return self.__id
    
    def getTempoEntrada(self):
        return self.__tempo_entrada
    
    def getTipo(self):
        return self.__tipo

    @abstractmethod
    def calcularValor(self, tempo_saida: int):
        pass

    @abstractmethod
    def pagar(self):
        pass

    def __str__(self):
        tipo_str = self.getTipo().rjust(10, '_')
        id_str = self.getId().rjust(10, '_')
        return f"{tipo_str} : {id_str} : {self.__tempo_entrada}"
    
class Carro(Veiculo):
    def __init__(self, tipo: str, id: str, tempo_entrada: int):
        super().__init__(tipo, id, tempo_entrada)  

    def calcularValor(self, tempo_saida: int):
        duracao = tempo_saida - self.getTempoEntrada()
        valorMin = 5.00
        valor = duracao / 10
        if valor < valorMin:
            return valorMin
        return valor
    
    def pagar(self):
        return f"Carro chegou {self.__tempo_entrada} saiu {self.__tempo_saida}. Pagar: {self.calcularValor}"
    

class Moto(Veiculo):
    def __init__(self, tipo: str, id: str, tempo_entrada: int):
        super().__init__(tipo, id, tempo_entrada)  

    def calcularValor(self, tempo_saida: int):
        duracao = tempo_saida - self.getTempoEntrada()
        valorTotal = duracao / 20
        return valorTotal
    
    def pagar(self):
        return f"Moto chegou {self.__tempo_entrada} saiu {self.__tempo_saida}. Pagar: {self.calcularValor}"

class Bike(Veiculo):
    def __init__(self, tipo: str, id: str, tempo_entrada: int):
        super().__init__(tipo, id, tempo_entrada)  

    def calcularValor(self, tempo_saida: int):
        valorFixo = 3.00
        return valorFixo
    
    def pagar(self):
        return f"Carro chegou {self.__tempo_entrada} saiu {self.__tempo_saida}. Pagar: {self.calcularValor}"


class Estacionamento:
    def __init__(self, hora_atual: int):
        self.__veiculos: list[Veiculo] = []
        self.__hora_atual = hora_atual

    def getVeiculos(self):
        return self.__veiculos
    
    def getHoraAtual(self):
        return self.__hora_atual
    
    def setHoraAtual(self, hora: int):
        self.__hora_atual += hora
    
    def estacionar(self, veiculo: Veiculo):
        self.__veiculos.append(veiculo)

    def procurarVeiculo(self, id: str):
        for veiculo in self.__veiculos:
            if veiculo.getId() == id:
                return veiculo
            
    def pagar(self, veiculo: Veiculo):
        tempo_saida = self.getHoraAtual()
        valor = veiculo.calcularValor(tempo_saida)
        return f"{veiculo.getTipo()} chegou {veiculo.getTempoEntrada()} saiu {tempo_saida}. Pagar R$ {valor:.2f}"

    def __str__(self):
        result = ""
        for veiculo in self.__veiculos:
            result += str(veiculo) + "\n"
        result += f"Hora atual: {self.__hora_atual}"
        return result


def main():
    estacionamento = Estacionamento(0)

    while True:
        try:

            line = input()
            print("$" + line)
            args = line.split()

            if args[0] == "end":
                break

            elif args[0] == "show":
                print(estacionamento)

            elif args[0] == "tempo":
                try:
                    nova_hora = int(args[1])
                    estacionamento.setHoraAtual(nova_hora)

                except ValueError:
                    print("fail: comando invalido")

            elif args[0] == "estacionar":
                try:
                    tipo = args[1].lower()
                    veiculo_id = args[2]
                    tempo_entrada = estacionamento.getHoraAtual()

                    if tipo == "carro":
                        veiculo = Carro("Carro", veiculo_id, tempo_entrada)
                        estacionamento.estacionar(veiculo)
                    elif tipo == "moto":
                        veiculo = Moto("Moto", veiculo_id, tempo_entrada)
                        estacionamento.estacionar(veiculo)
                    elif tipo == "bike":
                        veiculo = Bike("Bike", veiculo_id, tempo_entrada)
                        estacionamento.estacionar(veiculo)
                    else:
                        print("fail: tipo de veiculo invalido")
                        pass

                except ValueError:
                    print("fail: comando invalido")

            elif args[0] == "pagar":
                try:
                    veiculo_id = args[1]
                    veiculo = estacionamento.procurarVeiculo(veiculo_id)
                    if veiculo:
                        print(estacionamento.pagar(veiculo))
                    else:
                        print("fail: veiculo nao encontrado")

                except ValueError:
                    print("fail: comando invalido")

        except Exception as e:
            print(e)
main()