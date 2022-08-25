package Aula1.java;

public class main {
	public static void main(String[] args) {
		conversao c = new conversao();
		System.out.println(c.preFixPPosFix("@A"));
		System.out.println(c.preFixPPosFix("+@AB"));
		System.out.println(c.preFixPPosFix("*AB"));
		System.out.println(c.preFixPPosFix("*A+BC"));
		System.out.println(c.preFixPPosFix("**+AB-+CDEF"));
		System.out.println(c.preFixPPosFix("**+AB-+CD@E F"));
	}
}
