package device.controller;

import device.Device;

public class Controller {
    private Device device;

    public Controller(Device device) {
        if (device == null) {
            throw new IllegalArgumentException("Device cannot be null");
        }
        this.device = device;
    }

    public void togglePower() {
        device.togglePower();
    }

    public void increaseSpeed() {
        device.increaseSpeed();
    }

    public void decreaseSpeed() {
        device.decreaseSpeed();
    }
}
