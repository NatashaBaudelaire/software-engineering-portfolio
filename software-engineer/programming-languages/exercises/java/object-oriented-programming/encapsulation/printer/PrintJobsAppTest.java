package printer;

public class PrintJobsAppTest {
    public static void main(String[] args) {
        Printer printer = new Printer(1);

        printer.receivePrintJob("Coffee with Code: Exploring Java - Aldo Moura.pdf");
        printer.receivePrintJob("Secure Java: Best Practices and Security - Aldo Moura.pdf");
        printer.receivePrintJob("Java: Biggest Mistakes in the Logical World of Oscar - Aldo Moura.pdf");
        printer.receivePrintJob("The Path of the Javist - Aldo Moura.pdf");

        printer.showPrintQueue();

        System.out.println("\nPrinting jobs...");

        while (true) {
            printer.finishNextPrintJob();
            printer.showPrintQueue();
            if (printer.isPrintQueueEmpty()) break;
        }

        System.out.println("\nAll print jobs finished.");
    }
}
