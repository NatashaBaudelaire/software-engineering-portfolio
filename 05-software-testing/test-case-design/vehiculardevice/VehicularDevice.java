package vehiculardevice;

/**
 * Stateful model of a motor vehicle used for the test-case-design exercise.
 *
 * <p>The vehicle has four doors, a trunk, an alarm, and can be running or in
 * motion. The behaviour defined by the test suite and this contract is fully
 * implemented: a vehicle can only move when it is running, stationary, with
 * the trunk closed, the alarm inactive and every door locked; a door cannot be
 * opened while the alarm is active (the attempt soft-fails); and any door can
 * be locked regardless of whether it is open or closed.
 */
public class VehicularDevice {

    /** Number of doors on the vehicle. Door numbers range from 1 to this value. */
    private static final int NUMBER_OF_DOORS = 4;

    /** Error message used when a door number outside the valid range is supplied. */
    private static final String NON_EXISTENT_DOOR = "Non-existent door";

    private boolean running;
    private boolean inMotion;
    private boolean trunkOpen;
    private boolean alarmActive;

    /** {@code doorsOpen[doorNumber - 1]} is {@code true} when the door is open. */
    private final boolean[] doorsOpen = new boolean[NUMBER_OF_DOORS];

    /** {@code doorsLocked[doorNumber - 1]} is {@code true} when the door is locked. */
    private final boolean[] doorsLocked = new boolean[NUMBER_OF_DOORS];

    /**
     * Creates a vehicle in its default resting state: parked, engine off,
     * all doors closed and unlocked, trunk closed, alarm deactivated.
     */
    public VehicularDevice() {
    }

    /**
     * Attempts to put the vehicle into motion.
     *
     * <p>The vehicle can only start moving when it is running, stationary, the
     * trunk is closed, the alarm is inactive, and every door is locked. If any
     * of those preconditions is violated the attempt fails and the vehicle
     * remains stationary.
     *
     * @return {@code true} if the vehicle starts moving, {@code false} otherwise
     */
    public boolean move() {
        if (!running) {
            return false;
        }
        if (trunkOpen) {
            return false;
        }
        if (alarmActive) {
            return false;
        }
        if (inMotion) {
            return false;
        }
        for (int doorNumber = 1; doorNumber <= NUMBER_OF_DOORS; doorNumber++) {
            if (!isDoorLocked(doorNumber)) {
                return false;
            }
        }
        inMotion = true;
        return true;
    }

    /**
     * Attempts to open the given door.
     *
     * <p>A closed door can be opened unless the alarm is active; an alarm blocks
     * opening and the attempt soft-fails. Returning {@code false} (rather than
     * throwing) is consistent with how this method already reports the "cannot
     * open right now" case of an already-open door, and with how {@code move()}
     * refuses prohibited states; an active alarm is an expected runtime state,
     * not invalid input, so {@link IllegalArgumentException} remains reserved
     * for invalid door numbers.
     *
     * @param doorNumber door number between 1 and {@value #NUMBER_OF_DOORS}
     * @return {@code true} if the door was opened, {@code false} if it was already
     *         open or could not be opened because the alarm is active
     * @throws IllegalArgumentException if {@code doorNumber} is not a valid door
     */
    public boolean openDoor(int doorNumber) {
        validateDoorNumber(doorNumber);
        if (alarmActive || isDoorOpen(doorNumber)) {
            return false;
        }
        setDoorOpen(doorNumber, true);
        return true;
    }

    /**
     * Attempts to lock the given door.
     *
     * <p>Locking is always permitted: a door can be locked whether it is open or
     * closed. Locking an open door returns {@code true} and sets its locked flag
     * while leaving it open.
     *
     * @param doorNumber door number between 1 and {@value #NUMBER_OF_DOORS}
     * @return {@code true} if the door was locked, {@code false} if it was already locked
     * @throws IllegalArgumentException if {@code doorNumber} is not a valid door
     */
    public boolean lockDoor(int doorNumber) {
        validateDoorNumber(doorNumber);
        if (isDoorLocked(doorNumber)) {
            return false;
        }
        setDoorLocked(doorNumber, true);
        return true;
    }

    /**
     * @param running {@code true} to start the engine
     */
    public void setRunning(boolean running) {
        this.running = running;
    }

    /**
     * @param inMotion {@code true} to mark the vehicle as in motion
     */
    public void setInMotion(boolean inMotion) {
        this.inMotion = inMotion;
    }

    /**
     * @return {@code true} when the vehicle is in motion
     */
    public boolean isInMotion() {
        return inMotion;
    }

    /**
     * @param trunkOpen {@code true} to open the trunk
     */
    public void setTrunkOpen(boolean trunkOpen) {
        this.trunkOpen = trunkOpen;
    }

    /**
     * @return {@code true} when the trunk is open
     */
    public boolean isTrunkOpen() {
        return trunkOpen;
    }

    /**
     * @param alarmActive {@code true} to activate the alarm
     */
    public void setAlarmActive(boolean alarmActive) {
        this.alarmActive = alarmActive;
    }

    /**
     * @return {@code true} when the alarm is active
     */
    public boolean isAlarmActive() {
        return alarmActive;
    }

    /**
     * Opens or closes the given door.
     *
     * @param doorNumber door number between 1 and {@value #NUMBER_OF_DOORS}
     * @param open       {@code true} to open the door, {@code false} to close it
     * @throws IllegalArgumentException if {@code doorNumber} is not a valid door
     */
    public void setDoorOpen(int doorNumber, boolean open) {
        validateDoorNumber(doorNumber);
        doorsOpen[doorNumber - 1] = open;
    }

    /**
     * @param doorNumber door number between 1 and {@value #NUMBER_OF_DOORS}
     * @return {@code true} when the given door is open
     * @throws IllegalArgumentException if {@code doorNumber} is not a valid door
     */
    public boolean isDoorOpen(int doorNumber) {
        validateDoorNumber(doorNumber);
        return doorsOpen[doorNumber - 1];
    }

    /**
     * Locks or unlocks the given door.
     *
     * @param doorNumber door number between 1 and {@value #NUMBER_OF_DOORS}
     * @param locked     {@code true} to lock the door, {@code false} to unlock it
     * @throws IllegalArgumentException if {@code doorNumber} is not a valid door
     */
    public void setDoorLocked(int doorNumber, boolean locked) {
        validateDoorNumber(doorNumber);
        doorsLocked[doorNumber - 1] = locked;
    }

    /**
     * @param doorNumber door number between 1 and {@value #NUMBER_OF_DOORS}
     * @return {@code true} when the given door is locked
     * @throws IllegalArgumentException if {@code doorNumber} is not a valid door
     */
    public boolean isDoorLocked(int doorNumber) {
        validateDoorNumber(doorNumber);
        return doorsLocked[doorNumber - 1];
    }

    private void validateDoorNumber(int doorNumber) {
        if (doorNumber < 1 || doorNumber > NUMBER_OF_DOORS) {
            throw new IllegalArgumentException(NON_EXISTENT_DOOR);
        }
    }
}