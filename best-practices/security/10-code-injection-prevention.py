"""Question: Implement comprehensive code injection prevention techniques.

Create a secure code execution system that prevents various types of code injection attacks
including command injection, SQL injection, and eval injection.

Requirements:
1. Create a secure command executor that validates input
2. Create a secure SQL query builder with parameterized queries
3. Create a secure expression evaluator that prevents eval injection
4. Create input validation and sanitization utilities
5. Demonstrate safe and unsafe practices with examples

Example usage:
    executor = SecureCommandExecutor()
    result = executor.execute_command("ls", ["-la", "/home"])
    
    query_builder = SecureQueryBuilder()
    query = query_builder.select("users").where("id", user_id).build()
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
# - What are the different types of code injection attacks?
# - How can you validate and sanitize user input?
# - What makes command execution safe vs unsafe?
# - How do parameterized queries prevent SQL injection?
# - What are safe alternatives to eval()?
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


# Step 1: Import modules and create basic security utilities
# ===============================================================================

# Explanation:
# Code injection prevention starts with proper input validation and sanitization.
# We'll create utilities to validate different types of input safely.

import re
import subprocess
import shlex
import sqlite3
import ast
import operator
from typing import List, Dict, Any, Optional, Union
from pathlib import Path

class SecurityError(Exception):
    """Custom exception for security-related errors."""
    pass

class InputValidator:
    """Utility class for validating and sanitizing user input."""
    
    # Safe characters for different contexts
    SAFE_FILENAME_CHARS = re.compile(r'^[a-zA-Z0-9._-]+$')
    SAFE_COMMAND_CHARS = re.compile(r'^[a-zA-Z0-9._/-]+$')
    SAFE_SQL_IDENTIFIER = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    
    @staticmethod
    def validate_filename(filename: str) -> bool:
        """Validate that filename contains only safe characters."""
        if not filename or len(filename) > 255:
            return False
        return bool(InputValidator.SAFE_FILENAME_CHARS.match(filename))
    
    @staticmethod
    def validate_command_name(command: str) -> bool:
        """Validate that command name is safe."""
        if not command or len(command) > 100:
            return False
        return bool(InputValidator.SAFE_COMMAND_CHARS.match(command))
    
    @staticmethod
    def validate_sql_identifier(identifier: str) -> bool:
        """Validate SQL identifier (table/column name)."""
        if not identifier or len(identifier) > 64:
            return False
        return bool(InputValidator.SAFE_SQL_IDENTIFIER.match(identifier))
    
    @staticmethod
    def sanitize_string(input_str: str, max_length: int = 1000) -> str:
        """Sanitize string input by removing dangerous characters."""
        if not isinstance(input_str, str):
            raise SecurityError("Input must be a string")
        
        # Truncate if too long
        if len(input_str) > max_length:
            input_str = input_str[:max_length]
        
        # Remove null bytes and control characters
        sanitized = ''.join(char for char in input_str if ord(char) >= 32 or char in '\t\n\r')
        
        return sanitized

# What we accomplished in this step:
# - Created custom security exception
# - Created input validator with regex patterns for safe characters
# - Added validation methods for filenames, commands, and SQL identifiers
# - Added string sanitization to remove dangerous characters


# Step 2: Create secure command executor
# ===============================================================================

# Explanation:
# Command injection occurs when user input is passed directly to system commands.
# We'll create a secure executor that validates commands and uses safe execution methods.

import re
import subprocess
import shlex
import sqlite3
import ast
import operator
from typing import List, Dict, Any, Optional, Union
from pathlib import Path

class SecurityError(Exception):
    """Custom exception for security-related errors."""
    pass

class InputValidator:
    """Utility class for validating and sanitizing user input."""
    
    # Safe characters for different contexts
    SAFE_FILENAME_CHARS = re.compile(r'^[a-zA-Z0-9._-]+$')
    SAFE_COMMAND_CHARS = re.compile(r'^[a-zA-Z0-9._/-]+$')
    SAFE_SQL_IDENTIFIER = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    
    @staticmethod
    def validate_filename(filename: str) -> bool:
        """Validate that filename contains only safe characters."""
        if not filename or len(filename) > 255:
            return False
        return bool(InputValidator.SAFE_FILENAME_CHARS.match(filename))
    
    @staticmethod
    def validate_command_name(command: str) -> bool:
        """Validate that command name is safe."""
        if not command or len(command) > 100:
            return False
        return bool(InputValidator.SAFE_COMMAND_CHARS.match(command))
    
    @staticmethod
    def validate_sql_identifier(identifier: str) -> bool:
        """Validate SQL identifier (table/column name)."""
        if not identifier or len(identifier) > 64:
            return False
        return bool(InputValidator.SAFE_SQL_IDENTIFIER.match(identifier))
    
    @staticmethod
    def sanitize_string(input_str: str, max_length: int = 1000) -> str:
        """Sanitize string input by removing dangerous characters."""
        if not isinstance(input_str, str):
            raise SecurityError("Input must be a string")
        
        # Truncate if too long
        if len(input_str) > max_length:
            input_str = input_str[:max_length]
        
        # Remove null bytes and control characters
        sanitized = ''.join(char for char in input_str if ord(char) >= 32 or char in '\t\n\r')
        
        return sanitized

class SecureCommandExecutor:
    """Secure command executor that prevents command injection."""
    
    # Whitelist of allowed commands
    ALLOWED_COMMANDS = {
        'ls', 'cat', 'head', 'tail', 'grep', 'find', 'wc', 'sort', 'uniq',
        'date', 'whoami', 'pwd', 'echo', 'mkdir', 'rmdir', 'cp', 'mv'
    }
    
    # Dangerous characters that should never appear in arguments
    DANGEROUS_CHARS = {'&', '|', ';', '`', '$', '(', ')', '<', '>', '\n', '\r'}
    
    def __init__(self, allowed_commands: Optional[set] = None):
        """Initialize with optional custom command whitelist."""
        self.allowed_commands = allowed_commands or self.ALLOWED_COMMANDS.copy()
    
    def validate_command(self, command: str) -> bool:
        """Validate that command is in whitelist and safe."""
        if not InputValidator.validate_command_name(command):
            return False
        
        # Check if command is in whitelist
        command_base = Path(command).name  # Get just the command name, not full path
        return command_base in self.allowed_commands
    
    def validate_arguments(self, args: List[str]) -> bool:
        """Validate command arguments for dangerous characters."""
        for arg in args:
            if not isinstance(arg, str):
                return False
            
            # Check for dangerous characters
            if any(char in arg for char in self.DANGEROUS_CHARS):
                return False
            
            # Check length
            if len(arg) > 1000:
                return False
        
        return True
    
    def execute_command(self, command: str, args: List[str] = None, 
                       timeout: int = 30) -> Dict[str, Any]:
        """Safely execute a command with validation."""
        args = args or []
        
        # Validate command
        if not self.validate_command(command):
            raise SecurityError(f"Command '{command}' is not allowed")
        
        # Validate arguments
        if not self.validate_arguments(args):
            raise SecurityError("Invalid or dangerous arguments detected")
        
        try:
            # Use subprocess with shell=False to prevent shell injection
            cmd_list = [command] + args
            
            result = subprocess.run(
                cmd_list,
                capture_output=True,
                text=True,
                timeout=timeout,
                shell=False  # Critical: never use shell=True with user input
            )
            
            return {
                'success': True,
                'stdout': result.stdout,
                'stderr': result.stderr,
                'returncode': result.returncode
            }
            
        except subprocess.TimeoutExpired:
            raise SecurityError(f"Command timed out after {timeout} seconds")
        except subprocess.CalledProcessError as e:
            return {
                'success': False,
                'stdout': e.stdout,
                'stderr': e.stderr,
                'returncode': e.returncode
            }
        except Exception as e:
            raise SecurityError(f"Command execution failed: {str(e)}")

# What we accomplished in this step:
# - Created secure command executor with command whitelist
# - Added validation for commands and arguments
# - Used subprocess with shell=False to prevent injection
# - Added timeout protection and proper error handling


# Step 3: Create secure SQL query builder
# ===============================================================================

# Explanation:
# SQL injection occurs when user input is concatenated directly into SQL queries.
# We'll create a query builder that uses parameterized queries to prevent injection.

import re
import subprocess
import shlex
import sqlite3
import ast
import operator
from typing import List, Dict, Any, Optional, Union
from pathlib import Path

class SecurityError(Exception):
    """Custom exception for security-related errors."""
    pass

class InputValidator:
    """Utility class for validating and sanitizing user input."""
    
    # Safe characters for different contexts
    SAFE_FILENAME_CHARS = re.compile(r'^[a-zA-Z0-9._-]+$')
    SAFE_COMMAND_CHARS = re.compile(r'^[a-zA-Z0-9._/-]+$')
    SAFE_SQL_IDENTIFIER = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    
    @staticmethod
    def validate_filename(filename: str) -> bool:
        """Validate that filename contains only safe characters."""
        if not filename or len(filename) > 255:
            return False
        return bool(InputValidator.SAFE_FILENAME_CHARS.match(filename))
    
    @staticmethod
    def validate_command_name(command: str) -> bool:
        """Validate that command name is safe."""
        if not command or len(command) > 100:
            return False
        return bool(InputValidator.SAFE_COMMAND_CHARS.match(command))
    
    @staticmethod
    def validate_sql_identifier(identifier: str) -> bool:
        """Validate SQL identifier (table/column name)."""
        if not identifier or len(identifier) > 64:
            return False
        return bool(InputValidator.SAFE_SQL_IDENTIFIER.match(identifier))
    
    @staticmethod
    def sanitize_string(input_str: str, max_length: int = 1000) -> str:
        """Sanitize string input by removing dangerous characters."""
        if not isinstance(input_str, str):
            raise SecurityError("Input must be a string")
        
        # Truncate if too long
        if len(input_str) > max_length:
            input_str = input_str[:max_length]
        
        # Remove null bytes and control characters
        sanitized = ''.join(char for char in input_str if ord(char) >= 32 or char in '\t\n\r')
        
        return sanitized

class SecureCommandExecutor:
    """Secure command executor that prevents command injection."""
    
    # Whitelist of allowed commands
    ALLOWED_COMMANDS = {
        'ls', 'cat', 'head', 'tail', 'grep', 'find', 'wc', 'sort', 'uniq',
        'date', 'whoami', 'pwd', 'echo', 'mkdir', 'rmdir', 'cp', 'mv'
    }
    
    # Dangerous characters that should never appear in arguments
    DANGEROUS_CHARS = {'&', '|', ';', '`', '$', '(', ')', '<', '>', '\n', '\r'}
    
    def __init__(self, allowed_commands: Optional[set] = None):
        """Initialize with optional custom command whitelist."""
        self.allowed_commands = allowed_commands or self.ALLOWED_COMMANDS.copy()
    
    def validate_command(self, command: str) -> bool:
        """Validate that command is in whitelist and safe."""
        if not InputValidator.validate_command_name(command):
            return False
        
        # Check if command is in whitelist
        command_base = Path(command).name  # Get just the command name, not full path
        return command_base in self.allowed_commands
    
    def validate_arguments(self, args: List[str]) -> bool:
        """Validate command arguments for dangerous characters."""
        for arg in args:
            if not isinstance(arg, str):
                return False
            
            # Check for dangerous characters
            if any(char in arg for char in self.DANGEROUS_CHARS):
                return False
            
            # Check length
            if len(arg) > 1000:
                return False
        
        return True
    
    def execute_command(self, command: str, args: List[str] = None, 
                       timeout: int = 30) -> Dict[str, Any]:
        """Safely execute a command with validation."""
        args = args or []
        
        # Validate command
        if not self.validate_command(command):
            raise SecurityError(f"Command '{command}' is not allowed")
        
        # Validate arguments
        if not self.validate_arguments(args):
            raise SecurityError("Invalid or dangerous arguments detected")
        
        try:
            # Use subprocess with shell=False to prevent shell injection
            cmd_list = [command] + args
            
            result = subprocess.run(
                cmd_list,
                capture_output=True,
                text=True,
                timeout=timeout,
                shell=False  # Critical: never use shell=True with user input
            )
            
            return {
                'success': True,
                'stdout': result.stdout,
                'stderr': result.stderr,
                'returncode': result.returncode
            }
            
        except subprocess.TimeoutExpired:
            raise SecurityError(f"Command timed out after {timeout} seconds")
        except subprocess.CalledProcessError as e:
            return {
                'success': False,
                'stdout': e.stdout,
                'stderr': e.stderr,
                'returncode': e.returncode
            }
        except Exception as e:
            raise SecurityError(f"Command execution failed: {str(e)}")

class SecureQueryBuilder:
    """Secure SQL query builder that prevents SQL injection."""
    
    def __init__(self):
        """Initialize query builder."""
        self.reset()
    
    def reset(self):
        """Reset the query builder for a new query."""
        self._select_fields = []
        self._from_table = None
        self._where_conditions = []
        self._where_params = []
        self._order_by = []
        self._limit_value = None
        self._offset_value = None
    
    def select(self, *fields: str) -> 'SecureQueryBuilder':
        """Add SELECT fields with validation."""
        for field in fields:
            if field == '*':
                self._select_fields.append('*')
            elif InputValidator.validate_sql_identifier(field):
                self._select_fields.append(field)
            else:
                raise SecurityError(f"Invalid field name: {field}")
        return self
    
    def from_table(self, table: str) -> 'SecureQueryBuilder':
        """Set FROM table with validation."""
        if not InputValidator.validate_sql_identifier(table):
            raise SecurityError(f"Invalid table name: {table}")
        self._from_table = table
        return self
    
    def where(self, column: str, value: Any, operator: str = '=') -> 'SecureQueryBuilder':
        """Add WHERE condition with parameterized values."""
        # Validate column name
        if not InputValidator.validate_sql_identifier(column):
            raise SecurityError(f"Invalid column name: {column}")
        
        # Validate operator
        allowed_operators = {'=', '!=', '<', '>', '<=', '>=', 'LIKE', 'IN'}
        if operator.upper() not in allowed_operators:
            raise SecurityError(f"Invalid operator: {operator}")
        
        # Add parameterized condition
        self._where_conditions.append(f"{column} {operator} ?")
        self._where_params.append(value)
        return self
    
    def where_in(self, column: str, values: List[Any]) -> 'SecureQueryBuilder':
        """Add WHERE IN condition with parameterized values."""
        if not InputValidator.validate_sql_identifier(column):
            raise SecurityError(f"Invalid column name: {column}")
        
        if not values:
            raise SecurityError("WHERE IN requires at least one value")
        
        placeholders = ','.join(['?'] * len(values))
        self._where_conditions.append(f"{column} IN ({placeholders})")
        self._where_params.extend(values)
        return self
    
    def order_by(self, column: str, direction: str = 'ASC') -> 'SecureQueryBuilder':
        """Add ORDER BY clause with validation."""
        if not InputValidator.validate_sql_identifier(column):
            raise SecurityError(f"Invalid column name: {column}")
        
        if direction.upper() not in ['ASC', 'DESC']:
            raise SecurityError(f"Invalid sort direction: {direction}")
        
        self._order_by.append(f"{column} {direction.upper()}")
        return self
    
    def limit(self, count: int, offset: int = 0) -> 'SecureQueryBuilder':
        """Add LIMIT clause with validation."""
        if not isinstance(count, int) or count < 0:
            raise SecurityError("LIMIT count must be a non-negative integer")
        
        if not isinstance(offset, int) or offset < 0:
            raise SecurityError("OFFSET must be a non-negative integer")
        
        self._limit_value = count
        self._offset_value = offset
        return self
    
    def build(self) -> tuple[str, List[Any]]:
        """Build the final SQL query with parameters."""
        if not self._select_fields:
            raise SecurityError("SELECT fields are required")
        
        if not self._from_table:
            raise SecurityError("FROM table is required")
        
        # Build SELECT clause
        fields_str = ', '.join(self._select_fields)
        query = f"SELECT {fields_str} FROM {self._from_table}"
        
        # Build WHERE clause
        if self._where_conditions:
            where_str = ' AND '.join(self._where_conditions)
            query += f" WHERE {where_str}"
        
        # Build ORDER BY clause
        if self._order_by:
            order_str = ', '.join(self._order_by)
            query += f" ORDER BY {order_str}"
        
        # Build LIMIT clause
        if self._limit_value is not None:
            query += f" LIMIT {self._limit_value}"
            if self._offset_value:
                query += f" OFFSET {self._offset_value}"
        
        return query, self._where_params.copy()

# What we accomplished in this step:
# - Created secure SQL query builder with parameterized queries
# - Added validation for table names, column names, and operators
# - Used parameter placeholders (?) to prevent SQL injection
# - Added support for common SQL operations (SELECT, WHERE, ORDER BY, LIMIT)


# Step 4: Create secure expression evaluator
# ===============================================================================

# Explanation:
# Using eval() with user input is extremely dangerous as it can execute arbitrary code.
# We'll create a safe expression evaluator using AST parsing with restricted operations.

import re
import subprocess
import shlex
import sqlite3
import ast
import operator
from typing import List, Dict, Any, Optional, Union
from pathlib import Path

class SecurityError(Exception):
    """Custom exception for security-related errors."""
    pass

class InputValidator:
    """Utility class for validating and sanitizing user input."""
    
    # Safe characters for different contexts
    SAFE_FILENAME_CHARS = re.compile(r'^[a-zA-Z0-9._-]+$')
    SAFE_COMMAND_CHARS = re.compile(r'^[a-zA-Z0-9._/-]+$')
    SAFE_SQL_IDENTIFIER = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    
    @staticmethod
    def validate_filename(filename: str) -> bool:
        """Validate that filename contains only safe characters."""
        if not filename or len(filename) > 255:
            return False
        return bool(InputValidator.SAFE_FILENAME_CHARS.match(filename))
    
    @staticmethod
    def validate_command_name(command: str) -> bool:
        """Validate that command name is safe."""
        if not command or len(command) > 100:
            return False
        return bool(InputValidator.SAFE_COMMAND_CHARS.match(command))
    
    @staticmethod
    def validate_sql_identifier(identifier: str) -> bool:
        """Validate SQL identifier (table/column name)."""
        if not identifier or len(identifier) > 64:
            return False
        return bool(InputValidator.SAFE_SQL_IDENTIFIER.match(identifier))
    
    @staticmethod
    def sanitize_string(input_str: str, max_length: int = 1000) -> str:
        """Sanitize string input by removing dangerous characters."""
        if not isinstance(input_str, str):
            raise SecurityError("Input must be a string")
        
        # Truncate if too long
        if len(input_str) > max_length:
            input_str = input_str[:max_length]
        
        # Remove null bytes and control characters
        sanitized = ''.join(char for char in input_str if ord(char) >= 32 or char in '\t\n\r')
        
        return sanitized

class SecureCommandExecutor:
    """Secure command executor that prevents command injection."""
    
    # Whitelist of allowed commands
    ALLOWED_COMMANDS = {
        'ls', 'cat', 'head', 'tail', 'grep', 'find', 'wc', 'sort', 'uniq',
        'date', 'whoami', 'pwd', 'echo', 'mkdir', 'rmdir', 'cp', 'mv'
    }
    
    # Dangerous characters that should never appear in arguments
    DANGEROUS_CHARS = {'&', '|', ';', '`', '$', '(', ')', '<', '>', '\n', '\r'}
    
    def __init__(self, allowed_commands: Optional[set] = None):
        """Initialize with optional custom command whitelist."""
        self.allowed_commands = allowed_commands or self.ALLOWED_COMMANDS.copy()
    
    def validate_command(self, command: str) -> bool:
        """Validate that command is in whitelist and safe."""
        if not InputValidator.validate_command_name(command):
            return False
        
        # Check if command is in whitelist
        command_base = Path(command).name  # Get just the command name, not full path
        return command_base in self.allowed_commands
    
    def validate_arguments(self, args: List[str]) -> bool:
        """Validate command arguments for dangerous characters."""
        for arg in args:
            if not isinstance(arg, str):
                return False
            
            # Check for dangerous characters
            if any(char in arg for char in self.DANGEROUS_CHARS):
                return False
            
            # Check length
            if len(arg) > 1000:
                return False
        
        return True
    
    def execute_command(self, command: str, args: List[str] = None, 
                       timeout: int = 30) -> Dict[str, Any]:
        """Safely execute a command with validation."""
        args = args or []
        
        # Validate command
        if not self.validate_command(command):
            raise SecurityError(f"Command '{command}' is not allowed")
        
        # Validate arguments
        if not self.validate_arguments(args):
            raise SecurityError("Invalid or dangerous arguments detected")
        
        try:
            # Use subprocess with shell=False to prevent shell injection
            cmd_list = [command] + args
            
            result = subprocess.run(
                cmd_list,
                capture_output=True,
                text=True,
                timeout=timeout,
                shell=False  # Critical: never use shell=True with user input
            )
            
            return {
                'success': True,
                'stdout': result.stdout,
                'stderr': result.stderr,
                'returncode': result.returncode
            }
            
        except subprocess.TimeoutExpired:
            raise SecurityError(f"Command timed out after {timeout} seconds")
        except subprocess.CalledProcessError as e:
            return {
                'success': False,
                'stdout': e.stdout,
                'stderr': e.stderr,
                'returncode': e.returncode
            }
        except Exception as e:
            raise SecurityError(f"Command execution failed: {str(e)}")

class SecureQueryBuilder:
    """Secure SQL query builder that prevents SQL injection."""
    
    def __init__(self):
        """Initialize query builder."""
        self.reset()
    
    def reset(self):
        """Reset the query builder for a new query."""
        self._select_fields = []
        self._from_table = None
        self._where_conditions = []
        self._where_params = []
        self._order_by = []
        self._limit_value = None
        self._offset_value = None
    
    def select(self, *fields: str) -> 'SecureQueryBuilder':
        """Add SELECT fields with validation."""
        for field in fields:
            if field == '*':
                self._select_fields.append('*')
            elif InputValidator.validate_sql_identifier(field):
                self._select_fields.append(field)
            else:
                raise SecurityError(f"Invalid field name: {field}")
        return self
    
    def from_table(self, table: str) -> 'SecureQueryBuilder':
        """Set FROM table with validation."""
        if not InputValidator.validate_sql_identifier(table):
            raise SecurityError(f"Invalid table name: {table}")
        self._from_table = table
        return self
    
    def where(self, column: str, value: Any, operator: str = '=') -> 'SecureQueryBuilder':
        """Add WHERE condition with parameterized values."""
        # Validate column name
        if not InputValidator.validate_sql_identifier(column):
            raise SecurityError(f"Invalid column name: {column}")
        
        # Validate operator
        allowed_operators = {'=', '!=', '<', '>', '<=', '>=', 'LIKE', 'IN'}
        if operator.upper() not in allowed_operators:
            raise SecurityError(f"Invalid operator: {operator}")
        
        # Add parameterized condition
        self._where_conditions.append(f"{column} {operator} ?")
        self._where_params.append(value)
        return self
    
    def where_in(self, column: str, values: List[Any]) -> 'SecureQueryBuilder':
        """Add WHERE IN condition with parameterized values."""
        if not InputValidator.validate_sql_identifier(column):
            raise SecurityError(f"Invalid column name: {column}")
        
        if not values:
            raise SecurityError("WHERE IN requires at least one value")
        
        placeholders = ','.join(['?'] * len(values))
        self._where_conditions.append(f"{column} IN ({placeholders})")
        self._where_params.extend(values)
        return self
    
    def order_by(self, column: str, direction: str = 'ASC') -> 'SecureQueryBuilder':
        """Add ORDER BY clause with validation."""
        if not InputValidator.validate_sql_identifier(column):
            raise SecurityError(f"Invalid column name: {column}")
        
        if direction.upper() not in ['ASC', 'DESC']:
            raise SecurityError(f"Invalid sort direction: {direction}")
        
        self._order_by.append(f"{column} {direction.upper()}")
        return self
    
    def limit(self, count: int, offset: int = 0) -> 'SecureQueryBuilder':
        """Add LIMIT clause with validation."""
        if not isinstance(count, int) or count < 0:
            raise SecurityError("LIMIT count must be a non-negative integer")
        
        if not isinstance(offset, int) or offset < 0:
            raise SecurityError("OFFSET must be a non-negative integer")
        
        self._limit_value = count
        self._offset_value = offset
        return self
    
    def build(self) -> tuple[str, List[Any]]:
        """Build the final SQL query with parameters."""
        if not self._select_fields:
            raise SecurityError("SELECT fields are required")
        
        if not self._from_table:
            raise SecurityError("FROM table is required")
        
        # Build SELECT clause
        fields_str = ', '.join(self._select_fields)
        query = f"SELECT {fields_str} FROM {self._from_table}"
        
        # Build WHERE clause
        if self._where_conditions:
            where_str = ' AND '.join(self._where_conditions)
            query += f" WHERE {where_str}"
        
        # Build ORDER BY clause
        if self._order_by:
            order_str = ', '.join(self._order_by)
            query += f" ORDER BY {order_str}"
        
        # Build LIMIT clause
        if self._limit_value is not None:
            query += f" LIMIT {self._limit_value}"
            if self._offset_value:
                query += f" OFFSET {self._offset_value}"
        
        return query, self._where_params.copy()

class SecureExpressionEvaluator:
    """Secure expression evaluator that prevents code injection via eval()."""
    
    # Allowed operators for mathematical expressions
    ALLOWED_OPERATORS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }
    
    # Allowed comparison operators
    ALLOWED_COMPARISONS = {
        ast.Eq: operator.eq,
        ast.NotEq: operator.ne,
        ast.Lt: operator.lt,
        ast.LtE: operator.le,
        ast.Gt: operator.gt,
        ast.GtE: operator.ge,
    }
    
    # Allowed boolean operators
    ALLOWED_BOOLEAN = {
        ast.And: lambda x, y: x and y,
        ast.Or: lambda x, y: x or y,
        ast.Not: lambda x: not x,
    }
    
    def __init__(self, allowed_names: Optional[Dict[str, Any]] = None):
        """Initialize with optional allowed variable names."""
        self.allowed_names = allowed_names or {}
    
    def _validate_node(self, node: ast.AST) -> bool:
        """Validate that AST node contains only safe operations."""
        if isinstance(node, ast.Expression):
            return self._validate_node(node.body)
        
        elif isinstance(node, ast.Constant):
            # Allow constants (numbers, strings, booleans)
            return isinstance(node.value, (int, float, str, bool, type(None)))
        
        elif isinstance(node, ast.Name):
            # Only allow whitelisted variable names
            return node.id in self.allowed_names
        
        elif isinstance(node, ast.BinOp):
            # Allow binary operations with safe operators
            return (type(node.op) in self.ALLOWED_OPERATORS and
                    self._validate_node(node.left) and
                    self._validate_node(node.right))
        
        elif isinstance(node, ast.UnaryOp):
            # Allow unary operations with safe operators
            return (type(node.op) in self.ALLOWED_OPERATORS and
                    self._validate_node(node.operand))
        
        elif isinstance(node, ast.Compare):
            # Allow comparisons with safe operators
            return (all(type(op) in self.ALLOWED_COMPARISONS for op in node.ops) and
                    self._validate_node(node.left) and
                    all(self._validate_node(comp) for comp in node.comparators))
        
        elif isinstance(node, ast.BoolOp):
            # Allow boolean operations
            return (type(node.op) in self.ALLOWED_BOOLEAN and
                    all(self._validate_node(value) for value in node.values))
        
        else:
            # Reject all other node types (function calls, imports, etc.)
            return False
    
    def _evaluate_node(self, node: ast.AST) -> Any:
        """Safely evaluate an AST node."""
        if isinstance(node, ast.Expression):
            return self._evaluate_node(node.body)
        
        elif isinstance(node, ast.Constant):
            return node.value
        
        elif isinstance(node, ast.Name):
            return self.allowed_names[node.id]
        
        elif isinstance(node, ast.BinOp):
            left = self._evaluate_node(node.left)
            right = self._evaluate_node(node.right)
            op_func = self.ALLOWED_OPERATORS[type(node.op)]
            return op_func(left, right)
        
        elif isinstance(node, ast.UnaryOp):
            operand = self._evaluate_node(node.operand)
            op_func = self.ALLOWED_OPERATORS[type(node.op)]
            return op_func(operand)
        
        elif isinstance(node, ast.Compare):
            left = self._evaluate_node(node.left)
            result = True
            
            for op, comparator in zip(node.ops, node.comparators):
                right = self._evaluate_node(comparator)
                op_func = self.ALLOWED_COMPARISONS[type(op)]
                result = result and op_func(left, right)
                left = right  # For chained comparisons
            
            return result
        
        elif isinstance(node, ast.BoolOp):
            op_func = self.ALLOWED_BOOLEAN[type(node.op)]
            values = [self._evaluate_node(value) for value in node.values]
            
            if isinstance(node.op, ast.And):
                return all(values)
            elif isinstance(node.op, ast.Or):
                return any(values)
        
        else:
            raise SecurityError(f"Unsupported node type: {type(node)}")
    
    def evaluate(self, expression: str, variables: Optional[Dict[str, Any]] = None) -> Any:
        """Safely evaluate a mathematical expression."""
        if not isinstance(expression, str):
            raise SecurityError("Expression must be a string")
        
        if len(expression) > 1000:
            raise SecurityError("Expression too long")
        
        # Update allowed names with provided variables
        if variables:
            # Validate variable names
            for name in variables:
                if not InputValidator.validate_sql_identifier(name):
                    raise SecurityError(f"Invalid variable name: {name}")
            
            self.allowed_names.update(variables)
        
        try:
            # Parse expression into AST
            tree = ast.parse(expression, mode='eval')
            
            # Validate that AST contains only safe operations
            if not self._validate_node(tree):
                raise SecurityError("Expression contains unsafe operations")
            
            # Evaluate the safe AST
            return self._evaluate_node(tree)
            
        except SyntaxError:
            raise SecurityError("Invalid expression syntax")
        except (ValueError, TypeError, ZeroDivisionError) as e:
            raise SecurityError(f"Evaluation error: {str(e)}")

# What we accomplished in this step:
# - Created secure expression evaluator using AST parsing
# - Whitelisted only safe mathematical and logical operations
# - Prevented function calls, imports, and other dangerous operations
# - Added variable support with name validation


# Step 5: Demonstrate safe and unsafe practices with examples
# ===============================================================================

# Explanation:
# Let's test our secure implementations and show examples of both safe and unsafe
# practices to understand the importance of proper input validation.

import re
import subprocess
import shlex
import sqlite3
import ast
import operator
from typing import List, Dict, Any, Optional, Union
from pathlib import Path

class SecurityError(Exception):
    """Custom exception for security-related errors."""
    pass

class InputValidator:
    """Utility class for validating and sanitizing user input."""
    
    # Safe characters for different contexts
    SAFE_FILENAME_CHARS = re.compile(r'^[a-zA-Z0-9._-]+$')
    SAFE_COMMAND_CHARS = re.compile(r'^[a-zA-Z0-9._/-]+$')
    SAFE_SQL_IDENTIFIER = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    
    @staticmethod
    def validate_filename(filename: str) -> bool:
        """Validate that filename contains only safe characters."""
        if not filename or len(filename) > 255:
            return False
        return bool(InputValidator.SAFE_FILENAME_CHARS.match(filename))
    
    @staticmethod
    def validate_command_name(command: str) -> bool:
        """Validate that command name is safe."""
        if not command or len(command) > 100:
            return False
        return bool(InputValidator.SAFE_COMMAND_CHARS.match(command))
    
    @staticmethod
    def validate_sql_identifier(identifier: str) -> bool:
        """Validate SQL identifier (table/column name)."""
        if not identifier or len(identifier) > 64:
            return False
        return bool(InputValidator.SAFE_SQL_IDENTIFIER.match(identifier))
    
    @staticmethod
    def sanitize_string(input_str: str, max_length: int = 1000) -> str:
        """Sanitize string input by removing dangerous characters."""
        if not isinstance(input_str, str):
            raise SecurityError("Input must be a string")
        
        # Truncate if too long
        if len(input_str) > max_length:
            input_str = input_str[:max_length]
        
        # Remove null bytes and control characters
        sanitized = ''.join(char for char in input_str if ord(char) >= 32 or char in '\t\n\r')
        
        return sanitized

class SecureCommandExecutor:
    """Secure command executor that prevents command injection."""
    
    # Whitelist of allowed commands
    ALLOWED_COMMANDS = {
        'ls', 'cat', 'head', 'tail', 'grep', 'find', 'wc', 'sort', 'uniq',
        'date', 'whoami', 'pwd', 'echo', 'mkdir', 'rmdir', 'cp', 'mv'
    }
    
    # Dangerous characters that should never appear in arguments
    DANGEROUS_CHARS = {'&', '|', ';', '`', '$', '(', ')', '<', '>', '\n', '\r'}
    
    def __init__(self, allowed_commands: Optional[set] = None):
        """Initialize with optional custom command whitelist."""
        self.allowed_commands = allowed_commands or self.ALLOWED_COMMANDS.copy()
    
    def validate_command(self, command: str) -> bool:
        """Validate that command is in whitelist and safe."""
        if not InputValidator.validate_command_name(command):
            return False
        
        # Check if command is in whitelist
        command_base = Path(command).name  # Get just the command name, not full path
        return command_base in self.allowed_commands
    
    def validate_arguments(self, args: List[str]) -> bool:
        """Validate command arguments for dangerous characters."""
        for arg in args:
            if not isinstance(arg, str):
                return False
            
            # Check for dangerous characters
            if any(char in arg for char in self.DANGEROUS_CHARS):
                return False
            
            # Check length
            if len(arg) > 1000:
                return False
        
        return True
    
    def execute_command(self, command: str, args: List[str] = None, 
                       timeout: int = 30) -> Dict[str, Any]:
        """Safely execute a command with validation."""
        args = args or []
        
        # Validate command
        if not self.validate_command(command):
            raise SecurityError(f"Command '{command}' is not allowed")
        
        # Validate arguments
        if not self.validate_arguments(args):
            raise SecurityError("Invalid or dangerous arguments detected")
        
        try:
            # Use subprocess with shell=False to prevent shell injection
            cmd_list = [command] + args
            
            result = subprocess.run(
                cmd_list,
                capture_output=True,
                text=True,
                timeout=timeout,
                shell=False  # Critical: never use shell=True with user input
            )
            
            return {
                'success': True,
                'stdout': result.stdout,
                'stderr': result.stderr,
                'returncode': result.returncode
            }
            
        except subprocess.TimeoutExpired:
            raise SecurityError(f"Command timed out after {timeout} seconds")
        except subprocess.CalledProcessError as e:
            return {
                'success': False,
                'stdout': e.stdout,
                'stderr': e.stderr,
                'returncode': e.returncode
            }
        except Exception as e:
            raise SecurityError(f"Command execution failed: {str(e)}")

class SecureQueryBuilder:
    """Secure SQL query builder that prevents SQL injection."""
    
    def __init__(self):
        """Initialize query builder."""
        self.reset()
    
    def reset(self):
        """Reset the query builder for a new query."""
        self._select_fields = []
        self._from_table = None
        self._where_conditions = []
        self._where_params = []
        self._order_by = []
        self._limit_value = None
        self._offset_value = None
    
    def select(self, *fields: str) -> 'SecureQueryBuilder':
        """Add SELECT fields with validation."""
        for field in fields:
            if field == '*':
                self._select_fields.append('*')
            elif InputValidator.validate_sql_identifier(field):
                self._select_fields.append(field)
            else:
                raise SecurityError(f"Invalid field name: {field}")
        return self
    
    def from_table(self, table: str) -> 'SecureQueryBuilder':
        """Set FROM table with validation."""
        if not InputValidator.validate_sql_identifier(table):
            raise SecurityError(f"Invalid table name: {table}")
        self._from_table = table
        return self
    
    def where(self, column: str, value: Any, operator: str = '=') -> 'SecureQueryBuilder':
        """Add WHERE condition with parameterized values."""
        # Validate column name
        if not InputValidator.validate_sql_identifier(column):
            raise SecurityError(f"Invalid column name: {column}")
        
        # Validate operator
        allowed_operators = {'=', '!=', '<', '>', '<=', '>=', 'LIKE', 'IN'}
        if operator.upper() not in allowed_operators:
            raise SecurityError(f"Invalid operator: {operator}")
        
        # Add parameterized condition
        self._where_conditions.append(f"{column} {operator} ?")
        self._where_params.append(value)
        return self
    
    def where_in(self, column: str, values: List[Any]) -> 'SecureQueryBuilder':
        """Add WHERE IN condition with parameterized values."""
        if not InputValidator.validate_sql_identifier(column):
            raise SecurityError(f"Invalid column name: {column}")
        
        if not values:
            raise SecurityError("WHERE IN requires at least one value")
        
        placeholders = ','.join(['?'] * len(values))
        self._where_conditions.append(f"{column} IN ({placeholders})")
        self._where_params.extend(values)
        return self
    
    def order_by(self, column: str, direction: str = 'ASC') -> 'SecureQueryBuilder':
        """Add ORDER BY clause with validation."""
        if not InputValidator.validate_sql_identifier(column):
            raise SecurityError(f"Invalid column name: {column}")
        
        if direction.upper() not in ['ASC', 'DESC']:
            raise SecurityError(f"Invalid sort direction: {direction}")
        
        self._order_by.append(f"{column} {direction.upper()}")
        return self
    
    def limit(self, count: int, offset: int = 0) -> 'SecureQueryBuilder':
        """Add LIMIT clause with validation."""
        if not isinstance(count, int) or count < 0:
            raise SecurityError("LIMIT count must be a non-negative integer")
        
        if not isinstance(offset, int) or offset < 0:
            raise SecurityError("OFFSET must be a non-negative integer")
        
        self._limit_value = count
        self._offset_value = offset
        return self
    
    def build(self) -> tuple[str, List[Any]]:
        """Build the final SQL query with parameters."""
        if not self._select_fields:
            raise SecurityError("SELECT fields are required")
        
        if not self._from_table:
            raise SecurityError("FROM table is required")
        
        # Build SELECT clause
        fields_str = ', '.join(self._select_fields)
        query = f"SELECT {fields_str} FROM {self._from_table}"
        
        # Build WHERE clause
        if self._where_conditions:
            where_str = ' AND '.join(self._where_conditions)
            query += f" WHERE {where_str}"
        
        # Build ORDER BY clause
        if self._order_by:
            order_str = ', '.join(self._order_by)
            query += f" ORDER BY {order_str}"
        
        # Build LIMIT clause
        if self._limit_value is not None:
            query += f" LIMIT {self._limit_value}"
            if self._offset_value:
                query += f" OFFSET {self._offset_value}"
        
        return query, self._where_params.copy()

class SecureExpressionEvaluator:
    """Secure expression evaluator that prevents code injection via eval()."""
    
    # Allowed operators for mathematical expressions
    ALLOWED_OPERATORS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }
    
    # Allowed comparison operators
    ALLOWED_COMPARISONS = {
        ast.Eq: operator.eq,
        ast.NotEq: operator.ne,
        ast.Lt: operator.lt,
        ast.LtE: operator.le,
        ast.Gt: operator.gt,
        ast.GtE: operator.ge,
    }
    
    # Allowed boolean operators
    ALLOWED_BOOLEAN = {
        ast.And: lambda x, y: x and y,
        ast.Or: lambda x, y: x or y,
        ast.Not: lambda x: not x,
    }
    
    def __init__(self, allowed_names: Optional[Dict[str, Any]] = None):
        """Initialize with optional allowed variable names."""
        self.allowed_names = allowed_names or {}
    
    def _validate_node(self, node: ast.AST) -> bool:
        """Validate that AST node contains only safe operations."""
        if isinstance(node, ast.Expression):
            return self._validate_node(node.body)
        
        elif isinstance(node, ast.Constant):
            # Allow constants (numbers, strings, booleans)
            return isinstance(node.value, (int, float, str, bool, type(None)))
        
        elif isinstance(node, ast.Name):
            # Only allow whitelisted variable names
            return node.id in self.allowed_names
        
        elif isinstance(node, ast.BinOp):
            # Allow binary operations with safe operators
            return (type(node.op) in self.ALLOWED_OPERATORS and
                    self._validate_node(node.left) and
                    self._validate_node(node.right))
        
        elif isinstance(node, ast.UnaryOp):
            # Allow unary operations with safe operators
            return (type(node.op) in self.ALLOWED_OPERATORS and
                    self._validate_node(node.operand))
        
        elif isinstance(node, ast.Compare):
            # Allow comparisons with safe operators
            return (all(type(op) in self.ALLOWED_COMPARISONS for op in node.ops) and
                    self._validate_node(node.left) and
                    all(self._validate_node(comp) for comp in node.comparators))
        
        elif isinstance(node, ast.BoolOp):
            # Allow boolean operations
            return (type(node.op) in self.ALLOWED_BOOLEAN and
                    all(self._validate_node(value) for value in node.values))
        
        else:
            # Reject all other node types (function calls, imports, etc.)
            return False
    
    def _evaluate_node(self, node: ast.AST) -> Any:
        """Safely evaluate an AST node."""
        if isinstance(node, ast.Expression):
            return self._evaluate_node(node.body)
        
        elif isinstance(node, ast.Constant):
            return node.value
        
        elif isinstance(node, ast.Name):
            return self.allowed_names[node.id]
        
        elif isinstance(node, ast.BinOp):
            left = self._evaluate_node(node.left)
            right = self._evaluate_node(node.right)
            op_func = self.ALLOWED_OPERATORS[type(node.op)]
            return op_func(left, right)
        
        elif isinstance(node, ast.UnaryOp):
            operand = self._evaluate_node(node.operand)
            op_func = self.ALLOWED_OPERATORS[type(node.op)]
            return op_func(operand)
        
        elif isinstance(node, ast.Compare):
            left = self._evaluate_node(node.left)
            result = True
            
            for op, comparator in zip(node.ops, node.comparators):
                right = self._evaluate_node(comparator)
                op_func = self.ALLOWED_COMPARISONS[type(op)]
                result = result and op_func(left, right)
                left = right  # For chained comparisons
            
            return result
        
        elif isinstance(node, ast.BoolOp):
            op_func = self.ALLOWED_BOOLEAN[type(node.op)]
            values = [self._evaluate_node(value) for value in node.values]
            
            if isinstance(node.op, ast.And):
                return all(values)
            elif isinstance(node.op, ast.Or):
                return any(values)
        
        else:
            raise SecurityError(f"Unsupported node type: {type(node)}")
    
    def evaluate(self, expression: str, variables: Optional[Dict[str, Any]] = None) -> Any:
        """Safely evaluate a mathematical expression."""
        if not isinstance(expression, str):
            raise SecurityError("Expression must be a string")
        
        if len(expression) > 1000:
            raise SecurityError("Expression too long")
        
        # Update allowed names with provided variables
        if variables:
            # Validate variable names
            for name in variables:
                if not InputValidator.validate_sql_identifier(name):
                    raise SecurityError(f"Invalid variable name: {name}")
            
            self.allowed_names.update(variables)
        
        try:
            # Parse expression into AST
            tree = ast.parse(expression, mode='eval')
            
            # Validate that AST contains only safe operations
            if not self._validate_node(tree):
                raise SecurityError("Expression contains unsafe operations")
            
            # Evaluate the safe AST
            return self._evaluate_node(tree)
            
        except SyntaxError:
            raise SecurityError("Invalid expression syntax")
        except (ValueError, TypeError, ZeroDivisionError) as e:
            raise SecurityError(f"Evaluation error: {str(e)}")

def demonstrate_unsafe_practices():
    """Show examples of UNSAFE practices that lead to code injection."""
    print("=== UNSAFE PRACTICES (DO NOT USE!) ===\n")
    
    print("1. Command Injection - UNSAFE:")
    print("# NEVER do this:")
    print("user_input = 'file.txt; rm -rf /'")
    print("os.system(f'cat {user_input}')  # DANGEROUS!")
    print("# This could delete your entire system!\n")
    
    print("2. SQL Injection - UNSAFE:")
    print("# NEVER do this:")
    print("user_id = \"1; DROP TABLE users; --\"")
    print("query = f\"SELECT * FROM users WHERE id = {user_id}\"")
    print("# This could delete your database!\n")
    
    print("3. Code Injection via eval() - UNSAFE:")
    print("# NEVER do this:")
    print("user_expr = '__import__(\"os\").system(\"rm -rf /\")'")
    print("result = eval(user_expr)  # EXTREMELY DANGEROUS!")
    print("# This could execute any Python code!\n")

def demonstrate_safe_practices():
    """Show examples of SAFE practices using our secure implementations."""
    print("=== SAFE PRACTICES (RECOMMENDED) ===\n")
    
    # Test secure command executor
    print("1. Secure Command Execution:")
    executor = SecureCommandExecutor()
    
    try:
        # Safe command
        result = executor.execute_command("echo", ["Hello, World!"])
        print(f"✓ Safe command executed: {result['stdout'].strip()}")
        
        # Attempt dangerous command (will be blocked)
        try:
            executor.execute_command("rm", ["-rf", "/"])
        except SecurityError as e:
            print(f"✓ Dangerous command blocked: {e}")
        
        # Attempt command injection (will be blocked)
        try:
            executor.execute_command("echo", ["test; rm -rf /"])
        except SecurityError as e:
            print(f"✓ Command injection blocked: {e}")
    
    except Exception as e:
        print(f"Command execution test failed: {e}")
    
    print()
    
    # Test secure SQL query builder
    print("2. Secure SQL Query Building:")
    query_builder = SecureQueryBuilder()
    
    try:
        # Build safe parameterized query
        query, params = (query_builder
                        .select("name", "email")
                        .from_table("users")
                        .where("id", 123)
                        .where("status", "active")
                        .order_by("name")
                        .limit(10)
                        .build())
        
        print(f"✓ Safe query: {query}")
        print(f"✓ Parameters: {params}")
        
        # Attempt SQL injection (will be blocked)
        try:
            query_builder.reset()
            query_builder.from_table("users; DROP TABLE users; --")
        except SecurityError as e:
            print(f"✓ SQL injection blocked: {e}")
    
    except Exception as e:
        print(f"SQL query test failed: {e}")
    
    print()
    
    # Test secure expression evaluator
    print("3. Secure Expression Evaluation:")
    evaluator = SecureExpressionEvaluator()
    
    try:
        # Safe mathematical expressions
        result1 = evaluator.evaluate("2 + 3 * 4")
        print(f"✓ Math expression: 2 + 3 * 4 = {result1}")
        
        result2 = evaluator.evaluate("x * 2 + y", {"x": 10, "y": 5})
        print(f"✓ With variables: x * 2 + y = {result2}")
        
        result3 = evaluator.evaluate("a > 5 and b < 10", {"a": 7, "b": 8})
        print(f"✓ Boolean expression: a > 5 and b < 10 = {result3}")
        
        # Attempt code injection (will be blocked)
        try:
            evaluator.evaluate("__import__('os').system('echo hacked')")
        except SecurityError as e:
            print(f"✓ Code injection blocked: {e}")
        
        try:
            evaluator.evaluate("open('/etc/passwd').read()")
        except SecurityError as e:
            print(f"✓ File access blocked: {e}")
    
    except Exception as e:
        print(f"Expression evaluation test failed: {e}")
    
    print()

# Test the complete implementation
print("=== Testing Code Injection Prevention ===\n")

demonstrate_unsafe_practices()
demonstrate_safe_practices()

print("=== Key Security Principles ===")
print("1. Input Validation: Always validate user input against strict criteria")
print("2. Whitelisting: Use whitelists instead of blacklists when possible")
print("3. Parameterized Queries: Never concatenate user input into SQL")
print("4. Avoid eval(): Use safe alternatives like AST parsing")
print("5. Principle of Least Privilege: Only allow necessary operations")
print("6. Defense in Depth: Use multiple layers of security")

# What we accomplished in this step:
# - Demonstrated unsafe practices that lead to code injection
# - Showed how our secure implementations prevent these attacks
# - Tested all security components with real examples
# - Provided key security principles for developers


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Input validation and sanitization techniques
# - Command injection prevention using whitelists and subprocess
# - SQL injection prevention using parameterized queries
# - Code injection prevention using AST parsing instead of eval()
# - Security principles: defense in depth, least privilege, whitelisting
# - Proper error handling for security-related failures
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each security measure is necessary
# 4. Experiment with modifications (try adding more validation rules!)
#
# Remember: Security is not optional - it's essential!
# ===============================================================================

