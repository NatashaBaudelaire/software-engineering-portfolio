package apptestaccountbank;

public class TestAccountBank {
    public static void main(String[] args) {
        AccountBank normalAccount = new AccountBank(1, "1234", "000111");

        AccountBank specialAccount = new AccountBank(2, "5678", "222333", 1000.0);

        normalAccount.registerDeposit(500.0);
        specialAccount.registerDeposit(1200.0);

        System.out.println("Normal Account Balance: R$ " + normalAccount.getBalance());
        System.out.println("Special Account Balance: R$ " + specialAccount.getBalance());
        System.out.println("Special Account Credit Limit: R$ " + specialAccount.getCreditLimit());


        specialAccount.changeLimit(1500.0);
        System.out.println("Updated Credit Limit: R$ " + specialAccount.getCreditLimit());
    }
}
