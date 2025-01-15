#  Intermediário
#  Estrutura de Dados

# Desafio
# Vamos criar uma classe chamada UsuarioTelefone para representar um usuário de telefone. Você pode definir um método especial e depois aplicar conceitos de encapsulamento nos atributos dentro da classe. Lembre-se que, cada usuário terá um nome, um número de telefone e um plano associado, neste desafio, simulamos três planos, sendo: Plano Essencial Fibra, Plano Prata Fibra e Plano Premium Fibra.

# Entrada
# Nome do usuário, número de telefone e plano.

# Saída
# Mensagem indicando que o usuário foi criado com sucesso.

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# +-------------------------+---------------------------------+
# | Entrada                | Saída                            |
# +------------------------+----------------------------------+
# | Ana                    | Usuário Ana criado com sucesso.  |
# | (11) 91111-1111        |                                  |
# | Plano Essencial Fibra  |                                  |
# +------------------------+----------------------------------+
# | Sofia                  | Usuário Sofia criado com sucesso.|
# | (22) 92222-2222        |                                  |
# | Plano Prata Fibra      |                                  |
# +------------------------+----------------------------------+
# | Pedro                  | Usuário Pedro criado com sucesso.|
# | (33) 93333-3333        |                                  |
# | Plano Premium Fibra    |                                  |
# +------------------------+----------------------------------+


#########################################################

# # TODO: Crie uma classe UsuarioTelefone.  
# # TODO: Defina um método especial `__init__`, que é o construtor da classe.
# # O método `__init__`, irá inicializar os atributos da classe: `nome`, `numero` e `plano`.


        
#     # TODO: Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.
      

#     # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
#     def __str__(self):
#         return f"Usuário {self.nome} criado com sucesso."


# # Entrada:
# nome = input()  
# numero = input()  
# plano = input()  
# # TODO: Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:

# print(usuario)

#########################################################
#########################################################

class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano

    # Método especial __str__ para retornar uma representação em string do objeto
    def __str__(self):
        return f"Usuário {self.__nome} criado com sucesso."

# Entrada:
nome = input("Digite o nome do usuário: ")  
numero = input("Digite o número do telefone: ")
plano = input("Digite o plano do usuário: ")

# Criação do objeto UsuarioTelefone
usuario = UsuarioTelefone(nome, numero, plano)

# Exibição da mensagem de sucesso
print(usuario)