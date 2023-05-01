import SmartHome.Fridge;
import com.zeroc.Ice.Current;

public class FridgeI implements Fridge {
    private float temperature = 0;
    private boolean open = false;
    @Override
    public float getTemperature(Current current) {
        return temperature;
    }

    @Override
    public void setTemperature(float newTemperature, Current current) {
        temperature = newTemperature;
    }

    @Override
    public boolean getDoorState(Current current) {
        return open;
    }

    @Override
    public void setDoorState(boolean newDoorState, Current current) {
        open = newDoorState;
    }
}
