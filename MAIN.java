import java.io.*;
public class MAIN
{
    public static void main(String args[])throws IOException
    {
       BufferedReader p = new BufferedReader(new InputStreamReader(System.in));
       System.out.println("Enter the height of the triangle");
       double a = Double.parseDouble(p.readLine());
       System.out.println("Enter the base of the triangle");
       double b = Double.parseDouble(p.readLine());
       double c = 0.5*a*b;
       System.out.println("The hypotenuse of the triangle is"+" "+c);
    }
}
