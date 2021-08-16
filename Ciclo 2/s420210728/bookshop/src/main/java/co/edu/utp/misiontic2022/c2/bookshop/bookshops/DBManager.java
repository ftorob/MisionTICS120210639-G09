package co.edu.utp.misiontic2022.c2.bookshop.bookshops;

import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class DBManager implements AutoCloseable {
    private Connection connection;

    private static final String DATABASE_LOCATION = "BookShop.db";

    public DBManager() throws SQLException {
        connect();
    }

    private void connect() throws SQLException {
        // TODO: program this method
        String url = "jdbc:sqlite:" + DATABASE_LOCATION;
        
        try{
            this.connection = DriverManager.getConnection(url);
            File fileDB = new File(DATABASE_LOCATION);
            if (fileDB.length() == 0){
                var stmt = this.connection.createStatement();
                stmt.execute("CREATE TABLE books(id INTEGER NOT NULL PRIMARY KEY,"
                             + " title VARCHAR(100) NOT NULL, isbn VARCHAR(4) NOT NULL, "
                             + " years INTEGER(4) NOT NULL)");

                
                String sqlDatos = "INSERT INTO books (id,title,isbn,years) VALUES (?, ?, ?, ?)";
                PreparedStatement stmtPre = this.connection.prepareStatement(sqlDatos);

                stmtPre.setInt(1, 1);
                stmtPre.setString(2,"El coronel no tiene quien le escriba");
                stmtPre.setString(3,"0101");
                stmtPre.setInt(4,1976); 

                stmtPre.executeUpdate();  
            }
        } catch(SQLException e){
            System.out.println("Error de conexion : " + e);
        }
    }

    /**
     * Close the connection to the database if it is still open.
     *
     */
    public void close() throws SQLException {
        if (connection != null) {
            connection.close();
        }
        connection = null;
    }

     /**
     * Return the number of units in stock of the given book.
     *
     * @param book The book object.
     * @return The number of units in stock, or 0 if the book does not
     *         exist in the database.
     * @throws SQLException If somthing fails with the DB.
     */
    public int getStock(Book book) throws SQLException {
        return getStock(book.getId());
    }

    /**
     * Return the number of units in stock of the given book.
     *
     * @param bookId The book identifier in the database.
     * @return The number of units in stock, or 0 if the book does not
     *         exist in the database.
     */
    public int getStock(int bookId) throws SQLException {
        // TODO: program this method
        var cantidad = 0;
        connect();
        Connection conn = this.connection;
        PreparedStatement stmt = null;
        ResultSet rs = null;

        try {
            String sql = "SELECT COUNT(id) AS cantidad FROM books WHERE id = ? LIMIT 1";
            stmt = conn.prepareStatement(sql);
            stmt.setInt(1, bookId);

            rs = stmt.executeQuery();

            if(rs.next()){
                cantidad = rs.getInt("cantidad");
            }
        } finally {
            if (rs != null){
                rs.close();
            }
            if (stmt != null){
                stmt.close();
            }
            if (conn != null){
                conn.close();
            }
        }

        return cantidad;

    }

    /**
     * Search book by ISBN.
     *
     * @param isbn The ISBN of the book.
     * @return The Book object, or null if not found.
     * @throws SQLException If somthing fails with the DB.
     */
    public Book searchBook(String isbn) throws SQLException {
        // TODO: program this method
        Book book = null;

        Connection conn = this.connection;
        PreparedStatement stmt = null;
        ResultSet rs = null;

        try {
            String sql = "SELECT id,title,isbn,years FROM books WHERE isbn = ?";
            stmt = conn.prepareStatement(sql);
            stmt.setString(1,isbn);

            rs = stmt.executeQuery();

            if (rs.next()){
                book = new Book(
                    rs.getInt("id"),
                    rs.getString("title"),
                    rs.getString("isbn"),
                    rs.getInt("years")
                );
            }

            rs.close();
            stmt.close();

        } catch (SQLException e) {
            //TODO: handle exception
            System.out.println("Error SQL " + e);
        } finally{
            if (conn != null){
                conn.close();
            }
        }

        return book;
    }

    /**
     * Sell a book.
     *
     * @param book The book.
     * @param units Number of units that are being sold.
     * @return True if the operation succeeds, or false otherwise
     *         (e.g. when the stock of the book is not big enough).
     * @throws SQLException If somthing fails with the DB.
     */
    public boolean sellBook(Book book, int units) throws SQLException {
        return sellBook(book.getId(), units);
    }

    /**
     * Sell a book.
     *
     * @param book The book's identifier.
     * @param units Number of units that are being sold.
     * @return True if the operation succeeds, or false otherwise
     *         (e.g. when the stock of the book is not big enough).
     * @throws SQLException If something fails with the DB.
     */
    public boolean sellBook(int book, int units) throws SQLException {
        // TODO: program this method
        Boolean validarLibro = false;
        var unidades = this.getStock(book);

        if (unidades >= units){
            validarLibro = true;
        } else {
            validarLibro = false;
        }

        return validarLibro;
    }

    /**
     * Return a list with all the books in the database.
     *
     * @return List with all the books.
     * @throws SQLException If something fails with the DB.
     */
    public List<Book> listBooks() throws SQLException {
        var listaBook = new ArrayList<Book>();

        Connection conn = this.connection;
        PreparedStatement stmt = null;
        ResultSet rs = null;

        try {
            String sqlLista = "SELECT id,title,isbn,years FROM books";
            stmt = conn.prepareStatement(sqlLista);
            rs = stmt.executeQuery();

            while(rs.next()){
                var myBook = new Book(
                    rs.getInt("id"),
                    rs.getString("title"),
                    rs.getString("isbn"),
                    rs.getInt("years")
                );
                listaBook.add(myBook);
            }
        } finally{
            if(rs != null){
                rs.close();
            }
            if (stmt != null){
                stmt.close();
            }
            if (conn != null){
                conn.close();
            }
        }
        return listaBook;
    }

    public Book save(String title, String isbn, int year) throws SQLException {
        Book myBook = null;
        var nuevoConsecutivo = consecutivo();
        
        connect();
        Connection conn = this.connection;
        PreparedStatement stmt = null;

        try {
            myBook = new Book(
                nuevoConsecutivo,
                title,
                isbn,
                year
            );

            String sqlCrearLibro = "INSERT INTO books (id,title,isbn,years) VALUES (?,?,?,?)";
            stmt = conn.prepareStatement(sqlCrearLibro);
            stmt.setInt(1, nuevoConsecutivo);
            stmt.setString(2, myBook.getTitle());
            stmt.setString(3,myBook.getIsbn());
            stmt.setInt(4, myBook.getYear());

            stmt.executeUpdate();
        } finally {
            if (stmt != null){
                stmt.close();
            }
            if (conn != null){
                conn.close();
            }
        }

        return myBook;
    } 

    public int consecutivo() throws SQLException{
        var maximo = 1;
        connect();
        Connection conn = this.connection;
        PreparedStatement stmt = null;
        ResultSet rs = null;

        try {
            String sql = "SELECT MAX(id) as mayor FROM books LIMIT 1";
            stmt = conn.prepareStatement(sql);

            rs = stmt.executeQuery();

            if (rs.next()){
                maximo += rs.getInt("mayor");
            }

        } finally {
            if(rs != null){
                rs.close();
            }
            if(stmt != null){
                stmt.close();
            }
            if(conn != null){
                conn.close();
            }
        }

        return maximo;
    }

    public Book update(int id, String title, String isbn, int year) throws SQLException{
        Book myBook = null;

        connect();
        Connection conn = this.connection;
        PreparedStatement stmt = null;

        try {
            myBook = new Book(
                id,
                title,
                isbn,
                year
            );

            String sql = "UPDATE books SET title = ?, isbn = ?, years = ? WHERE id = ?";
            
            stmt = conn.prepareStatement(sql);
            stmt.setString(1, myBook.getTitle());
            stmt.setString(2, myBook.getIsbn());
            stmt.setInt(3, myBook.getYear());
            stmt.setInt(4, myBook.getId());
            
            stmt.executeUpdate();
        } finally{
            if(stmt != null){
                stmt.close();
            }
            if(conn != null){
                conn.close();
            }
        }
        return myBook;
    }

    public String deleteString(int id) throws SQLException{
        String result = "";

        connect();
        Connection conn = this.connection;
        PreparedStatement stmt = null;

        try{
            String sql = "DELETE FROM books WHERE id = ?";
            stmt = conn.prepareStatement(sql);
            stmt.setInt(1, id);

            stmt.executeUpdate();

            result = "Libro eliminado correctamente ";

        } finally{
            if(stmt != null){
                stmt.close();
            }
            if(conn != null){
                conn.close();
            }
        }
        return result;
    }

    public boolean delete(int id) throws SQLException{
        boolean result = false;

        connect();
        Connection conn = this.connection;
        PreparedStatement stmt = null;

        try{
            String sql = "DELETE FROM books WHERE id = ?";
            stmt = conn.prepareStatement(sql);
            stmt.setInt(1, id);

            stmt.executeUpdate();

            result = true;
            
        } finally{
            if(stmt != null){
                stmt.close();
            }
            if(conn != null){
                conn.close();
            }
        }
        return result;
    }

}