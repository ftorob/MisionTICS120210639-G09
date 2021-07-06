import java.awt.*; //importa librería de gráficas
import java.io.BufferedReader; //Libreria de entrada de datos 1A
import java.io.InputStreamReader; //Libreria de entrada de datos 1B
import java.util.Scanner; //Libreria de entrada de datos 2
import java.io.*; //Importa todas las librerias de JAVA pero a veces da un error

public class App { //El nombre de la clase debe ser exactamente igual al titulo del archivo o no compila :OOOOOOO

/**
 * Sintaxis de comentario llamado Java_document
 * al principio del proyecto
 * para escribir la documentación
 * No hay simil en Python
 */

    public static void main(String[] args) throws Exception {
        System.out.println("Hola Mundo Java"); //Así se hace una impresión en JAVA
    
    int i = 1; //cada sentencia debe terminar con ; o sino arrojaría error

    int x = 15; // con el int se declará el tipo de variable entera (siempre se debe declarar y no va a cambiar con el tiempo) y con el 15 se inicializa la variable
    String nombre = "Angel"; //Declarar alfanumerico --> No funciona las comillas sensillas y se debe usar dobles
    double a = 3.5; //Declarar decimales o flotantes
    boolean bNuevo = true; //Declarar booleano es true no True
    int[] datos; //Declarar arrays

    //A partir de Java 10 con la expresión "var" no se necesita declarar el tipo de variable
    var ejemplo = "ejemplo_1"; 
    //var b; --> Pero se debe agregar un elemento a la variable para que lo pueda reconocer
    
    int y = 214748664; //El límite de un entero va desde -2.147.486.648 a 2.147.486.647

    //--------------------------------------------------------------------------------------------
    //--------------------------------------------------------------------------------------------
    //caracteres especiales
    // \t (tabular), \b (backspace), \n (nueva linea)
    System.out.println("Hola \t Mundo \n Java"); //Tabular + Salto de linea
    System.out.println("Hola \b Mundo Java"); //Quitó un espacio
    System.out.println("Hola \b Mundo Java"); //Quitó un espacio
    System.out.println("Hola\r Mundo Java"); //Quitó el hola
    System.out.println("Hola \f Mundo Java"); //Salto de linea

    //--------------------------------------------------------------------------------------------
    //--------------------------------------------------------------------------------------------
    //clase STRING
    // Van en comillas dobles

    //--------------------------------------------------------------------------------------------
    //--------------------------------------------------------------------------------------------
    //IDENTIFICADORES
    // 4num = 4; --> Error al comenzar con número
    //z# = 4; --> No valido al tener caracter especial
    // "Edad" = 45; --> No valido por comillas
    // año-nacimiento = 45; --> No valido al usar -
    // public = 45; --> No valido al ser palabra reservada de Java
        
    //Recibiendo datos de usuario --> Similar a INPUT en Python
    Scanner sc = new Scanner(System.in);
    System.out.print("Por favor ingrese su nombre ");
    String nombreEntrada = sc.nextLine();
    System.out.println("Su nombre es " + nombreEntrada);
    
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    System.out.println("Ingrese su nombre ");
    String nombre_br = br.readLine();
    System.out.println("Su nombre es: " + nombre_br);
    }
}

//Este es un comentario de una linea de código --> # en python

/*
Este es un comentario de un bloque de código
--> ''' en python ''''
*/

