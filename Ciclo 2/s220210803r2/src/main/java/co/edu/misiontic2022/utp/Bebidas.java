package co.edu.misiontic2022.utp;

public class Bebidas extends ProductosAlimentarios{
    //Atributos
    private static final char LUGAR_ORIGEN = 'N';
    
    private char lugarOrigen;

    //Constructores
    public Bebidas(){
        super();
        this.lugarOrigen = LUGAR_ORIGEN;
    }

    public Bebidas(Double precioBase, Integer peso){
        super(precioBase , peso);
        this.lugarOrigen = LUGAR_ORIGEN;
    }

    public Bebidas(Double precioBase, Integer peso, char lugarOrigen){
        super(precioBase , peso);
        comprobarLugarOrigen(lugarOrigen);
    }

    //Método - son acciones y empiezan con minúscula
    public void comprobarLugarOrigen(char lugarOrigen){
        //Condición validar lugar de origen N , I
        //Las constantes finales deben ser nombradas con MAYÚSCULA SOSTENIDA
        if ((lugarOrigen == 'N') || (lugarOrigen == 'I')){
            this.lugarOrigen = lugarOrigen;
        }
        else{
            this.lugarOrigen = LUGAR_ORIGEN;
        }
    }

    //Método - son acciones y empiezan con minúscula
    public Double calcularPrecio(){ //--> Cambiar void por Double
        //Código calcular precio final
        Double precioFinal = 0.0;
        Integer vLugarOrigen = 0;

        vLugarOrigen = (lugarOrigen == 'N') ? 5 : 15;
        precioFinal = super.calcularPrecio() + vLugarOrigen;
        return precioFinal;
    }
}
