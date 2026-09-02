package device;

public class Device {
    private boolean isOn;
    private int speed;

    public Device() {
        this.isOn = false;
        this.speed = 1;
    }

    public void togglePower() {
        this.isOn = !this.isOn;
    }

    public void increaseSpeed() {
        if (this.speed < 3) {
            this.speed++;
        }
    }

    public void decreaseSpeed() {
        if (this.speed > 1) {
            this.speed--;
        }
    }

    public boolean isOn() {
        return isOn;
    }

    public int getSpeed() {
        return speed;
    }

    @Override
    public String toString() {
        return "Device [isOn=" + isOn + ", speed=" + speed + "]";
    }
}
