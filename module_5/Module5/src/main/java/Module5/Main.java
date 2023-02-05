// Matthew Archer
// 1/29/23
// Module 5 Assignment
package Module5;

public class Main {

    public static void main(String[] args) {
        float i = 3;
        
        while (i < 100) {
            if (i == 99.0) {
                System.out.print("1/" + i);
            }
            else
                System.out.print("1/" + i + " + ");
            i += 3.0;
        }
        
        System.out.println();
        System.out.println();
        
        float j = 99;
    
        while (j > 2) {
            if (j == 3.0) {
                System.out.print("1/" + j);
            }
            else
                System.out.print("1/" + j + " + ");
            j -= 3.0;
        }
    }
}
