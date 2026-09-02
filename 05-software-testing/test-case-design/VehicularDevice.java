package VehicularDevice;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class VehicularDeviceTest {

    private VehicularDevice vehicle;

    @BeforeEach
    void setUp() {
        vehicle = new VehicularDevice();
    }

    // CT035: Put a running, stationary vehicle with the trunk open into motion
    @Test
    void CT035_moveRunningStationaryVehicleWithTrunkOpen() {
        vehicle.setRunning(true);
        vehicle.setTrunkOpen(true);

        boolean result = vehicle.move();

        assertFalse(result, "Vehicle should not move when trunk is open");
        assertFalse(vehicle.isInMotion());
    }

    // CT051: Open door 2 of a stationary vehicle, with alarm deactivated and only door 2 closed
    @Test
    void CT051_openDoor2_alarmOff_door2Closed() {
        vehicle.setDoorOpen(1, true);
        vehicle.setDoorOpen(3, true);
        vehicle.setDoorOpen(4, true);
        // door 2 remains closed (default)

        boolean result = vehicle.openDoor(2);

        assertTrue(result, "Door 2 should open successfully");
        assertTrue(vehicle.isDoorOpen(2));
    }

    // CT052: Open door 2 of a stationary vehicle, with alarm deactivated and only door 2 open
    @Test
    void CT052_openDoor2_alarmOff_door2AlreadyOpen() {
        vehicle.setDoorOpen(2, true);

        boolean result = vehicle.openDoor(2);

        assertFalse(result, "Should return false — door 2 is already open");
        assertTrue(vehicle.isDoorOpen(2));
    }

    // CT073: Lock door 4 of a vehicle with all doors unlocked
    @Test
    void CT073_lockDoor4_allDoorsUnlocked() {
        // Default state: all doors unlocked and closed

        boolean result = vehicle.lockDoor(4);

        assertTrue(result, "Door 4 should be locked successfully");
        assertTrue(vehicle.isDoorLocked(4));
    }

    // CT079: Lock door 7 — door does not exist, expect exception
    @Test
    void CT079_lockDoor7_doorDoesNotExist() {
        assertThrows(IllegalArgumentException.class, () -> {
            vehicle.lockDoor(7);
        }, "Door 7 does not exist — should throw IllegalArgumentException");
    }
}