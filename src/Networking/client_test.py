import networking

HOST = "127.0.0.1"
PORT = 5000

if __name__ == "__main__":
    networking.Client(HOST, PORT, print)
