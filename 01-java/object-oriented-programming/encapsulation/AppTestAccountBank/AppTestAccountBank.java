package apptestaccountbank;

import java.util.Scanner;

public class AppTestAccountBank {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		AppTestAccountBank[] account = new AppTestAccountBank[4];

		AppTestAccountBank c1 = new AppTestAccountBank("N");
		AppTestAccountBank c2 = new AppTestAccountBank("Y");
		AppTestAccountBank c3 = new AppTestAccountBank("Y");

		account[0] = c1;
		account[1] = c2;
		account[2] = c3;

		System.out.println("Account Bank" + account);
		System.out.println("AccountID: " + account[0].getAccountID());
		System.out.println("Agency: " + account[0].getAgency());
		System.out.println("type: " + (account[0].getType().equals("N") ? "Normal" : "Special"));
		System.out.println("Number: " + account[0].getNumber());
		System.out.println("Balance: " + account[0].getBalance());

		System.out.println("Enter the Account ID of the bank for withdrawal");
		String AccountID = input.nextLine();

		int found = -1;
		for (int i = 0; i < account.length; i++) {
			if (account[i].getAccountID().equals(AccountID)) {
				found = i;
				break;
			}
		}
		if (found != -1) {
			System.out.println("Enter the deposit");
			double deposit = input.nextDouble();
			if (account[found].registerDeposit(deposit)) {
				System.out.println("Deposit was made sucessfully");
				System.out.println("AccountID: " + account[found].getAccountID());
			} else {
				System.out.println("Withdrawal was made insufficent!");
			}
		} else {
			System.out.println("Account was not found!");
		}

		input.close();
	}
}
