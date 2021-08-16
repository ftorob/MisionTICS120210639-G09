package co.edu.misiontic2022.utp;

import java.io.Serializable;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "Estudiante")

public class Estudiante implements Serializable{

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)

    @Column(name = "id") //Llave primaria
    private Integer id;

    @Column(name = "nombres")
    private String nombres;
    @Column(name = "apellidos")
    private String apellidos;
    @Column(name = "telefono")
    private String telefono;

    public Estudiante(){

    }
}
