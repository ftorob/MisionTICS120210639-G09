package co.edu.misiontic2022.utp;

import java.lang.System.Logger;
import java.util.logging.Level;
import java.util.logging.LogManager;

import javax.persistence.Persistence;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        System.out.println( "Inicio...." );

        /* --- Creación base de datos
        Persona persona = new Persona("Isarael Arbona" , 33); //Agregar un nuevo registro a la BD
        
        var emf = Persistence.createEntityManagerFactory("clase12-pu");
        var em = emf.createEntityManager();
        try{
            em.getTransaction().begin();
            em.persist(persona);
            em.getTransaction().commit();
        } catch(Exception e){
            e.printStackTrace();
        } finally{
            em.close();
        }
        */

        disableLogging();
        mostrarFind();
        //removerPersona();
        consultaJPQL();
        consultaApi();
        
    }

    public static void disableLogging(){ //Elimina toda esa secuencia de comandos de la terminal
        LogManager logManager = LogManager.getLogManager();
        java.util.logging.Logger logger = logManager.getLogger("");
        logger.setLevel(Level.SEVERE);
    }


    public static void mostrarFind(){ //Realizar la consulta de un registro
        System.out.println("Persona .......");
        
        var emf = Persistence.createEntityManagerFactory("clase12-pu");
        var em = emf.createEntityManager();

        try{
            var persona = em.find(Persona.class, "Isarael Arbona"); ///Ojo con el nombre ya que se elimino en la otra clase y genera error
            System.out.println(persona.getnombre());
            System.out.println(persona.getEdad());
            System.out.print(persona.getnombre() + " " + persona.getEdad());
        } catch(Exception e){
            e.printStackTrace();
        } finally {
            em.close();
        }
    }

    public static void removerPersona(){ //Eliminar un registro

        var emf = Persistence.createEntityManagerFactory("clase12-pu");
        var em = emf.createEntityManager();

        try{
            var persona = em.find(Persona.class, "Isarael Arbona");
            em.getTransaction().begin();
            em.remove(persona);
            em.getTransaction().commit();
        } catch (Exception e){
            e.printStackTrace();
        } finally {
            em.close();
        }
    }

    public static void consultaJPQL(){ //Realizar un filtro o busqueda tipo SQL
        
        var emf = Persistence.createEntityManagerFactory("clase12-pu");
        var em = emf.createEntityManager();

        try{
            var query = em.createQuery("SELECT p.nombre FROM Persona p WHERE p.nombre LIKE 'M%' "); //Solo traer el nombre
            var personas = query.getResultList();
            personas.forEach(System.out::println);
        } catch (Exception e){
            e.printStackTrace();
        } finally{
            em.close();
        }
    }

    public static void consultaApi(){ //Realizar otro método para consulta tipo SQL
        var emf = Persistence.createEntityManagerFactory("clase12-pu");
        var em = emf.createEntityManager();

        try{
            var cb = em.getCriteriaBuilder(); //Traer nombre y edad
            var cq = cb.createQuery(Persona.class);
            var rootEntry = cq.from(Persona.class);
            var all = cq.select(rootEntry);

            var query = em.createQuery(all);
            var personas = query.getResultList();
            personas.forEach(System.out::println);
        } catch(Exception e){
            e.printStackTrace();
        } finally{
            em.close();
        }
    }
}