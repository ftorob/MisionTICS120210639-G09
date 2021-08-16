package co.edu.misiontic2022.utp.model.vo;

public class Requerimiento_2 {

    //Atributo
    private String fecIni;
    private String nombreCiudad;
    private String constructora;
    private String nombreLider;
    private Integer codigoTipo;
    private Integer estrato;

    public Requerimiento_2(){

    }

    public Requerimiento_2(String fecIni , String nombreCiudad , String constructora, String nombreLider , Integer codigoTipo , Integer estrato){
        this.fecIni = fecIni;
        this.nombreCiudad = nombreCiudad;
        this.constructora = constructora;
        this.nombreLider = nombreLider;
        this.codigoTipo = codigoTipo;
        this.estrato = estrato;
    }

    public Integer getEstrato() {
        return estrato;
    }

    public String getConstructora() {
        return constructora;
    }

    public String getFecIni() {
        return fecIni;
    }

    public void setFecIni(String fecIni) {
        this.fecIni = fecIni;
    }

    public String getNombreCiudad() {
        return nombreCiudad;
    }

    public void setNombreCiudad(String nombreCiudad) {
        this.nombreCiudad = nombreCiudad;
    }

    public String getNombreLider() {
        return nombreLider;
    }

    public void setNombreLider(String nombreLider) {
        this.nombreLider = nombreLider;
    }

    public Integer getCodigoTipo() {
        return codigoTipo;
    }

    public void setCodigoTipo(Integer codigoTipo) {
        this.codigoTipo = codigoTipo;
    }

    public void setConstructora(String constructora) {
        this.constructora = constructora;
    }

    public void setEstrato(Integer estrato) {
        this.estrato = estrato;
    }

}
