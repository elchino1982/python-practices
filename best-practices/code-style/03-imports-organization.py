"""Question: Demonstrate proper import organization and best practices in Python.

Learn how to organize imports following PEP 8 guidelines and best practices
for maintainable, readable, and efficient Python code.

Requirements:
1. Show proper import order (standard library, third-party, local)
2. Demonstrate different import styles and when to use them
3. Show how to handle import conflicts and aliases
4. Demonstrate conditional imports and lazy loading
5. Show best practices for organizing imports in larger projects

Example usage:
    # Proper import organization at the top of a module
    import os
    import sys
    
    import requests
    import numpy as np
    
    from myproject import utils
    from myproject.models import User
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read PEP 8 import guidelines
# - Think about import order and grouping
# - Consider readability and maintainability
# - Practice different import styles
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
# - What is the proper order for imports?
# - When should you use 'import module' vs 'from module import item'?
# - How do you handle long import lists?
# - What about import aliases and conflicts?
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


# Step 1: Basic import organization - Standard library imports
# ===============================================================================

# Explanation:
# According to PEP 8, imports should be organized in three groups:
# 1. Standard library imports
# 2. Related third-party imports  
# 3. Local application/library specific imports
# Each group should be separated by a blank line.

# Standard library imports (alphabetically ordered)
import collections
import datetime
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Union

print("Step 1: Basic standard library imports")
print("Standard library modules imported:", ['collections', 'datetime', 'json', 'os', 'sys', 'pathlib', 'typing'])
print()


# Step 2: Add third-party imports with proper separation
# ===============================================================================

# Explanation:
# Third-party imports come after standard library imports, separated by a blank line.
# These should also be alphabetically ordered for consistency.
# Use specific imports when you only need certain functions/classes.

# Standard library imports (from Step 1)
import collections
import datetime
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Union

# Third-party imports (alphabetically ordered)
import requests
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String

print("Step 2: Added third-party imports")
print("Third-party modules:", ['requests', 'numpy', 'pandas', 'flask', 'sqlalchemy'])
print("Notice the blank line separation between import groups")
print()


# Step 3: Add local/application imports and demonstrate import styles
# ===============================================================================

# Explanation:
# Local imports come last, after another blank line.
# Different import styles serve different purposes:
# - 'import module' for general use
# - 'from module import item' for specific items
# - 'from module import item as alias' for avoiding conflicts

# Standard library imports (from Steps 1-2)
import collections
import datetime
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Union

# Third-party imports (from Step 2)
import requests
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String

# Local application imports
import myproject.config
from myproject import utils
from myproject.models import User, Product
from myproject.database import DatabaseManager
from myproject.auth import authenticate_user as auth_user  # Alias to avoid conflicts

# Demonstration of different import styles
def demonstrate_import_styles():
    """Show when to use different import styles."""
    
    # Style 1: Import entire module (good for multiple uses)
    config_value = myproject.config.get_setting('database_url')
    
    # Style 2: Import specific items (good for frequently used items)
    user = User(name="John", email="john@example.com")
    
    # Style 3: Import with alias (good for avoiding name conflicts)
    is_authenticated = auth_user("john", "password123")
    
    return config_value, user, is_authenticated

print("Step 3: Added local imports and import styles")
print("Local modules:", ['myproject.config', 'myproject.utils', 'myproject.models', 'myproject.database', 'myproject.auth'])
print("Demonstrated different import styles: module, specific items, and aliases")
print()


# Step 4: Handle import conflicts and demonstrate advanced techniques
# ===============================================================================

# Explanation:
# Sometimes you need to import items with the same name from different modules.
# Use aliases to resolve conflicts and make code more readable.
# Also demonstrate multiline imports for better readability.

# Standard library imports (from Steps 1-3)
import collections
import datetime
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Union

# Third-party imports (from Steps 2-3)
import requests
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String

# Local application imports (from Step 3)
import myproject.config
from myproject import utils
from myproject.models import User, Product
from myproject.database import DatabaseManager
from myproject.auth import authenticate_user as auth_user

# Advanced import techniques
from collections import (
    defaultdict,
    namedtuple,
    OrderedDict,
    Counter
)

# Handling name conflicts with aliases
from datetime import datetime as dt  # Avoid conflict with datetime module
from json import loads as json_loads, dumps as json_dumps  # More descriptive names
from myproject.utils import validate as validate_data  # Avoid conflict with built-in
from myproject.models import User as AppUser  # Distinguish from other User classes

def demonstrate_conflict_resolution():
    """Show how to handle import conflicts."""
    
    # Using aliased imports to avoid conflicts
    current_time = dt.now()  # Clear it's datetime.datetime, not datetime module
    
    # Using descriptive aliases
    data = json_loads('{"name": "John"}')
    json_string = json_dumps(data)
    
    # Using module-specific aliases
    app_user = AppUser(name="Jane")
    
    # Using multiline imports for readability
    user_data = defaultdict(list)
    UserTuple = namedtuple('UserTuple', ['name', 'email'])
    
    return current_time, data, json_string, app_user, user_data, UserTuple

print("Step 4: Handled import conflicts and advanced techniques")
print("Demonstrated aliases for conflicts:", ['datetime as dt', 'loads as json_loads', 'User as AppUser'])
print("Showed multiline imports for better readability")
print()


# Step 5: Conditional imports and lazy loading
# ===============================================================================

# Explanation:
# Sometimes you need to import modules conditionally (based on availability)
# or lazily (only when needed) to improve startup time or handle optional dependencies.

# Standard library imports (from Steps 1-4)
import collections
import datetime
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Union

# Third-party imports (from Steps 2-4)
import requests
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String

# Local application imports (from Steps 3-4)
import myproject.config
from myproject import utils
from myproject.models import User, Product
from myproject.database import DatabaseManager
from myproject.auth import authenticate_user as auth_user

# Advanced import techniques (from Step 4)
from collections import (
    defaultdict,
    namedtuple,
    OrderedDict,
    Counter
)
from datetime import datetime as dt
from json import loads as json_loads, dumps as json_dumps
from myproject.utils import validate as validate_data
from myproject.models import User as AppUser

# Conditional imports for optional dependencies
try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    plt = None

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    Image = None

# Platform-specific imports
if sys.platform == 'win32':
    import winsound
elif sys.platform.startswith('linux'):
    import subprocess as linux_subprocess

def demonstrate_conditional_imports():
    """Show how to use conditional imports."""
    
    if HAS_MATPLOTLIB:
        # Only use matplotlib if available
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3], [1, 4, 9])
        print("Matplotlib is available - created a plot")
    else:
        print("Matplotlib not available - skipping plot creation")
    
    if HAS_PIL:
        # Only use PIL if available
        print("PIL is available - can process images")
    else:
        print("PIL not available - image processing disabled")

def lazy_import_example():
    """Demonstrate lazy importing - import only when needed."""
    
    # Import heavy modules only when actually needed
    def process_large_dataset():
        import scipy.sparse as sparse  # Lazy import
        import sklearn.cluster as cluster  # Lazy import
        
        print("Heavy scientific computing modules loaded only when needed")
        return "Dataset processed"
    
    # Import is deferred until function is called
    return process_large_dataset

print("Step 5: Conditional imports and lazy loading")
print("Optional dependencies handled:", ['matplotlib', 'PIL'])
print("Platform-specific imports demonstrated")
print("Lazy importing pattern shown")
print()


# Step 6: Best practices for larger projects and import organization
# ===============================================================================

# Explanation:
# In larger projects, import organization becomes crucial for maintainability.
# This step shows advanced patterns and best practices for complex applications.

# Standard library imports (from Steps 1-5)
import collections
import datetime
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Union, TYPE_CHECKING

# Third-party imports (from Steps 2-5)
import requests
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String

# Local application imports (from Steps 3-5)
import myproject.config
from myproject import utils
from myproject.models import User, Product
from myproject.database import DatabaseManager
from myproject.auth import authenticate_user as auth_user

# Advanced import techniques (from Steps 4-5)
from collections import (
    defaultdict,
    namedtuple,
    OrderedDict,
    Counter
)
from datetime import datetime as dt
from json import loads as json_loads, dumps as json_dumps
from myproject.utils import validate as validate_data
from myproject.models import User as AppUser

# Conditional imports (from Step 5)
try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    plt = None

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    Image = None

# TYPE_CHECKING imports - only for type hints, not runtime
if TYPE_CHECKING:
    from myproject.advanced_models import ComplexModel
    from myproject.external_service import ExternalAPI

# Import organization patterns for larger projects
class ImportBestPractices:
    """Demonstrates import organization best practices."""
    
    def __init__(self):
        # Avoid imports in __init__ unless necessary
        pass
    
    def demonstrate_type_checking_imports(self) -> Optional['ComplexModel']:
        """Show how to use TYPE_CHECKING for type hints."""
        # ComplexModel is only imported for type checking
        # This avoids circular imports and reduces runtime overhead
        return None
    
    def demonstrate_local_imports(self):
        """Show when to use local imports within functions."""
        
        def heavy_computation():
            # Import heavy modules only when this function is called
            import tensorflow as tf
            import torch
            
            print("Heavy ML frameworks imported locally")
            return "Computation complete"
        
        def database_operation():
            # Import database modules only for database operations
            from myproject.database.advanced import AdvancedQuery
            from myproject.database.migrations import MigrationRunner
            
            print("Database modules imported locally")
            return "Database operation complete"
        
        return heavy_computation, database_operation
    
    def demonstrate_import_grouping(self):
        """Show how to group related imports."""
        
        # Group 1: Core functionality
        from myproject.core import (
            BaseModel,
            BaseView,
            BaseController
        )
        
        # Group 2: Authentication and security
        from myproject.auth import (
            login_required,
            permission_required,
            TokenManager
        )
        
        # Group 3: Database and models
        from myproject.models import (
            User,
            Product,
            Order,
            Category
        )
        
        print("Imports grouped by functionality for better organization")
        return BaseModel, BaseView, TokenManager

def demonstrate_import_anti_patterns():
    """Show what NOT to do with imports."""
    
    # ANTI-PATTERN 1: Wildcard imports (avoid these)
    # from myproject.models import *  # DON'T DO THIS
    
    # ANTI-PATTERN 2: Imports in the middle of code (avoid)
    # Code here...
    # import some_module  # DON'T DO THIS
    
    # ANTI-PATTERN 3: Circular imports (restructure to avoid)
    # from myproject.a import something_from_a  # If a.py imports from this file
    
    print("Anti-patterns to avoid:")
    print("1. Wildcard imports (from module import *)")
    print("2. Imports in the middle of code")
    print("3. Circular imports")

print("Step 6: Best practices for larger projects")
print("Demonstrated TYPE_CHECKING imports for type hints")
print("Showed local imports within functions")
print("Illustrated import grouping by functionality")
print("Highlighted import anti-patterns to avoid")
print()


# Step 7: Complete example with all best practices combined
# ===============================================================================

# Explanation:
# This final step combines all the import organization best practices
# into a comprehensive example that you can use as a template.

# COMPLETE IMPORT ORGANIZATION TEMPLATE
# =====================================

# Standard library imports (alphabetically ordered)
import collections
import datetime
import json
import os
import sys
import warnings
from pathlib import Path
from typing import Dict, List, Optional, Union, TYPE_CHECKING

# Third-party imports (alphabetically ordered)
import requests
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String

# Local application imports (alphabetically ordered)
import myproject.config
from myproject import utils
from myproject.models import User, Product
from myproject.database import DatabaseManager
from myproject.auth import authenticate_user as auth_user

# Advanced import techniques
from collections import (
    defaultdict,
    namedtuple,
    OrderedDict,
    Counter
)
from datetime import datetime as dt
from json import loads as json_loads, dumps as json_dumps
from myproject.utils import validate as validate_data
from myproject.models import User as AppUser

# Conditional imports for optional dependencies
try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    plt = None

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    Image = None

# Platform-specific imports
if sys.platform == 'win32':
    import winsound
elif sys.platform.startswith('linux'):
    import subprocess as linux_subprocess

# TYPE_CHECKING imports - only for type hints
if TYPE_CHECKING:
    from myproject.advanced_models import ComplexModel
    from myproject.external_service import ExternalAPI

class ComprehensiveImportExample:
    """A complete example demonstrating all import best practices."""
    
    def __init__(self):
        self.config = myproject.config
        self.db_manager = DatabaseManager()
    
    def demonstrate_all_patterns(self):
        """Demonstrate all import patterns in one comprehensive example."""
        
        # 1. Using standard library imports
        current_path = Path.cwd()
        current_time = dt.now()
        
        # 2. Using third-party imports with aliases
        data = np.array([1, 2, 3, 4, 5])
        df = pd.DataFrame({'values': data})
        
        # 3. Using local imports with aliases
        user = AppUser(name="Demo User")
        is_valid = validate_data(user.name)
        
        # 4. Using conditional imports
        if HAS_MATPLOTLIB:
            fig, ax = plt.subplots()
            ax.plot(data)
            plot_created = True
        else:
            plot_created = False
        
        # 5. Using lazy imports when needed
        def process_heavy_data():
            import scipy.stats as stats  # Lazy import
            return stats.describe(data)
        
        # 6. Using collections with proper imports
        counter = Counter(data)
        user_data = defaultdict(list)
        
        results = {
            'current_path': str(current_path),
            'current_time': current_time.isoformat(),
            'data_stats': {
                'mean': float(np.mean(data)),
                'std': float(np.std(data))
            },
            'user_valid': is_valid,
            'plot_created': plot_created,
            'counter': dict(counter),
            'heavy_processing': process_heavy_data()
        }
        
        return results

def main():
    """Main function demonstrating the complete import organization."""
    
    print("=" * 80)
    print("COMPREHENSIVE IMPORT ORGANIZATION DEMONSTRATION")
    print("=" * 80)
    
    # Create example instance
    example = ComprehensiveImportExample()
    
    # Run comprehensive demonstration
    results = example.demonstrate_all_patterns()
    
    print("\nResults from comprehensive example:")
    print(f"Current path: {results['current_path']}")
    print(f"Current time: {results['current_time']}")
    print(f"Data statistics: {results['data_stats']}")
    print(f"User validation: {results['user_valid']}")
    print(f"Plot created: {results['plot_created']}")
    print(f"Data counter: {results['counter']}")
    print(f"Heavy processing: {results['heavy_processing']}")
    
    print("\n" + "=" * 80)
    print("IMPORT ORGANIZATION SUMMARY")
    print("=" * 80)
    print("✓ Standard library imports (alphabetically ordered)")
    print("✓ Third-party imports (alphabetically ordered)")
    print("✓ Local application imports (alphabetically ordered)")
    print("✓ Multiline imports for readability")
    print("✓ Import aliases to avoid conflicts")
    print("✓ Conditional imports for optional dependencies")
    print("✓ Platform-specific imports")
    print("✓ TYPE_CHECKING imports for type hints")
    print("✓ Lazy imports for performance")
    print("✓ Proper import grouping and separation")
    print("=" * 80)

if __name__ == "__main__":
    main()

print("Step 7: Complete comprehensive example")
print("Combined all import organization best practices")
print("Provided a template for real-world usage")
print("Demonstrated practical application of all concepts")
print()


# ===============================================================================
#                                   SUMMARY
# ===============================================================================
#
# IMPORT ORGANIZATION BEST PRACTICES LEARNED:
#
# 1. **Import Order (PEP 8)**:
#    - Standard library imports first
#    - Third-party imports second
#    - Local application imports last
#    - Separate each group with blank lines
#
# 2. **Import Styles**:
#    - Use 'import module' for general use
#    - Use 'from module import item' for specific items
#    - Use 'from module import item as alias' for conflicts
#
# 3. **Advanced Techniques**:
#    - Multiline imports for readability
#    - Conditional imports for optional dependencies
#    - Lazy imports for performance
#    - TYPE_CHECKING imports for type hints
#
# 4. **Best Practices**:
#    - Alphabetical ordering within groups
#    - Descriptive aliases
#    - Avoid wildcard imports
#    - Group related imports
#    - Handle platform differences
#
# 5. **Anti-patterns to Avoid**:
#    - Wildcard imports (from module import *)
#    - Imports in the middle of code
#    - Circular imports
#    - Unnecessary imports
#
# Remember: Good import organization makes code more readable, maintainable,
# and helps prevent common issues like circular imports and namespace conflicts.
#
# ===============================================================================