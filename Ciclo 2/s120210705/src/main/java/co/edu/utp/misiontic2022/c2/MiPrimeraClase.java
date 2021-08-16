package co.edu.utp.misiontic2022.c2;

public final class MiPrimeraClase { //final es porque no va a tener subclases //CLASE
    private static final double PI = 3.1416; //ATRIBUTO //Constante final en mayúscula sostenida
    private Integer contador = 0; //Se debe usar el envoltorio Integer en lugar de solo int

    public void incrementarContador(){ //VOID no permite incluir un return dentro del bloque porque da error
        contador =+ contador;
        //return contador;
    }

    public Integer getContador(){ //MÉTODO // Get sirve para visualizar datos //si se coloca PRIVATE en APP no se podría acceder al método y genera error
        return contador;
    }

    public void setContador(Integer c){ //Set sirve para modificar datos //MÉTODO
        contador = c;
    }

    private Integer contadora;

    public MiPrimeraClase(){ //CONSTRUCTOR debe tener el mismo nombre de la clase y sirve para crear objetos debe estar vacio
        this.contadora = 5;
    }

    public MiPrimeraClase(int contadora){ //CONSTRUCTOR no es un método pero se pueden hacer métodos dentro
        this.contadora = contadora;
    }

    public Integer getContadora(){
        return this.contadora;
    }

    public void setContadora(int contadora){
        this.contadora = contadora;
    }
}
