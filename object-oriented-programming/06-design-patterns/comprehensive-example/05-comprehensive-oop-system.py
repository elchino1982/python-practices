"""Question: Implement a comprehensive OOP system that demonstrates multiple design patterns
working together. Create a simple game engine that uses Observer, Strategy, State, and Factory patterns.
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about what classes and methods you need
# - Start with a simple implementation
# - Test your code step by step
# - Don't worry if it's not perfect - learning is a process!
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
#
# Take your time, experiment, and enjoy the learning process!

# Try to implement your solution here:
# (Write your code below this line)































# HINT SECTION (Only look if you're really stuck!)
#
# Think about:
# - How can multiple design patterns work together in a real system?
# - What would be a good example that uses Observer, Strategy, State, and Factory?
# - How do you design classes that are both cohesive and loosely coupled?
# - What are the benefits of combining different patterns?
#
# Remember: Start simple and build up complexity gradually!


# ===============================================================================
#                           STEP-BY-STEP SOLUTION
# ===============================================================================
#
# CLASSROOM-STYLE WALKTHROUGH
#
# Let's solve this problem step by step, just like in a programming class!
# Each step builds upon the previous one, so you can follow along and understand
# the complete thought process.
#
# ===============================================================================


# Step 1: Define the Observer pattern for game events
# ===============================================================================

# Explanation:
# Let's start with the Observer pattern to handle game events like score changes,
# level completion, and player actions.

class GameEventObserver:
    def update(self, event_type, data):
        raise NotImplementedError("Subclasses must implement update")

class GameEventSubject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self, event_type, data):
        for observer in self._observers:
            observer.update(event_type, data)

# What we accomplished in this step:
# - Created Observer pattern foundation for game events
# - Defined interfaces for observers and subjects


# Step 2: Implement Strategy pattern for different AI behaviors
# ===============================================================================

# Explanation:
# Now let's add the Strategy pattern to handle different AI behaviors
# for game entities.

class AIStrategy:
    def execute(self, entity, game_state):
        raise NotImplementedError("Subclasses must implement execute")

class AggressiveAI(AIStrategy):
    def execute(self, entity, game_state):
        return f"{entity.name} attacks aggressively!"

class DefensiveAI(AIStrategy):
    def execute(self, entity, game_state):
        return f"{entity.name} defends cautiously!"

class RandomAI(AIStrategy):
    def execute(self, entity, game_state):
        import random
        actions = ["moves randomly", "waits", "explores"]
        action = random.choice(actions)
        return f"{entity.name} {action}!"

# What we accomplished in this step:
# - Created Strategy pattern for AI behaviors
# - Implemented different AI strategies (aggressive, defensive, random)


# Step 3: Add State pattern for game entity states
# ===============================================================================

# Explanation:
# Let's implement the State pattern to manage different states that
# game entities can be in (idle, moving, attacking, etc.).

class EntityState:
    def handle_input(self, entity, input_type):
        raise NotImplementedError("Subclasses must implement handle_input")
    
    def update(self, entity):
        raise NotImplementedError("Subclasses must implement update")
    
    def get_state_name(self):
        raise NotImplementedError("Subclasses must implement get_state_name")

class IdleState(EntityState):
    def handle_input(self, entity, input_type):
        if input_type == "move":
            entity.change_state(MovingState())
            return "Started moving"
        elif input_type == "attack":
            entity.change_state(AttackingState())
            return "Started attacking"
        return "Remaining idle"

    def update(self, entity):
        return f"{entity.name} is idle"

    def get_state_name(self):
        return "Idle"

class MovingState(EntityState):
    def handle_input(self, entity, input_type):
        if input_type == "stop":
            entity.change_state(IdleState())
            return "Stopped moving"
        elif input_type == "attack":
            entity.change_state(AttackingState())
            return "Started attacking while moving"
        return "Continuing to move"

    def update(self, entity):
        return f"{entity.name} is moving"

    def get_state_name(self):
        return "Moving"

class AttackingState(EntityState):
    def handle_input(self, entity, input_type):
        if input_type == "stop":
            entity.change_state(IdleState())
            return "Stopped attacking"
        return "Still attacking"

    def update(self, entity):
        # Attack for a limited time, then return to idle
        entity.attack_timer -= 1
        if entity.attack_timer <= 0:
            entity.change_state(IdleState())
            return f"{entity.name} finished attacking"
        return f"{entity.name} is attacking"

    def get_state_name(self):
        return "Attacking"

# What we accomplished in this step:
# - Created State pattern for entity states
# - Implemented different states with transitions and behaviors


# Step 4: Create Factory pattern for game entity creation
# ===============================================================================

# Explanation:
# Now let's implement the Factory pattern to create different types
# of game entities with appropriate configurations.

class GameEntity:
    def __init__(self, name, entity_type):
        self.name = name
        self.entity_type = entity_type
        self.health = 100
        self.attack_power = 10
        self.state = IdleState()
        self.ai_strategy = None
        self.attack_timer = 0

    def change_state(self, new_state):
        self.state = new_state

    def set_ai_strategy(self, strategy):
        self.ai_strategy = strategy

    def handle_input(self, input_type):
        return self.state.handle_input(self, input_type)

    def update(self):
        return self.state.update(self)

    def execute_ai(self, game_state):
        if self.ai_strategy:
            return self.ai_strategy.execute(self, game_state)
        return f"{self.name} has no AI"

    def get_info(self):
        return {
            'name': self.name,
            'type': self.entity_type,
            'health': self.health,
            'state': self.state.get_state_name(),
            'ai': type(self.ai_strategy).__name__ if self.ai_strategy else "None"
        }

class EntityFactory:
    @staticmethod
    def create_player(name):
        player = GameEntity(name, "Player")
        player.health = 150
        player.attack_power = 15
        # Players don't need AI
        return player

    @staticmethod
    def create_enemy(name, difficulty="normal"):
        enemy = GameEntity(name, "Enemy")
        
        if difficulty == "easy":
            enemy.health = 50
            enemy.attack_power = 5
            enemy.set_ai_strategy(DefensiveAI())
        elif difficulty == "normal":
            enemy.health = 75
            enemy.attack_power = 8
            enemy.set_ai_strategy(RandomAI())
        elif difficulty == "hard":
            enemy.health = 100
            enemy.attack_power = 12
            enemy.set_ai_strategy(AggressiveAI())
        
        return enemy

    @staticmethod
    def create_npc(name, role="merchant"):
        npc = GameEntity(name, "NPC")
        npc.health = 80
        npc.attack_power = 0  # NPCs don't attack
        
        if role == "merchant":
            npc.set_ai_strategy(DefensiveAI())
        elif role == "guard":
            npc.set_ai_strategy(AggressiveAI())
        else:
            npc.set_ai_strategy(RandomAI())
        
        return npc

# What we accomplished in this step:
# - Created Factory pattern for entity creation
# - Implemented different entity types with appropriate configurations


# Step 5: Create the main Game class that ties everything together
# ===============================================================================

# Explanation:
# Let's create the main Game class that uses all the patterns together
# and includes observers for game events.

class ScoreObserver(GameEventObserver):
    def __init__(self):
        self.score = 0

    def update(self, event_type, data):
        if event_type == "enemy_defeated":
            self.score += data.get("points", 10)
            print(f"Score updated! Current score: {self.score}")
        elif event_type == "level_complete":
            self.score += data.get("bonus", 100)
            print(f"Level bonus! Current score: {self.score}")

class HealthObserver(GameEventObserver):
    def update(self, event_type, data):
        if event_type == "player_damaged":
            player = data.get("player")
            damage = data.get("damage", 0)
            print(f"Player took {damage} damage! Health: {player.health}")
        elif event_type == "player_healed":
            player = data.get("player")
            healing = data.get("healing", 0)
            print(f"Player healed {healing} points! Health: {player.health}")

class Game(GameEventSubject):
    def __init__(self):
        super().__init__()
        self.entities = []
        self.turn_count = 0
        self.game_state = {"level": 1, "difficulty": "normal"}

    def add_entity(self, entity):
        self.entities.append(entity)
        print(f"Added {entity.name} ({entity.entity_type}) to the game")

    def remove_entity(self, entity):
        if entity in self.entities:
            self.entities.remove(entity)
            print(f"Removed {entity.name} from the game")

    def process_turn(self):
        self.turn_count += 1
        print(f"\n=== Turn {self.turn_count} ===")
        
        for entity in self.entities:
            # Update entity state
            state_message = entity.update()
            print(f"  {state_message}")
            
            # Execute AI if entity has one
            if entity.ai_strategy:
                ai_message = entity.execute_ai(self.game_state)
                print(f"  {ai_message}")

    def player_action(self, player_name, action):
        player = self._find_entity(player_name)
        if player and player.entity_type == "Player":
            if action == "attack":
                player.attack_timer = 3  # Attack for 3 turns
            
            result = player.handle_input(action)
            print(f"{player_name}: {result}")
            
            # Simulate combat if attacking
            if action == "attack":
                self._simulate_combat(player)
        else:
            print(f"Player {player_name} not found")

    def _find_entity(self, name):
        for entity in self.entities:
            if entity.name == name:
                return entity
        return None

    def _simulate_combat(self, attacker):
        # Find an enemy to attack
        enemies = [e for e in self.entities if e.entity_type == "Enemy"]
        if enemies:
            target = enemies[0]  # Attack first enemy
            damage = attacker.attack_power
            target.health -= damage
            
            print(f"  {attacker.name} attacks {target.name} for {damage} damage!")
            
            if target.health <= 0:
                print(f"  {target.name} is defeated!")
                self.remove_entity(target)
                self.notify_observers("enemy_defeated", {"points": 20})

    def get_game_status(self):
        status = {
            "turn": self.turn_count,
            "entities": len(self.entities),
            "players": len([e for e in self.entities if e.entity_type == "Player"]),
            "enemies": len([e for e in self.entities if e.entity_type == "Enemy"]),
            "npcs": len([e for e in self.entities if e.entity_type == "NPC"])
        }
        return status

# What we accomplished in this step:
# - Created main Game class that integrates all patterns
# - Added observers for score and health tracking
# - Implemented turn-based gameplay with combat


# Step 6: Test the complete system
# ===============================================================================

# Explanation:
# Let's test our complete game system that demonstrates all four patterns
# working together.

print("=== Testing Complete OOP Game System ===")

# Create the game and add observers
game = Game()
score_observer = ScoreObserver()
health_observer = HealthObserver()

game.add_observer(score_observer)
game.add_observer(health_observer)

# Create entities using Factory pattern
print("\nCreating game entities:")
player = EntityFactory.create_player("Hero")
enemy1 = EntityFactory.create_enemy("Goblin", "easy")
enemy2 = EntityFactory.create_enemy("Orc", "normal")
enemy3 = EntityFactory.create_enemy("Dragon", "hard")
npc = EntityFactory.create_npc("Shopkeeper", "merchant")

# Add entities to game
game.add_entity(player)
game.add_entity(enemy1)
game.add_entity(enemy2)
game.add_entity(enemy3)
game.add_entity(npc)

# Display initial status
print(f"\nGame Status: {game.get_game_status()}")

print("\nEntity Information:")
for entity in game.entities:
    info = entity.get_info()
    print(f"  {info}")

# Simulate gameplay
print("\n=== Starting Gameplay ===")

# Turn 1: Player starts moving
game.player_action("Hero", "move")
game.process_turn()

# Turn 2: Player attacks
game.player_action("Hero", "attack")
game.process_turn()

# Turn 3: Continue attacking
game.process_turn()

# Turn 4: Player stops
game.player_action("Hero", "stop")
game.process_turn()

# Turn 5: Player attacks again
game.player_action("Hero", "attack")
game.process_turn()

print(f"\nFinal Game Status: {game.get_game_status()}")
print(f"Final Score: {score_observer.score}")

# What we accomplished in this step:
# - Demonstrated all four patterns working together in a cohesive system
# - Observer pattern: Score and health tracking
# - Strategy pattern: Different AI behaviors for entities
# - State pattern: Entity state management (idle, moving, attacking)
# - Factory pattern: Creating different types of entities
# - Showed how patterns can complement each other in real applications


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the comprehensive OOP solution!
#
# Key concepts learned:
# - Integrating multiple design patterns in a single system
# - Observer pattern for event handling and notifications
# - Strategy pattern for interchangeable algorithms (AI behaviors)
# - State pattern for managing object state transitions
# - Factory pattern for object creation with different configurations
# - How patterns work together to create flexible, maintainable code
# - Real-world application of OOP principles in game development
#
# This example demonstrates:
# - Separation of concerns (each pattern handles a specific responsibility)
# - Loose coupling (patterns interact through well-defined interfaces)
# - High cohesion (related functionality is grouped together)
# - Extensibility (easy to add new AI strategies, states, entity types, observers)
# - Maintainability (changes to one pattern don't affect others)
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each pattern is used and how they interact
# 4. Experiment with modifications (add new AI strategies, states, entity types!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================