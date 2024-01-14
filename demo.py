import os

from linksys import Linksys

linksys = Linksys("192.168.1.1", os.environ["ROUTER_ADMIN_PASSWORD"])

info = linksys.get_device_info()

print(info.manufacturer, info.model_number)
print(info.description)
print(info.firmware_version)
print()

print("Connected Devices:")
print("==================")
devices = linksys.get_device_list()
for device in devices:
    if device.is_connected:
        print(device.name, device.mac_address)
