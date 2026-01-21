import socket

# Configuração do alvo
alvo = "192.168.0.0"  # IP do seu próprio computador para teste (localhost)
portas_comuns = [21, 22, 80, 443, 3306, 3389]

print(f"Iniciando scan no alvo: {alvo}")

for porta in portas_comuns:
    # Criação do objeto socket (AF_INET = IPV4, SOCK_STREAM = TCP)
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.5) # Definindo um tempo curto para não travar
    
    # Tenta a conexão (connect_ex retorna 0 se for bem sucedida)
    codigo_retorno = cliente.connect_ex((alvo, porta))
    
    if codigo_retorno == 0:
        print(f"Porta {porta}: [ABERTA] - Atenção!")
    else:
        print(f"Porta {porta}: [FECHADA]")
        
    cliente.close()
#porta 21 = FTP; porta 22 = SSH; porta 80 = HTTP; porta 443 = HTTPS; porta 3306 = MySQL; porta 3389 = RDP;
print("Scan finalizado.")
