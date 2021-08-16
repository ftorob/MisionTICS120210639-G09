package co.edu.misiontic2022.utp;

public class ProductosAlimentarios {
    //Atributos
    private static final char TIPO_ALIMENTO = 'N';
    private static final Double PRECIO_BASE = 80.0;
    private static final Integer PESO_BASE = 5;

    private char tipoAlimento;
    private Double precioBase;
    private Integer peso;

    //Constructores
    public ProductosAlimentarios(){
        this.tipoAlimento = TIPO_ALIMENTO;
        this.precioBase = PRECIO_BASE;
        this.peso = PESO_BASE;
    }

    public ProductosAlimentarios(Double precioBase, Integer peso){
        this.tipoAlimento = TIPO_ALIMENTO;
        this.precioBase = precioBase;
        this.peso = peso;
    }

    public ProductosAlimentarios(Double precioBase, Integer peso, char tipoAlimento){
        this.precioBase = precioBase;
        this.peso = peso;
        comprobarTipoAlimento(tipoAlimento);
    }

    //Método - son acciones y empiezan con minúscula - los parámetros están entre ()
    public void comprobarTipoAlimento(char tipoAlimento){
        //Condicion validar tipo alimento N , C
        if ((tipoAlimento == 'N') || (tipoAlimento == 'C')){
            this.tipoAlimento = tipoAlimento;
        }
        else{
            this.tipoAlimento = TIPO_ALIMENTO;
        }
    }

    //Método - son acciones y empiezan con minúscula - los parámetros están entre ()
    public Double calcularPrecio(){ //---> Void cambiar por Double
        //Código calcular precio final
        Double precioFinal = 0.0;
        Integer vTipoAlimento = 0;
        Integer vPeso = 0;
        
        vTipoAlimento = (tipoAlimento == 'N') ? 40 : 20;
        vPeso = (peso >= 0 && peso <=9) ? 6 : (peso > 9 && peso <= 16) ? 8 : 20;
        precioFinal = precioBase + vTipoAlimento + vPeso;
        return precioFinal;
    }
}

/*
if(tipoAlimento == 'N'){
    vTipoAlimento = 40;
}
else{
    vTipoAliemnto = 20;
}
*/