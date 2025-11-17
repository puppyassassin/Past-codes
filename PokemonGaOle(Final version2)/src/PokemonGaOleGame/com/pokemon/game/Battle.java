package com.pokemon.game;

import java.util.Random;
import java.util.Scanner;

public class Battle {
    private Random rand;

    public Battle() {
        this.rand = new Random();
    }

    public boolean startBattle(Scanner scanner, Game game, Pokemon playerPokemon, Pokemon opponentPokemon) {
        System.out.println("Battle started between " + playerPokemon.getName() + " and " + opponentPokemon.getName());

        while (playerPokemon.getHp() > 0 && opponentPokemon.getHp() > 0) {
            // Player turn
            System.out.println("Choose a skill:");
            Skill[] playerSkills = playerPokemon.getSkills();
            for (int i = 0; i < playerSkills.length; i++) {
                Skill skill = playerSkills[i];
                System.out.println((i + 1) + ". " + skill.getName() + " (Power: " + skill.getPower() + ")");
            }
            
            int skillChoice = scanner.nextInt() - 1;
            scanner.nextLine(); // consume newline
            
            if (skillChoice < 0 || skillChoice >= playerSkills.length) {
                System.out.println("Invalid skill choice. Try again.");
                continue;
            }
            
            Skill chosenSkill = playerSkills[skillChoice];

            // Calculate damage
            int damage = chosenSkill.getPower();
            opponentPokemon.setHp(opponentPokemon.getHp() - damage);
            System.out.println(playerPokemon.getName() + " used " + chosenSkill.getName() + " on " + opponentPokemon.getName() + "!");
            
            if (opponentPokemon.getHp() <= 0) {
                System.out.println(opponentPokemon.getName() + " has been defeated!");
                game.scoreCal(opponentPokemon, true, false);
                return false; // Battle ended with player win
            }

            // Opponent turn
            Skill opponentSkill = opponentPokemon.getSkills()[rand.nextInt(opponentPokemon.getSkills().length)];
            int opponentDamage = opponentSkill.getPower();
            playerPokemon.setHp(playerPokemon.getHp() - opponentDamage);
            System.out.println(opponentPokemon.getName() + " used " + opponentSkill.getName() + " on " + playerPokemon.getName() + "!");
            
            if (playerPokemon.getHp() <= 0) {
                System.out.println(playerPokemon.getName() + " has been defeated!");
                game.scoreCal(playerPokemon, false, true);
                return true; // Battle ended with player loss
            }
        }
        return false; // In case of unexpected exit
    }
}
