
import com.zeroc.Ice.Communicator;
import com.zeroc.Ice.Identity;
import com.zeroc.Ice.ObjectAdapter;
import com.zeroc.Ice.Util;

public class IceServer {
    public void t1(String[] args) {
        int status = 0;
        Communicator communicator = null;

        try {
            communicator = Util.initialize(args);
            ObjectAdapter adapter1 = communicator.createObjectAdapterWithEndpoints("Adapter1", "tcp -h 127.0.0.1 -p 10000 -z : udp -h 127.0.0.1 -p 10000 -z");
            ObjectAdapter adapter2 = communicator.createObjectAdapterWithEndpoints("Adapter2", "tcp -h 127.0.0.1 -p 10001 -z : udp -h 127.0.0.1 -p 10001 -z");

            // Utworzenie serwanta/serwantów
            BulbulatorI bulbulator1 = new BulbulatorI();
            FridgeI fridge1 = new FridgeI();
            LightBulbI lightBulb1 = new LightBulbI();
            RGBBulbI rgbBulb1 = new RGBBulbI();
            RGBBulbI rgbBulb2 = new RGBBulbI();
            MonitoringCameraI monitoringCamera1 = new MonitoringCameraI();
            MonitoringCameraI monitoringCamera2 = new MonitoringCameraI();

            // Dodanie wpisów do tablicy ASM, skojarzenie nazwy obiektu (Identity) z serwantem
            adapter1.add(bulbulator1, new Identity("bulbulator1", "bulbulator"));
            adapter1.add(fridge1, new Identity("fridge1", "fridge"));
            adapter2.add(lightBulb1, new Identity("lightBulb1", "lightBulb"));
            adapter2.add(rgbBulb1, new Identity("rgbBulb1", "rgbBulb"));
            adapter1.add(rgbBulb2, new Identity("rgbBulb2", "rgbBulb"));
            adapter1.add(monitoringCamera1, new Identity("monitoringCamera1", "monitoringCamera"));
            adapter2.add(monitoringCamera2, new Identity("monitoringCamera2", "monitoringCamera1"));

            // Aktywacja adaptera i wejście w pętlę przetwarzania żądań
            adapter1.activate();
            adapter2.activate();

            //show objects in adapter
            System.out.println("Entering event processing loop...");
            communicator.waitForShutdown();

        } catch (Exception e) {
            e.printStackTrace(System.err);
            status = 1;
        }
        if (communicator != null) {
            try {
                communicator.destroy();
            } catch (Exception e) {
                e.printStackTrace(System.err);
                status = 1;
            }
        }
        System.exit(status);
    }


    public static void main(String[] args) {
        IceServer app = new IceServer();
        app.t1(args);
    }
}