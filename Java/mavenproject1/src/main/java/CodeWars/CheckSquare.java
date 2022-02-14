package CodeWars;

import java.lang.Math;
import static java.lang.Math.floor;
public class CheckSquare {
    
    public static boolean isSquare(int n){
       if (n>=0){
           double x = Math.sqrt(n);
           return ( floor(x) == x);
       } 
        return false;   
    };
    
    public static void main(String[] args) {
//        System.out.println("Halo Nama Saya Ihsan Ahsanu Amala");
        System.out.println(isSquare(5));
    }
}
