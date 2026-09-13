package printer;

import java.util.ArrayList;

public class Printer {

    private int printerId;
    private boolean printing;
    private ArrayList<PrintJob> printJobs;

    public Printer(int printerId) {
        this.printerId = printerId;
        this.printing = false;
        this.printJobs = new ArrayList<>();
    }

    public int getPrinterId() {
        return printerId;
    }

    public void setPrinterId(int printerId) {
        this.printerId = printerId;
    }

    public boolean isPrinting() {
        return printing;
    }

    public ArrayList<PrintJob> getPrintJobs() {
        return printJobs;
    }

    @Override
    public String toString() {
        String status = printing ? "Printing" : "Idle";
        String fileName = printJobs.isEmpty() ? "No file" : printJobs.get(0).getFileName();

        return "File: " + fileName +
               " | Printer ID: " + printerId +
               " | Status: " + status;
    }


    public void receivePrint(PrintJob job) {
        printJobs.add(job);
        if (!printing) {
            printing = true;
        }
    }

    public void receivePrintJob(String fileName) {
        PrintJob job = new PrintJob(fileName, this.printerId);
        receivePrint(job);
    }

    public void finishPrint() {
        if (!printJobs.isEmpty()) {
            printJobs.remove(0);
        }
        if (printJobs.isEmpty()) {
            printing = false;
        }
    }

    public void finishNextPrintJob() {
        finishPrint();
    }

    public void showPrintQueue() {
        System.out.println(toString());
        for (int i = 0; i < printJobs.size(); i++) {
            System.out.println("  " + (i + 1) + ". " + printJobs.get(i).getFileName());
        }
    }

    public boolean isPrintQueueEmpty() {
        return printJobs.isEmpty();
    }
}
