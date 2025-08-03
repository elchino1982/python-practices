"""Question: Implement the Template Method pattern using abstract classes.
Create an abstract DataProcessor class with a template method process_data() that defines
the algorithm steps. Implement concrete subclasses CSVProcessor and JSONProcessor.
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
# - What is the Template Method pattern?
# - How do you define a template method that calls abstract methods?
# - What steps might be common to all data processors?
# - How do concrete classes customize specific steps?
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


# Step 1: Create the abstract DataProcessor class
# ===============================================================================

# Explanation:
# The Template Method pattern defines the skeleton of an algorithm in a base class,
# letting subclasses override specific steps without changing the algorithm structure.

from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def process_data(self, source, destination):
        """Template method that defines the data processing algorithm"""
        print(f"Starting data processing from {source} to {destination}")
        
        # Step 1: Load data
        data = self.load_data(source)
        
        # Step 2: Validate data
        if self.validate_data(data):
            # Step 3: Transform data
            transformed_data = self.transform_data(data)
            
            # Step 4: Save data
            self.save_data(transformed_data, destination)
            
            print("Data processing completed successfully")
        else:
            print("Data validation failed")

# What we accomplished in this step:
# - Created the abstract base class with template method
# - Defined the algorithm structure in process_data()


# Step 2: Add abstract methods for customization points
# ===============================================================================

# Explanation:
# Abstract methods define the steps that subclasses must implement.
# These are the customization points in our template method.

from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def process_data(self, source, destination):
        """Template method that defines the data processing algorithm"""
        print(f"Starting data processing from {source} to {destination}")
        
        # Step 1: Load data
        data = self.load_data(source)
        
        # Step 2: Validate data
        if self.validate_data(data):
            # Step 3: Transform data
            transformed_data = self.transform_data(data)
            
            # Step 4: Save data
            self.save_data(transformed_data, destination)
            
            print("Data processing completed successfully")
        else:
            print("Data validation failed")
    
    @abstractmethod
    def load_data(self, source):
        """Load data from source - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def validate_data(self, data):
        """Validate loaded data - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def transform_data(self, data):
        """Transform data - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def save_data(self, data, destination):
        """Save data to destination - must be implemented by subclasses"""
        pass

# What we accomplished in this step:
# - Added abstract methods for each customization point
# - Defined the contract that subclasses must follow


# Step 3: Implement CSVProcessor
# ===============================================================================

# Explanation:
# The CSVProcessor implements all abstract methods with CSV-specific logic.
# It inherits the template method but customizes the individual steps.

from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def process_data(self, source, destination):
        """Template method that defines the data processing algorithm"""
        print(f"Starting data processing from {source} to {destination}")
        
        # Step 1: Load data
        data = self.load_data(source)
        
        # Step 2: Validate data
        if self.validate_data(data):
            # Step 3: Transform data
            transformed_data = self.transform_data(data)
            
            # Step 4: Save data
            self.save_data(transformed_data, destination)
            
            print("Data processing completed successfully")
        else:
            print("Data validation failed")
    
    @abstractmethod
    def load_data(self, source):
        """Load data from source - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def validate_data(self, data):
        """Validate loaded data - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def transform_data(self, data):
        """Transform data - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def save_data(self, data, destination):
        """Save data to destination - must be implemented by subclasses"""
        pass

class CSVProcessor(DataProcessor):
    def load_data(self, source):
        print(f"📄 Loading CSV data from {source}")
        # Simulate CSV loading
        return [
            ["Name", "Age", "City"],
            ["Alice", "25", "New York"],
            ["Bob", "30", "San Francisco"],
            ["Charlie", "35", "Chicago"]
        ]
    
    def validate_data(self, data):
        print("✅ Validating CSV data structure")
        # Check if we have headers and data rows
        if len(data) < 2:
            return False
        # Check if all rows have same number of columns
        header_length = len(data[0])
        return all(len(row) == header_length for row in data)
    
    def transform_data(self, data):
        print("🔄 Transforming CSV data (converting to uppercase)")
        # Convert all text to uppercase except headers
        transformed = [data[0]]  # Keep headers as-is
        for row in data[1:]:
            transformed.append([cell.upper() if isinstance(cell, str) else cell for cell in row])
        return transformed
    
    def save_data(self, data, destination):
        print(f"💾 Saving CSV data to {destination}")
        # Simulate saving CSV
        for row in data:
            print(f"  {','.join(row)}")

# What we accomplished in this step:
# - Implemented CSVProcessor with CSV-specific logic
# - Each method handles CSV format appropriately


# Step 4: Implement JSONProcessor
# ===============================================================================

# Explanation:
# The JSONProcessor shows how the same template method can work with
# completely different data formats and processing logic.

from abc import ABC, abstractmethod
import json

class DataProcessor(ABC):
    def process_data(self, source, destination):
        """Template method that defines the data processing algorithm"""
        print(f"Starting data processing from {source} to {destination}")
        
        # Step 1: Load data
        data = self.load_data(source)
        
        # Step 2: Validate data
        if self.validate_data(data):
            # Step 3: Transform data
            transformed_data = self.transform_data(data)
            
            # Step 4: Save data
            self.save_data(transformed_data, destination)
            
            print("Data processing completed successfully")
        else:
            print("Data validation failed")
    
    @abstractmethod
    def load_data(self, source):
        """Load data from source - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def validate_data(self, data):
        """Validate loaded data - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def transform_data(self, data):
        """Transform data - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def save_data(self, data, destination):
        """Save data to destination - must be implemented by subclasses"""
        pass

class CSVProcessor(DataProcessor):
    def load_data(self, source):
        print(f"📄 Loading CSV data from {source}")
        return [
            ["Name", "Age", "City"],
            ["Alice", "25", "New York"],
            ["Bob", "30", "San Francisco"],
            ["Charlie", "35", "Chicago"]
        ]
    
    def validate_data(self, data):
        print("✅ Validating CSV data structure")
        if len(data) < 2:
            return False
        header_length = len(data[0])
        return all(len(row) == header_length for row in data)
    
    def transform_data(self, data):
        print("🔄 Transforming CSV data (converting to uppercase)")
        transformed = [data[0]]
        for row in data[1:]:
            transformed.append([cell.upper() if isinstance(cell, str) else cell for cell in row])
        return transformed
    
    def save_data(self, data, destination):
        print(f"💾 Saving CSV data to {destination}")
        for row in data:
            print(f"  {','.join(row)}")

class JSONProcessor(DataProcessor):
    def load_data(self, source):
        print(f"📋 Loading JSON data from {source}")
        # Simulate JSON loading
        return {
            "users": [
                {"name": "Alice", "age": 25, "city": "New York"},
                {"name": "Bob", "age": 30, "city": "San Francisco"},
                {"name": "Charlie", "age": 35, "city": "Chicago"}
            ],
            "metadata": {"version": "1.0", "created": "2025-01-01"}
        }
    
    def validate_data(self, data):
        print("✅ Validating JSON data structure")
        # Check if data is a dictionary with users array
        if not isinstance(data, dict) or "users" not in data:
            return False
        # Check if users is a list
        return isinstance(data["users"], list)
    
    def transform_data(self, data):
        print("🔄 Transforming JSON data (adding processed flag)")
        # Add processed timestamp to each user
        transformed_data = data.copy()
        for user in transformed_data["users"]:
            user["processed"] = True
            user["processed_at"] = "2025-01-01T12:00:00Z"
        return transformed_data
    
    def save_data(self, data, destination):
        print(f"💾 Saving JSON data to {destination}")
        # Pretty print the JSON
        print(json.dumps(data, indent=2))

# What we accomplished in this step:
# - Implemented JSONProcessor with JSON-specific logic
# - Showed how different formats can use the same template


# Step 5: Test the Template Method pattern
# ===============================================================================

# Explanation:
# Let's test both processors to see how the template method works
# with different implementations.

from abc import ABC, abstractmethod
import json

class DataProcessor(ABC):
    def process_data(self, source, destination):
        """Template method that defines the data processing algorithm"""
        print(f"Starting data processing from {source} to {destination}")
        
        # Step 1: Load data
        data = self.load_data(source)
        
        # Step 2: Validate data
        if self.validate_data(data):
            # Step 3: Transform data
            transformed_data = self.transform_data(data)
            
            # Step 4: Save data
            self.save_data(transformed_data, destination)
            
            print("Data processing completed successfully")
        else:
            print("Data validation failed")
    
    @abstractmethod
    def load_data(self, source):
        pass
    
    @abstractmethod
    def validate_data(self, data):
        pass
    
    @abstractmethod
    def transform_data(self, data):
        pass
    
    @abstractmethod
    def save_data(self, data, destination):
        pass

class CSVProcessor(DataProcessor):
    def load_data(self, source):
        print(f"📄 Loading CSV data from {source}")
        return [
            ["Name", "Age", "City"],
            ["Alice", "25", "New York"],
            ["Bob", "30", "San Francisco"],
            ["Charlie", "35", "Chicago"]
        ]
    
    def validate_data(self, data):
        print("✅ Validating CSV data structure")
        if len(data) < 2:
            return False
        header_length = len(data[0])
        return all(len(row) == header_length for row in data)
    
    def transform_data(self, data):
        print("🔄 Transforming CSV data (converting to uppercase)")
        transformed = [data[0]]
        for row in data[1:]:
            transformed.append([cell.upper() if isinstance(cell, str) else cell for cell in row])
        return transformed
    
    def save_data(self, data, destination):
        print(f"💾 Saving CSV data to {destination}")
        for row in data:
            print(f"  {','.join(row)}")

class JSONProcessor(DataProcessor):
    def load_data(self, source):
        print(f"📋 Loading JSON data from {source}")
        return {
            "users": [
                {"name": "Alice", "age": 25, "city": "New York"},
                {"name": "Bob", "age": 30, "city": "San Francisco"},
                {"name": "Charlie", "age": 35, "city": "Chicago"}
            ],
            "metadata": {"version": "1.0", "created": "2025-01-01"}
        }
    
    def validate_data(self, data):
        print("✅ Validating JSON data structure")
        if not isinstance(data, dict) or "users" not in data:
            return False
        return isinstance(data["users"], list)
    
    def transform_data(self, data):
        print("🔄 Transforming JSON data (adding processed flag)")
        transformed_data = data.copy()
        for user in transformed_data["users"]:
            user["processed"] = True
            user["processed_at"] = "2025-01-01T12:00:00Z"
        return transformed_data
    
    def save_data(self, data, destination):
        print(f"💾 Saving JSON data to {destination}")
        print(json.dumps(data, indent=2))

# Test the Template Method pattern:
print("=== Testing CSV Processor ===")
csv_processor = CSVProcessor()
csv_processor.process_data("data.csv", "output.csv")

print("\n=== Testing JSON Processor ===")
json_processor = JSONProcessor()
json_processor.process_data("data.json", "output.json")

# Demonstrate polymorphism:
print("\n=== Polymorphic Processing ===")
processors = [CSVProcessor(), JSONProcessor()]
sources = ["employees.csv", "users.json"]
destinations = ["processed_employees.csv", "processed_users.json"]

for processor, source, dest in zip(processors, sources, destinations):
    print(f"\nProcessing with {type(processor).__name__}:")
    processor.process_data(source, dest)

# What we accomplished in this step:
# - Tested both processors with the same template method
# - Demonstrated polymorphism with different processor types
# - Showed how the algorithm structure remains consistent


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Template Method pattern implementation
# - Abstract methods as customization points
# - Algorithm structure preservation with flexible implementation
# - Polymorphism through abstract base classes
# - Code reuse through inheritance and abstraction
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding XMLProcessor or DatabaseProcessor!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================