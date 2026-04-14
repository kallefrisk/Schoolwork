package Java.WolterDemo;

import java.util.Scanner;

public class FiveTries {
  
  /**
   * Checks whether the password is correct.
   * 
   * @param pass password to check
   * @return true/false
   */
  static boolean isAuthorized(int pass) {

    int truePass = 123;

    return (truePass == pass);
  }

  public static void main(String[] args) {

    Scanner s = new Scanner(System.in);

    boolean authorized;
    int tries = 0;
    int maxTries = 5;

    while (tries < maxTries) {

      System.out.print("\nPlease enter your password: ");
      int pass = s.nextInt();

      authorized = isAuthorized(pass);
      tries++;

      if (authorized) {
        System.out.println("\nYou ARE authorized!\n");
        break;
      } else if (tries < maxTries) {
        System.out.println("\nWrong password! Tries remaining: " + (maxTries - tries));
      } else {
        System.out.println("\nYou have failed " + maxTries + " times and are now locked out!\n");
      }
    }
  }
}
