package co.edu.utp.misiontic2022.c2.bookshop.bookshops;

public class Book {
    private String title;
    private String isbn;
    private int year;
    private int id;

    public Book(){

    }

    public Book(int id, String title, String isbn, int year){
        this.id = id;
        this.title = title;
        this.isbn = isbn;
        this.year = year;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String toString() {
        return isbn + " " + title + " (" + year + ")";
    }
}


