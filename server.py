from http.server import HTTPServer, SimpleHTTPRequestHandler

AZUL = "\033[94m"
VERDE = "\033[92m"
CIANO = "\033[96m"
RESET = "\033[0m"

HOST = "127.0.0.1"
PORTA = 8000

servidor = HTTPServer(
    (HOST, PORTA),
    SimpleHTTPRequestHandler
)

print()
print(f"{CIANO}======================================{RESET}")
print(f"{CIANO}       LABORATÓRIO CYBER SECURITY{RESET}")
print(f"{CIANO}======================================{RESET}")
print()
print(f"{AZUL}[SERVIDOR]{RESET} Sistema iniciado.")
print(f"{AZUL}[SERVIDOR]{RESET} Acesse:")
print(f"{VERDE}http://127.0.0.1:8000/login.html{RESET}")
print()
print(f"{AZUL}[SERVIDOR]{RESET} Aguardando conexões...")
print()

servidor.serve_forever()