# %% [markdown]
# Import Libaries

# %%
import os # for clearing the terminal
import time # for adding pauses

# %% [markdown]
# Welcome Message

# %%
print("Simple Emissions Calculator Ready!")

# Pause for 2 seconds
time.sleep(2) 

# %% [markdown]
# Defining Variables

# %%
# Dictionary of emission factors in kg CO2 per km
emission_factors = {
    'car': 0.192,      
    'train': 0.041,
    'plane': 0.255
}

# %% [markdown]
# Calculation Function

# %%
def calculate_emissions(mode, distance_km):
    factor = emission_factors.get(mode.lower())
    if factor:
        return round(factor * distance_km, 2)
    else:
        return "\nInvalid transport mode selected."

# %% [markdown]
# Leader Board

# %%
database = []

# %% [markdown]
# Function: Calculating the Emissions

# %%
#Get user input, calculate emissions, and optionally save the result.
def handle_trip_calculation():

    # Get a valid transport mode or exit
    while True:
        mode = input("\nEnter mode of transport (car/train/plane) or 'menu' to go back: ").strip().lower()
        if mode == 'menu':
            return  # Go back to main menu
        if mode in emission_factors:
            break
        else:
            print("\nInvalid transport mode. Please enter car, train, or plane.")

    # Get a valid distance or exit
    while True:
        distance_input = input("\nEnter distance in km or 'menu' to go back: ").strip().lower()
        if distance_input == 'menu':
            return
        try:
            distance = float(distance_input)
            break
        except ValueError:
            print("\nInvalid input. Please enter a number for distance.")

    # Calculate emissions
    factor = emission_factors[mode]
    result = round(factor * distance, 2)
    print(f"\nEstimated CO2 emissions: {result} kg")

    # Ask to save result or return to menu
    save = input("\nDo you want to save this result? (y/n or 'menu' to go back): ").strip().lower()
    if save == 'menu':
        return
    if save == 'y':
        name = input("\nEnter your first name or type 'menu' to cancel saving: ").strip().lower()
        if name.lower() == 'menu':
            return
        database.append({
            "name": name, 
            "emissions": result,
            "mode": mode,
            "distance": distance
        })

        print("\nResult saved!")


    print("\nPress Enter to return to the menu...")
    input()
#

# %% [markdown]
# Function: Print the Leader Board

# %%
#Display the saved leaderboard.
def show_leaderboard():

    clear_screen()

    if not database:
        print("\nNo entries in leaderboard yet.")

    else:
        print("\n--- Leaderboard (Lowest to Highest Total CO2 Emissions) ---")

# Step 1: Aggregate total emissions per player
        totals = {}
        for entry in database:
            name = entry['name']
            emissions = entry['emissions']
            if name in totals:
                totals[name] += emissions
            else:
                totals[name] = emissions

# Step 2: Sort totals by emission values
        sorted_totals = sorted(totals.items(), key=lambda x: x[1])

# Step 3: Print results with capitalization of name
        for i, (name, total_emissions) in enumerate(sorted_totals, start=1):
            print(f"{i}. {name.capitalize()}: {round(total_emissions, 2)} kg CO2")
        

    print("\nPress Enter to return to the menu...")
    input()


# %% [markdown]
# Function: History of Trips

# %%
#Display all entries in the database chronologically with transport details.
def show_history():

    clear_screen()
    if not database:
        print("\nNo history yet. Calculate and save a trip first.")
    
    else:
        print("\n--- Emissions History ---")
        for i, entry in enumerate(database, start=1):
            print(f"{i}. {entry['name']} took a {entry['mode']} trip of {entry['distance']} km "
                  f"-> {entry['emissions']} kg CO2")

    print("\nPress Enter to return to the menu...")
    input()

# %% [markdown]
# Function: Show Players

# %%
#Display the names of all players in the leaderboard.
def show_player_names():
    clear_screen()
    if not database:
        print("\nNo players have been added yet.")
    
    else:
        print("\n--- Player Names (Alphabetical) ---")
        # Use a set to remove duplicates, then sort alphabetically
        unique_names = sorted(set(entry['name'] for entry in database))
        for name in unique_names:
            print(name.capitalize())  # Capitalize only the first letter

    print("\nPress Enter to return to the menu...")
    input()

# %% [markdown]
# Function: Clear Outputs

# %%
#Clear the terminal screen !! Only visible in the terminal. !!
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# %% [markdown]
# Function: Show Menu

# %%
def show_menu():
    """Display menu options and get user's choice."""
    print("\n=== Emissions Calculator Menu ===")
    print("1. Calculate a new trip")
    print("2. Show leaderboard")
    print("3. Show all player names")
    print("4. Show all trip history")
    print("5. Exit")
    return input("Choose an option (1/2/3/4/5): ").strip()

# %% [markdown]
# Main Program

# %%
def main():
    while True:
        # Clear the screen for a fresh start after each loop
        clear_screen() 

        choice = show_menu()

        if choice == '1':
            handle_trip_calculation()

        elif choice == '2':
            show_leaderboard()
                    
        elif choice == '3':
            show_player_names()

        elif choice == '4':
            show_history()
            
        elif choice == '5':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please select a valid option.")

main()


