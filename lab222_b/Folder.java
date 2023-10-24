package lab222_b;

public class Folder extends Document{
	private int typeOfFolder;
	public Folder(String title, int size, int typeOfFolder) {
		super(title, size);
		this.typeOfFolder = typeOfFolder;
	}

	@Override
	public boolean equals(Object o) {
		if(this == o) return true;
		if (o == null)return false;
		if(getClass() != o.getClass()) return false;
		 if (!super.equals(o)) return false;
		Folder folder = (Folder) o;
		return typeOfFolder == typeOfFolder;
	}
		@Override
		public int hashCode() {
			int result = super.hashCode();
			result = 31 * result + typeOfFolder;
	        return result;
		}
		
		public void getInfo() {
			System.out.println("Title: " + title);
	        System.out.println("Size: " + size);
	        System.out.println("Type of folder: " + typeOfFolder);
		}
}
