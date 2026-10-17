// DLS26 Fan Website - Java Backend
// Enterprise-grade backend service

import java.util.ArrayList;
import java.util.List;

public class Player {
    private int id;
    private String name;
    private String position;
    private int rating;
    
    public Player(int id, String name, String position, int rating) {
        this.id = id;
        this.name = name;
        this.position = position;
        this.rating = rating;
    }
    
    public String getInfo() {
        return String.format("%s - %s (Rating: %d)", name, position, rating);
    }
    
    // Getters
    public int getId() { return id; }
    public String getName() { return name; }
    public String getPosition() { return position; }
    public int getRating() { return rating; }
}

public class DLS26Manager {
    private List<Player> players;
    
    public DLS26Manager() {
        this.players = new ArrayList<>();
    }
    
    public void addPlayer(Player player) {
        players.add(player);
    }
    
    public List<Player> getAllPlayers() {
        return new ArrayList<>(players);
    }
    
    public static void main(String[] args) {
        DLS26Manager manager = new DLS26Manager();
        manager.addPlayer(new Player(1, "Player 1", "Forward", 95));
        manager.addPlayer(new Player(2, "Player 2", "Midfielder", 88));
        
        for (Player p : manager.getAllPlayers()) {
            System.out.println(p.getInfo());
        }
    }
}
