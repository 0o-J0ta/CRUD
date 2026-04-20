#CRUD_SIMPLES

banco_d_dados = []

id = 0

def gerador_id():
    global id
    id = id + 1
    return id

def selecao():
    return input('''O que deseja realizar?\n
[1] - Criar um produto novo.
[2] - Listar o inventario.
[3] - Ajustar um produto.
[4] - Excluir um produto.
[5] - Sair.
Qual opção deseja selecionar? '''.upper())
print("  ")

#Create
def criando_produto():
    produto = [
        gerador_id(),
        input("Digite o nome do produto: ".upper()), 
        float(input("Digite o valor do produto: ")), 
        input("Digite a unidade de medida: ".upper())
    ]

    banco_d_dados.append(produto)
    for elemento in banco_d_dados:
        print(f"produto {elemento[1]} cadastrado".upper())

#Read
def listagem_produtos():
    for inventario in banco_d_dados:
        print(f"ID: {inventario[0]} | Nome: {inventario[1]} | Valor: {inventario[2]} | Unidade: {inventario[3]}".upper())

#Update
def alterar_produto():
    id_produto = int(input("Qual o ID do produto que vai alterar? ".upper()))
    
    for inventario in banco_d_dados:
        if inventario[0] == id_produto:

            opcao = int(input('''O que deseja alterar?
[1] - Nome
[2] - valor
[3] - Unidade                           
opção: '''.upper()))
            
            if opcao == 1:
                novo_nome = input("Novo nome: ".upper())
                inventario[1] = novo_nome

            if opcao == 2:
                novo_valor = input("Novo valor: ".upper())
                inventario[2] = novo_valor

            if opcao == 3:
                nova_unidade = input("Nova unidade de medida: ".upper())
                inventario[3] = nova_unidade

            else:
                print("Opção invalida".upper())
                return
            
            print("Produto atualizado!".upper())
            return

#Delete


#Programa

menu = selecao()
print("  ")
while menu == '1' or menu == '2' or menu == '3':

    if menu == '1':
        print("  ")
        criando_produto()
        

    if menu == "2":
        print("  ")
        listagem_produtos()
        
        
    if menu == "3":
        print("  ")
        alterar_produto()
        
    
    if menu == 5:
        break
   
    menu = selecao()