import SmartHome
from light_bulb import LightBulbClient


class RGBBulbClient(LightBulbClient):
    def get_stub(self, base):
        return SmartHome.RGBBulbPrx.checkedCast(base)


@RGBBulbClient.command
def get_color(self):
    color = self._stub.getColor()
    print(f"r: {color.r}, g: {color.g}, b: {color.b}")


@RGBBulbClient.command
def set_color(self):
    color = SmartHome.Color()
    color.r = float(input("r: "))
    color.g = float(input("g: "))
    color.b = float(input("b: "))
    try:
        self._stub.setColor(color)
    except SmartHome.InvaildColorException:
        print("Invalid color")
