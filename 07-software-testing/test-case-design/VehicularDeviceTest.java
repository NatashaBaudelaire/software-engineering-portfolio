package VehicularDevice;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;


public class VehicularDeviceTest {

    private VehicularDevice vd;

    @BeforeEach
    void setUp() {
        vd = new VehicularDevice();
    }

    @Test
    @DisplayName("CT035: Moving a running, stationary vehicle with the trunk open should return false")
    void ct035_moveVehicleWithTrunkOpen_shouldReturnFalse() {

        vd.setRunning(true);
        vd.setInMotion(false);
        vd.setTrunkOpen(true);

        boolean result = vd.move();

        assertFalse(result, "Move should return false when the trunk is open");
        assertFalse(vd.isInMotion(), "Vehicle should not be in motion");
        assertTrue(vd.isTrunkOpen(), "Trunk should remain open");
    }

    // CT051: Open door 2: stationary, alarm deactivated, only door 2 closed (doors 1, 3 and 4 open and only door 2 closed)
    @Test
    @DisplayName("CT051: Open closed door 2 (others open): should return true and door 2 become open")
    void ct051_openClosedDoor2_shouldReturnTrue() {

        vd.setRunning(false);
        vd.setInMotion(false);
        vd.setAlarmActive(false);
        vd.setDoorOpen(1, true);
        vd.setDoorOpen(2, false);
        vd.setDoorOpen(3, true);
        vd.setDoorOpen(4, true);

        boolean result = vd.openDoor(2);

        assertTrue(result, "Opening door 2 should return true");
        assertTrue(vd.isDoorOpen(2), "Door 2 should be open");
        assertTrue(vd.isDoorOpen(1), "Door 1 should remain open");
        assertTrue(vd.isDoorOpen(3), "Door 3 should remain open");
        assertTrue(vd.isDoorOpen(4), "Door 4 should remain open");
    }

    // CT052: Open door 2 already open: stationary, alarm deactivated, door 2 open
    @Test
    @DisplayName("CT052: Opening an already open door 2 should return false")
    void ct052_openAlreadyOpenDoor2_shouldReturnFalse() {

        vd.setRunning(false);
        vd.setInMotion(false);
        vd.setAlarmActive(false);
        vd.setDoorOpen(1, false);
        vd.setDoorOpen(2, true);
        vd.setDoorOpen(3, false);
        vd.setDoorOpen(4, false);

        boolean result = vd.openDoor(2);

        assertFalse(result, "Opening an already open door should return false");
        assertTrue(vd.isDoorOpen(2), "Door 2 should remain open");
        assertFalse(vd.isDoorOpen(1), "Door 1 should remain closed");
        assertFalse(vd.isDoorOpen(3), "Door 3 should remain closed");
        assertFalse(vd.isDoorOpen(4), "Door 4 should remain closed");
    }


    // CT073: Lock door 4 with all doors unlocked
    @Test
    @DisplayName("CT073 - Locking door 4 (closed and unlocked) should return true")
    void ct073_lockUnlockedDoor4_shouldReturnTrue() {

        for (int i = 1; i <= 4; i++) {
            vd.setDoorOpen(i, false);
            vd.setDoorLocked(i, false);
        }

        boolean result = vd.lockDoor(4);

        assertTrue(result, "Locking door 4 should return true");
        assertTrue(vd.isDoorLocked(4), "Door 4 should be locked");
        assertFalse(vd.isDoorLocked(1), "Door 1 should remain unlocked");
        assertFalse(vd.isDoorLocked(2), "Door 2 should remain unlocked");
        assertFalse(vd.isDoorLocked(3), "Door 3 should remain unlocked");
    }

    // CT079: Lock door 7 (non-existent) should throw an exception
    @Test
    @DisplayName("CT079: Locking non-existent door 7 should throw IllegalArgumentException with message 'Non-existent door'")
    void ct079_lockNonExistentDoor_shouldThrowException() {

        for (int i = 1; i <= 4; i++) {
            vd.setDoorOpen(i, false);
            vd.setDoorLocked(i, false);
        }

        IllegalArgumentException ex = assertThrows(
            IllegalArgumentException.class,
            () -> vd.lockDoor(7),
            "Should throw IllegalArgumentException for a non-existent door"
        );
        assertEquals("Non-existent door", ex.getMessage(),
            "Exception message should be 'Non-existent door'");

        for (int i = 1; i <= 4; i++) {
            assertFalse(vd.isDoorLocked(i), "Door " + i + " should not be locked");
        }
    }
}