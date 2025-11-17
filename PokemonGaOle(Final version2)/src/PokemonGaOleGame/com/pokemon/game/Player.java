package com.pokemon.game;

import java.util.ArrayList;
import java.util.List;

public class Player {
    private String name;
    private List<Pokemon> caughtPokemons;
    private int score;

    public Player(String name) {
        this.name = name;
        this.caughtPokemons = new ArrayList<>();
        this.score = 0;
    }

    public String getName() {
        return name;
    }

    public List<Pokemon> getCaughtPokemons() {
        return caughtPokemons;
    }

    public void catchPokemon(Pokemon pokemon) {
        caughtPokemons.add(pokemon);
    }

    public void addToScore(int points) {
        this.score += points;
    }

    public int getScore() {
        return score;
    }

	public void removePokemon(Pokemon playerPokemon) {
		
	}
}
