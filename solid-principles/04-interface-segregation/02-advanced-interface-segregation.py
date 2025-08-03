"""Question: Create an interface Worker with methods work and eat.
Implement classes HumanWorker and RobotWorker that adhere to
the Interface Segregation Principle.
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
# - What is the Interface Segregation Principle (ISP)?
# - How does the original Worker interface violate ISP?
# - What happens when RobotWorker is forced to implement eat()?
# - How can you create smaller, more focused interfaces?
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


# Step 1: Identify the ISP violation in the original design
# ===============================================================================

# Explanation:
# Let's examine the original Worker interface that violates ISP by forcing
# all workers to implement both work and eat methods.

from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class HumanWorker(Worker):
    def work(self):
        return "Human is working"

    def eat(self):
        return "Human is eating"

class RobotWorker(Worker):
    def work(self):
        return "Robot is working"

    def eat(self):
        raise NotImplementedError("Robot does not eat")

# What we can observe:
# - The Worker interface forces ALL workers to implement both work and eat
# - HumanWorker can implement both methods naturally
# - RobotWorker violates ISP by being forced to implement eat() method it can't use
# - Clients depending on Worker interface may get unexpected exceptions

print("=== Original Design (ISP Violation) ===")
workers = [HumanWorker(), RobotWorker()]

print("Testing all worker behaviors:")
for i, worker in enumerate(workers, 1):
    worker_type = worker.__class__.__name__
    print(f"\nWorker {i} ({worker_type}):")
    print(f"  Work: {worker.work()}")
    
    try:
        print(f"  Eat: {worker.eat()}")
    except Exception as e:
        print(f"  Eat: ERROR - {e}")

print("\nISP Violation: RobotWorker is forced to implement eat() method it cannot use!")


# Step 2: Design focused interfaces following ISP
# ===============================================================================

# Explanation:
# Let's create smaller, more focused interfaces that follow ISP by
# separating work and eating concerns.

from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

# What we accomplished in this step:
# - Created two focused interfaces, each with a single responsibility
# - Workable: for entities that can work
# - Eatable: for entities that can eat
# - Each interface is cohesive and focused


# Step 3: Implement HumanWorker with both interfaces
# ===============================================================================

# Explanation:
# Now let's implement HumanWorker by inheriting from both focused
# interfaces, since humans can both work and eat.

from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class HumanWorker(Workable, Eatable):
    def work(self):
        return "Human is working"

    def eat(self):
        return "Human is eating"

# What we accomplished in this step:
# - HumanWorker implements both Workable and Eatable interfaces naturally
# - Each method has a clear purpose and implementation
# - No forced implementation of inappropriate methods


# Step 4: Implement RobotWorker with only appropriate interface
# ===============================================================================

# Explanation:
# Let's implement RobotWorker by inheriting only from the Workable interface,
# since robots can work but don't eat.

from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class HumanWorker(Workable, Eatable):
    def work(self):
        return "Human is working"

    def eat(self):
        return "Human is eating"

class RobotWorker(Workable):
    def work(self):
        return "Robot is working"

# What we accomplished in this step:
# - RobotWorker only implements Workable interface
# - No forced implementation of eat() method
# - Follows ISP: clients only depend on methods they actually use


# Step 5: Test our ISP-compliant design
# ===============================================================================

# Explanation:
# Let's test our redesigned interfaces to verify that they follow ISP
# and provide appropriate functionality for different client needs.

from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class HumanWorker(Workable, Eatable):
    def work(self):
        return "Human is working"

    def eat(self):
        return "Human is eating"

class RobotWorker(Workable):
    def work(self):
        return "Robot is working"

# Test our ISP-compliant design:
print("\n=== ISP-Compliant Design ===")

human = HumanWorker()
robot = RobotWorker()

# Test work functionality (both can work)
workable_entities = [human, robot]
print("Testing Workable interface:")
for entity in workable_entities:
    entity_type = entity.__class__.__name__
    print(f"  {entity_type}: {entity.work()}")

# Test eating functionality (only humans can eat)
eatable_entities = [entity for entity in [human, robot] if isinstance(entity, Eatable)]
print(f"\nTesting Eatable interface ({len(eatable_entities)} entities):")
for entity in eatable_entities:
    entity_type = entity.__class__.__name__
    print(f"  {entity_type}: {entity.eat()}")

print("\nISP Success: Each entity only implements interfaces it can actually use!")

# What we accomplished in this step:
# - Verified that all entities can work through Workable interface
# - Demonstrated that only appropriate entities implement Eatable
# - Confirmed that no exceptions are thrown due to inappropriate method calls


# Step 6: Enhanced example with more worker types and advanced capabilities
# ===============================================================================

# Explanation:
# Let's create a more comprehensive example that shows how ISP enables
# flexible workforce management with diverse worker types and capabilities.

from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Rechargeable(ABC):
    @abstractmethod
    def recharge(self):
        pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self):
        pass

class Maintainable(ABC):
    @abstractmethod
    def maintain(self):
        pass

class Learnable(ABC):
    @abstractmethod
    def learn(self, skill):
        pass

# Different types of workers with various capabilities
class HumanWorker(Workable, Eatable, Sleepable, Learnable):
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.energy = 100
        self.skills = set()

    def work(self):
        self.energy -= 20
        return f"Human {self.name} ({self.role}) is working (energy: {self.energy})"

    def eat(self):
        self.energy = min(100, self.energy + 30)
        return f"Human {self.name} is eating (energy: {self.energy})"

    def sleep(self):
        self.energy = 100
        return f"Human {self.name} is sleeping (energy restored to {self.energy})"

    def learn(self, skill):
        self.skills.add(skill)
        return f"Human {self.name} learned {skill} (skills: {len(self.skills)})"

class RobotWorker(Workable, Rechargeable, Maintainable, Learnable):
    def __init__(self, model, version):
        self.model = model
        self.version = version
        self.battery = 100
        self.maintenance_cycles = 0
        self.algorithms = set()

    def work(self):
        self.battery -= 15
        return f"Robot {self.model} v{self.version} is working (battery: {self.battery}%)"

    def recharge(self):
        self.battery = 100
        return f"Robot {self.model} is recharging (battery: {self.battery}%)"

    def maintain(self):
        self.maintenance_cycles += 1
        return f"Robot {self.model} maintenance cycle {self.maintenance_cycles} completed"

    def learn(self, algorithm):
        self.algorithms.add(algorithm)
        return f"Robot {self.model} installed {algorithm} (algorithms: {len(self.algorithms)})"

class AIWorker(Workable, Learnable):
    def __init__(self, name, intelligence_level):
        self.name = name
        self.intelligence_level = intelligence_level
        self.processing_power = 100
        self.knowledge_base = set()

    def work(self):
        self.processing_power -= 10
        return f"AI {self.name} (IQ: {self.intelligence_level}) is processing (power: {self.processing_power}%)"

    def learn(self, knowledge):
        self.knowledge_base.add(knowledge)
        self.intelligence_level += 1
        return f"AI {self.name} acquired {knowledge} (IQ: {self.intelligence_level}, knowledge: {len(self.knowledge_base)})"

class AnimalWorker(Workable, Eatable, Sleepable):
    def __init__(self, species, name):
        self.species = species
        self.name = name
        self.energy = 80

    def work(self):
        self.energy -= 25
        return f"{self.species} {self.name} is working (energy: {self.energy})"

    def eat(self):
        self.energy = min(100, self.energy + 40)
        return f"{self.species} {self.name} is eating (energy: {self.energy})"

    def sleep(self):
        self.energy = min(100, self.energy + 60)
        return f"{self.species} {self.name} is sleeping (energy: {self.energy})"

# Specialized managers that depend only on specific interfaces
class WorkManager:
    def __init__(self):
        self.workers = []

    def add_worker(self, worker):
        if isinstance(worker, Workable):
            self.workers.append(worker)
        else:
            raise TypeError("Worker must implement Workable interface")

    def assign_work_to_all(self):
        """Client code that only depends on Workable interface"""
        results = []
        for worker in self.workers:
            result = worker.work()
            results.append(result)
        return results

    def get_worker_count(self):
        return len(self.workers)

class NutritionManager:
    def provide_meals(self, entities):
        """Client code that only depends on Eatable interface"""
        results = []
        for entity in entities:
            if isinstance(entity, Eatable):
                result = entity.eat()
                results.append(result)
            else:
                results.append(f"{entity.__class__.__name__} doesn't need meals")
        return results

class RestManager:
    def provide_rest_periods(self, entities):
        """Client code that only depends on Sleepable interface"""
        results = []
        for entity in entities:
            if isinstance(entity, Sleepable):
                result = entity.sleep()
                results.append(result)
            else:
                results.append(f"{entity.__class__.__name__} doesn't need rest")
        return results

class TechnicalManager:
    def perform_technical_maintenance(self, entities):
        """Client code that only depends on Rechargeable/Maintainable interfaces"""
        results = []
        for entity in entities:
            if isinstance(entity, Rechargeable):
                result = entity.recharge()
                results.append(result)
            if isinstance(entity, Maintainable):
                result = entity.maintain()
                results.append(result)
            if not isinstance(entity, (Rechargeable, Maintainable)):
                results.append(f"{entity.__class__.__name__} doesn't need technical maintenance")
        return results

class TrainingManager:
    def conduct_training(self, entities, training_content):
        """Client code that only depends on Learnable interface"""
        results = []
        for entity in entities:
            if isinstance(entity, Learnable):
                result = entity.learn(training_content)
                results.append(result)
            else:
                results.append(f"{entity.__class__.__name__} cannot learn")
        return results

class WorkforceManagementSystem:
    def __init__(self):
        self.work_manager = WorkManager()
        self.nutrition_manager = NutritionManager()
        self.rest_manager = RestManager()
        self.technical_manager = TechnicalManager()
        self.training_manager = TrainingManager()

    def add_worker(self, worker):
        self.work_manager.add_worker(worker)

    def run_daily_operations(self):
        """Simulate a full day of workforce operations"""
        all_workers = self.work_manager.workers
        
        print("=== Daily Workforce Operations ===")
        
        print("\n1. Morning Work Assignment:")
        work_results = self.work_manager.assign_work_to_all()
        for result in work_results:
            print(f"   {result}")
        
        print("\n2. Lunch Break:")
        meal_results = self.nutrition_manager.provide_meals(all_workers)
        for result in meal_results:
            print(f"   {result}")
        
        print("\n3. Afternoon Training Session:")
        training_results = self.training_manager.conduct_training(all_workers, "Productivity Enhancement")
        for result in training_results:
            print(f"   {result}")
        
        print("\n4. Technical Maintenance:")
        maintenance_results = self.technical_manager.perform_technical_maintenance(all_workers)
        for result in maintenance_results:
            print(f"   {result}")
        
        print("\n5. Rest Period:")
        rest_results = self.rest_manager.provide_rest_periods(all_workers)
        for result in rest_results:
            print(f"   {result}")

    def get_workforce_statistics(self):
        """Get statistics about workforce capabilities"""
        all_workers = self.work_manager.workers
        stats = {
            'total_workers': len(all_workers),
            'workable': len([w for w in all_workers if isinstance(w, Workable)]),
            'eatable': len([w for w in all_workers if isinstance(w, Eatable)]),
            'sleepable': len([w for w in all_workers if isinstance(w, Sleepable)]),
            'rechargeable': len([w for w in all_workers if isinstance(w, Rechargeable)]),
            'maintainable': len([w for w in all_workers if isinstance(w, Maintainable)]),
            'learnable': len([w for w in all_workers if isinstance(w, Learnable)])
        }
        return stats

# Test enhanced ISP design:
print("\n=== Enhanced ISP Design with Workforce Management ===")

# Create workforce management system
workforce = WorkforceManagementSystem()

# Add diverse workers
workers = [
    HumanWorker("Alice", "Engineer"),
    RobotWorker("R2D2", "2.1"),
    AIWorker("JARVIS", 150),
    AnimalWorker("Horse", "Thunder"),
    HumanWorker("Bob", "Manager"),
    RobotWorker("C3PO", "1.5")
]

for worker in workers:
    workforce.add_worker(worker)

# Run daily operations
workforce.run_daily_operations()

# Display workforce statistics
print("\n=== Workforce Statistics ===")
stats = workforce.get_workforce_statistics()
for capability, count in stats.items():
    print(f"{capability.replace('_', ' ').title()}: {count}")

# Demonstrate ISP benefits
print(f"\n=== Advanced ISP Benefits Demonstrated ===")
print(f"- WorkManager only depends on Workable interface")
print(f"- NutritionManager only depends on Eatable interface")
print(f"- RestManager only depends on Sleepable interface")
print(f"- TechnicalManager only depends on Rechargeable/Maintainable interfaces")
print(f"- TrainingManager only depends on Learnable interface")
print(f"- Each manager is isolated from changes in unrelated interfaces")
print(f"- Workers only implement capabilities they actually possess")
print(f"- System easily accommodates new worker types with different capability combinations")

# What we accomplished in this step:
# - Created diverse worker types with different capability combinations
# - Demonstrated specialized managers that depend only on specific interfaces
# - Showed how ISP enables flexible and realistic workforce management
# - Illustrated that the system scales well with new worker types and capabilities


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the advanced Interface Segregation Principle solution!
#
# Key concepts learned:
# - Advanced application of ISP with capability-based workforce management
# - Creating realistic systems that model diverse entity capabilities
# - Benefits of multiple inheritance with focused interfaces
# - How ISP enables flexible management systems with specialized responsibilities
# - Avoiding forced implementation of inappropriate capabilities
# - Building scalable systems that accommodate diverse worker types
#
# Advanced ISP Benefits demonstrated:
# - Workers only implement capabilities they actually possess
# - Managers depend only on specific capability interfaces
# - System can easily accommodate new worker types with different capabilities
# - Changes to one capability don't affect unrelated managers
# - Natural modeling of real-world constraints and abilities
# - Easy testing and validation of specific capabilities
# - Flexible workforce composition and management
#
# Real-world applications:
# - Human resource management systems with role-specific capabilities
# - Manufacturing systems with diverse machine and worker capabilities
# - Game systems with character classes and abilities
# - Robotics systems with different sensor and actuator capabilities
# - Employee training systems with skill-based learning paths
# - Project management systems with team member specializations
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY capability-based interfaces are more flexible
# 4. Experiment with adding new worker types (ContractorWorker, InternWorker, etc.)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
