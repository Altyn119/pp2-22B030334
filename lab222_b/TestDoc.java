package lab222_b;
import java.util.HashSet;

public class TestDoc {
	public static void main() {
		HashSet<Document> doc = new HashSet<>();
		Document d1 = new Document("OOPSylabys", 100);
		Document d2 = new Document("AlgosSylabys", 200);
		Folder f1 = new Folder("OOPSylabys", 100, 350);
		Folder f2 = new Folder("AlgosSylabys", 200, 54);
		
		doc.add(d1);
		doc.add(d2);
		doc.add(f1);
		doc.add(f2);

		for(Document item : doc) {
			if(item instanceof Folder) {
				Folder folder = (Folder)item;
			}
		}
	}
}
