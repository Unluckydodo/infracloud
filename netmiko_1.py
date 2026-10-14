import datetime

from netmiko import ConnectHandler

HOST = "192.168.56.101"      
USERNAME = "cisco"           
PASSWORD = "cisco123!"       
SECRET = "cisco123!"        

print(datetime.datetime.now())

device = {
    "device_type": "cisco_ios",
    "host": HOST,
    "username": USERNAME,
    "password": PASSWORD,
    "secret": SECRET,
}

try:
    connection = ConnectHandler(**device, conn_timeout=10)
    connection.enable()
    output = connection.send_command("show ip interface brief")
    print(output)
    connection.disconnect()
except Exception as e:
    print("Verbinding mislukt:", type(e).__name__)
    print("Controleer: draait de CSR1000v, klopt het IP-adres en kan je pingen (ping", HOST, ")?")
