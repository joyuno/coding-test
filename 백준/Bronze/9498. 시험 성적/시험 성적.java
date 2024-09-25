import java.util.*;

class Main {
public static void main(String[] args) {
	int score = 0;
	String grade = "";
	
	Scanner sc = new Scanner(System.in);
	score = sc.nextInt();
	if(0<=score && score<=100) {
		if(score>=90) {
			grade = "A";
		}else if(score>=80) {
			grade = "B";
		}else if(score>= 70) {
			grade = "C";
		}else if(score>=60){
			grade = "D";
		}else {
			grade = "F";
			
		}
		System.out.println(grade);
	}else {
		System.out.println("다시입력해주세요");
		
	}
	
	}	
}
