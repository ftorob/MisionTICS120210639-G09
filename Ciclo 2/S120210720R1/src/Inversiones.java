/**
 * Clase Inversiones...
*/

public class Inversiones { //Solución correcta
    public static void main(String[] args) throws Exception {

      String respuesta = validarInversion(12,2000000,0);
      System.out.println(respuesta);    
    }

    public static String validarInversion (int vTiempo, double vMonto, double vInteres){
        
        double interesSimple = vMonto * vInteres * vTiempo;
        double interesCompuesto = vMonto * (Math.pow((1 + vInteres), vTiempo) - 1);
        
        double validarInversion = interesCompuesto - interesSimple;
        if (validarInversion > 0){
            return ("La diferencia en el total de intereses generados para el proyecto, " +  
            "si escogemos entre evaluarlo a una tasa de interés Compuesto y evaluarlo a una tasa de " +
            "interés Simple, asciende a la cifra de: $" + validarInversion);
        }
        else{
            return ("Faltan datos para calcular la diferencia en el total de intereses generados " + 
            "para el proyecto.");
        }
    }
}        

//--------------------------------------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------------------

/* --> Solución de partida para entender la lógica y luego acomodar
        int vTiempo = 0;
        double vMonto = 2000000;
        double vInteres = 0.05;

        double interesSimple = vMonto * vInteres * vTiempo;
        System.out.println(interesSimple);

        double interesCompuesto = vMonto * (Math.pow((1 + vInteres), vTiempo) - 1);
        System.out.println(interesCompuesto);

        double validarInversion = interesCompuesto - interesSimple;
        System.out.println(validarInversion);

        if (validarInversion > 0){
            System.out.println("La diferencia en el total de intereses generados para el proyecto, " +  
            "si escogemos entre evaluarlo a una tasa de interés Compuesto y evaluarlo a una tasa de " +
            "interés Simple, asciende a la cifra de: $" + validarInversion);
        }

        else{
            System.out.println("Faltan datos para calcular la diferencia en el total de intereses generados " + 
            "para el proyecto");
        }
    }
}
*/

