from socket import*
serverName="127.0.0.1"
serverPort=12000
clientSocket=socket(AF_INET,SOCK_STREAM)

sentence=input("\n Enter file name: ")

clientSocket.sendto(bytes(sentence,"utf-8"),(serverName,serverPort))

filecontents,serverAddress=clientSocket.recvfrom(2048)

print("\n Reply from server: \n")
print(filecontents.decode("utf-8"))
clientSocket.close()