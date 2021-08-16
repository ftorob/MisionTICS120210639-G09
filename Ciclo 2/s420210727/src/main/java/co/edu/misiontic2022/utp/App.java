package co.edu.misiontic2022.utp;
import java.beans.Statement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import co.edu.misiontic2022.utp.model.Employees;
/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        /*
        String url = "jdbc:sqlite:dbgrupo09.db";

        Connection conn = null;

        try {
            conn = DriverManager.getConnection(url);
            File file = new File("dbgrupo09.db");
            if (file.length() == 0){
                var statement = conn.createStatement();
                statement.execute("CREATE TABLE paises(pais_id INTEGER NOT NULL PRIMARY KEY,"
                        + "nombre VARCHAR(50) NOT NULL);");
            }
        } catch (SQLException e) {
            //TODO: handle exception
            System.out.println("Error de conexión : " + e);
        }
        */

        String db = "C://Users/FERNANDO TORO/Documents/MisionTic2022/Ciclo 2/S320210719/hr.db";
        String url = "jdbc:sqlite:" + db;

        Connection conn = null;
        ResultSet rs = null;
        java.sql.Statement stmt = null;

        var listaEmployees = new ArrayList<Employees>();

        try {
            conn = DriverManager.getConnection(url);
            stmt = conn.createStatement();
            var sql = "SELECT employee_id, first_name, last_name, email FROM employees;";
            rs = stmt.executeQuery(sql);
            while(rs.next()){
                var employees = new Employees();

                int id = rs.getInt("employee_id");
                String nombre = rs.getString("first_name");
                String apellido = rs.getString("last_name");
                String email = rs.getString("email");
                
                //System.out.println("Id : " + id + " nombre : " + nombre);

                employees.setEmployee_id(id);
                employees.setFirst_name(nombre);
                employees.setLast_name(apellido);
                employees.setEmail(email);

                listaEmployees.add(employees);

            }

        } catch (SQLException e) {
            //TODO: handle exception
            System.out.println("Error consulta SQL: " + e);
        } finally {
            try {
                if (rs != null){
                    rs.close();
                }
                if (stmt != null){
                    stmt.close();
                }
                if (conn != null){
                    conn.close();
                }
            } catch (SQLException e) {
                //TODO: handle exception
                System.out.println("Conexión close! -> " + e);
            }
        }

        for (Employees emm : listaEmployees){
            System.out.println(emm);
            //System.out.println(emm.getEmail());
        }

        //listaEmployees.forEach(System.out::println); //También imprime lo mismo del FOR anterior
    }
}
