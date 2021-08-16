package co.edu.utp.misiontic2022.c2;

public class ImpresoraTinta implements Impresora{
    private int velocidad;

    public ImpresoraTinta(int velocidad){
        this.velocidad = velocidad;
    }

    @Override
    public void imprimir(String texto){
        System.out.println("La impresora de tinta imprime: " + texto);
    }

    @Override
    public int getVelocidad(){
        return velocidad;
    }
}