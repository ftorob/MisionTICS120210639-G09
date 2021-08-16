package co.edu.misiontic2022.utp.controller;

import java.sql.SQLException;
import java.util.ArrayList;

import co.edu.misiontic2022.utp.model.dao.RequerimientoDao_1;
import co.edu.misiontic2022.utp.model.dao.RequerimientoDao_2;
import co.edu.misiontic2022.utp.model.dao.RequerimientoDao_3;
import co.edu.misiontic2022.utp.model.vo.Requerimiento_1;
import co.edu.misiontic2022.utp.model.vo.Requerimiento_2;
import co.edu.misiontic2022.utp.model.vo.Requerimiento_3;

public class ControllerRequerimientos {
    private final RequerimientoDao_1 requerimientoDao_1 = new RequerimientoDao_1();
    private final RequerimientoDao_2 requerimientoDao_2 = new RequerimientoDao_2();
    private final RequerimientoDao_3 requerimientoDao_3 = new RequerimientoDao_3();

    public ArrayList<Requerimiento_1> consultaRequerimiento_1() throws SQLException{
        return this.requerimientoDao_1.requerimiento1();
    }

    public ArrayList<Requerimiento_2> consultaRequerimiento_2() throws SQLException{
        return this.requerimientoDao_2.requerimiento2();
    }

    public ArrayList<Requerimiento_3> consultaRequerimiento_3() throws SQLException{
        return this.requerimientoDao_3.requerimiento3();
    }
}
