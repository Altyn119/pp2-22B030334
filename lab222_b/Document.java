package lab222_b;

public class Document {
	public String title;
	public int size;
	
	public Document(String title, int size) {
		this.title = title;
		this.size = size;
	}
	public String getTitle() {
		return title;
	}
	public int size() {
		return size;
	}
	@Override
	public boolean equals(Object o) {
		if(this == o) {
			return true;
		}
		if (o == null) {
			return false;
		}
		if(getClass() != o.getClass()) {
			return false;
		}
		
		Document document = (Document) o;
		return size == document.size && title.equals(document.title);
	}
	
	@Override
	public int hashCode() {
		return title.hashCode() + size; 
	}
	
}
