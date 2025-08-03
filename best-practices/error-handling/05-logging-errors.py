"""Question: Implement comprehensive error logging strategies for robust applications.

Create a logging system that demonstrates different logging levels, formatters,
handlers, and error tracking patterns for production applications.

Requirements:
1. Set up basic logging configuration with different levels
2. Create custom formatters for different output formats
3. Implement file and console handlers
4. Create error tracking and monitoring systems
5. Demonstrate logging in exception handling
6. Show structured logging with context
7. Implement log rotation and management

Example usage:
    logger = setup_application_logger()
    try:
        risky_operation()
    except Exception as e:
        logger.error("Operation failed", exc_info=True, extra={'user_id': 123})
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about what logging components you need
# - Start with basic logging setup
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
# - What logging levels do you need? (DEBUG, INFO, WARNING, ERROR, CRITICAL)
# - How to format log messages for different purposes?
# - Where should logs be written? (console, files, remote systems)
# - How to handle log rotation and file management?
# - How to add context information to logs?
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


# Step 1: Import modules and set up basic logging
# ===============================================================================

# Explanation:
# We start with the essential imports and basic logging configuration.
# This establishes the foundation for our logging system.

import logging
import sys
from datetime import datetime

# Basic logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Create a basic logger
basic_logger = logging.getLogger('basic_example')

# Demonstrate basic logging levels
def demonstrate_basic_logging():
    """Show different logging levels in action."""
    basic_logger.debug("This is a debug message")
    basic_logger.info("Application started successfully")
    basic_logger.warning("This is a warning message")
    basic_logger.error("An error occurred")
    basic_logger.critical("Critical system failure!")

# What we accomplished in this step:
# - Imported necessary logging modules
# - Set up basic logging configuration
# - Created a simple logger and demonstrated different levels


# Step 2: Create custom formatters for different output formats
# ===============================================================================

# Explanation:
# Custom formatters allow us to control how log messages appear.
# We'll create different formatters for console and file output.

import logging
import sys
from datetime import datetime
import json

# Basic logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Create a basic logger
basic_logger = logging.getLogger('basic_example')

# Demonstrate basic logging levels
def demonstrate_basic_logging():
    """Show different logging levels in action."""
    basic_logger.debug("This is a debug message")
    basic_logger.info("Application started successfully")
    basic_logger.warning("This is a warning message")
    basic_logger.error("An error occurred")
    basic_logger.critical("Critical system failure!")

class DetailedFormatter(logging.Formatter):
    """Custom formatter with detailed information."""
    
    def format(self, record):
        # Add custom fields
        record.module_name = record.module
        record.function_name = record.funcName
        record.line_number = record.lineno
        
        # Create detailed format
        detailed_format = (
            "%(asctime)s | %(levelname)-8s | %(name)s | "
            "%(module_name)s.%(function_name)s:%(line_number)d | %(message)s"
        )
        
        formatter = logging.Formatter(detailed_format)
        return formatter.format(record)

class JSONFormatter(logging.Formatter):
    """Custom formatter that outputs JSON format."""
    
    def format(self, record):
        log_entry = {
            'timestamp': datetime.fromtimestamp(record.created).isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno,
            'message': record.getMessage(),
        }
        
        # Add exception info if present
        if record.exc_info:
            log_entry['exception'] = self.formatException(record.exc_info)
        
        # Add extra fields
        for key, value in record.__dict__.items():
            if key not in ['name', 'msg', 'args', 'levelname', 'levelno', 'pathname',
                          'filename', 'module', 'lineno', 'funcName', 'created',
                          'msecs', 'relativeCreated', 'thread', 'threadName',
                          'processName', 'process', 'getMessage', 'exc_info',
                          'exc_text', 'stack_info']:
                log_entry[key] = value
        
        return json.dumps(log_entry)

# What we accomplished in this step:
# - Created DetailedFormatter for human-readable detailed logs
# - Created JSONFormatter for structured logging
# - Added custom fields and exception handling to formatters


# Step 3: Implement file and console handlers with rotation
# ===============================================================================

# Explanation:
# Handlers determine where log messages go. We'll create console and file handlers
# with different configurations and add log rotation for file management.

import logging
import sys
from datetime import datetime
import json
import os
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

# Basic logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Create a basic logger
basic_logger = logging.getLogger('basic_example')

# Demonstrate basic logging levels
def demonstrate_basic_logging():
    """Show different logging levels in action."""
    basic_logger.debug("This is a debug message")
    basic_logger.info("Application started successfully")
    basic_logger.warning("This is a warning message")
    basic_logger.error("An error occurred")
    basic_logger.critical("Critical system failure!")

class DetailedFormatter(logging.Formatter):
    """Custom formatter with detailed information."""
    
    def format(self, record):
        # Add custom fields
        record.module_name = record.module
        record.function_name = record.funcName
        record.line_number = record.lineno
        
        # Create detailed format
        detailed_format = (
            "%(asctime)s | %(levelname)-8s | %(name)s | "
            "%(module_name)s.%(function_name)s:%(line_number)d | %(message)s"
        )
        
        formatter = logging.Formatter(detailed_format)
        return formatter.format(record)

class JSONFormatter(logging.Formatter):
    """Custom formatter that outputs JSON format."""
    
    def format(self, record):
        log_entry = {
            'timestamp': datetime.fromtimestamp(record.created).isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno,
            'message': record.getMessage(),
        }
        
        # Add exception info if present
        if record.exc_info:
            log_entry['exception'] = self.formatException(record.exc_info)
        
        # Add extra fields
        for key, value in record.__dict__.items():
            if key not in ['name', 'msg', 'args', 'levelname', 'levelno', 'pathname',
                          'filename', 'module', 'lineno', 'funcName', 'created',
                          'msecs', 'relativeCreated', 'thread', 'threadName',
                          'processName', 'process', 'getMessage', 'exc_info',
                          'exc_text', 'stack_info']:
                log_entry[key] = value
        
        return json.dumps(log_entry)

def setup_application_logger(name='app', log_dir='logs'):
    """Set up a comprehensive logger with multiple handlers."""
    
    # Create logs directory if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Clear any existing handlers
    logger.handlers.clear()
    
    # Console handler with simple format
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(console_formatter)
    
    # File handler with detailed format and rotation
    file_handler = RotatingFileHandler(
        filename=os.path.join(log_dir, f'{name}.log'),
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(DetailedFormatter())
    
    # Error file handler for errors and critical messages
    error_handler = RotatingFileHandler(
        filename=os.path.join(log_dir, f'{name}_errors.log'),
        maxBytes=5*1024*1024,  # 5MB
        backupCount=3
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(DetailedFormatter())
    
    # JSON handler for structured logging
    json_handler = TimedRotatingFileHandler(
        filename=os.path.join(log_dir, f'{name}_structured.log'),
        when='midnight',
        interval=1,
        backupCount=7
    )
    json_handler.setLevel(logging.INFO)
    json_handler.setFormatter(JSONFormatter())
    
    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.addHandler(error_handler)
    logger.addHandler(json_handler)
    
    return logger

# What we accomplished in this step:
# - Created setup_application_logger function with multiple handlers
# - Added RotatingFileHandler for size-based log rotation
# - Added TimedRotatingFileHandler for time-based rotation
# - Configured different log levels for different handlers
# - Set up separate error log file for critical issues


# Step 4: Create error tracking and monitoring systems
# ===============================================================================

# Explanation:
# Error tracking helps monitor application health and identify issues.
# We'll create classes to track errors, performance metrics, and system health.

import logging
import sys
from datetime import datetime
import json
import os
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import traceback
import threading
from collections import defaultdict, deque
import time

# Basic logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Create a basic logger
basic_logger = logging.getLogger('basic_example')

# Demonstrate basic logging levels
def demonstrate_basic_logging():
    """Show different logging levels in action."""
    basic_logger.debug("This is a debug message")
    basic_logger.info("Application started successfully")
    basic_logger.warning("This is a warning message")
    basic_logger.error("An error occurred")
    basic_logger.critical("Critical system failure!")

class DetailedFormatter(logging.Formatter):
    """Custom formatter with detailed information."""
    
    def format(self, record):
        # Add custom fields
        record.module_name = record.module
        record.function_name = record.funcName
        record.line_number = record.lineno
        
        # Create detailed format
        detailed_format = (
            "%(asctime)s | %(levelname)-8s | %(name)s | "
            "%(module_name)s.%(function_name)s:%(line_number)d | %(message)s"
        )
        
        formatter = logging.Formatter(detailed_format)
        return formatter.format(record)

class JSONFormatter(logging.Formatter):
    """Custom formatter that outputs JSON format."""
    
    def format(self, record):
        log_entry = {
            'timestamp': datetime.fromtimestamp(record.created).isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno,
            'message': record.getMessage(),
        }
        
        # Add exception info if present
        if record.exc_info:
            log_entry['exception'] = self.formatException(record.exc_info)
        
        # Add extra fields
        for key, value in record.__dict__.items():
            if key not in ['name', 'msg', 'args', 'levelname', 'levelno', 'pathname',
                          'filename', 'module', 'lineno', 'funcName', 'created',
                          'msecs', 'relativeCreated', 'thread', 'threadName',
                          'processName', 'process', 'getMessage', 'exc_info',
                          'exc_text', 'stack_info']:
                log_entry[key] = value
        
        return json.dumps(log_entry)

def setup_application_logger(name='app', log_dir='logs'):
    """Set up a comprehensive logger with multiple handlers."""
    
    # Create logs directory if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Clear any existing handlers
    logger.handlers.clear()
    
    # Console handler with simple format
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(console_formatter)
    
    # File handler with detailed format and rotation
    file_handler = RotatingFileHandler(
        filename=os.path.join(log_dir, f'{name}.log'),
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(DetailedFormatter())
    
    # Error file handler for errors and critical messages
    error_handler = RotatingFileHandler(
        filename=os.path.join(log_dir, f'{name}_errors.log'),
        maxBytes=5*1024*1024,  # 5MB
        backupCount=3
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(DetailedFormatter())
    
    # JSON handler for structured logging
    json_handler = TimedRotatingFileHandler(
        filename=os.path.join(log_dir, f'{name}_structured.log'),
        when='midnight',
        interval=1,
        backupCount=7
    )
    json_handler.setLevel(logging.INFO)
    json_handler.setFormatter(JSONFormatter())
    
    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.addHandler(error_handler)
    logger.addHandler(json_handler)
    
    return logger

class ErrorTracker:
    """Track and monitor application errors."""
    
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)
        self.error_counts = defaultdict(int)
        self.recent_errors = deque(maxlen=100)
        self.lock = threading.Lock()
    
    def track_error(self, error, context=None):
        """Track an error occurrence."""
        with self.lock:
            error_key = f"{type(error).__name__}: {str(error)}"
            self.error_counts[error_key] += 1
            
            error_info = {
                'timestamp': datetime.now().isoformat(),
                'error_type': type(error).__name__,
                'error_message': str(error),
                'traceback': traceback.format_exc(),
                'context': context or {}
            }
            
            self.recent_errors.append(error_info)
            
            # Log the error
            self.logger.error(
                f"Error tracked: {error_key}",
                exc_info=True,
                extra={'error_context': context}
            )
    
    def get_error_summary(self):
        """Get summary of tracked errors."""
        with self.lock:
            return {
                'total_unique_errors': len(self.error_counts),
                'total_error_occurrences': sum(self.error_counts.values()),
                'most_common_errors': dict(sorted(
                    self.error_counts.items(),
                    key=lambda x: x[1],
                    reverse=True
                )[:10]),
                'recent_errors_count': len(self.recent_errors)
            }

class PerformanceMonitor:
    """Monitor application performance metrics."""
    
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)
        self.metrics = defaultdict(list)
        self.lock = threading.Lock()
    
    def record_timing(self, operation, duration):
        """Record timing for an operation."""
        with self.lock:
            self.metrics[operation].append({
                'timestamp': datetime.now().isoformat(),
                'duration': duration
            })
            
            # Keep only last 1000 measurements
            if len(self.metrics[operation]) > 1000:
                self.metrics[operation] = self.metrics[operation][-1000:]
            
            # Log slow operations
            if duration > 1.0:  # Log operations taking more than 1 second
                self.logger.warning(
                    f"Slow operation detected: {operation} took {duration:.2f}s"
                )
    
    def get_performance_summary(self):
        """Get performance metrics summary."""
        with self.lock:
            summary = {}
            for operation, timings in self.metrics.items():
                if timings:
                    durations = [t['duration'] for t in timings]
                    summary[operation] = {
                        'count': len(durations),
                        'avg_duration': sum(durations) / len(durations),
                        'max_duration': max(durations),
                        'min_duration': min(durations)
                    }
            return summary

# What we accomplished in this step:
# - Created ErrorTracker class to monitor and count errors
# - Added PerformanceMonitor class to track operation timings
# - Implemented thread-safe error and performance tracking
# - Added methods to get summaries and statistics


# Step 5: Demonstrate logging in exception handling with context
# ===============================================================================

# Explanation:
# Proper exception handling with logging provides valuable debugging information.
# We'll show how to log exceptions with context and structured data.

import logging
import sys
from datetime import datetime
import json
import os
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import traceback
import threading
from collections import defaultdict, deque
import time
from contextlib import contextmanager
from functools import wraps

# Basic logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Create a basic logger
basic_logger = logging.getLogger('basic_example')

# Demonstrate basic logging levels
def demonstrate_basic_logging():
    """Show different logging levels in action."""
    basic_logger.debug("This is a debug message")
    basic_logger.info("Application started successfully")
    basic_logger.warning("This is a warning message")
    basic_logger.error("An error occurred")
    basic_logger.critical("Critical system failure!")

class DetailedFormatter(logging.Formatter):
    """Custom formatter with detailed information."""
    
    def format(self, record):
        # Add custom fields
        record.module_name = record.module
        record.function_name = record.funcName
        record.line_number = record.lineno
        
        # Create detailed format
        detailed_format = (
            "%(asctime)s | %(levelname)-8s | %(name)s | "
            "%(module_name)s.%(function_name)s:%(line_number)d | %(message)s"
        )
        
        formatter = logging.Formatter(detailed_format)
        return formatter.format(record)

class JSONFormatter(logging.Formatter):
    """Custom formatter that outputs JSON format."""
    
    def format(self, record):
        log_entry = {
            'timestamp': datetime.fromtimestamp(record.created).isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno,
            'message': record.getMessage(),
        }
        
        # Add exception info if present
        if record.exc_info:
            log_entry['exception'] = self.formatException(record.exc_info)
        
        # Add extra fields
        for key, value in record.__dict__.items():
            if key not in ['name', 'msg', 'args', 'levelname', 'levelno', 'pathname',
                          'filename', 'module', 'lineno', 'funcName', 'created',
                          'msecs', 'relativeCreated', 'thread', 'threadName',
                          'processName', 'process', 'getMessage', 'exc_info',
                          'exc_text', 'stack_info']:
                log_entry[key] = value
        
        return json.dumps(log_entry)

def setup_application_logger(name='app', log_dir='logs'):
    """Set up a comprehensive logger with multiple handlers."""
    
    # Create logs directory if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Clear any existing handlers
    logger.handlers.clear()
    
    # Console handler with simple format
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(console_formatter)
    
    # File handler with detailed format and rotation
    file_handler = RotatingFileHandler(
        filename=os.path.join(log_dir, f'{name}.log'),
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(DetailedFormatter())
    
    # Error file handler for errors and critical messages
    error_handler = RotatingFileHandler(
        filename=os.path.join(log_dir, f'{name}_errors.log'),
        maxBytes=5*1024*1024,  # 5MB
        backupCount=3
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(DetailedFormatter())
    
    # JSON handler for structured logging
    json_handler = TimedRotatingFileHandler(
        filename=os.path.join(log_dir, f'{name}_structured.log'),
        when='midnight',
        interval=1,
        backupCount=7
    )
    json_handler.setLevel(logging.INFO)
    json_handler.setFormatter(JSONFormatter())
    
    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.addHandler(error_handler)
    logger.addHandler(json_handler)
    
    return logger

class ErrorTracker:
    """Track and monitor application errors."""
    
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)
        self.error_counts = defaultdict(int)
        self.recent_errors = deque(maxlen=100)
        self.lock = threading.Lock()
    
    def track_error(self, error, context=None):
        """Track an error occurrence."""
        with self.lock:
            error_key = f"{type(error).__name__}: {str(error)}"
            self.error_counts[error_key] += 1
            
            error_info = {
                'timestamp': datetime.now().isoformat(),
                'error_type': type(error).__name__,
                'error_message': str(error),
                'traceback': traceback.format_exc(),
                'context': context or {}
            }
            
            self.recent_errors.append(error_info)
            
            # Log the error
            self.logger.error(
                f"Error tracked: {error_key}",
                exc_info=True,
                extra={'error_context': context}
            )
    
    def get_error_summary(self):
        """Get summary of tracked errors."""
        with self.lock:
            return {
                'total_unique_errors': len(self.error_counts),
                'total_error_occurrences': sum(self.error_counts.values()),
                'most_common_errors': dict(sorted(
                    self.error_counts.items(),
                    key=lambda x: x[1],
                    reverse=True
                )[:10]),
                'recent_errors_count': len(self.recent_errors)
            }

class PerformanceMonitor:
    """Monitor application performance metrics."""
    
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)
        self.metrics = defaultdict(list)
        self.lock = threading.Lock()
    
    def record_timing(self, operation, duration):
        """Record timing for an operation."""
        with self.lock:
            self.metrics[operation].append({
                'timestamp': datetime.now().isoformat(),
                'duration': duration
            })
            
            # Keep only last 1000 measurements
            if len(self.metrics[operation]) > 1000:
                self.metrics[operation] = self.metrics[operation][-1000:]
            
            # Log slow operations
            if duration > 1.0:  # Log operations taking more than 1 second
                self.logger.warning(
                    f"Slow operation detected: {operation} took {duration:.2f}s"
                )
    
    def get_performance_summary(self):
        """Get performance metrics summary."""
        with self.lock:
            summary = {}
            for operation, timings in self.metrics.items():
                if timings:
                    durations = [t['duration'] for t in timings]
                    summary[operation] = {
                        'count': len(durations),
                        'avg_duration': sum(durations) / len(durations),
                        'max_duration': max(durations),
                        'min_duration': min(durations)
                    }
            return summary

@contextmanager
def log_context(logger, operation, **context):
    """Context manager for logging operations with timing and error handling."""
    start_time = time.time()
    logger.info(f"Starting operation: {operation}", extra=context)
    
    try:
        yield
        duration = time.time() - start_time
        logger.info(
            f"Completed operation: {operation} in {duration:.2f}s",
            extra={**context, 'duration': duration}
        )
    except Exception as e:
        duration = time.time() - start_time
        logger.error(
            f"Failed operation: {operation} after {duration:.2f}s - {str(e)}",
            exc_info=True,
            extra={**context, 'duration': duration, 'error': str(e)}
        )
        raise

def log_exceptions(logger=None):
    """Decorator to automatically log exceptions from functions."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_logger = logger or logging.getLogger(func.__module__)
            try:
                return func(*args, **kwargs)
            except Exception as e:
                func_logger.error(
                    f"Exception in {func.__name__}: {str(e)}",
                    exc_info=True,
                    extra={
                        'function': func.__name__,
                        'args': str(args)[:200],  # Limit arg length
                        'kwargs': str(kwargs)[:200]
                    }
                )
                raise
        return wrapper
    return decorator

# Example functions demonstrating exception logging
def risky_database_operation(user_id, operation_type):
    """Simulate a database operation that might fail."""
    logger = logging.getLogger(__name__)
    
    try:
        logger.info(
            f"Starting database operation: {operation_type}",
            extra={'user_id': user_id, 'operation': operation_type}
        )
        
        # Simulate different types of failures
        if operation_type == "invalid_user":
            raise ValueError(f"Invalid user ID: {user_id}")
        elif operation_type == "connection_error":
            raise ConnectionError("Database connection failed")
        elif operation_type == "timeout":
            raise TimeoutError("Operation timed out")
        
        # Simulate success
        logger.info(
            f"Database operation completed successfully",
            extra={'user_id': user_id, 'operation': operation_type}
        )
        return {"status": "success", "user_id": user_id}
        
    except ValueError as e:
        logger.error(
            f"Validation error in database operation",
            exc_info=True,
            extra={
                'user_id': user_id,
                'operation': operation_type,
                'error_type': 'validation'
            }
        )
        raise
    except (ConnectionError, TimeoutError) as e:
        logger.error(
            f"Infrastructure error in database operation",
            exc_info=True,
            extra={
                'user_id': user_id,
                'operation': operation_type,
                'error_type': 'infrastructure'
            }
        )
        raise
    except Exception as e:
        logger.critical(
            f"Unexpected error in database operation",
            exc_info=True,
            extra={
                'user_id': user_id,
                'operation': operation_type,
                'error_type': 'unexpected'
            }
        )
        raise

@log_exceptions()
def process_user_data(user_data):
    """Process user data with automatic exception logging."""
    if not isinstance(user_data, dict):
        raise TypeError("User data must be a dictionary")
    
    if 'email' not in user_data:
        raise KeyError("Email is required")
    
    # Simulate processing
    return {"processed": True, "email": user_data['email']}

# What we accomplished in this step:
# - Created log_context context manager for operation logging
# - Added log_exceptions decorator for automatic exception logging
# - Implemented example functions showing different exception types
# - Demonstrated structured logging with context information
# - Added timing and error tracking to operations


# Step 6: Complete application with comprehensive logging system
# ===============================================================================

# Explanation:
# Now we'll create a complete application class that integrates all our logging
# components and demonstrates real-world usage patterns.

import logging
import sys
from datetime import datetime
import json
import os
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import traceback
import threading
from collections import defaultdict, deque
import time
from contextlib import contextmanager
from functools import wraps

# Basic logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Create a basic logger
basic_logger = logging.getLogger('basic_example')

# Demonstrate basic logging levels
def demonstrate_basic_logging():
    """Show different logging levels in action."""
    basic_logger.debug("This is a debug message")
    basic_logger.info("Application started successfully")
    basic_logger.warning("This is a warning message")
    basic_logger.error("An error occurred")
    basic_logger.critical("Critical system failure!")

class DetailedFormatter(logging.Formatter):
    """Custom formatter with detailed information."""
    
    def format(self, record):
        # Add custom fields
        record.module_name = record.module
        record.function_name = record.funcName
        record.line_number = record.lineno
        
        # Create detailed format
        detailed_format = (
            "%(asctime)s | %(levelname)-8s | %(name)s | "
            "%(module_name)s.%(function_name)s:%(line_number)d | %(message)s"
        )
        
        formatter = logging.Formatter(detailed_format)
        return formatter.format(record)

class JSONFormatter(logging.Formatter):
    """Custom formatter that outputs JSON format."""
    
    def format(self, record):
        log_entry = {
            'timestamp': datetime.fromtimestamp(record.created).isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno,
            'message': record.getMessage(),
        }
        
        # Add exception info if present
        if record.exc_info:
            log_entry['exception'] = self.formatException(record.exc_info)
        
        # Add extra fields
        for key, value in record.__dict__.items():
            if key not in ['name', 'msg', 'args', 'levelname', 'levelno', 'pathname',
                          'filename', 'module', 'lineno', 'funcName', 'created',
                          'msecs', 'relativeCreated', 'thread', 'threadName',
                          'processName', 'process', 'getMessage', 'exc_info',
                          'exc_text', 'stack_info']:
                log_entry[key] = value
        
        return json.dumps(log_entry)

def setup_application_logger(name='app', log_dir='logs'):
    """Set up a comprehensive logger with multiple handlers."""
    
    # Create logs directory if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Clear any existing handlers
    logger.handlers.clear()
    
    # Console handler with simple format
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(console_formatter)
    
    # File handler with detailed format and rotation
    file_handler = RotatingFileHandler(
        filename=os.path.join(log_dir, f'{name}.log'),
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(DetailedFormatter())
    
    # Error file handler for errors and critical messages
    error_handler = RotatingFileHandler(
        filename=os.path.join(log_dir, f'{name}_errors.log'),
        maxBytes=5*1024*1024,  # 5MB
        backupCount=3
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(DetailedFormatter())
    
    # JSON handler for structured logging
    json_handler = TimedRotatingFileHandler(
        filename=os.path.join(log_dir, f'{name}_structured.log'),
        when='midnight',
        interval=1,
        backupCount=7
    )
    json_handler.setLevel(logging.INFO)
    json_handler.setFormatter(JSONFormatter())
    
    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.addHandler(error_handler)
    logger.addHandler(json_handler)
    
    return logger

class ErrorTracker:
    """Track and monitor application errors."""
    
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)
        self.error_counts = defaultdict(int)
        self.recent_errors = deque(maxlen=100)
        self.lock = threading.Lock()
    
    def track_error(self, error, context=None):
        """Track an error occurrence."""
        with self.lock:
            error_key = f"{type(error).__name__}: {str(error)}"
            self.error_counts[error_key] += 1
            
            error_info = {
                'timestamp': datetime.now().isoformat(),
                'error_type': type(error).__name__,
                'error_message': str(error),
                'traceback': traceback.format_exc(),
                'context': context or {}
            }
            
            self.recent_errors.append(error_info)
            
            # Log the error
            self.logger.error(
                f"Error tracked: {error_key}",
                exc_info=True,
                extra={'error_context': context}
            )
    
    def get_error_summary(self):
        """Get summary of tracked errors."""
        with self.lock:
            return {
                'total_unique_errors': len(self.error_counts),
                'total_error_occurrences': sum(self.error_counts.values()),
                'most_common_errors': dict(sorted(
                    self.error_counts.items(),
                    key=lambda x: x[1],
                    reverse=True
                )[:10]),
                'recent_errors_count': len(self.recent_errors)
            }

class PerformanceMonitor:
    """Monitor application performance metrics."""
    
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)
        self.metrics = defaultdict(list)
        self.lock = threading.Lock()
    
    def record_timing(self, operation, duration):
        """Record timing for an operation."""
        with self.lock:
            self.metrics[operation].append({
                'timestamp': datetime.now().isoformat(),
                'duration': duration
            })
            
            # Keep only last 1000 measurements
            if len(self.metrics[operation]) > 1000:
                self.metrics[operation] = self.metrics[operation][-1000:]
            
            # Log slow operations
            if duration > 1.0:  # Log operations taking more than 1 second
                self.logger.warning(
                    f"Slow operation detected: {operation} took {duration:.2f}s"
                )
    
    def get_performance_summary(self):
        """Get performance metrics summary."""
        with self.lock:
            summary = {}
            for operation, timings in self.metrics.items():
                if timings:
                    durations = [t['duration'] for t in timings]
                    summary[operation] = {
                        'count': len(durations),
                        'avg_duration': sum(durations) / len(durations),
                        'max_duration': max(durations),
                        'min_duration': min(durations)
                    }
            return summary

@contextmanager
def log_context(logger, operation, **context):
    """Context manager for logging operations with timing and error handling."""
    start_time = time.time()
    logger.info(f"Starting operation: {operation}", extra=context)
    
    try:
        yield
        duration = time.time() - start_time
        logger.info(
            f"Completed operation: {operation} in {duration:.2f}s",
            extra={**context, 'duration': duration}
        )
    except Exception as e:
        duration = time.time() - start_time
        logger.error(
            f"Failed operation: {operation} after {duration:.2f}s - {str(e)}",
            exc_info=True,
            extra={**context, 'duration': duration, 'error': str(e)}
        )
        raise

def log_exceptions(logger=None):
    """Decorator to automatically log exceptions from functions."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_logger = logger or logging.getLogger(func.__module__)
            try:
                return func(*args, **kwargs)
            except Exception as e:
                func_logger.error(
                    f"Exception in {func.__name__}: {str(e)}",
                    exc_info=True,
                    extra={
                        'function': func.__name__,
                        'args': str(args)[:200],  # Limit arg length
                        'kwargs': str(kwargs)[:200]
                    }
                )
                raise
        return wrapper
    return decorator

# Example functions demonstrating exception logging
def risky_database_operation(user_id, operation_type):
    """Simulate a database operation that might fail."""
    logger = logging.getLogger(__name__)
    
    try:
        logger.info(
            f"Starting database operation: {operation_type}",
            extra={'user_id': user_id, 'operation': operation_type}
        )
        
        # Simulate different types of failures
        if operation_type == "invalid_user":
            raise ValueError(f"Invalid user ID: {user_id}")
        elif operation_type == "connection_error":
            raise ConnectionError("Database connection failed")
        elif operation_type == "timeout":
            raise TimeoutError("Operation timed out")
        
        # Simulate success
        logger.info(
            f"Database operation completed successfully",
            extra={'user_id': user_id, 'operation': operation_type}
        )
        return {"status": "success", "user_id": user_id}
        
    except ValueError as e:
        logger.error(
            f"Validation error in database operation",
            exc_info=True,
            extra={
                'user_id': user_id,
                'operation': operation_type,
                'error_type': 'validation'
            }
        )
        raise
    except (ConnectionError, TimeoutError) as e:
        logger.error(
            f"Infrastructure error in database operation",
            exc_info=True,
            extra={
                'user_id': user_id,
                'operation': operation_type,
                'error_type': 'infrastructure'
            }
        )
        raise
    except Exception as e:
        logger.critical(
            f"Unexpected error in database operation",
            exc_info=True,
            extra={
                'user_id': user_id,
                'operation': operation_type,
                'error_type': 'unexpected'
            }
        )
        raise

@log_exceptions()
def process_user_data(user_data):
    """Process user data with automatic exception logging."""
    if not isinstance(user_data, dict):
        raise TypeError("User data must be a dictionary")
    
    if 'email' not in user_data:
        raise KeyError("Email is required")
    
    # Simulate processing
    return {"processed": True, "email": user_data['email']}

class LoggingApplication:
    """Complete application with comprehensive logging system."""
    
    def __init__(self, name='MyApp', log_dir='logs'):
        self.name = name
        self.logger = setup_application_logger(name, log_dir)
        self.error_tracker = ErrorTracker(self.logger)
        self.performance_monitor = PerformanceMonitor(self.logger)
        
        self.logger.info(f"Application {name} initialized")
    
    def run_operation(self, operation_name, operation_func, *args, **kwargs):
        """Run an operation with comprehensive logging and monitoring."""
        with log_context(self.logger, operation_name, **kwargs):
            start_time = time.time()
            try:
                result = operation_func(*args, **kwargs)
                duration = time.time() - start_time
                self.performance_monitor.record_timing(operation_name, duration)
                return result
            except Exception as e:
                duration = time.time() - start_time
                self.performance_monitor.record_timing(operation_name, duration)
                self.error_tracker.track_error(e, {
                    'operation': operation_name,
                    'args': str(args)[:100],
                    'kwargs': str(kwargs)[:100]
                })
                raise
    
    def get_health_status(self):
        """Get application health status."""
        error_summary = self.error_tracker.get_error_summary()
        performance_summary = self.performance_monitor.get_performance_summary()
        
        health_status = {
            'application': self.name,
            'timestamp': datetime.now().isoformat(),
            'errors': error_summary,
            'performance': performance_summary,
            'status': 'healthy' if error_summary['total_error_occurrences'] == 0 else 'degraded'
        }
        
        self.logger.info(
            f"Health check completed - Status: {health_status['status']}",
            extra={'health_status': health_status}
        )
        
        return health_status

# Demonstration function
def demonstrate_comprehensive_logging():
    """Demonstrate the complete logging system."""
    
    # Create application
    app = LoggingApplication('DemoApp')
    
    # Demonstrate successful operations
    print("=== Demonstrating successful operations ===")
    try:
        result = app.run_operation(
            'user_data_processing',
            process_user_data,
            {'email': 'user@example.com', 'name': 'John Doe'},
            user_id=123
        )
        print(f"Success: {result}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Demonstrate error scenarios
    print("\n=== Demonstrating error scenarios ===")
    error_scenarios = [
        ('invalid_user', 999),
        ('connection_error', 123),
        ('timeout', 456)
    ]
    
    for operation_type, user_id in error_scenarios:
        try:
            app.run_operation(
                'database_operation',
                risky_database_operation,
                user_id,
                operation_type,
                user_id=user_id
            )
        except Exception as e:
            print(f"Expected error for {operation_type}: {type(e).__name__}")
    
    # Show health status
    print("\n=== Application Health Status ===")
    health = app.get_health_status()
    print(json.dumps(health, indent=2))

# What we accomplished in this step:
# - Created LoggingApplication class integrating all components
# - Added comprehensive operation monitoring and error tracking
# - Implemented health status reporting
# - Created demonstration function showing real-world usage
# - Integrated all previous logging components into a cohesive system


# ===============================================================================
#                              FINAL DEMONSTRATION
# ===============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("COMPREHENSIVE ERROR LOGGING DEMONSTRATION")
    print("=" * 80)
    
    # Run basic logging demonstration
    print("\n1. Basic Logging Levels:")
    print("-" * 40)
    demonstrate_basic_logging()
    
    # Run comprehensive logging demonstration
    print("\n2. Comprehensive Application Logging:")
    print("-" * 40)
    demonstrate_comprehensive_logging()
    
    print("\n" + "=" * 80)
    print("DEMONSTRATION COMPLETE")
    print("=" * 80)
    print("\nCheck the 'logs' directory for generated log files:")
    print("- DemoApp.log (detailed logs)")
    print("- DemoApp_errors.log (error-only logs)")
    print("- DemoApp_structured.log (JSON format logs)")
    
    print("\nKey Learning Points:")
    print("- Use different log levels appropriately")
    print("- Structure your logs with context information")
    print("- Implement log rotation to manage file sizes")
    print("- Track errors and performance metrics")
    print("- Use decorators and context managers for automatic logging")
    print("- Create comprehensive logging systems for production applications")


# ===============================================================================
#                              SUMMARY AND BEST PRACTICES
# ===============================================================================

"""
COMPREHENSIVE ERROR LOGGING BEST PRACTICES SUMMARY:

1. LOGGING LEVELS:
   - DEBUG: Detailed diagnostic information
   - INFO: General application flow
   - WARNING: Something unexpected but not critical
   - ERROR: Serious problem that needs attention
   - CRITICAL: Very serious error that may abort the program

2. FORMATTERS:
   - Use detailed formatters for file logs
   - Use simple formatters for console output
   - Consider JSON formatters for structured logging
   - Include context information (module, function, line number)

3. HANDLERS:
   - Console handlers for immediate feedback
   - File handlers with rotation for persistent storage
   - Separate error handlers for critical issues
   - Consider remote handlers for centralized logging

4. ERROR TRACKING:
   - Track error frequencies and patterns
   - Store recent errors for debugging
   - Monitor application health metrics
   - Implement alerting for critical errors

5. PERFORMANCE MONITORING:
   - Track operation timing
   - Identify slow operations
   - Monitor system performance trends
   - Set up alerts for performance degradation

6. CONTEXT AND STRUCTURED LOGGING:
   - Include relevant context in log messages
   - Use extra fields for structured data
   - Implement correlation IDs for request tracking
   - Add user and session information where appropriate

7. EXCEPTION HANDLING:
   - Always log exceptions with full stack traces
   - Include context about what was being attempted
   - Categorize exceptions by type and severity
   - Implement proper exception chaining

8. LOG MANAGEMENT:
   - Implement log rotation to prevent disk space issues
   - Set appropriate retention policies
   - Consider log compression for archived files
   - Monitor log file sizes and growth rates

9. SECURITY CONSIDERATIONS:
   - Never log sensitive information (passwords, tokens)
   - Sanitize user input in log messages
   - Implement access controls for log files
   - Consider log encryption for sensitive applications

10. PRODUCTION DEPLOYMENT:
    - Use configuration files for logging setup
    - Implement different logging levels for different environments
    - Set up centralized logging for distributed systems
    - Monitor logging system health and performance

Remember: Good logging is essential for debugging, monitoring, and maintaining
production applications. Invest time in setting up comprehensive logging
systems early in your development process.
"""

