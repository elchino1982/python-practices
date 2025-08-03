"""Question: Implement a class Visitor that uses the Visitor pattern to perform
operations on elements of an object structure.
Define elements ElementA and ElementB that accept visitors.
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
# - What is the Visitor pattern and when is it useful?
# - How do you separate operations from the objects they operate on?
# - What is double dispatch and how does it work?
# - How do elements accept visitors and visitors visit elements?
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


# Step 1: Define the abstract Visitor class
# ===============================================================================

# Explanation:
# Let's start by creating the abstract Visitor class. This defines the interface
# for all visitors that can operate on different types of elements.

class Visitor:
    def visit_element_a(self, element):
        raise NotImplementedError("Subclasses must implement this method")

    def visit_element_b(self, element):
        raise NotImplementedError("Subclasses must implement this method")

# What we accomplished in this step:
# - Created abstract Visitor class with visit methods for each element type
# - Used NotImplementedError to enforce implementation in subclasses


# Step 2: Define the abstract Element class
# ===============================================================================

# Explanation:
# Now let's create the abstract Element class. Elements accept visitors
# and delegate the operation to the appropriate visitor method.

class Visitor:
    def visit_element_a(self, element):
        raise NotImplementedError("Subclasses must implement this method")

    def visit_element_b(self, element):
        raise NotImplementedError("Subclasses must implement this method")

class Element:
    def accept(self, visitor):
        raise NotImplementedError("Subclasses must implement this method")

# What we accomplished in this step:
# - Created abstract Element class with accept method
# - Elements will use this method to accept visitors


# Step 3: Create concrete element classes
# ===============================================================================

# Explanation:
# Let's create concrete element classes that implement the accept method.
# Each element calls the appropriate visitor method for its type.

class Visitor:
    def visit_element_a(self, element):
        raise NotImplementedError("Subclasses must implement this method")

    def visit_element_b(self, element):
        raise NotImplementedError("Subclasses must implement this method")

class Element:
    def accept(self, visitor):
        raise NotImplementedError("Subclasses must implement this method")

class ElementA(Element):
    def accept(self, visitor):
        visitor.visit_element_a(self)

class ElementB(Element):
    def accept(self, visitor):
        visitor.visit_element_b(self)

# What we accomplished in this step:
# - Created ElementA and ElementB classes that inherit from Element
# - Each element calls the appropriate visitor method (double dispatch)


# Step 4: Create a concrete visitor
# ===============================================================================

# Explanation:
# Now let's create a concrete visitor that implements specific operations
# for each type of element.

class Visitor:
    def visit_element_a(self, element):
        raise NotImplementedError("Subclasses must implement this method")

    def visit_element_b(self, element):
        raise NotImplementedError("Subclasses must implement this method")

class Element:
    def accept(self, visitor):
        raise NotImplementedError("Subclasses must implement this method")

class ElementA(Element):
    def accept(self, visitor):
        visitor.visit_element_a(self)

class ElementB(Element):
    def accept(self, visitor):
        visitor.visit_element_b(self)

class ConcreteVisitor(Visitor):
    def visit_element_a(self, element):
        print("Visiting ElementA")

    def visit_element_b(self, element):
        print("Visiting ElementB")

# What we accomplished in this step:
# - Created ConcreteVisitor that implements specific operations
# - Each visit method performs different operations based on element type


# Step 5: Test our basic Visitor pattern
# ===============================================================================

# Explanation:
# Let's test our Visitor pattern by creating elements and applying
# a visitor to them.

class Visitor:
    def visit_element_a(self, element):
        raise NotImplementedError("Subclasses must implement this method")

    def visit_element_b(self, element):
        raise NotImplementedError("Subclasses must implement this method")

class Element:
    def accept(self, visitor):
        raise NotImplementedError("Subclasses must implement this method")

class ElementA(Element):
    def accept(self, visitor):
        visitor.visit_element_a(self)

class ElementB(Element):
    def accept(self, visitor):
        visitor.visit_element_b(self)

class ConcreteVisitor(Visitor):
    def visit_element_a(self, element):
        print("Visiting ElementA")

    def visit_element_b(self, element):
        print("Visiting ElementB")

# Test our basic Visitor pattern:
print("=== Testing Basic Visitor Pattern ===")

elements = [ElementA(), ElementB(), ElementA(), ElementB()]
visitor = ConcreteVisitor()

print("Applying visitor to elements:")
for i, element in enumerate(elements):
    print(f"Element {i+1}: ", end="")
    element.accept(visitor)

# What we accomplished in this step:
# - Created a collection of different element types
# - Applied the same visitor to all elements
# - Demonstrated how visitor pattern enables different operations on different types


# Step 6: Enhanced Visitor with multiple operations
# ===============================================================================

# Explanation:
# Let's create a more realistic example with a document structure and
# multiple types of visitors performing different operations.

class DocumentElement:
    def accept(self, visitor):
        raise NotImplementedError("Subclasses must implement this method")

class Paragraph(DocumentElement):
    def __init__(self, text):
        self.text = text

    def accept(self, visitor):
        visitor.visit_paragraph(self)

class Heading(DocumentElement):
    def __init__(self, text, level):
        self.text = text
        self.level = level

    def accept(self, visitor):
        visitor.visit_heading(self)

class Image(DocumentElement):
    def __init__(self, src, alt_text):
        self.src = src
        self.alt_text = alt_text

    def accept(self, visitor):
        visitor.visit_image(self)

class Table(DocumentElement):
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[f"Cell {i},{j}" for j in range(columns)] for i in range(rows)]

    def accept(self, visitor):
        visitor.visit_table(self)

class DocumentVisitor:
    def visit_paragraph(self, paragraph):
        raise NotImplementedError()

    def visit_heading(self, heading):
        raise NotImplementedError()

    def visit_image(self, image):
        raise NotImplementedError()

    def visit_table(self, table):
        raise NotImplementedError()

class HTMLExportVisitor(DocumentVisitor):
    def __init__(self):
        self.html_output = []

    def visit_paragraph(self, paragraph):
        self.html_output.append(f"<p>{paragraph.text}</p>")

    def visit_heading(self, heading):
        self.html_output.append(f"<h{heading.level}>{heading.text}</h{heading.level}>")

    def visit_image(self, image):
        self.html_output.append(f'<img src="{image.src}" alt="{image.alt_text}" />')

    def visit_table(self, table):
        html = "<table>\n"
        for row in table.data:
            html += "  <tr>\n"
            for cell in row:
                html += f"    <td>{cell}</td>\n"
            html += "  </tr>\n"
        html += "</table>"
        self.html_output.append(html)

    def get_html(self):
        return "\n".join(self.html_output)

class WordCountVisitor(DocumentVisitor):
    def __init__(self):
        self.word_count = 0
        self.element_counts = {"paragraphs": 0, "headings": 0, "images": 0, "tables": 0}

    def visit_paragraph(self, paragraph):
        self.word_count += len(paragraph.text.split())
        self.element_counts["paragraphs"] += 1

    def visit_heading(self, heading):
        self.word_count += len(heading.text.split())
        self.element_counts["headings"] += 1

    def visit_image(self, image):
        self.word_count += len(image.alt_text.split())
        self.element_counts["images"] += 1

    def visit_table(self, table):
        for row in table.data:
            for cell in row:
                self.word_count += len(cell.split())
        self.element_counts["tables"] += 1

    def get_statistics(self):
        return {
            "total_words": self.word_count,
            "elements": self.element_counts
        }

class ValidationVisitor(DocumentVisitor):
    def __init__(self):
        self.issues = []

    def visit_paragraph(self, paragraph):
        if len(paragraph.text) < 10:
            self.issues.append("Paragraph too short (less than 10 characters)")
        if not paragraph.text.strip():
            self.issues.append("Empty paragraph found")

    def visit_heading(self, heading):
        if heading.level < 1 or heading.level > 6:
            self.issues.append(f"Invalid heading level: {heading.level}")
        if len(heading.text) > 100:
            self.issues.append("Heading too long (over 100 characters)")

    def visit_image(self, image):
        if not image.src:
            self.issues.append("Image missing source URL")
        if not image.alt_text:
            self.issues.append("Image missing alt text")

    def visit_table(self, table):
        if table.rows == 0 or table.columns == 0:
            self.issues.append("Empty table found")

    def get_issues(self):
        return self.issues

# Test enhanced Visitor pattern:
print("\n=== Enhanced Visitor Pattern with Document Processing ===")

# Create a document structure
document = [
    Heading("Introduction", 1),
    Paragraph("This is the introduction paragraph with some sample text."),
    Image("diagram.png", "System architecture diagram"),
    Heading("Data Analysis", 2),
    Paragraph("Here we analyze the data."),
    Table(3, 2),
    Paragraph("Conclusion text here.")
]

# Apply HTML export visitor
html_visitor = HTMLExportVisitor()
print("Generating HTML:")
for element in document:
    element.accept(html_visitor)

print("HTML Output:")
print(html_visitor.get_html())

# Apply word count visitor
word_count_visitor = WordCountVisitor()
print("\nCounting words:")
for element in document:
    element.accept(word_count_visitor)

stats = word_count_visitor.get_statistics()
print(f"Statistics: {stats}")

# Apply validation visitor
validation_visitor = ValidationVisitor()
print("\nValidating document:")
for element in document:
    element.accept(validation_visitor)

issues = validation_visitor.get_issues()
if issues:
    print("Validation issues found:")
    for issue in issues:
        print(f"  - {issue}")
else:
    print("No validation issues found")

# What we accomplished in this step:
# - Created realistic document processing example
# - Implemented multiple visitors for different operations (HTML export, word count, validation)
# - Demonstrated how visitor pattern separates operations from data structure
# - Showed how new operations can be added without modifying existing elements


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Understanding the Visitor pattern and its benefits
# - Implementing double dispatch for type-specific operations
# - Separating operations from object structure
# - Creating multiple visitors for different operations
# - Adding new operations without modifying existing classes
# - Understanding when to use Visitor vs other patterns
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try creating a file system visitor!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
