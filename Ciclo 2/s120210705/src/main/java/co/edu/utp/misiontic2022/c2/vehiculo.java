package co.edu.utp.misiontic2022.c2;

import co.edu.utp.misiontic2022.c2.enumeraciones.Color;

public class vehiculo { //CLASE
    
    private Color color; //ATRIBUTO
    private Integer numSerie; //ATRIBUTO

    public vehiculo(){ //CONSTRUCTOR VACIÓ --> ES UNO POR CLASE
    }

    public vehiculo(Color color , int numSerie){
        this.color = color;
        this.numSerie = numSerie;
    }

    public Color getColor(){
        return color;
    }

    public void setColor(Color color){
        this.color = color;
    }

    public Integer getNumSerie(){ //MÉTODO
        return this.numSerie;
    }
}
