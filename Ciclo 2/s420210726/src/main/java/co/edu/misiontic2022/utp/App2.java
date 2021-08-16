package co.edu.misiontic2022.utp;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class App2 {
    public static void main( String [] args ){
        try{
            Path archivo = Paths.get("emptyFile.txt");
            if (Files.notExists(archivo)){
                archivo = Files.createFile(Paths.get("emptyFile.txt"));
            }

            var contenido = new String(Files.readAllBytes(Paths.get("emptyFile.txt")),StandardCharsets.UTF_8);
            System.out.println(contenido);

        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}
