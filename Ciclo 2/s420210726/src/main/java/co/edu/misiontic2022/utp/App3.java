package co.edu.misiontic2022.utp;

import java.sql.Connection;
import java.sql.DriverManager;

public class App3 {
    String url = "jdbc:sqlite:grupo09.db";

    Connection conn = null;

    try {
        conn = DriverManager.getConnection(url);
    } catch (Exception e) {
        //TODO: handle exception
    }
    
}
