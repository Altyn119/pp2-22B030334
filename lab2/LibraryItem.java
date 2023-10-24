package lab2;

public abstract class LibraryItem {
	public String title;
	public String autor;
	public int publicationYear;
	public LibraryItem(String title, String autor, int publicationYear) {
		this.title = title;
		this.autor = autor;
		this.publicationYear = publicationYear;
	}
	public String getTitle() {
		return title;
	}
	public String getAutor() {
		return autor;
	}
	public int getPublicationYear() {
		return publicationYear;
	}
}
