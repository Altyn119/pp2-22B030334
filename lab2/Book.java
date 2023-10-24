package lab2;

public class Book extends LibraryItem {
	private String nameOfTheBook;
	
	public Book(String title, String autor, int publicationYear, String nameOfTheBook) {
		super(title, autor, publicationYear);
		this.nameOfTheBook = nameOfTheBook;
	}
	public String getNameOfTheBook() {
		return nameOfTheBook;
	}
}
