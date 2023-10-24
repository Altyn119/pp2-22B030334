package lab2;

public class Magazine extends LibraryItem {
	private int costMagazine;
	public Magazine(String title, String autor, int publicationYear, int costMagazine) {
		super(title, autor, publicationYear);
		this.costMagazine = costMagazine;
	}
	public int getCostMagazine() {
		return costMagazine;
	}
}
