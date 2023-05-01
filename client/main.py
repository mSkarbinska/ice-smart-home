import sys
import Ice
from bulbulator import BulbulatorClient
from light_bulb import LightBulbClient
from rgb_bulb import RGBBulbClient
from fridge import FridgeClient
from monitoring_camera import MonitoringCameraClient

AVAILABLE_TYPES = {
    'bulbulator': BulbulatorClient,
    'lightBulb': LightBulbClient,
    'rgbBulb': RGBBulbClient,
    'fridge': FridgeClient,
    'monitoringCamera': MonitoringCameraClient,
}

INSTANCE_LOCATIONS = {
    'bulbulator1': ('127.0.0.1', 10000),
    'lightBulb1': ('127.0.0.1', 10001),
    'rgbBulb1': ('127.0.0.1', 10001),
    'rgbBulb2': ('127.0.0.1', 10000),
    'fridge1': ('127.0.0.1', 10000),
    'monitoringCamera1': ('127.0.0.1', 10000),
    'monitoringCamera2': ('127.0.0.1', 10001)

}

if __name__ == '__main__':
    with Ice.initialize(sys.argv) as communicator:
        while True:
            print('> ', end='')
            try:
                command = input()
            except KeyboardInterrupt:
                break
            split_command = command.rstrip().split(' ')
            if split_command[0] == 'help':
                print('syntax: <type> <name>')
            elif split_command[0] == 'exit':
                break
            elif len(split_command) == 2:
                client_class = AVAILABLE_TYPES.get(split_command[0])
                if client_class is None:
                    print(f'Unknown type: {split_command[0]}, available types: {", ".join(AVAILABLE_TYPES.keys())}')
                    continue
                try:
                    ip, port = INSTANCE_LOCATIONS[split_command[1]]
                    client = client_class(communicator, split_command[0], split_command[1], ip, port)
                    client.interact()
                except Ice.ObjectNotExistException:
                    print(f"Object {split_command[1]} does not exist")
            else:
                print(f'Invalid command: {split_command[0]}')
