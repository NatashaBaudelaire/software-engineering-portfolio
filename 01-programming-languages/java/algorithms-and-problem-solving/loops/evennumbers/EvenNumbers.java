package evennumbers;

import java.util.Scanner;

public class EvenNumbers {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);


        int i = 2;


        do {
            System.out.println(i);
            i += 2;
        } while (i <= 20);


        input.close();
    }
}
