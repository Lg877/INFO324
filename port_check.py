import socket

def check_port(host, port, timeout=1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    result = s.connect_ex((host, port))
    s.close()
    return result == 0

if __name__ == "__main__":
    host = "127.0.0.1"
    for port in [22, 80, 443, 3306]:
        state = "open" if check_port(host, port) else "closed"
        print(f"{host}:{port} -> {state}")
