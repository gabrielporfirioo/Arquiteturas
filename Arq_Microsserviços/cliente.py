import requests

def adicionar_contato():
    nome = input("Nome do contato: ")
    telefone = input("Telefone do contato: ")
    email = input("E-mail do contato: ")
    response = requests.post('http://localhost:5000/contatos', json={'nome': nome, 'telefone': telefone, 'email': email})
    print(f"Contato adicionado com ID: {response.json()['id']}")

def adicionar_compromisso():
    descricao = input("Descrição do compromisso: ")
    data = input("Data do compromisso (YYYY-MM-DD HH:MM): ")
    contato_id = input("ID do contato (opcional): ")
    data = {'descricao': descricao, 'data': data}
    if contato_id:
        data['contato_id'] = int(contato_id)
    response = requests.post('http://localhost:5001/compromissos', json=data)
    print(f"Compromisso adicionado com ID: {response.json()['id']}")

def listar_contatos():
    response = requests.get('http://localhost:5000/contatos')
    contatos = response.json()
    for contato in contatos:
        print(f"ID: {contato['id']}, Nome: {contato['nome']}, Telefone: {contato['telefone']}, E-mail: {contato['email']}")

def listar_compromissos():
    response = requests.get('http://localhost:5001/compromissos')
    compromissos = response.json()
    for compromisso in compromissos:
        contato = compromisso.get('contato', {})
        print(f"ID: {compromisso['id']}, Descrição: {compromisso['descricao']}, Data: {compromisso['data']}, Contato: {contato.get('nome', 'N/A')}")

def listar_compromissos_por_data():
    data_inicio = input("Data inicial (YYYY-MM-DD HH:MM): ")
    data_fim = input("Data final (YYYY-MM-DD HH:MM): ")
    params = {'data_inicio': data_inicio, 'data_fim': data_fim}
    response = requests.get('http://localhost:5001/compromissos', params=params)
    try:
        compromissos = response.json()
        if compromissos:
            for compromisso in compromissos:
                contato = compromisso.get('contato', {})
                print("COMPROMISSO ENCONTRADO: ")
                print(f"ID: {compromisso['id']}, Descrição: {compromisso['descricao']}, Data: {compromisso['data']}, Contato: {contato.get('nome', 'N/A')}")
        else: 
            print("Não foi encontrado compromisso entre estas datas.")
    except requests.exceptions.JSONDecodeError:
        print("Erro ao decodificar a resposta. Verifique a URL e os parâmetros.")
        print("Resposta do servidor:", response.text)
        print("Código de status:", response.status_code)

def main():
    while True:
        print("\n1. Adicionar Contato")
        print("2. Adicionar Compromisso")
        print("3. Listar Contatos")
        print("4. Listar Compromissos")
        print("5. Listar por intervalo de data")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_contato()
        elif opcao == '2':
            adicionar_compromisso()
        elif opcao == '3':
            listar_contatos()
        elif opcao == '4':
            listar_compromissos()
        elif opcao == '5':
            listar_compromissos_por_data()
        elif opcao == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
