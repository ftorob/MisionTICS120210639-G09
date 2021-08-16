/* Para crear un nuevo archivo básico vamos a HELP --> WELCOME --> LEARN --> FIND AND RUN ALL COMANDS
--> JAVA CREATE JAVA PROJECTS --> NO BUILD TOOLS --> CREO UNA CARPETA EN WINDOWS CON "Y" -->
DOY EL MISMO NOMBRE AL ARCHIVO "Y" --> LISTO
*/

import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        //System.out.println("Hello, World!");

        /* 
        if (1 == 1){ //{} Esto es un boque de código == sirve para comparar pero no siempre por eso se usan métodos de Java
            System.out.println("Verdadero");
        }
        */

        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese su nombre: "); //Aquí solicito el nombre primero
        String nom = sc.nextLine(); //Aquí lo ingreso para iniciar el ciclo --> nom es un objeto y tiene métodos

        if (nom.equals("Fernando")){ // == no sirve para hacer comparaciones de texto (solo  números) en Java y se debe usar .equals para comparar
            System.out.println("Es correcto!");
        }
        else if (nom.equals("Eduardo")){ //Es similar al ELIF en Python
            System.out.println("Casi correcto!");
        }
        else{
            System.out.println("Respuesta incorrecta :(");
        }

        //IF
        if (7 == 38){ //Igualdad de números
            System.out.println("Es correcto!");
        }
        else{
            System.out.println("No es correcto :(");
        }

        if ("a" != "k"){ //Diferentes caracteres
            System.out.println("Es correcto!");
        }
        else{
            System.out.println("No es correcto :(");
        }

        //Condicional con SWITCH
        Scanner tc = new Scanner(System.in); //Se debe cambiar a tc u otro valor para que no quede repetido
        System.out.println("Ingrese un valor: ");
        int valor = tc.nextInt();
        String respuesta = "";

        switch(valor){ //Serviría para hacer una calculadora
            case 1:
                // Operación
                respuesta = "Caso 1 correcto";
                break;
            case 2:
                // Operación
                respuesta = "Caso 2 correcto";
                break;
            default:
                // Operación
                respuesta = "Ninguna de las anteriores";
        }
        System.out.println(respuesta);

        //CICLOS FOR
        for(var i = 0; i < 100; i++){
            System.out.println(i);
        }

        //CICLOS WHILE (PREGUNTA --> EJECUTA)
        int y = 0;
        while (y <= 100){
            System.out.println("El valor de la variables es -> " + y);
            y = y + 10;
        }

        //CICLO DO - WHILE (EJECUTA --> PREGUNTA)
        int x = 0;
        do {
            System.out.println("El valor de la variable es -> " + x);
            x++;
        }
        while (x < 200);

        //MANEJO DE INCREMENTALES Y DECREMENTALES
        int a = 5;
        int b = a++; //++ a la derecha --> se toma pero en la siguiente linea
        System.out.println(a); //6
        System.out.println(b); //5

        int c = 5;
        int d = --c; //++ a la izquierda --> se toma
        System.out.println(c); //6
        System.out.println(d); //6

        a += b; //Es igual a decir a = a + b;
        System.out.println(a); //11

        // OPERADORES LÓGICOS
        if ((5 == 5) || (5 < 4)){ //Si la primera es verdadera se salta y arroja TRUE. || --> Representa a suma lógica con cortocircuito
            System.out.println("Correcto!");
        }

        if ((5 == 5) && (5 < 4)){ //&& --> Representa al AND que es producto lógica con cortocircuito
            System.out.println("Correcto!");
        }
        
    //Ejercicio 1 --> Está definida dentro de la función MINE
        var nom_bre = "Fernando Toro Bernal";
        var resul_tado = saludo(nom_bre);
        System.out.println(resul_tado);

    //Ejercicio 2
        var fc = new Scanner(System.in);
        System.out.println("Introduce un número entero: ");
        var numero = fc.nextInt();

        var digito = numeroDigito(numero);
        
        System.out.println("El número tiene " + digito + " cifras");

    //Ejercicio 3
        Scanner gc = new Scanner(System.in); //Creamos el objeto de scanner para pedir el dato númerico
        System.out.println("Ingrese un número entero: "); //Impresión por consola con la clase system
        var entero = gc.nextInt(); //Asignamos a una variable número el valor ingresado por teclado

        System.out.println("El doble del " + entero + " es " + numeroDoble(entero)); //Impresion doble
        System.out.println("El triple del " + entero + " es " + (entero*3)); //Impresión triple
        System.out.println(numeroRespuesta(entero)); //Impresión total en STR

    //Ejercicio 5
        var mc = new Scanner(System.in);
        System.out.println("Ingrese un número entero: ");
        var val_ip = mc.nextInt();

        var resultado_ip = validarNumero(val_ip);
        System.out.println(resultado_ip);

    //Ejercicio 6 - Métodos de STRING
        var oc = new Scanner(System.in);
        System.out.println("Ingrese una palabra aquí");
        var longpal = oc.nextLine();

        var evapal = longpal.length();
        System.out.println(evapal);

    }

    //Ejercicio 1
    public static String saludo(String nom_bre){ //Así se define una función SALUDO
        return "Hola " + nom_bre + "!";
    }

    //Ejercicio 2
    public static int numeroDigito(int numero) {
        var cifras = 0;

        while (numero != 0){
            numero /= 10;
            cifras++;
        }

        return cifras;
    }

    //Ejercicio 3
    public static int numeroDoble(int entero){
        return entero * 2;
    }

    public static String numeroRespuesta(int entero){
        return "El doble de " + entero + " es " + (entero * 2) +
                "\n y el triple de " + entero + " es " + (entero * 3);
    }

    //Ejercicio 5
    public static String validarNumero(int val_ip){
        return (val_ip % 2 == 0 ? val_ip + " Es par" : val_ip + " Es impar"); //? es un operador condicional similar a IF
        //Si se cumple da la primera parte y sino se cumple va la segunta parte (:)
        // return (val_ip % 2 != 0 ? val_ip + " Es impar" : val_ip + " Es par"); --> otra forma de decir lo mismo
    }
}
