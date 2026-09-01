package Printer;

public class PrintJob {
    private int printerId;
    private String fileName;
    private boolean status; // false = in queue, true = finished

    public PrintJob(String fileName, int printerId) {
        this.printerId = printerId;
        this.fileName = fileName;
        this.status = false;
    }

    public void startJob() {
        status = true;
        System.out.println("Finished printing: " + fileName);
    }

    public int getPrinterId() {
        return printerId;
    }

    public String getFileName() {
        return fileName;
    }

    public boolean isFinished() {
        return status;
    }

    @Override
    public String toString() {
        return fileName + " | Printer ID: " + printerId + " | Status: " + (status ? "Finished" : "In queue");
    }
}
