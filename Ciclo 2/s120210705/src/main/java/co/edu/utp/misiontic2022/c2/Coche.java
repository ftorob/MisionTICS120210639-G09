package co.edu.utp.misiontic2022.c2;

import co.edu.utp.misiontic2022.c2.enumeraciones.Color;

public class Coche extends vehiculo{ //SUBCLASE
    
    private Integer numRuedas; //ATRIBUTO

    public Coche(){
        super();
    }

    public Coche(Color color , Integer numSerie , Integer numRuedas){ //CONSTRUCTOR
        super(color , numSerie);
        this.numRuedas = numRuedas;
    }

    public Integer getNumRuedas(){ //MÉTODO 1
        return numRuedas;
    }

    public void setNumRuedas(Integer numRuedas){ //MÉTODO 2
        this.numRuedas = numRuedas;
    }
}
