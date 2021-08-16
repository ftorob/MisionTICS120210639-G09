package co.edu.misiontic2022.utp;

import java.io.Serializable;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "Persona")

public class Persona implements Serializable {
    
    @Id
    private String nombre;
    private Integer edad;

    public Persona(){

    }

    public Persona(String nombre, Integer edad){
        this.nombre = nombre;
        this.edad = edad;
    }

    public String getnombre() {
        return nombre;
    }

    public void setnombre(String nombre) {
        this.nombre = nombre;
    }

    public Integer getEdad() {
        return edad;
    }

    public void setEdad(Integer edad) {
        this.edad = edad;
    }

    public String toString(){
        return this.nombre + " - " + this.edad;
    }
}
