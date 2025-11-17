package com.pokemon.game;

import java.io.*;
import java.util.*;

public class Game {
	private List<ScoreboardEntry> scoreboard;
    private Player player;
    private Random rand;
    private String currentStage;
    static final int MAX_POKEMON = 3; 
    private List<Pokemon> predefinedPokemons;
    private List<Pokeball> availablePokeballs;

    public Game() {
        scoreboard = new ArrayList<>();
        rand = new Random();
        currentStage = null; // Initialize as null to force stage selection
        predefinedPokemons = new ArrayList<>();
        availablePokeballs = new ArrayList<>();
        initializePokemons();
        initializePokeballs();
    }
    
    private void saveScoreboard1(List<ScoreboardEntry>scoreboard) {
    	FileWriter file;
		Formatter output;
		try {
			output = new Formatter(new FileWriter("scoreboard.txt",true));
			output.format("%s, %d\r\n", player.getName(), player.getScore());
			output.close();
		} catch (SecurityException se) {
			System.out.println("You do not have write access.");
			System.exit(1);
		} catch(FileNotFoundException fe) {
			System.out.println("Error Opening/creating file");
			System.exit(1);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			System.out.println("Error");
		}
    }

    private void updateScoreboard() {
        boolean found = false;
        for (ScoreboardEntry entry : scoreboard) {
            if (entry.getPlayerName().equals(player.getName())) {
                entry.setScore(player.getScore());
                found = true;
                break;
            }
        }
        if (!found) {
            scoreboard.add(new ScoreboardEntry(player.getName(), player.getScore()));
        }
        // Sort scoreboard after updating
        scoreboard.sort(Comparator.comparingInt(ScoreboardEntry::getScore).reversed());
        saveScoreboard1(scoreboard); // Save the updated scoreboard to file
    }



    private void initializePokemons() {
        predefinedPokemons.add(new Pokemon(
            "Pikachu", 100, "Electric",
            new Skill[] {
                new Skill("Thunderbolt", 30, 15, "Electric"),
                new Skill("Quick Attack", 20, 20, "Normal"),
                new Skill("Iron Tail", 25, 10, "Steel")
            }
        ));
        predefinedPokemons.add(new Pokemon(
                "Charmander", 100, "Fire",
                new Skill[] {
                    new Skill("Flamethrower", 30, 15, "Fire"),
                    new Skill("Scratch", 15, 20, "Normal"),
                    new Skill("Ember", 20, 25, "Fire")
                }
            ));
            predefinedPokemons.add(new Pokemon(
                "Squirtle", 100, "Water",
                new Skill[] {
                    new Skill("Water Gun", 30, 15, "Water"),
                    new Skill("Tackle", 15, 20, "Normal"),
                    new Skill("Bubble", 20, 25, "Water")
                }
            ));
            predefinedPokemons.add(new Pokemon(
                "Bulbasaur", 100, "Grass",
                new Skill[] {
                    new Skill("Vine Whip", 30, 15, "Grass"),
                    new Skill("Tackle", 15, 20, "Normal"),
                    new Skill("Razor Leaf", 20, 25, "Grass")
                }
            ));
            predefinedPokemons.add(new Pokemon(
                "Jigglypuff", 100, "Fairy",
                new Skill[] {
                    new Skill("Sing", 20, 20, "Fairy"),
                    new Skill("Pound", 15, 25, "Normal"),
                    new Skill("Body Slam", 25, 10, "Normal")
                }
            ));
            predefinedPokemons.add(new Pokemon(
                "Meowth", 100, "Normal",
                new Skill[] {
                    new Skill("Scratch", 15, 20, "Normal"),
                    new Skill("Bite", 20, 15, "Dark"),
                    new Skill("Pay Day", 25, 10, "Normal")
                }
            ));
            predefinedPokemons.add(new Pokemon(
                "Pidgey", 100, "Flying",
                new Skill[] {
                    new Skill("Gust", 20, 15, "Flying"),
                    new Skill("Tackle", 15, 20, "Normal"),
                    new Skill("Wing Attack", 25, 10, "Flying")
                }
            ));
            predefinedPokemons.add(new Pokemon(
                "Eevee", 100, "Normal",
                new Skill[] {
                    new Skill("Quick Attack", 20, 15, "Normal"),
                    new Skill("Tackle", 15, 20, "Normal"),
                    new Skill("Bite", 25, 10, "Dark")
                }
            ));
            predefinedPokemons.add(new Pokemon(
                "Vulpix", 100, "Fire",
                new Skill[] {
                    new Skill("Flame Burst", 25, 15, "Fire"),
                    new Skill("Quick Attack", 15, 20, "Normal"),
                    new Skill("Flame Wheel", 20, 10, "Fire")
                }
            ));
            predefinedPokemons.add(new Pokemon(
                "Snorlax", 200, "Normal",
                new Skill[] {
                    new Skill("Body Slam", 40, 10, "Normal"),
                    new Skill("Lick", 25, 15, "Ghost"),
                    new Skill("Headbutt", 35, 10, "Normal")
                }
            ));
            predefinedPokemons.add(new Pokemon(
                "Gengar", 100, "Ghost",
                new Skill[] {
                    new Skill("Shadow Ball", 30, 15, "Ghost"),
                    new Skill("Lick", 20, 20, "Ghost"),
                    new Skill("Dark Pulse", 25, 10, "Dark")
                }
            ));
            predefinedPokemons.add(new Pokemon(
                "Onix", 150, "Rock",
                new Skill[] {
                    new Skill("Rock Throw", 30, 15, "Rock"),
                    new Skill("Tackle", 15, 20, "Normal"),
                    new Skill("Earthquake", 40, 10, "Ground")
                }
            ));
            predefinedPokemons.add(new Pokemon(
                "Lapras", 150, "Water",
                new Skill[] {
                    new Skill("Ice Beam", 35, 15, "Ice"),
                    new Skill("Water Gun", 20, 20, "Water"),
                    new Skill("Body Slam", 30, 10, "Normal")
                }
            ));
            predefinedPokemons.add(new Pokemon(
                "Magikarp", 50, "Water",
                new Skill[] {
                    new Skill("Splash", 5, 30, "Water"),
                    new Skill("Tackle", 10, 20, "Normal"),
                    new Skill("Flail", 15, 15, "Water")
                }
            ));
            predefinedPokemons.add(new Pokemon(
                "Gyarados", 200, "Water",
                new Skill[] {
                    new Skill("Hydro Pump", 40, 10, "Water"),
                    new Skill("Bite", 25, 20, "Dark"),
                    new Skill("Dragon Rage", 35, 15, "Dragon")
                }
            ));
            predefinedPokemons.add(new Pokemon(
                "Jolteon", 100, "Electric",
                new Skill[] {
                    new Skill("Thunderbolt", 30, 15, "Electric"),
                    new Skill("Quick Attack", 20, 20, "Normal"),
                    new Skill("Thunder Wave", 25, 10, "Electric")
                }
            ));
            predefinedPokemons.add(new Pokemon(
                "Flareon", 100, "Fire",
                new Skill[] {
                    new Skill("Flamethrower", 35, 15, "Fire"),
                    new Skill("Quick Attack", 20, 20, "Normal"),
                    new Skill("Fire Spin", 25, 10, "Fire")
                }
            ));
            predefinedPokemons.add(new Pokemon(
                "Vaporeon", 100, "Water",
                new Skill[] {
                    new Skill("Water Gun", 30, 15, "Water"),
                    new Skill("Quick Attack", 20, 20, "Normal"),
                    new Skill("Hydro Pump", 35, 10, "Water")
                }
            ));
    }

    private void initializePokeballs() {
        availablePokeballs.add(new Pokeball("Standard Poké Ball", 0.5));
        availablePokeballs.add(new Pokeball("Great Ball", 0.7));
        availablePokeballs.add(new Pokeball("Ultra Ball", 0.9));
        availablePokeballs.add(new Pokeball("Master Ball", 1.0));

    }

    public void start(Scanner scanner) {
        System.out.println("Welcome to Pokémon Battle Game!");
        System.out.print("Enter your name: ");
        String playerName = scanner.nextLine();
        player = new Player(playerName);

        boolean play = true;
        while (play) {
            System.out.println("\n1. Catch Pokémon");
            System.out.println("2. Select Stage");
            System.out.println("3. Battle");
            System.out.println("4. View Caught Pokémon");
            System.out.println("5. View Scoreboard");
            System.out.println("6. Exit");
            System.out.print("Choose an option: ");
            int choice = scanner.nextInt();
            scanner.nextLine(); // consume the newline

            switch (choice) {
                case 1:
                    if (currentStage == null) {
                        System.out.println("Select a stage before catching Pokémon.");
                    } else {
                        catchPokemon(scanner);
                    }
                    break;
                case 2:
                    selectStage(scanner);
                    break;
                case 3:
                    if (currentStage == null) {
                        System.out.println("Please select a stage first.");
                    } else {
                        battle(scanner);
                    }
                    break;
                case 4:
                    viewCaughtPokemon();
                    break;
                case 5:
                    viewScoreboard();
                    break;
                case 6:
                    play = false;
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
                    break;
            }
        }

        System.out.println("Thanks for playing!");
    }

    private void catchPokemon(Scanner scanner) {
        // If the player has caught the maximum number of Pokémon, allow catching if a Pokémon was defeated
        if (player.getCaughtPokemons().size() >= MAX_POKEMON) {
            System.out.println("You have caught the maximum number of Pokémon. One of your Pokémon needs to be defeated first.");
            return;
        }

        Pokemon wildPokemon = predefinedPokemons.get(rand.nextInt(predefinedPokemons.size()));
        System.out.println("A wild " + wildPokemon.getName() + " appeared!");

        System.out.println("Choose a Poké Ball:");
        for (int i = 0; i < availablePokeballs.size(); i++) {
            Pokeball pokeball = availablePokeballs.get(i);
            System.out.println((i + 1) + ". " + pokeball.getName() + " (Catch Rate: " + pokeball.getCatchRate() + ")");
        }

        int pokeballChoice = scanner.nextInt() - 1;
        scanner.nextLine(); // consume the newline

        if (pokeballChoice < 0 || pokeballChoice >= availablePokeballs.size()) {
            System.out.println("Invalid Poké Ball choice.");
            return;
        }

        Pokeball chosenPokeball = availablePokeballs.get(pokeballChoice);

        double catchChance = chosenPokeball.getCatchRate();
        if (rand.nextDouble() < catchChance) {
            player.catchPokemon(wildPokemon);
            System.out.println("You caught a " + wildPokemon.getName() + "!");
        } else {
            System.out.println("The Pokémon escaped!");
        }
    }

    private void selectStage(Scanner scanner) {
        System.out.println("Select a stage:");
        System.out.println("1. Forest");
        System.out.println("2. Beach");
        System.out.println("3. Mountain");
        System.out.print("Choose an option: ");
        int stageChoice = scanner.nextInt();
        scanner.nextLine(); // consume the newline

        switch (stageChoice) {
            case 1:
                currentStage = "Forest";
                break;
            case 2:
                currentStage = "Beach";
                break;
            case 3:
                currentStage = "Mountain";
                break;
            default:
                System.out.println("Invalid choice. Stage not set.");
                return;
        }

        System.out.println("Stage selected: " + currentStage);
    }

    private void battle(Scanner scanner) {
        if (player.getCaughtPokemons().isEmpty()) {
            System.out.println("You have no Pokémon to battle with.");
            return;
        }

        System.out.println("Choose your Pokémon:");
        List<Pokemon> playerPokemons = player.getCaughtPokemons();
        for (int i = 0; i < playerPokemons.size(); i++) {
            Pokemon pokemon = playerPokemons.get(i);
            System.out.println((i + 1) + ". " + pokemon.getName() + " (HP: " + pokemon.getHp() + ")");
        }
        
        int pokemonChoice = scanner.nextInt() - 1;
        scanner.nextLine(); // consume the newline

        if (pokemonChoice < 0 || pokemonChoice >= playerPokemons.size()) {
            System.out.println("Invalid Pokémon choice.");
            return;
        }

        Pokemon playerPokemon = playerPokemons.get(pokemonChoice);
        Pokemon opponentPokemon = predefinedPokemons.get(rand.nextInt(predefinedPokemons.size()));

        Battle battle = new Battle();
        boolean playerWon = battle.startBattle(scanner, this, playerPokemon, opponentPokemon);

        // If the player's Pokémon was defeated, remove it from the bag
        if (!playerWon) {
            player.removePokemon(playerPokemon);
        }
    }

    private void viewCaughtPokemon() {
        if (player.getCaughtPokemons().isEmpty()) {
            System.out.println("You have no caught Pokémon.");
            return;
        }

        System.out.println("Caught Pokémon:");
        for (Pokemon pokemon : player.getCaughtPokemons()) {
            System.out.println(pokemon.getName() + " (HP: " + pokemon.getHp() + ")");
        }
    }

    private void viewScoreboard() {
    	loadScoreboard();
        if (scoreboard.isEmpty()) {
            System.out.println("The scoreboard is empty.");
            return;
        } else {
        	System.out.println("Scoreboard:");
        	 if (scoreboard.size()<5) {
         		for(int i=0;i<scoreboard.size();i++) {
             		System.out.println(i+1 +". " + scoreboard.get(i).getScore() + ", " + scoreboard.get(i).getPlayerName());
             	}
         	}else {
         	for(int i=0;i<5;i++) {System.out.println(i+1 +". " + scoreboard.get(i).getScore() + ", " + scoreboard.get(i).getPlayerName());}
         	}
        }

    }

    public void scoreCal(Pokemon pokemon, boolean playerWin, boolean playerLoss) {
        if (playerWin) {
            player.addToScore(10); // Add 10 points for winning
            System.out.println("You won the battle! Score updated.");
        } else if (playerLoss) {
            player.addToScore(-5); // Deduct 5 points for losing
            System.out.println("You lost the battle. Score deducted.");
        }
        
        updateScoreboard();

    }

    private void loadScoreboard() {
    	Scanner input;
    	try {
			input = new Scanner(new File("scoreboard.txt"));
			while(input.hasNext()) {
				String line = input.nextLine();
				String[] data = line.split(",\\s*");
				if (data.length == 2) {
					String player = data[0];
					int total = Integer.parseInt(data[1]);
					scoreboard.add(new ScoreboardEntry(player,total));
					}
			}
		    //using point as determinant to sort
			scoreboard.sort(Comparator.comparingInt(ScoreboardEntry::getScore).reversed());
			
		}catch (FileNotFoundException fe) {
			System.out.println("Error opening file.");
		}
		catch (NoSuchElementException ex) {
			System.out.println("File improperly formed.");
		}
    }

}

