package com.pokemon.game;

import java.util.List;

public class Stage {
    private String name;
    private List<Pokemon> stagePokemons;

    public Stage(String name, List<Pokemon> stagePokemons) {
        this.name = name;
        this.stagePokemons = stagePokemons;
    }

    public String getName() {
        return name;
    }

    public List<Pokemon> getStagePokemons() {
        return stagePokemons;
    }
}
