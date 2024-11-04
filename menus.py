import re

# funcao para imprimir o menu principal
def imprimir_menu_principal():
    print('_________________________')
    print('|                        |')
    print('|     MENU DE OPÇÕES     |')
    print('|________________________|')
    print('|                        |')
    print("| 1 - Criar conta        |")
    print("| 2 - Login              |")
    print("| 3 - Sair               |")
    print('|________________________|')

# funcao para imprimir o sub menu
def imprimir_menu_sub():
    print('_________________________________')
    print('|                                |')
    print('|         MENU DE OPÇÕES         |')
    print('|________________________________|')
    print('|                                |')
    print("| 1 - Adicionar veículo          |")
    print("| 2 - Remover veículo            |")
    print("| 3 - Realizar diagnóstico       |")
    print("| 4 - Histórico de diagnósticos  |")
    print("| 5 - Voltar                     |")
    print('|________________________________|')

# funcao para escolher a opcao do menu principal
def menu_principal():
    while True:
        imprimir_menu_principal()  
        
        try:
            opcao = int(input("Escolha uma opção: "))  
            
            match opcao:
                case 1:
                    criar_conta()
                case 2:
                    login()
                case 3:
                    print("Programa encerrado!")
                    break
                case _:
                    print("Opção inválida.")
            
        except ValueError:
            print("Entrada inválida, deve ser um número inteiro.")
            

       
# funcao para escolher a opcao do sub menu
def menu_sub(usuario):
    while True:
        imprimir_menu_sub()
        
        try:
            opcao_sub = int(input("Escolha uma opção: "))  
            
            match opcao_sub:
                case 1:
                    adicionar_veiculo(usuario["veiculos"])
                case 2:
                    remover_veiculo(usuario["veiculos"])
                case 3:
                    realizar_diagnostico(usuario["veiculos"])
                case 4:
                    consultar_diagnosticos_veiculo(usuario["veiculos"])
                case 5:
                    break
                case _:
                    print("\nOpção inválida.")
                    
        except ValueError:
            print("Entrada inválida, deve ser um número inteiro.")

            
# funcao para consultar se um usuario ja existe
def consultar_usuario(email):
    # mock de usuario para simular fluxo de login e caso de usuario ja existente no criar_conta()
    usuarios = [
        {
            "nome": "José Luiz",
            "email": "jose.luiz@gmail.com",
            "senha": "senha123",
            "veiculos": [
                {
                    "fabricante": "Toyota",
                    "modelo": "Corolla",
                    "ano": 2015,
                    "cor": "preto",
                    "placa": "ABC-1234",
                    "diagnosticos": [
                    {
                        "problema_veiculo": "barulho ao virar o volante",
                        "resultados": [
                            {
                                "problema": "barulho ao virar o volante",
                                "causa": "Desgaste na junta homocinética.",
                                "solucao": "Substituição da junta homocinética.",
                                "orcamento": 150.00
                            },
                            {
                                "problema": "barulho ao virar o volante",
                                "causa": "Problema na caixa de direção.",
                                "solucao": "Reparo na caixa de direção.",
                                "orcamento": 350.00
                            }
                            ]
                        }
                    ]
                },
                {
                    "fabricante": "Honda",
                    "modelo": "Civic",
                    "ano": 2018,
                    "cor": "prata",
                    "placa": "ATC-3214",
                    "diagnosticos": [
                        {
                            "problema_veiculo": "vazamento de óleo no motor",
                            "resultados": [
                                {
                                    "problema": "vazamento de óleo no motor",
                                    "causa": "Vazamento na junta da tampa de válvulas.",
                                    "solucao": "Troca da junta da tampa de válvulas.",
                                    "orcamento": 200.00
                                },
                                {
                                    "problema": "vazamento de óleo no motor",
                                    "causa": "Falha no retentor do motor.",
                                    "solucao": "Substituição do retentor do motor.",
                                    "orcamento": 400.00,
                                    
                                },
                            ],
                        },
                    ],
                },
            ],
        }
    ]
    
    # percorre a lista de usuarios
    for usuario in usuarios:
        
        # verifica se existe um usuario com o email informado
        if usuario["email"] == email:
            
            #retorna o usuario encontrado
            return usuario
        
    return None

# funcao para criar uma nova conta
def criar_conta():
    while True:
        nome = input("Digite o seu nome: ")
        if nome.strip():
            break
        print("Nome não pode ser vazio. Tente novamente.")

    while True:
        email = input("Digite o seu email: ")
        if re.match(r"[^@]+@[^@]+\.[^@]+", email.strip()):
            break
        print("Email inválido. Tente novamente.")

    while True:
        senha = input("Digite a sua senha: ")
        if len(senha.strip()) >= 6:
            break
        print("A senha deve ter pelo menos 6 caracteres. Tente novamente.")
    
    usuario = consultar_usuario(email)
    
    if usuario is None:
        usuario = {"nome": nome, "email": email, "senha": senha, "veiculos": []}
        print("\nConta criada com sucesso!")
        
        adicionar_veiculo(usuario["veiculos"])
        
        menu_sub(usuario)
    else:
        print("\n Já existe uma conta com o email informado. Tente novamente.")

# funcao de login
def login():
    email = input("Digite o seu email: ")
    senha = input("Digite a sua senha: ")
    
    usuario = consultar_usuario(email)
    
    # verifica se o usuario foi encontrado e se a senha informada é a mesma do usuario
    if usuario and usuario["senha"] == senha:
        print(f"\nBem-vindo(a), {usuario['nome']}!")
        
        menu_sub(usuario)
        # retorna o usuario encontrado
        return usuario
    else:
        # mensagem de erro caso nenhum usuario seja encontrado com os dados informados
        print("\nemail ou senha incorretos.")
        return False

# funcao para exibir o menu de seleção de fabricantes
def selecionar_fabricante():
    fabricantes_predefinidos = ["Toyota", "Honda", "Ford", "Chevrolet"]

    print("\nFabricantes disponíveis:")
    for i  in range(len(fabricantes_predefinidos)):
        fabricante = fabricantes_predefinidos[i]
        
        print(f"{i+1} - {fabricante}")

    while True:
        posicao = input("Escolha o número do fabricante: ")
        try:
            posicao = int(posicao)
            if len(fabricantes_predefinidos) >= posicao and posicao >= 1:
                return fabricantes_predefinidos[posicao - 1]
            else:
                print("\nOpção inválida, tente novamente.")
        except ValueError:
            print("\nEntrada inválida, deve ser um número inteiro.")

# funcao para exibir o menu de seleção de modelos
def selecionar_modelo(fabricante):
    modelos_predefinidos = {
        "Toyota": ["Corolla", "Camry", "Hilux"],
        "Honda": ["Civic", "Accord", "Fit"],
        "Ford": ["Focus", "Fiesta", "Ecosport"],
        "Chevrolet": ["Onix", "Sonic", "Tracker"]
    }
    
    modelos = modelos_predefinidos.get(fabricante, [])

    print(f"\nModelos disponíveis para {fabricante}:")
    
    for i in range(len(modelos)):
        modelo = modelos[i]
        print(f"{i+1} - {modelo}")

    while True:
        try:
            posicao = int(input("Escolha o número do modelo: "))
            
            if len(modelos) >= posicao and posicao >= 1:
                return modelos[posicao - 1]
            else:
                print("\nOpção inválida, tente novamente.")
        except ValueError:
            print("\nEntrada inválida, deve ser um número inteiro.")

# funcao para adicionar veículo
def adicionar_veiculo(usuario_veiculos):
    print('\nInsira os dados do seu veículo:')
    
    veiculo = {}
    veiculo["fabricante"] = selecionar_fabricante()
    veiculo["modelo"] = selecionar_modelo(veiculo["fabricante"])

    while True:
        try:
            veiculo["ano"] = int(input("Digite o ano do veículo: "))
            break
        
        except ValueError:
            print("\nEntrada inválida, Deve ser um número inteiro.")
        
    veiculo["cor"] = input("Digite a cor do veículo: ")
    veiculo["placa"] = input("Digite a placa do veículo: ")

    # adiciona o veículo na lista de veículos do usuário
    usuario_veiculos.append(veiculo)
    
    
    print("\nVeículo cadastrado com sucesso!")
    # retorna a lista de veículos atualizada
    return usuario_veiculos

# funcao para imprimir a funcao de selecionar veiculo
def imprimir_selecionar_veiculo(veiculos):
    if veiculos:
        print("\nVeículos cadastrados:")
        
        # percorre a lista de veículos
        for i in range(len(veiculos)):
            veiculo = veiculos[i]
            print(f"{i + 1} - {veiculo['fabricante']} {veiculo['modelo']} ({veiculo['ano']}) {veiculo['cor']} [{veiculo['placa']}]")

# funcao para selecionar o veículo
def selecionar_veiculo(veiculos):
    imprimir_selecionar_veiculo(veiculos)

    if (veiculos):
        while True:
            try:
                posicao = int(input("Escolha o número do veículo: "))
                
                # verifica se a posicao informada existe na lista de veiculos
                if len(veiculos) >= posicao and posicao >= 1:
                    
                    # retorna a posicao do veiculo selecionado
                    return (posicao - 1)
                else:
                    print("Opção inválida, tente novamente.")
                        
            except ValueError:
                print("Entrada inválida, deve ser um número inteiro.")
    else:
        return None
    

        
# funcao para remover veículo
def remover_veiculo(veiculos):
    
    posicao_veiculo = selecionar_veiculo(veiculos)
    
    if posicao_veiculo is not None:
        print("\nSelecione o número do veículo que deseja remover:")
        
        # remove o veículo da lista usando a posição retornada
        veiculos.pop(posicao_veiculo)
        print("\nVeículo removido com sucesso!")
        
        # retorna a lista de veículos atualizada
        return veiculos
    
    print("Nenhum veículo cadastrado para remover.")
    return None
 


# Função para buscar problemas semelhantes
def consultar_base_de_problemas(problema_veiculo):
    
    problemas = [
        {
            "problema": "barulho ao virar o volante",
            "resultados": [
                {
                    "causa": "Desgaste na junta homocinética.",
                    "solucao": "Substituição da junta homocinética.",
                    "orcamento": 150.00
                },
                {
                    "causa": "Problema na caixa de direção.",
                    "solucao": "Reparo na caixa de direção.",
                    "orcamento": 350.00
                }
            ]
        },
        {
            "problema": "vazamento de óleo no motor",
            "resultados": [
                {
                    "causa": "Vazamento na junta da tampa de válvulas.",
                    "solucao": "Troca da junta da tampa de válvulas.",
                    "orcamento": 200.00
                },
            ]
        },
        {
            "problema": "freios fazem barulho ao serem acionados",
            "resultados": [
                {
                    "causa": "Desgaste nas pastilhas de freio.",
                    "solucao": "Substituição das pastilhas de freio.",
                    "orcamento": 120.00
                },
                {
                    "causa": "Problema no disco de freio.",
                    "solucao": "Troca do disco de freio.",
                    "orcamento": 250.00
                }
            ]
        },
        {
            "problema": "carro não liga",
            "resultados": [
                {
                    "causa": "Bateria descarregada.",
                    "solucao": "Troca da bateria.",
                    "orcamento": 300.00
                },
                {
                    "causa": "Defeito no motor de partida.",
                    "solucao": "Reparo no motor de partida.",
                    "orcamento": 500.00
                }
            ]
        }
    ]
    
    problema_encontrado = None
    
    for problema in problemas:
        if problema_veiculo.lower() in problema["problema"].lower():
            problema_encontrado = problema
            break
        
    return problema_encontrado

# funcao para imprimir o diagnóstico realizado
def imprimir_diagnostico(diagnostico):
    print("\n" + "_" * 40)
    print("\nDIAGNÓSTICO")
    print("\n" + "_" * 40)
    print(f"Problema relatado: {diagnostico['problema_veiculo']}")
    print("_" * 40)
    
    # verifica se há resultados no diagnóstico
    if diagnostico['resultados']:
        print(f"Com base no problema relatado, os resultados encontrados foram:\n")

        for i in range(len(diagnostico['resultados'])):
            resultado = diagnostico['resultados'][i]

            print(f"{i+1} - resultado:")
            print(f"Causa: {resultado['causa']}")
            print(f"Solução: {resultado['solucao']}")
            print(f"Orçamento estimado: R$ {resultado['orcamento']:.2f}")
            print("_" * 40)
    else:
        print("Nenhum resultado encontrado para o problema relatado.")
        print("_" * 40)


# funcao para relatar o problema e realizar diagnóstico
def realizar_diagnostico(veiculos):
    # verifica se a lista de veiculos esta vazia
    if (veiculos):
        posicao_veiculo = selecionar_veiculo(veiculos)
        
        veiculo = veiculos[posicao_veiculo]
        
        problema_veiculo = input("Descreva o problema do veículo: ")
        
        problema_encontrado = consultar_base_de_problemas(problema_veiculo)
        
        # inicializa o diagnóstico com o problema descrito pelo usuário
        diagnostico = {
            "problema_veiculo": problema_veiculo,
            "resultados": []
        }
        
        if problema_encontrado:
            
            resultado = {}
            
            # adiciona o problema encontrado no diagnóstico
            resultado["problema"] = problema_encontrado["problema"]
            
            # percorre a lista de problemas encontrados
            for resultado in problema_encontrado["resultados"]:
                
                resultado = {	
                    "causa": resultado['causa'],
                    "solucao": resultado['solucao'],
                    "orcamento": resultado['orcamento']         
                }
                
                # adiciona o resultado na lista de resultados do diagnóstico
                diagnostico['resultados'].append(resultado) 
            
        diagnosticos = veiculo.get("diagnosticos", [])
            
        diagnosticos.append(diagnostico)
            
        imprimir_diagnostico(diagnostico)
        
        # retorna o diagnóstico realizado
        return diagnostico
    else:
        print("Nenhum veículo cadastrado para realizar diagnóstico.")
        return None

# funcao para consultar os diagnósticos do veículo
def consultar_diagnosticos_veiculo(veiculos):
    # verifica se a lista de veiculos esta vazia
    if (veiculos):
        print("\nSelecione o número do veículo que deseja visualizar o histórico de diagnósticos:")
        posicao_veiculo = selecionar_veiculo(veiculos)
        veiculo = veiculos[posicao_veiculo]
        
        if veiculo is not None:
            diagnosticos = veiculo.get("diagnosticos", [])
            imprimir_diagnosticos(diagnosticos)
        else:
            print("Nenhum veículo selecionado para visualizar o histórico.")
    else:
        print("Nenhum veículo cadastrado para visualizar o histórico de diagnósticos.")
        return None


# funcao para imprimir os diagnosticos do veículo
def imprimir_diagnosticos(diagnosticos):
    if not diagnosticos:
        print("Nenhum diagnóstico registrado para este veículo.")
        return
    
    for diag in diagnosticos:
        print(f"\nProblema relatado: {diag['problema_veiculo']}")
        
        # Verifica se há resultados para o diagnóstico
        if diag['resultados']:
            for i in range(len(diag['resultados'])):
                resultado = diag['resultados'][i]
                print(f"\nResultado {i+1}:")
                print(f"Causa: {resultado['causa']}")
                print(f"Solução: {resultado['solucao']}")
                print(f"Orçamento: R${resultado['orcamento']:.2f}")
                print("-" * 40)
        else:
            print("Nenhum resultado encontrado para este diagnóstico.")


# inicia o programa
menu_principal()
