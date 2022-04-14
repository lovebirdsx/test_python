import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.sendto(bytes('RestartFlowEditor', 'utf-8'), ('127.0.0.1', 8888))