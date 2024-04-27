import java.util.Scanner;

public class run {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int flag = 1;

        while(flag != 0){
            SMLSimulator simulator = new SMLSimulator();
            simulator.runSimulator ();
            
            System.out.printf("%s\n%s\n",
            "*** Enter 1 to again. ***",
                    "*** Enter 0 to exit. ***");
            flag = scanner.nextInt();
        }
    }
}
