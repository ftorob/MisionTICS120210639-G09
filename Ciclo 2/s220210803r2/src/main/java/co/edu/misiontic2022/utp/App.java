package co.edu.misiontic2022.utp;

//Esta clase es para las pruebas, no se debe subir como parte de la solución
public class App 
{
    public static void main( String[] args )
    {
        
        ProductosAlimentarios listaProductosAlimentarios1[] = new ProductosAlimentarios [5];
        listaProductosAlimentarios1[0] = new ProductosAlimentarios(); //Es el llamado de un constructor usando el operador new para crear un objeto
        listaProductosAlimentarios1[1] = new Bebidas(200.0, 10, 'N');
        listaProductosAlimentarios1[2] = new Refrigerados(140.0, 20);
        listaProductosAlimentarios1[3] = new Bebidas(120.0, 10, 'I');
        listaProductosAlimentarios1[4] = new Refrigerados(110.0,7);

        PrecioTotal solucion1 = new PrecioTotal(listaProductosAlimentarios1);
        solucion1.mostrarTotal();
        System.out.println();
        

        ProductosAlimentarios listaProductosAlimentarios2[] = new ProductosAlimentarios[10];
        listaProductosAlimentarios2[0] = new ProductosAlimentarios();
        listaProductosAlimentarios2[1] = new ProductosAlimentarios(120.0,35,'C');
        listaProductosAlimentarios2[2] = new Bebidas();
        listaProductosAlimentarios2[3] = new Refrigerados();
        listaProductosAlimentarios2[4] = new Bebidas(230.0,70);
        listaProductosAlimentarios2[5] = new Refrigerados(40.2,50,4);
        listaProductosAlimentarios2[6] = new Refrigerados(130.2,150,9);
        listaProductosAlimentarios2[7] = new Bebidas(103.3,77,'N');
        listaProductosAlimentarios2[8] = new Refrigerados(143.2,190,12);
        listaProductosAlimentarios2[9] = new Refrigerados(87.2,450,21);
 
        PrecioTotal solucion2 = new PrecioTotal(listaProductosAlimentarios2);
        solucion2.mostrarTotal();
        System.out.println();
    }
}

/* El siguiente código se envío a IMASTER

public class PrecioTotal {
    //Atributos serían las mismas variables a definir usando WRAPPER y en letra minúscula
    private Double tProductosAlimentarios;
    private Double tBebidas;
    private Double tRefrigerados;
    
    private ProductosAlimentarios listaProductosAlimentarios[];

    //Constructores - son métodos especiales que permiten la creación de objetos de la clase
    //El nombre de los constructores debe ser igual al nombre de la clase y no retornan ningún valor
    //El constructor por defecto es aquel que se define sin parámetros. Sino defino uno, el sistema lo crea automático
    public PrecioTotal(){
        this.tProductosAlimentarios = 0.0;
        this.tBebidas = 0.0;
        this.tRefrigerados = 0.0;
    }

    //Función de los que vamos hacer
    public PrecioTotal(ProductosAlimentarios listaProductosAlimentarios[]){
        this.tProductosAlimentarios = 0.0;
        this.tBebidas = 0.0;
        this.tRefrigerados = 0.0;

        this.listaProductosAlimentarios = listaProductosAlimentarios;
    }

    //Método mostrar total - son acciones y empiezan con minúscula - los parámetros están entre ()
    public void mostrarTotal(){
        //Código calculo total
        for(ProductosAlimentarios el : listaProductosAlimentarios){
            if (el instanceof ProductosAlimentarios){
                tProductosAlimentarios = tProductosAlimentarios + el.calcularPrecio();
            }
            if (el instanceof Bebidas){
                tBebidas += el.calcularPrecio();
            }
            if (el instanceof Refrigerados){
                tRefrigerados = tRefrigerados + el.calcularPrecio();
            }
        }
        
        System.out.println("El precio total de los Productos Alimentarios es de " + tProductosAlimentarios);
        System.out.println("La suma del precio de las Bebidas es de " + tBebidas);
        System.out.println("La suma del precio de los Refrigerados es de " + tRefrigerados);
    }
}

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

    /*
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
*/