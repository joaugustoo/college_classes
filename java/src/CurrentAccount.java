public class CurrentAccount {
  private int account;
  private double balance;

  public void setAccount(int account){
   this.account = account;
  }

  public int getAccount(){
    return this.account;
  }

  public void setBalance(double balance){
    this.balance = balance;
   }

  public double getBalance(){
    return this.balance;
  }

  @Override
  public String toString(){
   return "Conta 01 [account: " + account + " , balance: " + balance + "]";
  }
}
