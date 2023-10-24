package lab2_c;

public abstract class Piece {
	private Color color;

	public Piece(Color color) {
		this.color = color;
	}
	
	public abstract boolean isLegalMove(Position a, Position b);
}
