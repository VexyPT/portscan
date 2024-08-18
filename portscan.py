import socket

def get_timeout():
    while True:
        print("\nChoose the timeout for the scan (in seconds):")
        for i in range(1, 11):
            print(f"{i}: {i/10} seconds")
        try:
            choice = int(input("Choose an option (1-10): "))
            if 1 <= choice <= 10:
                return choice / 10
            else:
                print("Error: Please choose a number between 1 and 10.")
        except ValueError:
            print("Error: Please enter a valid integer.")

def get_ports():
    while True:
        ports_input = input("Enter ports (separated by commas): ")
        try:
            ports = list(set(int(port.strip()) for port in ports_input.split(',')))
            return ports
        except ValueError:
            print("Error: Please enter valid integers separated by commas.")

try:
    ports = get_ports()
    timeout = get_timeout()

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(timeout)

    for port in ports:
        try:
            code = client.connect_ex(("bancocn.com", port))
            if code == 0:
                print(f"Port {port} is open")
            else:
                print(f"Port {port} is closed")
        except socket.error as err:
            print(f"Connection error on port {port}: {err}")

except socket.error as err:
    print(f"Socket error: {err}")

finally:
    client.close()