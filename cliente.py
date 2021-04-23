# Importação de algumas bibliotecas
import socket
import threading
import time
import sys

# Definição das variáveis
host = "192.168.1.20"                                      # Exemplo: 192.168.1.20
port = 7777                                                # Número da porta que vai ser usada para a comunicação
buffer_size = 2048                                         # Tamanho da memória utilizada para os dados

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # Criação de um objeto socket que irá funcionar com IPv4 em modo TCP
s.connect((host, port))                                    # Uso do connect para fazer a conexão com host e porta

nickname = input("Nickname: ")                             # Input para o utilizador colocar o seu nickname


def receive():                                             # Função para receber os dados dos clientes
    while True:                                            # Ciclo que vai estar a receber os dados dos clientes
        try:
            mensagem = s.recv(buffer_size).decode()        # Criação de uma variável que vai guardar a infomação vinda do cliente
            
            if mensagem != "":                             # Se o valor dos bytes for diferente de vazio ele mostra a mensagem no terminal
                print(mensagem)
                
            time.sleep(0.2)                                # Delay da Thread
        except:
            print("Servidor desligado!")                   # Mostra a mensagem quando o servidor está desligado
            s.close()                                      # Fecha a conexão
            break                                          # Interrompe o ciclo


def write():                                               # Função para enviar os dados para o servidor
    while True:                                            # Ciclo que vai estar a enviar as mensagens
        try:
            mensagem = input("")                           # Mensagem para o servidor
    
            mensagem_bytes = nickname + ": " + mensagem    # Variável que vai concatenar o nickname do utilizador com a mensagem escrita
            s.send(mensagem_bytes.encode())                # Conversão da mensagem em string para bytes para enviar para o servidor
            time.sleep(0.2)                                # Delay da Thread 
        except:
            s.close()                                      # Fecha a conexão
            sys.exit(0)                                    # Fecha a aplicação


receive_thread = threading.Thread(name="receive", target=receive)  # Criação da thread receive() para receber os dados ao mesmo tempo que envia
receive_thread.start()                                             # Iniciação da thread receive()

write_thread = threading.Thread(name="write", target=write)        # Criação da thread write() para enviar os dados ao mesmo tempo que recebe
write_thread.start()                                               # Iniciação da thread write()
