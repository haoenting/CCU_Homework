// https://blog.csdn.net/hrlnldy/article/details/7993741
import java.util.Scanner;
public class SMLSimulator {
	private static final Scanner input = new Scanner(System.in);
	private static final int SIZE = 100;

	private int accumulator;
	private int instructionCounter;
	private int instructionRegister;
	private int operationCode;
	private int operand;
	private int [] memory;

	// Operation codes
	private static final int READ = 10;
	private static final int WRITE = 11;
	private static final int LOAD = 20;
	private static final int STORE = 21;
	private static final int ADD = 30;
	private static final int SUBTRACT = 31;
	private static final int DIVIDE = 32;
	private static final int MULTIPLY = 33;
	private static final int BRANCH = 40;
	private static final int BRANCHNEG = 41;
	private static final int BRANCHZERO = 42;
	private static final int HALT = 43;
	

	public SMLSimulator() {
        displayWelcomeMessage ();
		initialiseVariables ();
	}

	public void displayWelcomeMessage ( ) {
		System.out.printf ("\n%s\n%s\n%s\n%s\n%s\n%s\n", 
			"*** Welcome to Simpletron! ***",
			"*** Please enter your program one instruction    ***",
			"*** (or data word) at a time. I will display     ***",
			"*** the location number and a question mark (?). ***",
			"*** You then type the word for that location.    ***",
			"*** Type -99999 to stop entering your program.   ***");
    }

	public void initialiseVariables ( ){
		memory = new int [SIZE];
		instructionCounter = 0;
	}	

	public void runSimulator () {
		enterProgram();

        System.out.printf ("\n%s%s", 
		"*** Program loading completed ***\n", 
            	"*** Program excecution begins ***\n");	
		
		while(operationCode != HALT){
			loadInstruction(instructionCounter);
			execute(operand, operationCode);
		}
	}

	public void enterProgram() {
		int submittedInstruction = 0;
		int memoryPointer = 0;

		do{
			System.out.printf ("%d %s  ", memoryPointer, "?" );
			submittedInstruction = input.nextInt();
			if(submittedInstruction > 9999 || submittedInstruction < -9999){
				System.out.println("*** Warning: Instruction Register out of range ***");
				continue;
			}
			memory[memoryPointer++] = submittedInstruction;
		} while ( submittedInstruction != -99999 );
	}	

	public void loadInstruction(int counter){
		instructionRegister = memory[counter];
		operationCode = instructionRegister / 100;
		operand = instructionRegister % 100;
	}
	
	public void execute(int operands, int operation) {
		switch (operation) {
			case READ:
				System.out.println( " Enter an integer " );
				int number = input.nextInt();
				if(number > 9999 || number < -9999){
					System.err.println("*** Register Overflow ***");
					error();
				}
				instructionCounter++;
				break;
			case WRITE:
				System.out.println ("\nThe result of the operation is " + memory [ operands] +"\n");
				instructionCounter++;
				break;
			case LOAD:
				accumulator = memory[operands];
				instructionCounter++;
				break;
			case STORE:
				memory[operands] = accumulator;
				instructionCounter++;
				break;
			case ADD:
				accumulator += memory[operands];
				if(accumulator > 9999){
					System.err.println("*** Accumulator Overflow ***");
					error();
					break;
				}
				instructionCounter++;
				break;	
			case SUBTRACT: 
				accumulator -= memory[operands];
				if(accumulator < -9999){
					System.err.println("*** Accumulator Overflow ***");
					error();
					break;
				}
				instructionCounter++;
				break;
			case DIVIDE:
				if(memory[operands] == 0){
					System.out.println("*** Attempt to divide by zero ***");
					error();
					break;
				}
				accumulator /=  memory[operands];
				instructionCounter++;
				break;
			case MULTIPLY: 
				accumulator *= memory[operands];
				if(accumulator > 9999 || accumulator < -9999 ){
					System.err.println("*** Accumulator Overflow ***");
					error();
					break;
				}
				instructionCounter++;
				break;
			case BRANCH:
				instructionCounter = operands;
				break;
			case BRANCHNEG:	
				if (accumulator < 0)
					instructionCounter = operands;
				break;
			case BRANCHZERO:	
				if (accumulator == 0)
					instructionCounter = operands;
				break;
			case HALT:
				System.out.println("*** Simpletron execution terminated ***");
				dump();
				break;
			default:
				System.out.println("*** Attempt to execute invalid operation code ***");
				error();
				break;
		}
		
	}
	public void error(){
		System.out.println("*** Simpletron execution abnormally terminated ***");
		dump();
		operationCode = HALT;
	}

	public void dump(){
		System.out.println("REGISTER :");
		if (accumulator >= 0) 
			System.out.printf("%-25s%+04d\n", "accumulator", accumulator);
		else 
			System.out.printf("%-25s%04d\n", "accumulator", accumulator);
		System.out.printf("%-25s%02d\n", "instruction counter", instructionCounter);
		System.out.printf("%-25s+%04d\n", "instruction register", instructionRegister);
		System.out.printf("%-25s%02d\n", "operation code", operationCode);
		System.out.printf("%-25s%02d\n\n", "operand", operand);

		System.out.printf("MEMORY:\n");
		for (int i = 0; i < 10; i++)
			System.out.printf("%6d", i);
		System.out.println();
		int counter = 0;

		
		for (int i = 0; i < 10; i++ ) {
			if ( counter %10 == 0 )
				System.out.printf ("%2d ", counter);
			for (int j = 0; j < 10; j++) {	
				// Lets apply some formatting to improve the display
				System.out.printf("%s%04d ", memory[counter] >= 0 ? "+" : "-", memory[counter] < 0 ? memory[counter] * -1 : memory[counter]);
				counter++;

			}
		System.out.println();	
		}
	}
}
