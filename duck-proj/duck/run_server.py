from duck_u04.config import PORT, IP
from duck_u04.app import app


def run_server():
    app.run(IP, PORT)


if __name__ == '__main__':
    run_server()
