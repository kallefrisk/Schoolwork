package Java.Demos;

public class IntToString {
  
  public static String printProfile(String name, int age) {
    String string = name + ", " + String.valueOf(age) + "years old.";
    return string;
  }

  public static void main(String[] args) {
    
    String message = printProfile("Alex", 24);

    System.out.println(message);
  }
}
