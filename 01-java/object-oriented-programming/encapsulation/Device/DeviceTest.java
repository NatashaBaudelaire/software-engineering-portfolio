package device;

public class DeviceTest {
    public static void main(String[] args) {
        Device fan = new Device();

        System.out.println("Device ON? " + fan.isOn());
        fan.togglePower();
        System.out.println("Device ON? " + fan.isOn());

        System.out.println("Initial Speed: " + fan.getSpeed());

        fan.increaseSpeed();
        fan.increaseSpeed();
        System.out.println("Speed after increasing: " + fan.getSpeed());

        fan.increaseSpeed();
        System.out.println("Speed after attempting over-increase: " + fan.getSpeed());

        fan.decreaseSpeed();
        fan.decreaseSpeed();
        System.out.println("Speed after decreasing: " + fan.getSpeed());

        fan.decreaseSpeed();
        System.out.println("Speed after attempting over-decrease: " + fan.getSpeed());
    }
}