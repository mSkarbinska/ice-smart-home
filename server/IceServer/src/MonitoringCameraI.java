import SmartHome.*;
import com.zeroc.Ice.Current;

import java.util.ArrayList;

public class MonitoringCameraI implements MonitoringCamera {
    private final ArrayList<Recording> recordings = new ArrayList<>();
    @Override
    public void saveRecording(DateTime from, DateTime to, Current current) throws InvalidDateException, IvalidTimeBlockAException {
        if (from.hour < 0 || from.hour > 23 || from.minute < 0 || from.minute > 59)
            throw new InvalidDateException();
        if (to.hour < 0 || to.hour > 23 || to.minute < 0 || to.minute > 59)
            throw new InvalidDateException();
        if (from.hour > to.hour || (from.hour == to.hour && from.minute > to.minute))
            throw new IvalidTimeBlockAException();
        recordings.add(new Recording(from, to));
    }
    @Override
    public Recording getLastRecording(Current current) {
        return recordings.get(recordings.size() - 1);
    }
}
