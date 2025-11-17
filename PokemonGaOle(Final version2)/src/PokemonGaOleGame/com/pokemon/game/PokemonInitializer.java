package com.pokemon.game;

import java.util.ArrayList;
import java.util.List;

public class PokemonInitializer {
    public static void main(String[] args) {
        List<Pokemon> availablePokemons = new ArrayList<>();

        availablePokemons.add(new Pokemon(
            "Pikachu", 100, "Electric",
            new Skill[] {
                new Skill("Thunderbolt", 30, 15, "Electric"),
                new Skill("Quick Attack", 20, 20, "Normal"),
                new Skill("Iron Tail", 25, 10, "Steel")
            }
        ));
        availablePokemons.add(new Pokemon(
            "Charmander", 100, "Fire",
            new Skill[] {
                new Skill("Flamethrower", 30, 15, "Fire"),
                new Skill("Scratch", 15, 20, "Normal"),
                new Skill("Ember", 20, 25, "Fire")
            }
        ));
        availablePokemons.add(new Pokemon(
            "Squirtle", 100, "Water",
            new Skill[] {
                new Skill("Water Gun", 30, 15, "Water"),
                new Skill("Tackle", 15, 20, "Normal"),
                new Skill("Bubble", 20, 25, "Water")
            }
        ));
        availablePokemons.add(new Pokemon(
            "Bulbasaur", 100, "Grass",
            new Skill[] {
                new Skill("Vine Whip", 30, 15, "Grass"),
                new Skill("Tackle", 15, 20, "Normal"),
                new Skill("Razor Leaf", 20, 25, "Grass")
            }
        ));
        availablePokemons.add(new Pokemon(
            "Jigglypuff", 100, "Fairy",
            new Skill[] {
                new Skill("Sing", 20, 20, "Fairy"),
                new Skill("Pound", 15, 25, "Normal"),
                new Skill("Body Slam", 25, 10, "Normal")
            }
        ));
        availablePokemons.add(new Pokemon(
            "Meowth", 100, "Normal",
            new Skill[] {
                new Skill("Scratch", 15, 20, "Normal"),
                new Skill("Bite", 20, 15, "Dark"),
                new Skill("Pay Day", 25, 10, "Normal")
            }
        ));
        availablePokemons.add(new Pokemon(
            "Pidgey", 100, "Flying",
            new Skill[] {
                new Skill("Gust", 20, 15, "Flying"),
                new Skill("Tackle", 15, 20, "Normal"),
                new Skill("Wing Attack", 25, 10, "Flying")
            }
        ));
        availablePokemons.add(new Pokemon(
            "Eevee", 100, "Normal",
            new Skill[] {
                new Skill("Quick Attack", 20, 15, "Normal"),
                new Skill("Tackle", 15, 20, "Normal"),
                new Skill("Bite", 25, 10, "Dark")
            }
        ));
        availablePokemons.add(new Pokemon(
            "Vulpix", 100, "Fire",
            new Skill[] {
                new Skill("Flame Burst", 25, 15, "Fire"),
                new Skill("Quick Attack", 15, 20, "Normal"),
                new Skill("Flame Wheel", 20, 10, "Fire")
            }
        ));
        availablePokemons.add(new Pokemon(
            "Snorlax", 200, "Normal",
            new Skill[] {
                new Skill("Body Slam", 40, 10, "Normal"),
                new Skill("Lick", 25, 15, "Ghost"),
                new Skill("Headbutt", 35, 10, "Normal")
            }
        ));
        availablePokemons.add(new Pokemon(
            "Gengar", 100, "Ghost",
            new Skill[] {
                new Skill("Shadow Ball", 30, 15, "Ghost"),
                new Skill("Lick", 20, 20, "Ghost"),
                new Skill("Dark Pulse", 25, 10, "Dark")
            }
        ));
        availablePokemons.add(new Pokemon(
            "Onix", 150, "Rock",
            new Skill[] {
                new Skill("Rock Throw", 30, 15, "Rock"),
                new Skill("Tackle", 15, 20, "Normal"),
                new Skill("Earthquake", 40, 10, "Ground")
            }
        ));
        availablePokemons.add(new Pokemon(
            "Lapras", 150, "Water",
            new Skill[] {
                new Skill("Ice Beam", 35, 15, "Ice"),
                new Skill("Water Gun", 20, 20, "Water"),
                new Skill("Body Slam", 30, 10, "Normal")
            }
        ));
        availablePokemons.add(new Pokemon(
            "Magikarp", 50, "Water",
            new Skill[] {
                new Skill("Splash", 5, 30, "Water"),
                new Skill("Tackle", 10, 20, "Normal"),
                new Skill("Flail", 15, 15, "Water")
            }
        ));
        availablePokemons.add(new Pokemon(
            "Gyarados", 200, "Water",
            new Skill[] {
                new Skill("Hydro Pump", 40, 10, "Water"),
                new Skill("Bite", 25, 20, "Dark"),
                new Skill("Dragon Rage", 35, 15, "Dragon")
            }
        ));
        availablePokemons.add(new Pokemon(
            "Jolteon", 100, "Electric",
            new Skill[] {
                new Skill("Thunder Shock", 25, 20, "Electric"),
                new Skill("Quick Attack", 20, 15, "Normal"),
                new Skill("Thunder", 35, 10, "Electric")
            }
        ));
        availablePokemons.add(new Pokemon(
            "Flareon", 100, "Fire",
            new Skill[] {
                new Skill("Flame Thrower", 30, 15, "Fire"),
                new Skill("Bite", 20, 15, "Dark"),
                new Skill("Fire Spin", 25, 10, "Fire")
            }
        ));
        availablePokemons.add(new Pokemon(
            "Vaporeon", 100, "Water",
            new Skill[] {
                new Skill("Water Gun", 25, 20, "Water"),
                new Skill("Quick Attack", 20, 15, "Normal"),
                new Skill("Hydro Pump", 30, 10, "Water")
            }
        ));
        availablePokemons.add(new Pokemon(
            "Dragonite", 200, "Dragon",
            new Skill[] {
                new Skill("Dragon Claw", 35, 15, "Dragon"),
                new Skill("Wing Attack", 30, 20, "Flying"),
                new Skill("Hyper Beam", 40, 10, "Normal")
            }
        ));
        availablePokemons.add(new Pokemon(
            "Mewtwo", 250, "Psychic",
            new Skill[] {
                new Skill("Psystrike", 50, 10, "Psychic"),
                new Skill("Shadow Ball", 40, 15, "Ghost"),
                new Skill("Aura Sphere", 45, 10, "Fighting")
            }
        ));

        // Print the Pokémon list to verify
        for (Pokemon pokemon : availablePokemons) {
            System.out.println(pokemon.getName() + " with skills:");
            for (Skill skill : pokemon.getSkills()) {
                System.out.println(" - " + skill.getName() + " (Power: " + skill.getPower() + ", PP: " + skill.getpowerPoints() + ")");
            }
        }
    }
}
