package com.pokemon.game;

public class Pokeball {
    private String name;
    private double catchRate;

    public Pokeball(String name, double catchRate) {
        this.name = name;
        this.catchRate = catchRate;
    }

    public String getName() {
        return name;
    }

    public double getCatchRate() {
        return catchRate;
    }
}
