import SmartHome
from client import Client


class BulbulatorClient(Client):
    def get_stub(self, base):
        return SmartHome.BulbulatorPrx.checkedCast(base)


@BulbulatorClient.command
def mumble(self):
    print(self._stub.mumble())
