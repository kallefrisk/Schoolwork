package Java.Demos;

import java.util.Scanner;

public class Authorization {

  /**
   * Checks whether the three passwords passed are correct or not.
   * 
   * @param pass1 password 1
   * @param pass2 password 2
   * @param pass3 password 3
   * @return true/false
   */
  static boolean isAuthorized(int pass1, int pass2, int pass3) {
    
    int truePass1 = 1;
    int truePass2 = 12;
    int truePass3 = 123;

    return (truePass1 == pass1 && truePass2 == pass2 && truePass3 == pass3);
  }

  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);

    System.out.print("\nPlease enter the first password: ");
    int pass1 = s.nextInt();

    System.out.print("\nPlease enter the second password: ");
    int pass2 = s.nextInt();

    System.out.print("\nPlease enter the third password: ");
    int pass3 = s.nextInt();

    boolean authorized = isAuthorized(pass1, pass2, pass3);

    if (authorized) {
      System.out.println("\nYou ARE authorized!\n");
    } else {
      System.out.println("\nYou ARE NOT authorized!\n");
    }

    s.close();
  }
}