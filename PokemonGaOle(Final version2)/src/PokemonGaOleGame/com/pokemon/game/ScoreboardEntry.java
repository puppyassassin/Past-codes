package com.pokemon.game;

public class ScoreboardEntry {
    private String name;
    private int score;

    public ScoreboardEntry(String name, int score) {
        this.name = name;
        this.score = score;
    }

    public String getName() {
        return name;
    }

    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }

	public String getPlayerName() {
		return name;
	}
}
