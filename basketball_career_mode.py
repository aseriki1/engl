import random

class Game:
    def __init__(self):
        self.character = {}
        self.career_position = 0
        self.skills = {'Shooting': 50, 'Dribbling': 50, 'Defense': 50, 'Teamwork': 50}
        self.inventory = []
        self.career_path = [
            "You are a high school player with great potential. What's your first move?",
            "You've received scholarship offers from several colleges. Do you choose a prestigious basketball program or stay local?",
            "Congratulations! You've been drafted into the NBA! Do you focus on individual training or team chemistry?",
            "An endorsement deal from a major brand is on the table. Do you accept it or concentrate solely on your game?",
            "You've been selected for the All-Star game. Do you play for fun or showcase your skills to secure a better contract?"
        ]
        self.choices = [
            ["Join an intensive summer training camp", "Rest and enjoy the summer with friends"],
            ["Prestigious basketball program", "Local college with less pressure"],
            ["Intensive individual training", "Team chemistry building activities"],
            ["Accept the lucrative endorsement deal", "Focus purely on improving your game"],
            ["Play casually, enjoy the experience", "Play seriously, aiming for future opportunities"]
        ]
        self.outcomes = [
            ["Your skills improved significantly!", "You missed an opportunity to enhance your skills."],
            ["You gained great exposure and experience!", "You enjoyed a balanced college life."],
            ["Your skills skyrocketed, making you a standout player!", "Your team's synergy improved significantly!"],
            ["You gained massive popularity and wealth!", "Your skills and focus improved tremendously."],
            ["You enjoyed the game and fans loved your play style.", "You caught the attention of major teams and sponsors!"]
        ]
        self.random_events_high_school = [
            "You received an unexpected scholarship offer!",
            "A renowned coach noticed your talent and offered personal training sessions.",
            "You were invited to participate in an international exhibition game!"
        ]
        self.random_events_college = [
            "You were invited to a prestigious basketball camp!",
            "You suffered a minor injury; you'll need time to recover.",
            "You had an off-day during a critical match, affecting your stats.",
        ]
        self.random_events_nba = [
            "You were invited to a special training camp by an NBA legend!",
            "You suffered a minor injury; you'll need time to recover.",
            "You received an endorsement offer from a major sports brand!"
        ]

    def start_game(self):
        print("Welcome to Basketball Career Mode: The Path to Stardom!")
        self.character['name'] = input("Enter your player's name: ")
        self.character['position'] = input("Choose your position (Guard/Forward/Center): ")
        self.career_progression()

    def career_progression(self):
        while self.career_position < len(self.career_path):
            print(self.career_path[self.career_position])
            for i, choice in enumerate(self.choices[self.career_position]):
                print(f"{i + 1}. {choice}")
            
            print("Enter 's' to save the game.")  # Option to save the game
            
            choice = self.get_user_choice_with_save_option()
            if choice == 's':
                self.save_game()
                print("Game saved successfully!")
                continue

            self.handle_choice(choice)
            self.career_position += 1
            self.random_event()

        print("End of your career journey. Thank you for playing!")
        print(f"Final Stats: {self.skills}")
        print(f"Achievements: {', '.join(self.inventory) if self.inventory else 'None'}")

    def get_user_choice_with_save_option(self):
        choice = input("Choose an option (1/2) or 's' to save the game: ").lower()
        if choice == 's':
            return 's'
        try:
            choice = int(choice) - 1
            if choice not in [0, 1]:
                raise ValueError("Invalid choice")
            return choice
        except (ValueError, IndexError):
            print("Invalid input. Please enter 1, 2, or 's' to save the game.")
            return self.get_user_choice_with_save_option()

    def handle_choice(self, choice):
        outcome = self.outcomes[self.career_position][choice]
        print(outcome)
        if "improved" in outcome.lower() or "skyrocketed" in outcome.lower():
            self.improve_skills(choice)
        elif "scholarship" in outcome.lower() or "offer" in outcome.lower():
            if "Scholarship" not in self.inventory:
                self.inventory.append("Scholarship")
        elif "special training" in outcome.lower():
            self.skills['Shooting'] += 10
            self.skills['Dribbling'] += 10
            self.skills['Defense'] += 10
            self.skills['Teamwork'] += 10
        elif "endorsement" in outcome.lower() and "Endorsement Deal" not in self.inventory:
            self.inventory.append("Endorsement Deal")

    def improve_skills(self, choice):
        if choice == 0:  # Focused on intensive training
            self.skills['Shooting'] += random.randint(10, 20)
            self.skills['Dribbling'] += random.randint(10, 20)
            self.skills['Defense'] += random.randint(10, 20)
            self.skills['Teamwork'] += random.randint(10, 20)
        else:  # Focused on teamwork or balance
            self.skills['Shooting'] += random.randint(5, 15)
            self.skills['Dribbling'] += random.randint(5, 15)
            self.skills['Defense'] += random.randint(5, 15)
            self.skills['Teamwork'] += random.randint(5, 15)

        # Additional feedback based on current skill levels
        if self.skills['Defense'] > 80:
            print("Your defense is now top-tier!")
        if self.skills['Shooting'] > 80:
            print("Your shooting is now elite!")

    def random_event(self):
        if random.choice([True, False]):
            if self.career_position == 0:  # High School
                event = random.choice(self.random_events_high_school)
            elif self.career_position == 1:  # College
                event = random.choice(self.random_events_college)
            else:  # NBA
                event = random.choice(self.random_events_nba)
            
            print(event)
            self.handle_random_event(event)

    def handle_random_event(self, event):
        if "scholarship" in event.lower() and "Scholarship" not in self.inventory:
            self.inventory.append("Scholarship")
        elif "injury" in event.lower():
            self.skills['Shooting'] -= random.randint(1, 5)
            self.skills['Dribbling'] -= random.randint(1, 5)
            self.skills['Defense'] -= random.randint(1, 5)
        elif "personal training" in event.lower():
            self.skills['Shooting'] += 10
            self.skills['Dribbling'] += 10
        elif "exhibition game" in event.lower() or "camp" in event.lower() and "Special Training" not in self.inventory:
            self.inventory.append("Special Training")
        elif "off-day" in event.lower():
            self.skills['Shooting'] -= random.randint(1, 5)
        elif "endorsement" in event.lower() and "Endorsement Deal" not in self.inventory:
            self.inventory.append("Endorsement Deal")

    def save_game(self):
        with open('save_game.txt', 'w') as f:
            f.write(f"{self.character['name']}\n")
            f.write(f"{self.character['position']}\n")
            f.write(f"{self.career_position}\n")
            f.write(f"{self.skills['Shooting']},{self.skills['Dribbling']},{self.skills['Defense']},{self.skills['Teamwork']}\n")
            f.write(f"{','.join(self.inventory)}\n")

    def load_game(self):
        try:
            with open('save_game.txt', 'r') as f:
                self.character['name'] = f.readline().strip()
                self.character['position'] = f.readline().strip()
                self.career_position = int(f.readline().strip())
                skills = f.readline().strip().split(',')
                self.skills['Shooting'], self.skills['Dribbling'], self.skills['Defense'], self.skills['Teamwork'] = map(int, skills)
                self.inventory = f.readline().strip().split(',')
        except (FileNotFoundError, ValueError):
            print("No valid saved game found. Starting a new game.")
            self.start_game()

if __name__ == "__main__":
    game = Game()
    action = input("Do you want to (N)ew game or (L)oad game? ").lower()
    if action == 'n':
        game.start_game()
    elif action == 'l':
        game.load_game()
        game.career_progression()
    else:
        print("Invalid choice. Exiting.")

