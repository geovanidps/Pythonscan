import socket
import os
import time

# As portas mais comuns
portas_comuns = [7, 9, 13, 21, 22, 23, 25, 26, 37, 53, 79, 80, 81, 88, 106, 110, 113, 119, 135, 139, 143, 144, 179, 199, 389, 427, 443, 444, 445, 465, 513, 514, 515, 543, 544, 548, 554, 587, 631, 646, 873, 990, 993, 995, 1025, 1026, 1027, 1028, 1029, 111, 135, 139, 143, 445, 512, 513, 514, 515, 543, 544, 548, 554, 587, 631, 646, 873, 990, 993, 995, 1025, 1029, 111, 135, 139, 143, 445, 993, 995, 10443, 1720, 3306, 3389, 5900, 5985, 6379, 7001, 8000, 8008, 8080, 8081, 9090, 8090, 8443, 8888, 10000, 49152, 49153, 49154, 49155, 49156, 49157]

def detectar_portas_abertas(host, portas):
    portas_abertas = []
    for porta in portas:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        try:
            conexao = sock.connect((host, porta))
            print(f"A porta {porta} está aberta.")
            portas_abertas.append(porta)
            conexao.close()
        except:
            pass
        finally:
            sock.close()

    return portas_abertas
#Verificando se as ferramentas estão instaladas
def verificar_ferramentas():
    ferramentas = ['nmap']
    for ferramenta in ferramentas:
        if os.system(f"which {ferramenta}") != 0:
            print(f"A ferramenta {ferramenta} não :/ está intalada. Instalando :) ...")
            os.system(f"sudo apt-get install {ferramenta}")

# Ferramentas
def enumerar_servicos(host, portas):
    for porta in portas:
        print(f"Enumerando serviços na porta {porta} com nmap...")
        os.system(f"nmap -sV -sS -sV -Pn -p {porta} --script vuln {host}")
        print(f"Enumerando serviços na porta {porta} com NC...")
        os.system(f"nc -zv {host} {porta}")
        

# Solicitando informações do usuário

host = input("Por favor, insira o host: ")
portas_especificas = input("Por favor, insira as portas especificas separadas por virgula (deixe em branco para usar as portas comuns): ")

if portas_especificas:
    portas = list(map(int, portas_especificas.split(',')))
else:
    portas = portas_comuns

# função
portas_abertas = detectar_portas_abertas(host, portas)

#Enumerar
enumerar_servicos(host, portas_abertas)

#mensagem
print("###### Script Completo #######")


#byMaskot
