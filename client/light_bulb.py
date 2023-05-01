import SmartHome
from client import Client


class LightBulbClient(Client):
    def get_stub(self, base):
        return SmartHome.LightBulbPrx.checkedCast(base)


@LightBulbClient.command
def get_state(self):
    print("on" if self._stub.getState() else "off")


@LightBulbClient.command
def set_state(self):
    answer = input("New state [on/off]: ")
    self._stub.setState(answer == 'on')

