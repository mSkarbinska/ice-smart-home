import SmartHome.Bulbulator;
import com.zeroc.Ice.Current;

public class BulbulatorI implements Bulbulator {
    @Override
    public String mumble(Current current) {
        return "Bul bUl BuL";
    }
}
