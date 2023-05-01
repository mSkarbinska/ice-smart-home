module SmartHome {
    struct Color {
        float r;
        float g;
        float b;
    };

    struct DateTime {
        int year;
        int month;
        int day;
        int hour;
        int minute;
    };

     struct Recording {
        DateTime fromDate;
        DateTime toDate;
    };

    exception InvaildColorException {};
    exception InvalidDateException {};
    exception IvalidTimeBlockAException {};

    interface LightBulb {
        idempotent bool getState();
        void setState(bool newState);
    };

    interface Fridge {
        idempotent float getTemperature();
        void setTemperature(float newTemperature);
        idempotent bool getDoorState();
        void setDoorState(bool newDoorState);
    };

    interface RGBBulb extends LightBulb {
        idempotent Color getColor();
        void setColor(Color color) throws InvaildColorException;
    };

    interface MonitoringCamera {
        void saveRecording(DateTime from, DateTime to) throws InvalidDateException, IvalidTimeBlockAException;
        idempotent Recording getLastRecording();
    };

    interface Bulbulator {
        string mumble();
    };
};