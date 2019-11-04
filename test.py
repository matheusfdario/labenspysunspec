import sunspec.core.client as client

data = client.SunSpecClientDevice(client.TCP, 1, ipaddr="10.80.10.158", ipport=502, timeout=10)

data.inverter.read()

print(data.inverter)
