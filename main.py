from abc import abstractmethod
#1) Construir código necessário em Python para implementar o seguinte projeto: Uma classe abstrata chamada de Computador que contém os atributos/propriedades 
#   modelo, cor e preço. 
#   Esta classe também possui um método getInformacoes() que retorna todos os valores dos atributos. Esta classe também possui um método abstrato cadastrar().
#2) O projeto também deve possuir as classes Desktop e Notebook que herdam da classe Computador. A classe Desktop possui o atributo/propriedade fracamente privado 
#   potenciaDaFonte. 
#   Esta classe reimplementa o método getInformacoes() herdado de computador.
#3) A classe Notebook possui o atributo/propriedade fortemente privado tempoDeBateria. Esta classe reimplementa o método getInformacoes() herdado de computador.
#4) Construa um arquivo do tipo main com a utilização das classes construídas, para teste dos algoritmos.

class Computador():
    def __init__(self, modelo, cor, preco):
        self._modelo = modelo
        self._cor = cor
        self._preco = preco

    @abstractmethod
    def Cadastrar():
        @modelo.setter
        def set_modelo(self, modelo):
            self._modelo = modelo
            pass
        @cor.setter
        def set_cor(self, cor):
            self._cor = cor
            pass
        @preco.setter
        def set_preco(self, preco):
            self._preco = preco
            pass

    @property
    def get_Informacoes(self):
        return self._modelo, self._cor, self._preco

class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte

    def potenciaDaFonte(self):
        return self._potenciaDaFonte

    def get_Informacoes(self):
        super().get_Informacoes
        return print(f"Modelo:{self._modelo}. Cor:{self._cor}. Preco:{self._preco}. Fonte:{self._potenciaDaFonte}")

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria

    def tempoDeBateria(self):
        return self.__tempoDeBateria

    def get_Informacoes(self):
        super().get_Informacoes
        return print(f"Modelo:{self._modelo}. Cor:{self._cor}. Preco:{self._preco}. Bateria:{self.__tempoDeBateria}")

dt = Desktop("Intel", "Cinza", 2250.99, "110~220v")
dt.get_Informacoes()

nb = Notebook("Samsung", "Lilás", 1459.99, "10h")
nb.get_Informacoes()


