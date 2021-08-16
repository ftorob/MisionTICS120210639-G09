package utp.edu.co;

import utp.edu.co.animales.Cat;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Set;
import java.util.Map;

public class App 
{
    public static void main( String[] args )
    {
        Persona persona = new Persona(); //Aquí var no lo reconocia por error de versión entonces se debe ir al archivo POM.XML
        // <maven.compiler.source>1.8</maven.compiler.source> estaba en 1.7 se pasa a 1.8
        // <maven.compiler.target>1.8</maven.compiler.target> estaba en 1.7 se pasa a 1.8

        Cat cat = new Cat();
        cat.sonido();
        
        //LISTAS
        //Se debe imortar la libreria import java.util.List;
        List<Integer> listaManzanas;

        List<Integer> listaEntero = new ArrayList<>();
        listaEntero.add(2);
        listaEntero.add(15);
        listaEntero.add(17);
        listaEntero.add(23);
        listaEntero.indexOf(10);
        System.out.println(listaEntero.indexOf(10));

        for (Integer entero : listaEntero){ //Recorrer la lista MÉTODO A
            System.out.println(entero);
        }

        Iterator<Integer> iterador = listaEntero.iterator(); //Recorrer la lista MÉTODO B
        while (iterador.hasNext()){
            Integer entero = iterador.next();
            System.out.println(entero);
        }

        listaEntero.stream().forEach(System.out::println); //Recorrer la lista MÉTODO C

        for(int i = 0 ; i < listaEntero.size() ; i++){
            System.out.println(listaEntero.get(i));
        }        

        //CONJUNTOS
        //Se debe imortar la libreria import java.util.Set;
        Set<Integer> conjuntoNaranjas;

        Set<Integer> conjuntoEntero = new HashSet<>();
        conjuntoEntero.add(115);
        conjuntoEntero.add(217);
        conjuntoEntero.add(115);

        for(Integer entero : conjuntoEntero){
            System.out.println(entero);
        }

        //MAPAS
        //Se debe imortar la libreria import java.util.Map;
        Map<String , Integer> mapaNotas;



    }
}
