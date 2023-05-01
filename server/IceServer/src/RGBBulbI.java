import SmartHome.Color;
import SmartHome.InvaildColorException;
import SmartHome.RGBBulb;
import com.zeroc.Ice.Current;

public class RGBBulbI implements RGBBulb {
    private boolean state = false;
    private Color color = new Color(255, 255, 255);
    @Override
    public boolean getState(Current current) {
        return state;
    }

    @Override
    public void setState(boolean newState, Current current) {
        state = newState;
    }

    @Override
    public Color getColor(Current current) {
        return color;
    }

    @Override
    public void setColor(Color color, Current current) throws InvaildColorException {
        if(color.r < 0 || color.r > 255 || color.g < 0 || color.g > 255 || color.b < 0 || color.b > 255)
            throw new InvaildColorException();
        this.color = color;
    }
}
