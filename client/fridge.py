import SmartHome
from client import Client


class FridgeClient(Client):
    def get_stub(self, base):
        return SmartHome.FridgePrx.checkedCast(base)


@FridgeClient.command
def get_temperature(self):
    print(self._stub.getTemperature())


@FridgeClient.command
def set_temperature(self):
    temperature = float(input("New temperature: "))
    self._stub.setTemperature(temperature)


@FridgeClient.command
def get_door_state(self):
    print("open" if self._stub.getDoorState() else "closed")


@FridgeClient.command
def set_door_state(self):
    answer = input("New door state [open/closed]: ")
    self._stub.setDoorState(answer == 'open')