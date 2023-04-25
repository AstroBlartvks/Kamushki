import socket


class Server:
    def __init__(self, players_count: int, port: int = 1337, ip: str = "localhost"):
        self.TCPsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (ip, port)
        self.players_count = players_count
    

    def start_server(self):
        self.TCPsocket.bind(self.server_address)
        self.TCPsocket.listen(self.players_count)
    

    def take_connection(self):
        connections = []
        for _ in range(self.players_count):
            connection, client_address = self.TCPsocket.accept()
            print('К нам подключился:', client_address)
            connections.append(connection)
        return connections


    def close_connections(self):
        for conn in self.connections:
            conn.close()
            print("Соединение прервано", conn)
    
    
class Client:
    def __init__(self, port: int = 1337, ip: str = "localhost"):
        self.TCPsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (ip, port)
    

    def connect_server(self):
        self.TCPsocket.connect(self.server_address)


    def close_connections(self):
        self.TCPsocket.close()
        print("Соединение прервано", self.TCPsocket)

        