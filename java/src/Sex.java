
public class Sex {
  public static void main(String[] args) {
    String name = Teclado.leString("Digite seu nome:");
    char sexo = Teclado.leChar("Digite seu sexo:");

    if(sexo == 'F' && sexo == 'f')
    System.out.println("Sexo feminino!");

    else if(sexo == 'M' && sexo == 'm')
    System.out.println("Sexo masculino!");

    else
    System.out.println("Sexo inválido!");
  }
}
