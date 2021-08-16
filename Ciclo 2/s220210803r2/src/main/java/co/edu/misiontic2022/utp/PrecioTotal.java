package co.edu.misiontic2022.utp;

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
