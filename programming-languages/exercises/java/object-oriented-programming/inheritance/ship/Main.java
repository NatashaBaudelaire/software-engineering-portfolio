package ship;

public class Main {
    public static void main(String[] args) {

        ContainerShip containerShip = new ContainerShip("Container A", 15000, 5, 3, 10);
        System.out.println("Container Ship registered:");
        System.out.println(containerShip);

        BulkCarrierShip bulkCarrierShip = new BulkCarrierShip("Bulk Carrier B", 20000, 4, 2, 12);
        System.out.println("\nBulk Carrier Ship registered:");
        System.out.println(bulkCarrierShip);

        Trip trip = new Trip("2025-06-01");
        System.out.println("\nTrip registered:");
        System.out.println(trip);

  
        if (trip.allocateContainerShip(containerShip)) {
            System.out.println("\nContainer ship allocated successfully.");
        } else {
            System.out.println("\nFailed to allocate container ship.");
        }
        System.out.println(trip);


        if (containerShip.startLoading()) {
            System.out.println("\nContainer ship loading started successfully.");
        } else {
            System.out.println("\nFailed to start loading container ship.");
        }
        System.out.println(containerShip);


        if (containerShip.finishLoading()) {
            System.out.println("\nContainer ship loading finished successfully.");
        } else {
            System.out.println("\nFailed to finish loading container ship.");
        }
        System.out.println(containerShip);


        if (trip.startTrip()) {
            System.out.println("\nTrip started successfully.");
        } else {
            System.out.println("\nFailed to start trip.");
        }
        System.out.println(trip);


        if (trip.finishTrip()) {
            System.out.println("\nTrip finished successfully (unexpected).");
        } else {
            System.out.println("\nCannot finish trip before unloading.");
        }
        System.out.println(trip);


        if (containerShip.unload()) {
            System.out.println("\nContainer ship unloaded successfully.");
        } else {
            System.out.println("\nFailed to unload container ship.");
        }
        System.out.println(containerShip);


        if (trip.finishTrip()) {
            System.out.println("\nTrip finished successfully.");
        } else {
            System.out.println("\nFailed to finish trip.");
        }
        System.out.println(trip);
    }
}
