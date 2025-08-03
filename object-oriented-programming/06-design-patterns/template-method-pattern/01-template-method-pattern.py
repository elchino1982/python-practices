"""Question: Define a class TemplateMethod that uses the Template Method pattern
to define the skeleton of an algorithm.
Implement concrete classes that override specific steps of the algorithm.
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
# - What is the Template Method pattern and when is it useful?
# - How do you define a skeleton algorithm in a base class?
# - Which steps should be abstract and which can have default implementations?
# - How do subclasses customize specific steps while keeping the overall structure?
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


# Step 1: Define the abstract TemplateMethod class
# ===============================================================================

# Explanation:
# Let's start by creating the abstract TemplateMethod class. This class defines
# the skeleton of an algorithm with a template method that calls other methods.

class TemplateMethod:
    def execute(self):
        self.step1()
        self.step2()
        self.step3()

# What we accomplished in this step:
# - Created TemplateMethod class with execute method
# - Defined the algorithm skeleton that calls step1, step2, step3


# Step 2: Add abstract step methods
# ===============================================================================

# Explanation:
# Now let's add the abstract step methods that subclasses must implement.
# These methods define the customizable parts of the algorithm.

class TemplateMethod:
    def execute(self):
        self.step1()
        self.step2()
        self.step3()

    def step1(self):
        raise NotImplementedError("Subclasses must implement this method")

    def step2(self):
        raise NotImplementedError("Subclasses must implement this method")

    def step3(self):
        raise NotImplementedError("Subclasses must implement this method")

# What we accomplished in this step:
# - Added abstract step methods that must be implemented by subclasses
# - Used NotImplementedError to enforce implementation


# Step 3: Create concrete implementation classes
# ===============================================================================

# Explanation:
# Now let's create concrete classes that inherit from TemplateMethod and
# implement the abstract step methods with specific behavior.

class TemplateMethod:
    def execute(self):
        self.step1()
        self.step2()
        self.step3()

    def step1(self):
        raise NotImplementedError("Subclasses must implement this method")

    def step2(self):
        raise NotImplementedError("Subclasses must implement this method")

    def step3(self):
        raise NotImplementedError("Subclasses must implement this method")

class ConcreteClassA(TemplateMethod):
    def step1(self):
        print("ConcreteClassA: Step 1")

    def step2(self):
        print("ConcreteClassA: Step 2")

    def step3(self):
        print("ConcreteClassA: Step 3")

class ConcreteClassB(TemplateMethod):
    def step1(self):
        print("ConcreteClassB: Step 1")

    def step2(self):
        print("ConcreteClassB: Step 2")

    def step3(self):
        print("ConcreteClassB: Step 3")

# What we accomplished in this step:
# - Created ConcreteClassA and ConcreteClassB that inherit from TemplateMethod
# - Each class implements the abstract step methods with specific behavior


# Step 4: Test our basic Template Method pattern
# ===============================================================================

# Explanation:
# Let's test our Template Method pattern by creating instances of concrete
# classes and executing their algorithms.

class TemplateMethod:
    def execute(self):
        self.step1()
        self.step2()
        self.step3()

    def step1(self):
        raise NotImplementedError("Subclasses must implement this method")

    def step2(self):
        raise NotImplementedError("Subclasses must implement this method")

    def step3(self):
        raise NotImplementedError("Subclasses must implement this method")

class ConcreteClassA(TemplateMethod):
    def step1(self):
        print("ConcreteClassA: Step 1")

    def step2(self):
        print("ConcreteClassA: Step 2")

    def step3(self):
        print("ConcreteClassA: Step 3")

class ConcreteClassB(TemplateMethod):
    def step1(self):
        print("ConcreteClassB: Step 1")

    def step2(self):
        print("ConcreteClassB: Step 2")

    def step3(self):
        print("ConcreteClassB: Step 3")

# Test our basic Template Method pattern:
print("=== Testing Basic Template Method Pattern ===")

print("Executing ConcreteClassA:")
objA = ConcreteClassA()
objA.execute()

print("\nExecuting ConcreteClassB:")
objB = ConcreteClassB()
objB.execute()

# What we accomplished in this step:
# - Created instances of both concrete classes
# - Executed their algorithms using the template method
# - Verified that each class follows the same algorithm structure but with different implementations


# Step 5: Enhanced Template Method with hooks and default implementations
# ===============================================================================

# Explanation:
# Let's create a more sophisticated example with hook methods (optional overrides)
# and default implementations for some steps.

class DataProcessor:
    def process_data(self):
        """Template method defining the algorithm skeleton"""
        print("=== Starting Data Processing ===")
        
        # Step 1: Load data (must be implemented)
        data = self.load_data()
        
        # Step 2: Validate data (has default implementation)
        if self.validate_data(data):
            print("Data validation passed")
        else:
            print("Data validation failed, stopping process")
            return
        
        # Step 3: Transform data (must be implemented)
        transformed_data = self.transform_data(data)
        
        # Step 4: Optional hook - pre-save processing
        self.before_save_hook(transformed_data)
        
        # Step 5: Save data (must be implemented)
        self.save_data(transformed_data)
        
        # Step 6: Optional hook - post-save processing
        self.after_save_hook(transformed_data)
        
        print("=== Data Processing Complete ===")

    # Abstract methods (must be implemented)
    def load_data(self):
        raise NotImplementedError("Subclasses must implement load_data")

    def transform_data(self, data):
        raise NotImplementedError("Subclasses must implement transform_data")

    def save_data(self, data):
        raise NotImplementedError("Subclasses must implement save_data")

    # Default implementation (can be overridden)
    def validate_data(self, data):
        """Default validation - checks if data is not empty"""
        return data is not None and len(data) > 0

    # Hook methods (optional to override)
    def before_save_hook(self, data):
        """Hook called before saving data"""
        pass

    def after_save_hook(self, data):
        """Hook called after saving data"""
        pass

class CSVProcessor(DataProcessor):
    def __init__(self, filename):
        self.filename = filename

    def load_data(self):
        print(f"Loading CSV data from {self.filename}")
        # Simulate loading CSV data
        return ["row1,data1", "row2,data2", "row3,data3"]

    def transform_data(self, data):
        print("Transforming CSV data to uppercase")
        return [row.upper() for row in data]

    def save_data(self, data):
        print(f"Saving transformed CSV data to output_{self.filename}")
        for row in data:
            print(f"  Saved: {row}")

    def validate_data(self, data):
        """Custom validation for CSV - check for proper format"""
        if not super().validate_data(data):
            return False
        
        # Check if all rows contain commas (CSV format)
        for row in data:
            if ',' not in row:
                print(f"Invalid CSV format in row: {row}")
                return False
        return True

    def before_save_hook(self, data):
        print(f"CSV Hook: About to save {len(data)} rows")

class JSONProcessor(DataProcessor):
    def __init__(self, source):
        self.source = source

    def load_data(self):
        print(f"Loading JSON data from {self.source}")
        # Simulate loading JSON data
        return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

    def transform_data(self, data):
        print("Adding timestamp to JSON data")
        import datetime
        timestamp = datetime.datetime.now().isoformat()
        for item in data:
            item["processed_at"] = timestamp
        return data

    def save_data(self, data):
        print("Saving JSON data to database")
        for item in data:
            print(f"  Inserted: {item}")

    def after_save_hook(self, data):
        print(f"JSON Hook: Successfully processed {len(data)} records")

# Test enhanced Template Method:
print("\n=== Enhanced Template Method with Hooks ===")

print("Processing CSV file:")
csv_processor = CSVProcessor("data.csv")
csv_processor.process_data()

print("\nProcessing JSON data:")
json_processor = JSONProcessor("api_endpoint")
json_processor.process_data()

# What we accomplished in this step:
# - Created realistic data processing example with template method
# - Added hook methods for optional customization
# - Implemented default behavior that can be overridden
# - Demonstrated how template method controls the algorithm flow


# Step 6: Template Method with conditional steps
# ===============================================================================

# Explanation:
# Let's create an example where the template method includes conditional
# steps and more complex algorithm control.

class ReportGenerator:
    def generate_report(self, report_type="standard"):
        """Template method for generating reports"""
        print(f"=== Generating {report_type.upper()} Report ===")
        
        # Step 1: Initialize report
        self.initialize_report()
        
        # Step 2: Collect data
        data = self.collect_data()
        
        # Step 3: Process data
        processed_data = self.process_data(data)
        
        # Step 4: Conditional formatting based on report type
        if report_type == "detailed":
            formatted_data = self.format_detailed(processed_data)
        elif report_type == "summary":
            formatted_data = self.format_summary(processed_data)
        else:
            formatted_data = self.format_standard(processed_data)
        
        # Step 5: Add headers and footers
        final_report = self.add_headers_footers(formatted_data)
        
        # Step 6: Optional step - add charts if supported
        if self.supports_charts():
            final_report = self.add_charts(final_report)
        
        # Step 7: Output report
        self.output_report(final_report)
        
        print("=== Report Generation Complete ===")
        return final_report

    # Abstract methods
    def collect_data(self):
        raise NotImplementedError("Subclasses must implement collect_data")

    def process_data(self, data):
        raise NotImplementedError("Subclasses must implement process_data")

    def output_report(self, report):
        raise NotImplementedError("Subclasses must implement output_report")

    # Default implementations
    def initialize_report(self):
        print("Initializing report generation")

    def format_standard(self, data):
        return f"Standard Report:\n{data}"

    def format_summary(self, data):
        return f"Summary Report:\n{data[:100]}..."

    def format_detailed(self, data):
        return f"Detailed Report:\n{data}\n[Additional details included]"

    def add_headers_footers(self, content):
        header = "--- COMPANY REPORT ---\n"
        footer = "\n--- END OF REPORT ---"
        return header + content + footer

    def supports_charts(self):
        return False  # Default: no chart support

    def add_charts(self, report):
        return report + "\n[Charts would be added here]"

class SalesReport(ReportGenerator):
    def collect_data(self):
        print("Collecting sales data from database")
        return "Sales: Q1=$100K, Q2=$120K, Q3=$110K, Q4=$130K"

    def process_data(self, data):
        print("Calculating sales trends and totals")
        return data + " | Total: $460K | Trend: +15%"

    def output_report(self, report):
        print("Saving sales report to PDF")
        print("Report content:")
        print(report)

    def supports_charts(self):
        return True  # Sales reports support charts

class InventoryReport(ReportGenerator):
    def collect_data(self):
        print("Collecting inventory data from warehouse system")
        return "Inventory: Widget A=50, Widget B=75, Widget C=25"

    def process_data(self, data):
        print("Analyzing stock levels and reorder points")
        return data + " | Low Stock: Widget C | Reorder: Widget A"

    def output_report(self, report):
        print("Sending inventory report via email")
        print("Report content:")
        print(report)

# Test conditional template method:
print("\n=== Template Method with Conditional Steps ===")

sales_report = SalesReport()
inventory_report = InventoryReport()

print("Generating standard sales report:")
sales_report.generate_report("standard")

print("\nGenerating detailed inventory report:")
inventory_report.generate_report("detailed")

print("\nGenerating summary sales report:")
sales_report.generate_report("summary")

# What we accomplished in this step:
# - Created template method with conditional logic
# - Demonstrated different report types using the same algorithm
# - Added optional features based on subclass capabilities
# - Showed how template method can handle complex business logic


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Understanding the Template Method pattern and its benefits
# - Creating algorithm skeletons in base classes
# - Implementing abstract methods that subclasses must override
# - Using hook methods for optional customization
# - Providing default implementations that can be overridden
# - Adding conditional logic within template methods
# - Understanding when to use Template Method vs other patterns
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try creating a game level template!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
