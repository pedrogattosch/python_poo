# Python — Programação Orientada a Objetos

Repositório de estudo com exercícios, desafios e anotações sobre programação orientada a objetos em Python.

## Sumário

1. [Conceitos fundamentais](#1-conceitos-fundamentais)
2. [UML e modelagem](#2-uml-e-modelagem)
3. [Classes, objetos, self e construtor](#3-classes-objetos-self-e-construtor)
4. [Atributos de instância e de classe](#4-atributos-de-instância-e-de-classe)
5. [Métodos, retornos e estado](#5-métodos-retornos-e-estado)
6. [Documentação e métodos especiais](#6-documentação-e-métodos-especiais)
7. [Herança](#7-herança)
8. [Abstração e classes abstratas](#8-abstração-e-classes-abstratas)
9. [Encapsulamento](#9-encapsulamento)
10. [Getters, setters e propriedades](#10-getters-setters-e-propriedades)
11. [Polimorfismo](#11-polimorfismo)
12. [Módulos e organização](#12-módulos-e-organização)

## 1. Conceitos fundamentais

**POO** significa **Programação Orientada a Objetos**. A ideia é organizar o programa em objetos que reúnem características e comportamentos relacionados.

Os quatro pilares são:

- **Abstração:** focar no essencial para o problema.
- **Encapsulamento:** controlar como o estado interno é consultado e alterado.
- **Herança:** organizar tipos gerais e tipos especializados.
- **Polimorfismo:** permitir comportamentos diferentes por uma mesma forma de uso.

Em Python, números, strings, listas, funções, classes e módulos também são objetos. Quando você usa `lista.append(...)`, já está chamando um método de um objeto.

## 2. UML e modelagem

**UML** significa *Unified Modeling Language*, em português, **Linguagem de Modelagem Unificada**. Ela possui diferentes diagramas; em POO, o mais utilizado é o diagrama de classes.

O desenho separa a classe em três partes:

```text
+---------------------------+
| NomeClasse                |
+---------------------------+
| atributos                 | -> Características que tenho
+---------------------------+
| métodos                   | -> Coisas que posso fazer
+---------------------------+
```

Na notação UML, os símbolos `+`, `#` e `-` representam, respectivamente, público, protegido e privado.

Na herança, a seta de generalização com triângulo vazio aponta da subclasse para a superclasse.

## 3. Classes, objetos, self e construtor

Uma classe reúne **atributos** e **métodos**. Ela é definida com `class`:

```python
class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def consultar_saldo(self):
        return self.saldo
```

Nesse exemplo, `titular` e `saldo` são atributos de cada conta. `depositar()` e `consultar_saldo()` são métodos.

---

Um objeto, também chamado de instância, é criado ao chamar a classe:

```python
conta_pedro = Conta("Pedro", 500)
conta_sofia = Conta("Sofia", 100)

print(conta_pedro.consultar_saldo())  # 500
print(conta_sofia.consultar_saldo())  # 100
```

As duas contas pertencem à mesma classe, mas cada uma guarda seus próprios valores. A notação de ponto permite acessar atributos e chamar métodos.

---

`self` é o parâmetro que recebe o próprio objeto em um método de instância. Ele permite acessar os atributos e outros métodos desse objeto.

```python
def depositar(self, valor):
    self.saldo += valor
```

Ao chamar `conta_pedro.depositar(200)`, Python passa `conta_pedro` automaticamente como primeiro argumento. Nesse exemplo, a chamada equivale a:

```python
Conta.depositar(conta_pedro, 200)
```

---

`__init__` define o estado inicial de uma instância. É chamado automaticamente durante a criação do objeto:

```python
conta = Conta("Pedro", 500)
```

No exemplo da classe, essa chamada faz com que:

```python
self.titular = "Pedro"
self.saldo = 500
```

Como `saldo=0` tem um valor padrão, `Conta("Pedro")` começa com saldo zero.

Embora frequentemente chamado de construtor, `__init__` é, tecnicamente, o inicializador, o objeto já foi criado por `__new__` quando ele é executado. `__init__` não deve retornar um valor diferente de `None`.

## 4. Atributos de instância e de classe

Os atributos de instância guardam dados específicos de cada objeto. Normalmente são definidos no `__init__`, usando `self`:

```python
class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

pedro = Conta("Pedro", 500)
sofia = Conta("Sofia", 100)

pedro.saldo += 200

print(pedro.saldo)  # 700
print(sofia.saldo)  # 100
```

Cada conta tem seus próprios atributos `titular` e `saldo`. Alterar o saldo de Pedro não altera o de Sofia.

O `__init__` é o lugar habitual para definir esses atributos, mas outros métodos também podem criá-los com `self.nome = valor`.

---

Os atributos de classe são definidos no corpo da classe, fora dos métodos. São úteis para informações comuns às instâncias:

```python
class Conta:
    moeda = "BRL"  # Atributo de classe

    def __init__(self, titular):
        self.titular = titular  # Atributo de instância

pedro = Conta("Pedro")
sofia = Conta("Sofia")

print(Conta.moeda)  # BRL
print(pedro.moeda)  # BRL
print(sofia.moeda)  # BRL
```

Nesse caso, `moeda` não foi copiada para cada objeto: as instâncias consultam o atributo da classe.

```python
Conta.moeda = "USD"

print(pedro.moeda)  # USD
```

## 5. Métodos, retornos e estado

Um método é uma função definida em uma classe. Um **método de instância** recebe o objeto no parâmetro `self`, permitindo acessar seus atributos e outros métodos.

```python
class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor deve ser positivo")
        self.saldo += valor

    def consultar_saldo(self):
        return self.saldo
```

Para chamar um método, usamos o objeto, um ponto e o nome do método com parênteses:

```python
conta = Conta("Pedro", 500)
conta.depositar(200)
```

Nessa chamada, `self` recebe `conta` automaticamente e `valor` recebe `200`.

---

`return` encerra a execução do método e entrega um resultado ao código que o chamou. Esse resultado pode ser armazenado, usado em expressões ou passado para outra função.

```python
saldo_atual = conta.consultar_saldo()

print(saldo_atual)       # 700
print(saldo_atual > 500) # True
```

Se a execução chegar ao fim sem um `return`, o resultado será `None`. Um `return` sem valor também retorna `None`.

```python
resultado = conta.depositar(100)

print(resultado)   # None
print(conta.saldo)  # 800
```

---

O estado é o conjunto de valores que o objeto guarda em seus atributos em determinado momento.

```python
conta = Conta("Pedro", 500)
# Estado: titular = "Pedro", saldo = 500

conta.depositar(200)
# Estado: titular = "Pedro", saldo = 700
```

O método altera o estado quando modifica um atributo, como em `self.saldo += valor`.

Uma variável local, por outro lado, não se torna um atributo automaticamente:

```python
# Método que pode ser adicionado à classe Conta:
def simular_deposito(self, valor):
    saldo_simulado = self.saldo + valor
    return saldo_simulado
```

`saldo_simulado` é uma variável local. O cálculo usa o saldo da conta, mas não modifica `self.saldo`:

```python
conta = Conta("Pedro", 500)

print(conta.simular_deposito(200)) # 700
print(conta.saldo)                 # 500
```

## 6. Documentação e métodos especiais

Uma docstring é uma string escrita como a **primeira instrução** de uma classe, função ou método. Por convenção, usamos aspas triplas duplas, mesmo quando o texto ocupa uma linha.

```python
class Conta:
    """Representa uma conta com titular e saldo em reais."""

    def __init__(self, titular, saldo=0):
        """Inicializa a conta com titular e saldo opcional."""
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        """Adiciona um valor positivo ao saldo.

        Args:
            valor: Quantia a depositar, maior que zero.

        Returns:
            None. O saldo da conta é alterado diretamente.

        Raises:
            ValueError: Se o valor for menor ou igual a zero.
        """
        if valor <= 0:
            raise ValueError("O valor deve ser positivo")
        self.saldo += valor
```

Uma boa docstring explica o propósito e, quando necessário, os parâmetros, o retorno, as alterações de estado e os erros possíveis. As seções `Args`, `Returns` e `Raises` são uma convenção de documentação, não palavras obrigatórias do Python.

- **Docstring:** documenta como usar o código e fica disponível para ferramentas de ajuda.
- **Comentário:** explica uma decisão ou detalhe da implementação.

```python
help(Conta)
help(Conta.depositar)
print(Conta.depositar.__doc__)
```

`help()` apresenta a documentação, `__doc__` permite acessar o texto da docstring. `__doc__` é um atributo, não um método.

---

Métodos especiais são métodos com dois sublinhados antes e depois do nome, como `__init__` e `__str__`. Também são chamados de dunder methods.

Python os chama em situações específicas. Ao implementá-los, você define como seu objeto se comporta nessas situações.

| Método | Para que serve |
| --- | --- |
| `__init__` | Inicializa os atributos do objeto ao criá-lo. |
| `__str__` | Define o texto legível mostrado por `print(objeto)`. |
| `__repr__` | Define uma representação útil para inspecionar o objeto. |
| `__len__` | Informa o tamanho do objeto para `len(objeto)`. |
| `__eq__` | Define como comparar objetos com `==`. |
| `__lt__` | Define a comparação “menor que” com `<`. |
| `__add__` | Define o comportamento do operador `+`. |
| `__getitem__` | Permite acessar itens com `objeto[chave]`. |
| `__setitem__` | Permite atribuir itens com `objeto[chave] = valor`. |
| `__iter__` | Permite percorrer o objeto com `for`. |
| `__next__` | Retorna o próximo item de um iterador. |
| `__contains__` | Define a verificação com `item in objeto`. |
| `__call__` | Permite chamar o objeto como função: `objeto()`. |
| `__enter__` | Prepara o objeto para uso em `with`. |
| `__exit__` | Finaliza o uso do objeto ao sair de `with`. |

## 7. Herança

Uma das maiores vantagens da herança é o polimorfismo, diferentes subclasses podem responder à mesma chamada de maneiras próprias.

```python
class Animal:
    def emitir_som(self):
        return "Som desconhecido"


class Cachorro(Animal):
    def emitir_som(self):
        return "Au au!"


class Gato(Animal):
    def emitir_som(self):
        return "Miau!"
```

```python
animais = [Cachorro(), Gato()]

for animal in animais:
    print(animal.emitir_som())
    # Au au!
    # Miau!
```

O laço não precisa saber qual é a classe concreta de cada objeto. Ele apenas chama `emitir_som()`.

Uma subclasse também pode complementar, em vez de substituir totalmente, o comportamento da classe base:

```python
class Veiculo:
    def mover(self):
        return "O veículo está em movimento."


class Carro(Veiculo):
    def mover(self):
        mensagem_base = super().mover()
        return f"{mensagem_base} O carro usa rodas."
```

```python
carro = Carro()
print(carro.mover())
# O veículo está em movimento. O carro usa rodas.
```

Aqui, `super().mover()` chama o método herdado de `Veiculo`, e a subclasse acrescenta uma informação.

Também é possível herdar de mais de uma classe:

```python
class Voador:
    def voar(self):
        return "Voando"


class Nadador:
    def nadar(self):
        return "Nadando"


class Pato(Voador, Nadador):
    pass
```

```python
pato = Pato()

print(pato.voar())   # Voando
print(pato.nadar())  # Nadando
```

Isso se chama herança múltipla.

## 8. Abstração e classes abstratas

Abstração consiste em definir o que um objeto deve fazer sem precisar determinar todos os detalhes de como fará isso. Ela ajuda a criar uma regra comum para várias classes.

Por exemplo, todo meio de pagamento deve ter um método `pagar()`, mas cada tipo de pagamento executa essa ação de forma diferente.

Em Python, podemos criar uma classe abstrata com `ABC` e marcar métodos obrigatórios com `@abstractmethod`:

```python
from abc import ABC, abstractmethod


class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        """Realiza um pagamento."""
        pass
```

`Pagamento` define um contrato, qualquer classe concreta que herde dela precisa implementar `pagar()`.

```python
class PagamentoPix(Pagamento):
    def pagar(self, valor):
        return f"Pagamento de R$ {valor:.2f} realizado por Pix."


class PagamentoCartao(Pagamento):
    def pagar(self, valor):
        return f"Pagamento de R$ {valor:.2f} realizado por cartão."
```

```python
pix = PagamentoPix()
cartao = PagamentoCartao()

print(pix.pagar(50))
print(cartao.pagar(120))
```

Não é possível criar uma instância direta de uma classe abstrata enquanto ela tiver métodos abstratos:

```python
pagamento = Pagamento()  # TypeError
```

Se uma subclasse não implementar o método obrigatório, ela também continuará abstrata:

```python
class PagamentoBoleto(Pagamento):
    pass


boleto = PagamentoBoleto()  # TypeError
```

Uma classe abstrata pode ter métodos comuns já implementados, além dos métodos obrigatórios:

```python
class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass

    def validar_valor(self, valor):
        if valor <= 0:
            raise ValueError("O valor deve ser positivo.")
```

As subclasses podem chamar esse comportamento herdado:

```python
class PagamentoPix(Pagamento):
    def pagar(self, valor):
        self.validar_valor(valor)
        return f"Pix de R$ {valor:.2f} realizado."
```

## 9. Encapsulamento

Encapsulamento organiza e protege o acesso ao estado de um objeto. Em vez de qualquer parte do programa alterar um atributo livremente, a classe define como esse dado deve ser consultado ou modificado.

Em Python, não há atributos totalmente privados como em algumas outras linguagens. Há convenções e mecanismos que indicam a intenção do código.

```python
class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular      # público (+)
        self._agencia = "0001"      # protegido (#)
        self.__saldo = saldo        # privado (-)
```

| Forma | Significado |
| --- | --- |
| `self.nome` | Atributo público: pode ser usado externamente. |
| `self._nome` | Atributo interno: a convenção pede que não seja acessado diretamente fora da classe. |
| `self.__nome` | Atributo com alteração de nome feita pelo Python para reduzir acessos acidentais. |

Um atributo com dois sublinhados não desaparece, Python altera seu nome internamente:

```python
conta = Conta("Pedro", 500)

print(conta.__saldo)          # AttributeError
print(conta._Conta__saldo)    # 500
```

Por isso, `__saldo` não é segurança. Ele evita colisões de nomes e sinaliza que o atributo é interno.

## 10. Getters, setters e propriedades

Getters e setters controlam a leitura e a alteração de atributos. Em Python, `@property` permite oferecer esse controle usando uma sintaxe parecida com a de um atributo comum.

Um **getter** retorna um valor. Um **setter** define ou altera um valor, geralmente depois de validá-lo.

```python
class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, valor):
        if valor < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self._saldo = valor
```

```python
conta = Conta(500)

print(conta.get_saldo())
conta.set_saldo(700)
```

O prefixo `_saldo` indica que o atributo é interno por convenção. O controle está nos métodos `get_saldo()` e `set_saldo()`.

---

Em Python, é mais comum expor uma propriedade. Ela permite ler e alterar o valor com `conta.saldo`, mas executa métodos internamente.

```python
class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo

    @property
    def saldo(self):
        """Retorna o saldo atual da conta."""
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self._saldo = valor
```

Uso:

```python
conta = Conta(500)

print(conta.saldo)  # Getter

conta.saldo = 700  # Setter
print(conta.saldo)

conta.saldo = -100  # ValueError
```

Se a propriedade não tiver setter, seu valor não pode ser atribuído por meio do nome público:

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco

    @property
    def preco(self):
        return self._preco

produto = Produto("Livro", 50)

print(produto.preco)
produto.preco = 60  # AttributeError
```

---

Uma propriedade também pode controlar a exclusão de um atributo. Isso é menos comum, mas segue o mesmo padrão:

```python
class Usuario:
    def __init__(self, email):
        self._email = email

    @property
    def email(self):
        return self._email

    @email.deleter
    def email(self):
        raise AttributeError("O e-mail não pode ser removido.")
```

```python
usuario = Usuario("ana@exemplo.com")
del usuario.email
```

## 11. Polimorfismo

Polimorfismo permite usar objetos de classes diferentes por meio da mesma operação. Cada objeto responde de acordo com a sua própria implementação.

### Tipos de polimorfismo

- **Por sobrescrita:** uma subclasse redefine um método da classe base, como `Cachorro.emitir_som()`.
- **Por inclusão:** uma subclasse pode ser usada onde o código espera a classe base, como um `Cachorro` usado como `Animal`.
- **Ad hoc:** uma mesma operação possui regras para tipos diferentes; por exemplo, `+` funciona com números, strings e listas. Classes podem definir essa operação com `__add__`.
- **Paramétrico:** código genérico trabalha com valores de tipos variados, normalmente com `TypeVar` e anotações de tipo.
- **Duck typing:** o código usa um objeto pelo comportamento que ele oferece, sem precisar de herança, como qualquer objeto que implemente `exportar()`.

---

Polimorfismo costuma acontecer quando uma subclasse sobrescreve um método herdado:

```python
class Veiculo:
    def mover(self):
        return "O veículo está em movimento."


class Carro(Veiculo):
    def mover(self):
        return "O carro se move pelas ruas."


class Barco(Veiculo):
    def mover(self):
        return "O barco se move pela água."
```

```python
def descrever_movimento(veiculo):
    return veiculo.mover()


print(descrever_movimento(Carro())) # O carro se move pelas ruas.
print(descrever_movimento(Barco())) # O barco se move pela água.
```

A função aceita qualquer objeto que tenha um método `mover()` compatível. O comportamento escolhido depende do objeto recebido em tempo de execução.

---

Python usa tipagem dinâmica e também aceita o chamado *duck typing* se o objeto oferece o comportamento necessário, ele pode ser usado, mesmo sem herdar da mesma classe.

```python
class DocumentoPDF:
    def exportar(self):
        return "PDF exportado"


class Planilha:
    def exportar(self):
        return "Planilha exportada"


def salvar(documento):
    return documento.exportar()
```

```python
print(salvar(DocumentoPDF()))
print(salvar(Planilha()))
```

As duas classes não possuem uma classe base em comum definida no exemplo. Ainda assim, ambas atendem ao que `salvar()` que precisa de um método `exportar()`.

---

Uma classe abstrata pode formalizar o comportamento esperado das subclasses:

```python
from abc import ABC, abstractmethod


class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass


class PagamentoPix(Pagamento):
    def pagar(self, valor):
        return f"Pix de R$ {valor:.2f} realizado."


class PagamentoCartao(Pagamento):
    def pagar(self, valor):
        return f"Pagamento de R$ {valor:.2f} realizado no cartão."
```

```python
pagamentos = [PagamentoPix(), PagamentoCartao()]

for pagamento in pagamentos:
    print(pagamento.pagar(50))
```

Aqui, a abstração define que todo pagamento deve ter `pagar()`. O polimorfismo permite chamar esse método sem saber qual forma de pagamento está na lista.

## 12. Módulos e organização

Todo arquivo Python pode ser importado como módulo. Por exemplo, o arquivo `calculadora.py`:

```python
def somar(a, b):
    return a + b


PI = 3.14159
```

Pode ser usado em outro arquivo:

```python
import calculadora

resultado = calculadora.somar(2, 3)
print(resultado)
print(calculadora.PI)
```

O nome do módulo é o nome do arquivo sem `.py`.

---

Evite `from calculadora import *` fica difícil saber de onde veio cada nome e podem ocorrer conflitos.

```python
import calculadora
from calculadora import somar
from calculadora import somar as adicionar
```

---

Um pacote é uma pasta que organiza módulos relacionados. Uma estrutura simples para uma aplicação de contas pode ser:

```text
meu_projeto/
├── main.py
└── financeiro/
    ├── __init__.py
    ├── conta.py
    └── relatorios.py
```

`financeiro` é o pacote. `conta.py` e `relatorios.py` são módulos. O arquivo `__init__.py` é tradicionalmente usado para marcar e inicializar o pacote. Nas versões atuais do Python, alguns pacotes podem funcionar sem ele, mas mantê-lo costuma deixar a estrutura mais clara.

```python
from financeiro.conta import Conta
from financeiro.relatorios import gerar_extrato
```

---

Dentro de um pacote, um módulo pode importar outro pelo nome completo:

```python
from financeiro.conta import Conta
```

Evite importações circulares, nas quais `conta.py` importa `relatorios.py` e `relatorios.py` também importa `conta.py`. Elas podem deixar módulos parcialmente carregados e causar erros. Em geral, extraia o código compartilhado para um terceiro módulo ou reorganize as responsabilidades.

---

Um módulo pode ser importado ou executado diretamente. O bloco abaixo só é executado quando o arquivo é iniciado diretamente:

```python
def main():
    print("Aplicação iniciada")


if __name__ == "__main__":
    main()
```

Assim, funções e classes podem ser importadas sem iniciar a aplicação automaticamente.
