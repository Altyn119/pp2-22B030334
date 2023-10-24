package lab2;

public class DVD extends LibraryItem {
	private String typeOfDvd;
	public DVD(String title, String autor, int publicationYear, String typeOfDvd) {
		super(title, autor, publicationYear);
		this.typeOfDvd = typeOfDvd;
	}
	public String getTypeOfDvd() {
		return typeOfDvd;
	}
}
