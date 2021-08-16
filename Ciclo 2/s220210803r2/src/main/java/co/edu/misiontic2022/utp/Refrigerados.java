package co.edu.misiontic2022.utp;

public class Refrigerados extends ProductosAlimentarios {
    //Atributos
    private static final Integer TEMPERATURA = 10;

    private Integer temperatura;

    //Constructores

    public Refrigerados(){
        super();
        this.temperatura = TEMPERATURA;
    }

    public Refrigerados(Double precioBase, Integer peso){
        super(precioBase , peso);
        this.temperatura = TEMPERATURA;
    }

    public Refrigerados(Double precioBase, Integer peso, Integer temperatura){
        super(precioBase, peso);
        this.temperatura = temperatura;
    }

    //Método - son acciones y empiezan con minúscula
    //Condición validar rangos de temperatura no está
    /*
    public void comprobarTemperatura(Integer temperatura){
        //Condición validar lugar de origen N , I
        //Las constantes finales deben ser nombradas con MAYÚSCULA SOSTENIDA
        if(((temperatura < 5) || (temperatura >=5 && temperatura < 10) || (temperatura >=10 && temperatura <= 15) || (temperatura > 15 ))){
            this.temperatura = temperatura;
        }
        else{
            this.temperatura = TEMPERATURA;
        }
    }
    */

    public Double calcularPrecio(){
        //Código calcular precio final
        Double precioFinal = 0.0;
        Integer vTemperatura = 0;

        if(temperatura < 5){
            vTemperatura = 5;
        }
        if(temperatura >= 5 && temperatura < 10){
            vTemperatura = 20;
        }
        if(temperatura >= 10 && temperatura <= 15){
            vTemperatura = 18;
        }
        if(temperatura > 15){
            vTemperatura = 5;
        }
        precioFinal = super.calcularPrecio() + vTemperatura;
        return precioFinal;
    }
}

//Fin de la solución
//vTemperatura = (temperatura >= 5 && temperatura < 10) ? 20 : (temperatura >= 10 && temperatura <= 15) ? 18 : 5;
