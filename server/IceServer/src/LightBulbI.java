import SmartHome.LightBulb;
import com.zeroc.Ice.Current;

public class LightBulbI implements LightBulb {
    private boolean state = false;
    @Override
    public boolean getState(Current current) {
        return state;
    }

    @Override
    public void setState(boolean newState, Current current) {
        state = newState;
    }

}
