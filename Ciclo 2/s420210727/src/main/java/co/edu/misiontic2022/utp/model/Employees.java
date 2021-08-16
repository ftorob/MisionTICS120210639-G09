package co.edu.misiontic2022.utp.model;

public class Employees {
    private Integer employee_id;
    private String first_name;
    private String last_name;
    private String email;

    public Employees(){
    }

    public Employees(Integer employee_id, String first_name, String last_name, String email) {
        this.employee_id = employee_id;
        this.first_name = first_name;
        this.last_name = last_name;
        this.email = email;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getLast_name() {
        return last_name;
    }

    public void setLast_name(String last_name) {
        this.last_name = last_name;
    }

    public String getFirst_name() {
        return first_name;
    }

    public void setFirst_name(String first_name) {
        this.first_name = first_name;
    }

    public Integer getEmployee_id() {
        return employee_id;
    }

    public void setEmployee_id(Integer employee_id) {
        this.employee_id = employee_id;
    }

    public String toString(){
        return "(" + this.employee_id + ") " + this.first_name + " " + this.last_name;
    }
}
