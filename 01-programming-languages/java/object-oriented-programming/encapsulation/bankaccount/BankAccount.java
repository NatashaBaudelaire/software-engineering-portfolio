package bankaccount;


public class BankAccount {
    private int accountID;
    private String agency;
    private String accountNumber;
    private char type;
    private double balance;
    private double creditLimit;


    public BankAccount(int accountID, String agency, String accountNumber) {
        this.accountID = accountID;
        this.agency = agency;
        this.accountNumber = accountNumber;
        this.type = 'N';
        this.balance = 0.0;
        this.creditLimit = 0.0;
    }


    public BankAccount(int accountID, String agency, String accountNumber, double creditLimit) {
        this.accountID = accountID;
        this.agency = agency;
        this.accountNumber = accountNumber;
        this.type = 'S';
        this.balance = 0.0;
        this.creditLimit = creditLimit;
    }


    public boolean changeLimit(double newLimit) {
        if (type == 'S') {
            if (newLimit <= 0.0) {
                type = 'N';
                creditLimit = 0.0;
            } else {
                creditLimit = newLimit;
            }
            return true;
        }
        return false;
    }


    public boolean registerDeposit(double amount) {
        if (amount > 0) {
            balance += amount;
            return true;
        }
        return false;
    }


    public double getBalance() {
        return balance;
    }

    public double getCreditLimit() {
        return creditLimit;
    }

    public char getType() {
        return type;
    }

    public String getAccountNumber() {
        return accountNumber;
    }

    public String getAgency() {
        return agency;
    }

    public int getAccountID() {
        return accountID;
    }

    @Override
    public String toString() {
        return "BankAccount{" +
                "ID=" + accountID +
                ", Agency='" + agency + '\'' +
                ", AccountNumber='" + accountNumber + '\'' +
                ", Type=" + type +
                ", Balance=" + balance +
                ", CreditLimit=" + creditLimit +
                '}';
    }
}
