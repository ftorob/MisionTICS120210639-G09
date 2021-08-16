package co.edu.utp.misiontic2022.c2;

import co.edu.utp.misiontic2022.c2.enumeraciones.Color;
import co.edu.utp.misiontic2022.c2.enumeraciones.DiaSemana;

/**
 * Se creo un archivo JAVA MAVEN realizando los siguientes pasos:
 * 1) Verificar que java home sea una variable de entorno sino hacerlo
 * 2) Ir a FILE --> PREFERENCES --> SETTINGS --> buscamos "java home" y verificamos que esté la ruta del JDK
 * 2) Sino está entonces se coloca la ruta con doble \\ para que no genere error y reiniciar el VSC
 * 3) CTRL + SHIF + P --> Java: Create Java Project --> Maven --> maven-arquetipe-quickstart --> 1.4 --> Group id (minuscula)
 * 3) --> Id (nombre del archivo) --> Selecciona la ruta para guardar --> Enter --> Y --> Varibles por defecto --> OK
 * --- Hay una opción que es Java: Clean Java languaje server workspace que me reinicia Java en caso de al gún error
 * 
 */
public class App 
{
    public static void main( String[] args ) //main es la clase de partida donde se relacionan las demás
    {
        //System.out.println( "Hello World!" );
        MiPrimeraClase mpc = new MiPrimeraClase(); //se está generando una estancia de MiPrimeraClase //Objeto_1
        System.out.println("Valor del contador: " + mpc.getContadora());

        mpc.setContadora(10);
        System.out.println("Valor del contador: " + mpc.getContadora());

        MiPrimeraClase mpc_1 = new MiPrimeraClase(50); //Objeto_2
        System.out.println("Valor del contador: " + mpc_1.getContadora());
        
        mpc_1.setContadora(666);
        System.out.println("Valor del contador: " + mpc_1.getContadora());

        Coche coche = new Coche(Color.ROJO , 1115 , 4);
        System.out.println("Número de serie: " + coche.getNumSerie());
        System.out.println("El color del cohe es: " + coche.getColor());
        
        ImpresoraTinta impresoraTinta = new ImpresoraTinta(60);
        impresoraTinta.imprimir("Copias");

        System.out.println(DiaSemana.MARTES);

        //var vcoche = new Coche(); -->Desde Java10

        //ARRAYS
        int[] pEntero; //Declaración de array
        pEntero = new int[5]; //Inicialización de array
        System.out.println(pEntero);

        int[] intArray = {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10};
        System.out.println(intArray);

        int[] miArray = new int[2];
        miArray[0] = 15;
        miArray[1] = 30;

        for(int i = 0 ; i < miArray.length ; ++i ){
            System.out.println("Elemento en el indice " + i + " : " + miArray[i]);
        }

        Coche[] cocheArray = new Coche[2];
        cocheArray[0] = new Coche(Color.AZUL , 10 ,50);
        cocheArray[1] = new Coche(Color.ROJO , 3 , 7);

        for(int j = 0 ; j < cocheArray.length ; j++){
            System.out.println("Coche su número de serie es " + cocheArray[j].getNumSerie() + " y tiene "
            + cocheArray[j].getNumRuedas() + " ruedas");
        }

    }

}
