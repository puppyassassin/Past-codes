package com.pokemon.game;

public class Skill {
    private String name;
    private int power;
    private int powerPoints;
    private String type;

    public Skill(String name, int power, int powerPoints, String type) {
        this.name = name;
        this.power = power;
        this.powerPoints = powerPoints;
        this.type = type;
    }

    public String getName() {
        return name;
    }

    public int getPower() {
        return power;
    }

    public int getpowerPoints() {
        return powerPoints;
    }

    public String getType() {
        return type;
    }
}
