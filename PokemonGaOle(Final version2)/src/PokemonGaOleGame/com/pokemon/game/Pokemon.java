package com.pokemon.game;

public class Pokemon {
    private String name;
    private int hp;
    private String type;
    private Skill[] skills;

    public Pokemon(String name, int hp, String type, Skill[] skills) {
        this.name = name;
        this.hp = hp;
        this.type = type;
        this.skills = skills;
    }

    public String getName() {
        return name;
    }

    public int getHp() {
        return hp;
    }

    public void setHp(int hp) {
        this.hp = hp;
    }

    public String getType() {
        return type;
    }

    public Skill[] getSkills() {
        return skills;
    }
}
