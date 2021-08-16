package co.edu.misiontic2022.utp.model.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import co.edu.misiontic2022.utp.model.vo.Requerimiento_3;
import co.edu.misiontic2022.utp.util.JDBCUtilities;

public class RequerimientoDao_3 {
    public ArrayList<Requerimiento_3> requerimiento3() throws SQLException{
        
        ArrayList<Requerimiento_3> respuesta = new ArrayList<Requerimiento_3>();
        Connection conexion = JDBCUtilities.getConnection();
        
        try {
            String consulta = "SELECT SUBSTR(Lider.Nombre, 1 , 3) || SUBSTR(Lider.Primer_Apellido, 1 , 3) || SUBSTR(Lider.Segundo_Apellido, 1 , 3) as 'Abrev' " +
            "FROM Lider";
            
            PreparedStatement statement = conexion.prepareStatement(consulta);
            ResultSet resultSet = statement.executeQuery();

            while(resultSet.next()){
                Requerimiento_3 requerimiento_3 = new Requerimiento_3(
                    resultSet.getString("Abrev")
                );

                respuesta.add(requerimiento_3);
            }

            resultSet.close();
            statement.close();
            
        } catch (SQLException e) {
            System.err.println("Error en la consulta SQL Requerimiento 3 -> " + e);
        } finally {
            if (conexion != null){
                conexion.close();
            }
        }
        return respuesta;
    }}
