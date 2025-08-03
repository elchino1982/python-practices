"""Question: Implement comprehensive error recovery strategies for robust applications.

Create a system that demonstrates various error recovery techniques including
retry mechanisms, fallback strategies, circuit breakers, and graceful degradation.

Requirements:
1. Create retry mechanisms with exponential backoff
2. Implement fallback strategies for service failures
3. Create a circuit breaker pattern for external services
4. Implement graceful degradation techniques
5. Demonstrate error recovery in different scenarios

Example usage:
    service = ResilientService()
    result = service.process_with_recovery(data)
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
# - What types of errors can occur in applications?
# - How can you implement retry logic with backoff?
# - What is a circuit breaker and when should it open/close?
# - How can you provide fallback alternatives when services fail?
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


# Step 1: Import modules and create basic retry mechanism
# ===============================================================================

# Explanation:
# Error recovery starts with retry mechanisms. We'll create a basic retry
# decorator that can handle transient failures with exponential backoff.

import time
import random
import logging
from typing import Any, Callable, Optional, Type, Union
from functools import wraps
from enum import Enum

class RetryStrategy:
    """Configuration for retry behavior."""
    
    def __init__(self, 
                 max_attempts: int = 3,
                 base_delay: float = 1.0,
                 max_delay: float = 60.0,
                 exponential_base: float = 2.0,
                 jitter: bool = True):
        self.max_attempts = max_attempts
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.exponential_base = exponential_base
        self.jitter = jitter
    
    def get_delay(self, attempt: int) -> float:
        """Calculate delay for given attempt number."""
        delay = self.base_delay * (self.exponential_base ** (attempt - 1))
        delay = min(delay, self.max_delay)
        
        if self.jitter:
            # Add random jitter to prevent thundering herd
            delay *= (0.5 + random.random() * 0.5)
        
        return delay

def retry_with_backoff(strategy: RetryStrategy = None, 
                      exceptions: tuple = (Exception,)):
    """Decorator for retrying functions with exponential backoff."""
    if strategy is None:
        strategy = RetryStrategy()
    
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            
            for attempt in range(1, strategy.max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    
                    if attempt == strategy.max_attempts:
                        logging.error(f"Function {func.__name__} failed after {attempt} attempts")
                        raise e
                    
                    delay = strategy.get_delay(attempt)
                    logging.warning(f"Attempt {attempt} failed for {func.__name__}, retrying in {delay:.2f}s: {e}")
                    time.sleep(delay)
            
            # This should never be reached, but just in case
            raise last_exception
        
        return wrapper
    return decorator

# What we accomplished in this step:
# - Created RetryStrategy class to configure retry behavior
# - Implemented exponential backoff with jitter
# - Created retry decorator for easy application to functions


# Step 2: Implement Circuit Breaker Pattern
# ===============================================================================

# Explanation:
# Circuit breakers prevent cascading failures by stopping calls to failing services.
# They have three states: CLOSED (normal), OPEN (failing), HALF_OPEN (testing recovery).

import time
import random
import logging
from typing import Any, Callable, Optional, Type, Union
from functools import wraps
from enum import Enum

class RetryStrategy:
    """Configuration for retry behavior."""
    
    def __init__(self, 
                 max_attempts: int = 3,
                 base_delay: float = 1.0,
                 max_delay: float = 60.0,
                 exponential_base: float = 2.0,
                 jitter: bool = True):
        self.max_attempts = max_attempts
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.exponential_base = exponential_base
        self.jitter = jitter
    
    def get_delay(self, attempt: int) -> float:
        """Calculate delay for given attempt number."""
        delay = self.base_delay * (self.exponential_base ** (attempt - 1))
        delay = min(delay, self.max_delay)
        
        if self.jitter:
            # Add random jitter to prevent thundering herd
            delay *= (0.5 + random.random() * 0.5)
        
        return delay

def retry_with_backoff(strategy: RetryStrategy = None, 
                      exceptions: tuple = (Exception,)):
    """Decorator for retrying functions with exponential backoff."""
    if strategy is None:
        strategy = RetryStrategy()
    
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            
            for attempt in range(1, strategy.max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    
                    if attempt == strategy.max_attempts:
                        logging.error(f"Function {func.__name__} failed after {attempt} attempts")
                        raise e
                    
                    delay = strategy.get_delay(attempt)
                    logging.warning(f"Attempt {attempt} failed for {func.__name__}, retrying in {delay:.2f}s: {e}")
                    time.sleep(delay)
            
            # This should never be reached, but just in case
            raise last_exception
        
        return wrapper
    return decorator

class CircuitState(Enum):
    """Circuit breaker states."""
    CLOSED = "closed"      # Normal operation
    OPEN = "open"          # Failing, blocking calls
    HALF_OPEN = "half_open"  # Testing if service recovered

class CircuitBreakerOpenException(Exception):
    """Exception raised when circuit breaker is open."""
    pass

class CircuitBreaker:
    """Circuit breaker implementation for preventing cascading failures."""
    
    def __init__(self,
                 failure_threshold: int = 5,
                 recovery_timeout: float = 60.0,
                 expected_exception: Type[Exception] = Exception):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.expected_exception = expected_exception
        
        self.failure_count = 0
        self.last_failure_time = None
        self.state = CircuitState.CLOSED
    
    def call(self, func: Callable, *args, **kwargs) -> Any:
        """Execute function through circuit breaker."""
        if self.state == CircuitState.OPEN:
            if self._should_attempt_reset():
                self.state = CircuitState.HALF_OPEN
                logging.info("Circuit breaker moving to HALF_OPEN state")
            else:
                raise CircuitBreakerOpenException("Circuit breaker is OPEN")
        
        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        except self.expected_exception as e:
            self._on_failure()
            raise e
    
    def _should_attempt_reset(self) -> bool:
        """Check if enough time has passed to attempt reset."""
        return (self.last_failure_time and 
                time.time() - self.last_failure_time >= self.recovery_timeout)
    
    def _on_success(self):
        """Handle successful call."""
        self.failure_count = 0
        if self.state == CircuitState.HALF_OPEN:
            self.state = CircuitState.CLOSED
            logging.info("Circuit breaker reset to CLOSED state")
    
    def _on_failure(self):
        """Handle failed call."""
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if (self.state == CircuitState.CLOSED and 
            self.failure_count >= self.failure_threshold):
            self.state = CircuitState.OPEN
            logging.warning(f"Circuit breaker opened after {self.failure_count} failures")
        elif self.state == CircuitState.HALF_OPEN:
            self.state = CircuitState.OPEN
            logging.warning("Circuit breaker reopened during half-open test")

def circuit_breaker(failure_threshold: int = 5,
                   recovery_timeout: float = 60.0,
                   expected_exception: Type[Exception] = Exception):
    """Decorator for applying circuit breaker pattern."""
    breaker = CircuitBreaker(failure_threshold, recovery_timeout, expected_exception)
    
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            return breaker.call(func, *args, **kwargs)
        return wrapper
    return decorator

# What we accomplished in this step:
# - Created CircuitBreaker class with three states
# - Implemented failure tracking and automatic recovery
# - Added circuit breaker decorator for easy application


# Step 3: Implement Fallback Strategies
# ===============================================================================

# Explanation:
# Fallback strategies provide alternative responses when primary services fail.
# This includes cached responses, default values, or alternative service calls.

import time
import random
import logging
from typing import Any, Callable, Optional, Type, Union, Dict
from functools import wraps
from enum import Enum

class RetryStrategy:
    """Configuration for retry behavior."""
    
    def __init__(self, 
                 max_attempts: int = 3,
                 base_delay: float = 1.0,
                 max_delay: float = 60.0,
                 exponential_base: float = 2.0,
                 jitter: bool = True):
        self.max_attempts = max_attempts
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.exponential_base = exponential_base
        self.jitter = jitter
    
    def get_delay(self, attempt: int) -> float:
        """Calculate delay for given attempt number."""
        delay = self.base_delay * (self.exponential_base ** (attempt - 1))
        delay = min(delay, self.max_delay)
        
        if self.jitter:
            # Add random jitter to prevent thundering herd
            delay *= (0.5 + random.random() * 0.5)
        
        return delay

def retry_with_backoff(strategy: RetryStrategy = None, 
                      exceptions: tuple = (Exception,)):
    """Decorator for retrying functions with exponential backoff."""
    if strategy is None:
        strategy = RetryStrategy()
    
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            
            for attempt in range(1, strategy.max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    
                    if attempt == strategy.max_attempts:
                        logging.error(f"Function {func.__name__} failed after {attempt} attempts")
                        raise e
                    
                    delay = strategy.get_delay(attempt)
                    logging.warning(f"Attempt {attempt} failed for {func.__name__}, retrying in {delay:.2f}s: {e}")
                    time.sleep(delay)
            
            # This should never be reached, but just in case
            raise last_exception
        
        return wrapper
    return decorator

class CircuitState(Enum):
    """Circuit breaker states."""
    CLOSED = "closed"      # Normal operation
    OPEN = "open"          # Failing, blocking calls
    HALF_OPEN = "half_open"  # Testing if service recovered

class CircuitBreakerOpenException(Exception):
    """Exception raised when circuit breaker is open."""
    pass

class CircuitBreaker:
    """Circuit breaker implementation for preventing cascading failures."""
    
    def __init__(self,
                 failure_threshold: int = 5,
                 recovery_timeout: float = 60.0,
                 expected_exception: Type[Exception] = Exception):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.expected_exception = expected_exception
        
        self.failure_count = 0
        self.last_failure_time = None
        self.state = CircuitState.CLOSED
    
    def call(self, func: Callable, *args, **kwargs) -> Any:
        """Execute function through circuit breaker."""
        if self.state == CircuitState.OPEN:
            if self._should_attempt_reset():
                self.state = CircuitState.HALF_OPEN
                logging.info("Circuit breaker moving to HALF_OPEN state")
            else:
                raise CircuitBreakerOpenException("Circuit breaker is OPEN")
        
        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        except self.expected_exception as e:
            self._on_failure()
            raise e
    
    def _should_attempt_reset(self) -> bool:
        """Check if enough time has passed to attempt reset."""
        return (self.last_failure_time and 
                time.time() - self.last_failure_time >= self.recovery_timeout)
    
    def _on_success(self):
        """Handle successful call."""
        self.failure_count = 0
        if self.state == CircuitState.HALF_OPEN:
            self.state = CircuitState.CLOSED
            logging.info("Circuit breaker reset to CLOSED state")
    
    def _on_failure(self):
        """Handle failed call."""
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if (self.state == CircuitState.CLOSED and 
            self.failure_count >= self.failure_threshold):
            self.state = CircuitState.OPEN
            logging.warning(f"Circuit breaker opened after {self.failure_count} failures")
        elif self.state == CircuitState.HALF_OPEN:
            self.state = CircuitState.OPEN
            logging.warning("Circuit breaker reopened during half-open test")

def circuit_breaker(failure_threshold: int = 5,
                   recovery_timeout: float = 60.0,
                   expected_exception: Type[Exception] = Exception):
    """Decorator for applying circuit breaker pattern."""
    breaker = CircuitBreaker(failure_threshold, recovery_timeout, expected_exception)
    
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            return breaker.call(func, *args, **kwargs)
        return wrapper
    return decorator

class FallbackCache:
    """Simple cache for storing fallback values."""
    
    def __init__(self, ttl: float = 300.0):  # 5 minutes default TTL
        self.cache: Dict[str, tuple] = {}  # key -> (value, timestamp)
        self.ttl = ttl
    
    def get(self, key: str) -> Optional[Any]:
        """Get cached value if not expired."""
        if key in self.cache:
            value, timestamp = self.cache[key]
            if time.time() - timestamp < self.ttl:
                return value
            else:
                del self.cache[key]
        return None
    
    def set(self, key: str, value: Any):
        """Store value in cache with current timestamp."""
        self.cache[key] = (value, time.time())
    
    def clear(self):
        """Clear all cached values."""
        self.cache.clear()

class FallbackStrategy:
    """Manages fallback strategies for service failures."""
    
    def __init__(self):
        self.cache = FallbackCache()
        self.fallback_functions: Dict[str, Callable] = {}
        self.default_values: Dict[str, Any] = {}
    
    def register_fallback_function(self, key: str, fallback_func: Callable):
        """Register a fallback function for a specific operation."""
        self.fallback_functions[key] = fallback_func
    
    def register_default_value(self, key: str, default_value: Any):
        """Register a default value for a specific operation."""
        self.default_values[key] = default_value
    
    def execute_with_fallback(self, 
                            primary_func: Callable,
                            fallback_key: str,
                            cache_key: Optional[str] = None,
                            *args, **kwargs) -> Any:
        """Execute primary function with fallback strategies."""
        try:
            # Try primary function
            result = primary_func(*args, **kwargs)
            
            # Cache successful result
            if cache_key:
                self.cache.set(cache_key, result)
            
            return result
            
        except Exception as e:
            logging.warning(f"Primary function failed: {e}, attempting fallback")
            
            # Try cached result first
            if cache_key:
                cached_result = self.cache.get(cache_key)
                if cached_result is not None:
                    logging.info(f"Using cached result for {cache_key}")
                    return cached_result
            
            # Try registered fallback function
            if fallback_key in self.fallback_functions:
                try:
                    fallback_result = self.fallback_functions[fallback_key](*args, **kwargs)
                    logging.info(f"Using fallback function for {fallback_key}")
                    return fallback_result
                except Exception as fallback_error:
                    logging.error(f"Fallback function also failed: {fallback_error}")
            
            # Try default value
            if fallback_key in self.default_values:
                logging.info(f"Using default value for {fallback_key}")
                return self.default_values[fallback_key]
            
            # If all fallbacks fail, re-raise original exception
            raise e

def with_fallback(fallback_strategy: FallbackStrategy,
                 fallback_key: str,
                 cache_key: Optional[str] = None):
    """Decorator for applying fallback strategies."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            return fallback_strategy.execute_with_fallback(
                func, fallback_key, cache_key, *args, **kwargs
            )
        return wrapper
    return decorator

# What we accomplished in this step:
# - Created FallbackCache for storing temporary results
# - Implemented FallbackStrategy with multiple fallback options
# - Added support for cached results, fallback functions, and default values


# Step 4: Implement Graceful Degradation and Resilient Service
# ===============================================================================

# Explanation:
# Graceful degradation allows applications to continue operating with reduced
# functionality when some components fail. We'll create a comprehensive service
# that combines all recovery strategies.

import time
import random
import logging
from typing import Any, Callable, Optional, Type, Union, Dict, List
from functools import wraps
from enum import Enum
from dataclasses import dataclass

class RetryStrategy:
    """Configuration for retry behavior."""
    
    def __init__(self, 
                 max_attempts: int = 3,
                 base_delay: float = 1.0,
                 max_delay: float = 60.0,
                 exponential_base: float = 2.0,
                 jitter: bool = True):
        self.max_attempts = max_attempts
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.exponential_base = exponential_base
        self.jitter = jitter
    
    def get_delay(self, attempt: int) -> float:
        """Calculate delay for given attempt number."""
        delay = self.base_delay * (self.exponential_base ** (attempt - 1))
        delay = min(delay, self.max_delay)
        
        if self.jitter:
            # Add random jitter to prevent thundering herd
            delay *= (0.5 + random.random() * 0.5)
        
        return delay

def retry_with_backoff(strategy: RetryStrategy = None, 
                      exceptions: tuple = (Exception,)):
    """Decorator for retrying functions with exponential backoff."""
    if strategy is None:
        strategy = RetryStrategy()
    
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            
            for attempt in range(1, strategy.max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    
                    if attempt == strategy.max_attempts:
                        logging.error(f"Function {func.__name__} failed after {attempt} attempts")
                        raise e
                    
                    delay = strategy.get_delay(attempt)
                    logging.warning(f"Attempt {attempt} failed for {func.__name__}, retrying in {delay:.2f}s: {e}")
                    time.sleep(delay)
            
            # This should never be reached, but just in case
            raise last_exception
        
        return wrapper
    return decorator

class CircuitState(Enum):
    """Circuit breaker states."""
    CLOSED = "closed"      # Normal operation
    OPEN = "open"          # Failing, blocking calls
    HALF_OPEN = "half_open"  # Testing if service recovered

class CircuitBreakerOpenException(Exception):
    """Exception raised when circuit breaker is open."""
    pass

class CircuitBreaker:
    """Circuit breaker implementation for preventing cascading failures."""
    
    def __init__(self,
                 failure_threshold: int = 5,
                 recovery_timeout: float = 60.0,
                 expected_exception: Type[Exception] = Exception):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.expected_exception = expected_exception
        
        self.failure_count = 0
        self.last_failure_time = None
        self.state = CircuitState.CLOSED
    
    def call(self, func: Callable, *args, **kwargs) -> Any:
        """Execute function through circuit breaker."""
        if self.state == CircuitState.OPEN:
            if self._should_attempt_reset():
                self.state = CircuitState.HALF_OPEN
                logging.info("Circuit breaker moving to HALF_OPEN state")
            else:
                raise CircuitBreakerOpenException("Circuit breaker is OPEN")
        
        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        except self.expected_exception as e:
            self._on_failure()
            raise e
    
    def _should_attempt_reset(self) -> bool:
        """Check if enough time has passed to attempt reset."""
        return (self.last_failure_time and 
                time.time() - self.last_failure_time >= self.recovery_timeout)
    
    def _on_success(self):
        """Handle successful call."""
        self.failure_count = 0
        if self.state == CircuitState.HALF_OPEN:
            self.state = CircuitState.CLOSED
            logging.info("Circuit breaker reset to CLOSED state")
    
    def _on_failure(self):
        """Handle failed call."""
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if (self.state == CircuitState.CLOSED and 
            self.failure_count >= self.failure_threshold):
            self.state = CircuitState.OPEN
            logging.warning(f"Circuit breaker opened after {self.failure_count} failures")
        elif self.state == CircuitState.HALF_OPEN:
            self.state = CircuitState.OPEN
            logging.warning("Circuit breaker reopened during half-open test")

def circuit_breaker(failure_threshold: int = 5,
                   recovery_timeout: float = 60.0,
                   expected_exception: Type[Exception] = Exception):
    """Decorator for applying circuit breaker pattern."""
    breaker = CircuitBreaker(failure_threshold, recovery_timeout, expected_exception)
    
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            return breaker.call(func, *args, **kwargs)
        return wrapper
    return decorator

class FallbackCache:
    """Simple cache for storing fallback values."""
    
    def __init__(self, ttl: float = 300.0):  # 5 minutes default TTL
        self.cache: Dict[str, tuple] = {}  # key -> (value, timestamp)
        self.ttl = ttl
    
    def get(self, key: str) -> Optional[Any]:
        """Get cached value if not expired."""
        if key in self.cache:
            value, timestamp = self.cache[key]
            if time.time() - timestamp < self.ttl:
                return value
            else:
                del self.cache[key]
        return None
    
    def set(self, key: str, value: Any):
        """Store value in cache with current timestamp."""
        self.cache[key] = (value, time.time())
    
    def clear(self):
        """Clear all cached values."""
        self.cache.clear()

class FallbackStrategy:
    """Manages fallback strategies for service failures."""
    
    def __init__(self):
        self.cache = FallbackCache()
        self.fallback_functions: Dict[str, Callable] = {}
        self.default_values: Dict[str, Any] = {}
    
    def register_fallback_function(self, key: str, fallback_func: Callable):
        """Register a fallback function for a specific operation."""
        self.fallback_functions[key] = fallback_func
    
    def register_default_value(self, key: str, default_value: Any):
        """Register a default value for a specific operation."""
        self.default_values[key] = default_value
    
    def execute_with_fallback(self, 
                            primary_func: Callable,
                            fallback_key: str,
                            cache_key: Optional[str] = None,
                            *args, **kwargs) -> Any:
        """Execute primary function with fallback strategies."""
        try:
            # Try primary function
            result = primary_func(*args, **kwargs)
            
            # Cache successful result
            if cache_key:
                self.cache.set(cache_key, result)
            
            return result
            
        except Exception as e:
            logging.warning(f"Primary function failed: {e}, attempting fallback")
            
            # Try cached result first
            if cache_key:
                cached_result = self.cache.get(cache_key)
                if cached_result is not None:
                    logging.info(f"Using cached result for {cache_key}")
                    return cached_result
            
            # Try registered fallback function
            if fallback_key in self.fallback_functions:
                try:
                    fallback_result = self.fallback_functions[fallback_key](*args, **kwargs)
                    logging.info(f"Using fallback function for {fallback_key}")
                    return fallback_result
                except Exception as fallback_error:
                    logging.error(f"Fallback function also failed: {fallback_error}")
            
            # Try default value
            if fallback_key in self.default_values:
                logging.info(f"Using default value for {fallback_key}")
                return self.default_values[fallback_key]
            
            # If all fallbacks fail, re-raise original exception
            raise e

def with_fallback(fallback_strategy: FallbackStrategy,
                 fallback_key: str,
                 cache_key: Optional[str] = None):
    """Decorator for applying fallback strategies."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            return fallback_strategy.execute_with_fallback(
                func, fallback_key, cache_key, *args, **kwargs
            )
        return wrapper
    return decorator

@dataclass
class ServiceHealth:
    """Represents the health status of a service component."""
    name: str
    is_healthy: bool
    last_check: float
    error_count: int
    last_error: Optional[str] = None

class GracefulDegradationManager:
    """Manages graceful degradation of service functionality."""
    
    def __init__(self):
        self.service_health: Dict[str, ServiceHealth] = {}
        self.feature_flags: Dict[str, bool] = {}
        self.degradation_rules: Dict[str, List[str]] = {}  # service -> dependent features
    
    def register_service(self, service_name: str):
        """Register a service for health monitoring."""
        self.service_health[service_name] = ServiceHealth(
            name=service_name,
            is_healthy=True,
            last_check=time.time(),
            error_count=0
        )
    
    def register_feature(self, feature_name: str, enabled: bool = True):
        """Register a feature flag."""
        self.feature_flags[feature_name] = enabled
    
    def add_degradation_rule(self, service_name: str, dependent_features: List[str]):
        """Add rule for which features to disable when service fails."""
        self.degradation_rules[service_name] = dependent_features
    
    def report_service_error(self, service_name: str, error: str):
        """Report an error for a service."""
        if service_name in self.service_health:
            health = self.service_health[service_name]
            health.error_count += 1
            health.last_error = error
            health.last_check = time.time()
            
            # Mark as unhealthy if too many errors
            if health.error_count >= 3:
                health.is_healthy = False
                self._apply_degradation(service_name)
    
    def report_service_success(self, service_name: str):
        """Report successful operation for a service."""
        if service_name in self.service_health:
            health = self.service_health[service_name]
            health.error_count = max(0, health.error_count - 1)
            health.last_check = time.time()
            
            # Mark as healthy if errors are low
            if health.error_count == 0:
                health.is_healthy = True
                self._restore_features(service_name)
    
    def _apply_degradation(self, service_name: str):
        """Apply degradation rules for failed service."""
        if service_name in self.degradation_rules:
            for feature in self.degradation_rules[service_name]:
                if feature in self.feature_flags:
                    self.feature_flags[feature] = False
                    logging.warning(f"Disabled feature '{feature}' due to {service_name} failure")
    
    def _restore_features(self, service_name: str):
        """Restore features when service recovers."""
        if service_name in self.degradation_rules:
            for feature in self.degradation_rules[service_name]:
                if feature in self.feature_flags:
                    self.feature_flags[feature] = True
                    logging.info(f"Restored feature '{feature}' as {service_name} recovered")
    
    def is_feature_enabled(self, feature_name: str) -> bool:
        """Check if a feature is currently enabled."""
        return self.feature_flags.get(feature_name, False)
    
    def get_system_health(self) -> Dict[str, Any]:
        """Get overall system health status."""
        healthy_services = sum(1 for h in self.service_health.values() if h.is_healthy)
        total_services = len(self.service_health)
        enabled_features = sum(1 for f in self.feature_flags.values() if f)
        total_features = len(self.feature_flags)
        
        return {
            "healthy_services": f"{healthy_services}/{total_services}",
            "enabled_features": f"{enabled_features}/{total_features}",
            "services": {name: {"healthy": h.is_healthy, "errors": h.error_count} 
                        for name, h in self.service_health.items()},
            "features": self.feature_flags
        }

# What we accomplished in this step:
# - Created ServiceHealth dataclass for monitoring service status
# - Implemented GracefulDegradationManager for feature management
# - Added automatic feature disabling/enabling based on service health


# Step 5: Create Comprehensive Resilient Service
# ===============================================================================

# Explanation:
# Now we'll create a comprehensive service that combines all recovery strategies:
# retry, circuit breaker, fallback, and graceful degradation.

import time
import random
import logging
from typing import Any, Callable, Optional, Type, Union, Dict, List
from functools import wraps
from enum import Enum
from dataclasses import dataclass

class RetryStrategy:
    """Configuration for retry behavior."""
    
    def __init__(self, 
                 max_attempts: int = 3,
                 base_delay: float = 1.0,
                 max_delay: float = 60.0,
                 exponential_base: float = 2.0,
                 jitter: bool = True):
        self.max_attempts = max_attempts
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.exponential_base = exponential_base
        self.jitter = jitter
    
    def get_delay(self, attempt: int) -> float:
        """Calculate delay for given attempt number."""
        delay = self.base_delay * (self.exponential_base ** (attempt - 1))
        delay = min(delay, self.max_delay)
        
        if self.jitter:
            # Add random jitter to prevent thundering herd
            delay *= (0.5 + random.random() * 0.5)
        
        return delay

def retry_with_backoff(strategy: RetryStrategy = None, 
                      exceptions: tuple = (Exception,)):
    """Decorator for retrying functions with exponential backoff."""
    if strategy is None:
        strategy = RetryStrategy()
    
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            
            for attempt in range(1, strategy.max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    
                    if attempt == strategy.max_attempts:
                        logging.error(f"Function {func.__name__} failed after {attempt} attempts")
                        raise e
                    
                    delay = strategy.get_delay(attempt)
                    logging.warning(f"Attempt {attempt} failed for {func.__name__}, retrying in {delay:.2f}s: {e}")
                    time.sleep(delay)
            
            # This should never be reached, but just in case
            raise last_exception
        
        return wrapper
    return decorator

class CircuitState(Enum):
    """Circuit breaker states."""
    CLOSED = "closed"      # Normal operation
    OPEN = "open"          # Failing, blocking calls
    HALF_OPEN = "half_open"  # Testing if service recovered

class CircuitBreakerOpenException(Exception):
    """Exception raised when circuit breaker is open."""
    pass

class CircuitBreaker:
    """Circuit breaker implementation for preventing cascading failures."""
    
    def __init__(self,
                 failure_threshold: int = 5,
                 recovery_timeout: float = 60.0,
                 expected_exception: Type[Exception] = Exception):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.expected_exception = expected_exception
        
        self.failure_count = 0
        self.last_failure_time = None
        self.state = CircuitState.CLOSED
    
    def call(self, func: Callable, *args, **kwargs) -> Any:
        """Execute function through circuit breaker."""
        if self.state == CircuitState.OPEN:
            if self._should_attempt_reset():
                self.state = CircuitState.HALF_OPEN
                logging.info("Circuit breaker moving to HALF_OPEN state")
            else:
                raise CircuitBreakerOpenException("Circuit breaker is OPEN")
        
        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        except self.expected_exception as e:
            self._on_failure()
            raise e
    
    def _should_attempt_reset(self) -> bool:
        """Check if enough time has passed to attempt reset."""
        return (self.last_failure_time and 
                time.time() - self.last_failure_time >= self.recovery_timeout)
    
    def _on_success(self):
        """Handle successful call."""
        self.failure_count = 0
        if self.state == CircuitState.HALF_OPEN:
            self.state = CircuitState.CLOSED
            logging.info("Circuit breaker reset to CLOSED state")
    
    def _on_failure(self):
        """Handle failed call."""
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if (self.state == CircuitState.CLOSED and 
            self.failure_count >= self.failure_threshold):
            self.state = CircuitState.OPEN
            logging.warning(f"Circuit breaker opened after {self.failure_count} failures")
        elif self.state == CircuitState.HALF_OPEN:
            self.state = CircuitState.OPEN
            logging.warning("Circuit breaker reopened during half-open test")

def circuit_breaker(failure_threshold: int = 5,
                   recovery_timeout: float = 60.0,
                   expected_exception: Type[Exception] = Exception):
    """Decorator for applying circuit breaker pattern."""
    breaker = CircuitBreaker(failure_threshold, recovery_timeout, expected_exception)
    
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            return breaker.call(func, *args, **kwargs)
        return wrapper
    return decorator

class FallbackCache:
    """Simple cache for storing fallback values."""
    
    def __init__(self, ttl: float = 300.0):  # 5 minutes default TTL
        self.cache: Dict[str, tuple] = {}  # key -> (value, timestamp)
        self.ttl = ttl
    
    def get(self, key: str) -> Optional[Any]:
        """Get cached value if not expired."""
        if key in self.cache:
            value, timestamp = self.cache[key]
            if time.time() - timestamp < self.ttl:
                return value
            else:
                del self.cache[key]
        return None
    
    def set(self, key: str, value: Any):
        """Store value in cache with current timestamp."""
        self.cache[key] = (value, time.time())
    
    def clear(self):
        """Clear all cached values."""
        self.cache.clear()

class FallbackStrategy:
    """Manages fallback strategies for service failures."""
    
    def __init__(self):
        self.cache = FallbackCache()
        self.fallback_functions: Dict[str, Callable] = {}
        self.default_values: Dict[str, Any] = {}
    
    def register_fallback_function(self, key: str, fallback_func: Callable):
        """Register a fallback function for a specific operation."""
        self.fallback_functions[key] = fallback_func
    
    def register_default_value(self, key: str, default_value: Any):
        """Register a default value for a specific operation."""
        self.default_values[key] = default_value
    
    def execute_with_fallback(self, 
                            primary_func: Callable,
                            fallback_key: str,
                            cache_key: Optional[str] = None,
                            *args, **kwargs) -> Any:
        """Execute primary function with fallback strategies."""
        try:
            # Try primary function
            result = primary_func(*args, **kwargs)
            
            # Cache successful result
            if cache_key:
                self.cache.set(cache_key, result)
            
            return result
            
        except Exception as e:
            logging.warning(f"Primary function failed: {e}, attempting fallback")
            
            # Try cached result first
            if cache_key:
                cached_result = self.cache.get(cache_key)
                if cached_result is not None:
                    logging.info(f"Using cached result for {cache_key}")
                    return cached_result
            
            # Try registered fallback function
            if fallback_key in self.fallback_functions:
                try:
                    fallback_result = self.fallback_functions[fallback_key](*args, **kwargs)
                    logging.info(f"Using fallback function for {fallback_key}")
                    return fallback_result
                except Exception as fallback_error:
                    logging.error(f"Fallback function also failed: {fallback_error}")
            
            # Try default value
            if fallback_key in self.default_values:
                logging.info(f"Using default value for {fallback_key}")
                return self.default_values[fallback_key]
            
            # If all fallbacks fail, re-raise original exception
            raise e

def with_fallback(fallback_strategy: FallbackStrategy,
                 fallback_key: str,
                 cache_key: Optional[str] = None):
    """Decorator for applying fallback strategies."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            return fallback_strategy.execute_with_fallback(
                func, fallback_key, cache_key, *args, **kwargs
            )
        return wrapper
    return decorator

@dataclass
class ServiceHealth:
    """Represents the health status of a service component."""
    name: str
    is_healthy: bool
    last_check: float
    error_count: int
    last_error: Optional[str] = None

class GracefulDegradationManager:
    """Manages graceful degradation of service functionality."""
    
    def __init__(self):
        self.service_health: Dict[str, ServiceHealth] = {}
        self.feature_flags: Dict[str, bool] = {}
        self.degradation_rules: Dict[str, List[str]] = {}  # service -> dependent features
    
    def register_service(self, service_name: str):
        """Register a service for health monitoring."""
        self.service_health[service_name] = ServiceHealth(
            name=service_name,
            is_healthy=True,
            last_check=time.time(),
            error_count=0
        )
    
    def register_feature(self, feature_name: str, enabled: bool = True):
        """Register a feature flag."""
        self.feature_flags[feature_name] = enabled
    
    def add_degradation_rule(self, service_name: str, dependent_features: List[str]):
        """Add rule for which features to disable when service fails."""
        self.degradation_rules[service_name] = dependent_features
    
    def report_service_error(self, service_name: str, error: str):
        """Report an error for a service."""
        if service_name in self.service_health:
            health = self.service_health[service_name]
            health.error_count += 1
            health.last_error = error
            health.last_check = time.time()
            
            # Mark as unhealthy if too many errors
            if health.error_count >= 3:
                health.is_healthy = False
                self._apply_degradation(service_name)
    
    def report_service_success(self, service_name: str):
        """Report successful operation for a service."""
        if service_name in self.service_health:
            health = self.service_health[service_name]
            health.error_count = max(0, health.error_count - 1)
            health.last_check = time.time()
            
            # Mark as healthy if errors are low
            if health.error_count == 0:
                health.is_healthy = True
                self._restore_features(service_name)
    
    def _apply_degradation(self, service_name: str):
        """Apply degradation rules for failed service."""
        if service_name in self.degradation_rules:
            for feature in self.degradation_rules[service_name]:
                if feature in self.feature_flags:
                    self.feature_flags[feature] = False
                    logging.warning(f"Disabled feature '{feature}' due to {service_name} failure")
    
    def _restore_features(self, service_name: str):
        """Restore features when service recovers."""
        if service_name in self.degradation_rules:
            for feature in self.degradation_rules[service_name]:
                if feature in self.feature_flags:
                    self.feature_flags[feature] = True
                    logging.info(f"Restored feature '{feature}' as {service_name} recovered")
    
    def is_feature_enabled(self, feature_name: str) -> bool:
        """Check if a feature is currently enabled."""
        return self.feature_flags.get(feature_name, False)
    
    def get_system_health(self) -> Dict[str, Any]:
        """Get overall system health status."""
        healthy_services = sum(1 for h in self.service_health.values() if h.is_healthy)
        total_services = len(self.service_health)
        enabled_features = sum(1 for f in self.feature_flags.values() if f)
        total_features = len(self.feature_flags)
        
        return {
            "healthy_services": f"{healthy_services}/{total_services}",
            "enabled_features": f"{enabled_features}/{total_features}",
            "services": {name: {"healthy": h.is_healthy, "errors": h.error_count} 
                        for name, h in self.service_health.items()},
            "features": self.feature_flags
        }

class ResilientService:
    """Comprehensive service that combines all error recovery strategies."""
    
    def __init__(self):
        self.retry_strategy = RetryStrategy()
        self.circuit_breaker = CircuitBreaker()
        self.fallback_strategy = FallbackStrategy()
        self.degradation_manager = GracefulDegradationManager()
        
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Initialize services and features
        self._setup_services()
    
    def _setup_services(self):
        """Initialize service monitoring and fallback strategies."""
        # Register services
        self.degradation_manager.register_service("database")
        self.degradation_manager.register_service("external_api")
        self.degradation_manager.register_service("cache")
        
        # Register features
        self.degradation_manager.register_feature("advanced_analytics", True)
        self.degradation_manager.register_feature("real_time_updates", True)
        self.degradation_manager.register_feature("personalization", True)
        
        # Setup degradation rules
        self.degradation_manager.add_degradation_rule("database", ["advanced_analytics"])
        self.degradation_manager.add_degradation_rule("external_api", ["real_time_updates"])
        self.degradation_manager.add_degradation_rule("cache", ["personalization"])
        
        # Register fallback functions
        self.fallback_strategy.register_fallback_function(
            "user_data", self._get_default_user_data
        )
        self.fallback_strategy.register_default_value("weather", "Sunny, 72°F")
    
    def _get_default_user_data(self, user_id: str) -> Dict[str, Any]:
        """Fallback function for user data."""
        return {
            "id": user_id,
            "name": "Guest User",
            "preferences": {"theme": "default"},
            "source": "fallback"
        }
    
    def process_with_recovery(self, operation: str, *args, **kwargs) -> Any:
        """Process operation with full error recovery strategies."""
        service_name = kwargs.get('service', 'unknown')
        
        try:
            # Check if feature is enabled
            if 'feature' in kwargs:
                feature = kwargs['feature']
                if not self.degradation_manager.is_feature_enabled(feature):
                    self.logger.info(f"Feature {feature} is disabled, using degraded response")
                    return self._get_degraded_response(operation)
            
            # Execute with circuit breaker and retry
            result = self._execute_with_protection(operation, *args, **kwargs)
            
            # Report success
            if service_name != 'unknown':
                self.degradation_manager.report_service_success(service_name)
            
            return result
            
        except Exception as e:
            # Report failure
            if service_name != 'unknown':
                self.degradation_manager.report_service_error(service_name, str(e))
            
            # Try fallback strategies
            try:
                return self.fallback_strategy.execute_with_fallback(
                    self._execute_operation,
                    operation,
                    f"{operation}_{hash(str(args) + str(kwargs))}",
                    operation, *args, **kwargs
                )
            except Exception:
                # Final fallback - return degraded response
                self.logger.error(f"All recovery strategies failed for {operation}")
                return self._get_degraded_response(operation)
    
    def _execute_with_protection(self, operation: str, *args, **kwargs) -> Any:
        """Execute operation with circuit breaker and retry protection."""
        @retry_with_backoff(self.retry_strategy)
        def protected_operation():
            return self.circuit_breaker.call(self._execute_operation, operation, *args, **kwargs)
        
        return protected_operation()
    
    def _execute_operation(self, operation: str, *args, **kwargs) -> Any:
        """Simulate different operations that might fail."""
        # Simulate random failures for demonstration
        if random.random() < 0.3:  # 30% failure rate
            raise Exception(f"Simulated failure in {operation}")
        
        # Simulate different operations
        if operation == "get_user_data":
            user_id = args[0] if args else "unknown"
            return {
                "id": user_id,
                "name": f"User {user_id}",
                "preferences": {"theme": "dark", "language": "en"},
                "source": "primary"
            }
        elif operation == "get_weather":
            return "Partly cloudy, 68°F"
        elif operation == "get_analytics":
            return {"page_views": 1234, "unique_visitors": 567}
        else:
            return f"Result for {operation}"
    
    def _get_degraded_response(self, operation: str) -> Any:
        """Provide degraded response when all else fails."""
        degraded_responses = {
            "get_user_data": {"id": "guest", "name": "Guest", "source": "degraded"},
            "get_weather": "Weather unavailable",
            "get_analytics": {"message": "Analytics temporarily unavailable"}
        }
        return degraded_responses.get(operation, f"Service temporarily unavailable for {operation}")
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get comprehensive system status."""
        return {
            "circuit_breaker": {
                "state": self.circuit_breaker.state.value,
                "failure_count": self.circuit_breaker.failure_count
            },
            "system_health": self.degradation_manager.get_system_health(),
            "cache_size": len(self.fallback_strategy.cache.cache)
        }

# What we accomplished in this step:
# - Created ResilientService that combines all recovery strategies
# - Implemented comprehensive error handling with multiple fallback layers
# - Added system status monitoring and health reporting


# Step 6: Demonstration and Testing Examples
# ===============================================================================

# Explanation:
# Let's demonstrate how to use all the error recovery strategies we've built
# and provide comprehensive examples for testing the resilient system.

import time
import random
import logging
from typing import Any, Callable, Optional, Type, Union, Dict, List
from functools import wraps
from enum import Enum
from dataclasses import dataclass

class RetryStrategy:
    """Configuration for retry behavior."""
    
    def __init__(self, 
                 max_attempts: int = 3,
                 base_delay: float = 1.0,
                 max_delay: float = 60.0,
                 exponential_base: float = 2.0,
                 jitter: bool = True):
        self.max_attempts = max_attempts
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.exponential_base = exponential_base
        self.jitter = jitter
    
    def get_delay(self, attempt: int) -> float:
        """Calculate delay for given attempt number."""
        delay = self.base_delay * (self.exponential_base ** (attempt - 1))
        delay = min(delay, self.max_delay)
        
        if self.jitter:
            # Add random jitter to prevent thundering herd
            delay *= (0.5 + random.random() * 0.5)
        
        return delay

def retry_with_backoff(strategy: RetryStrategy = None, 
                      exceptions: tuple = (Exception,)):
    """Decorator for retrying functions with exponential backoff."""
    if strategy is None:
        strategy = RetryStrategy()
    
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            
            for attempt in range(1, strategy.max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    
                    if attempt == strategy.max_attempts:
                        logging.error(f"Function {func.__name__} failed after {attempt} attempts")
                        raise e
                    
                    delay = strategy.get_delay(attempt)
                    logging.warning(f"Attempt {attempt} failed for {func.__name__}, retrying in {delay:.2f}s: {e}")
                    time.sleep(delay)
            
            # This should never be reached, but just in case
            raise last_exception
        
        return wrapper
    return decorator

class CircuitState(Enum):
    """Circuit breaker states."""
    CLOSED = "closed"      # Normal operation
    OPEN = "open"          # Failing, blocking calls
    HALF_OPEN = "half_open"  # Testing if service recovered

class CircuitBreakerOpenException(Exception):
    """Exception raised when circuit breaker is open."""
    pass

class CircuitBreaker:
    """Circuit breaker implementation for preventing cascading failures."""
    
    def __init__(self,
                 failure_threshold: int = 5,
                 recovery_timeout: float = 60.0,
                 expected_exception: Type[Exception] = Exception):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.expected_exception = expected_exception
        
        self.failure_count = 0
        self.last_failure_time = None
        self.state = CircuitState.CLOSED
    
    def call(self, func: Callable, *args, **kwargs) -> Any:
        """Execute function through circuit breaker."""
        if self.state == CircuitState.OPEN:
            if self._should_attempt_reset():
                self.state = CircuitState.HALF_OPEN
                logging.info("Circuit breaker moving to HALF_OPEN state")
            else:
                raise CircuitBreakerOpenException("Circuit breaker is OPEN")
        
        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        except self.expected_exception as e:
            self._on_failure()
            raise e
    
    def _should_attempt_reset(self) -> bool:
        """Check if enough time has passed to attempt reset."""
        return (self.last_failure_time and 
                time.time() - self.last_failure_time >= self.recovery_timeout)
    
    def _on_success(self):
        """Handle successful call."""
        self.failure_count = 0
        if self.state == CircuitState.HALF_OPEN:
            self.state = CircuitState.CLOSED
            logging.info("Circuit breaker reset to CLOSED state")
    
    def _on_failure(self):
        """Handle failed call."""
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if (self.state == CircuitState.CLOSED and 
            self.failure_count >= self.failure_threshold):
            self.state = CircuitState.OPEN
            logging.warning(f"Circuit breaker opened after {self.failure_count} failures")
        elif self.state == CircuitState.HALF_OPEN:
            self.state = CircuitState.OPEN
            logging.warning("Circuit breaker reopened during half-open test")

def circuit_breaker(failure_threshold: int = 5,
                   recovery_timeout: float = 60.0,
                   expected_exception: Type[Exception] = Exception):
    """Decorator for applying circuit breaker pattern."""
    breaker = CircuitBreaker(failure_threshold, recovery_timeout, expected_exception)
    
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            return breaker.call(func, *args, **kwargs)
        return wrapper
    return decorator

class FallbackCache:
    """Simple cache for storing fallback values."""
    
    def __init__(self, ttl: float = 300.0):  # 5 minutes default TTL
        self.cache: Dict[str, tuple] = {}  # key -> (value, timestamp)
        self.ttl = ttl
    
    def get(self, key: str) -> Optional[Any]:
        """Get cached value if not expired."""
        if key in self.cache:
            value, timestamp = self.cache[key]
            if time.time() - timestamp < self.ttl:
                return value
            else:
                del self.cache[key]
        return None
    
    def set(self, key: str, value: Any):
        """Store value in cache with current timestamp."""
        self.cache[key] = (value, time.time())
    
    def clear(self):
        """Clear all cached values."""
        self.cache.clear()

class FallbackStrategy:
    """Manages fallback strategies for service failures."""
    
    def __init__(self):
        self.cache = FallbackCache()
        self.fallback_functions: Dict[str, Callable] = {}
        self.default_values: Dict[str, Any] = {}
    
    def register_fallback_function(self, key: str, fallback_func: Callable):
        """Register a fallback function for a specific operation."""
        self.fallback_functions[key] = fallback_func
    
    def register_default_value(self, key: str, default_value: Any):
        """Register a default value for a specific operation."""
        self.default_values[key] = default_value
    
    def execute_with_fallback(self, 
                            primary_func: Callable,
                            fallback_key: str,
                            cache_key: Optional[str] = None,
                            *args, **kwargs) -> Any:
        """Execute primary function with fallback strategies."""
        try:
            # Try primary function
            result = primary_func(*args, **kwargs)
            
            # Cache successful result
            if cache_key:
                self.cache.set(cache_key, result)
            
            return result
            
        except Exception as e:
            logging.warning(f"Primary function failed: {e}, attempting fallback")
            
            # Try cached result first
            if cache_key:
                cached_result = self.cache.get(cache_key)
                if cached_result is not None:
                    logging.info(f"Using cached result for {cache_key}")
                    return cached_result
            
            # Try registered fallback function
            if fallback_key in self.fallback_functions:
                try:
                    fallback_result = self.fallback_functions[fallback_key](*args, **kwargs)
                    logging.info(f"Using fallback function for {fallback_key}")
                    return fallback_result
                except Exception as fallback_error:
                    logging.error(f"Fallback function also failed: {fallback_error}")
            
            # Try default value
            if fallback_key in self.default_values:
                logging.info(f"Using default value for {fallback_key}")
                return self.default_values[fallback_key]
            
            # If all fallbacks fail, re-raise original exception
            raise e

def with_fallback(fallback_strategy: FallbackStrategy,
                 fallback_key: str,
                 cache_key: Optional[str] = None):
    """Decorator for applying fallback strategies."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            return fallback_strategy.execute_with_fallback(
                func, fallback_key, cache_key, *args, **kwargs
            )
        return wrapper
    return decorator

@dataclass
class ServiceHealth:
    """Represents the health status of a service component."""
    name: str
    is_healthy: bool
    last_check: float
    error_count: int
    last_error: Optional[str] = None

class GracefulDegradationManager:
    """Manages graceful degradation of service functionality."""
    
    def __init__(self):
        self.service_health: Dict[str, ServiceHealth] = {}
        self.feature_flags: Dict[str, bool] = {}
        self.degradation_rules: Dict[str, List[str]] = {}  # service -> dependent features
    
    def register_service(self, service_name: str):
        """Register a service for health monitoring."""
        self.service_health[service_name] = ServiceHealth(
            name=service_name,
            is_healthy=True,
            last_check=time.time(),
            error_count=0
        )
    
    def register_feature(self, feature_name: str, enabled: bool = True):
        """Register a feature flag."""
        self.feature_flags[feature_name] = enabled
    
    def add_degradation_rule(self, service_name: str, dependent_features: List[str]):
        """Add rule for which features to disable when service fails."""
        self.degradation_rules[service_name] = dependent_features
    
    def report_service_error(self, service_name: str, error: str):
        """Report an error for a service."""
        if service_name in self.service_health:
            health = self.service_health[service_name]
            health.error_count += 1
            health.last_error = error
            health.last_check = time.time()
            
            # Mark as unhealthy if too many errors
            if health.error_count >= 3:
                health.is_healthy = False
                self._apply_degradation(service_name)
    
    def report_service_success(self, service_name: str):
        """Report successful operation for a service."""
        if service_name in self.service_health:
            health = self.service_health[service_name]
            health.error_count = max(0, health.error_count - 1)
            health.last_check = time.time()
            
            # Mark as healthy if errors are low
            if health.error_count == 0:
                health.is_healthy = True
                self._restore_features(service_name)
    
    def _apply_degradation(self, service_name: str):
        """Apply degradation rules for failed service."""
        if service_name in self.degradation_rules:
            for feature in self.degradation_rules[service_name]:
                if feature in self.feature_flags:
                    self.feature_flags[feature] = False
                    logging.warning(f"Disabled feature '{feature}' due to {service_name} failure")
    
    def _restore_features(self, service_name: str):
        """Restore features when service recovers."""
        if service_name in self.degradation_rules:
            for feature in self.degradation_rules[service_name]:
                if feature in self.feature_flags:
                    self.feature_flags[feature] = True
                    logging.info(f"Restored feature '{feature}' as {service_name} recovered")
    
    def is_feature_enabled(self, feature_name: str) -> bool:
        """Check if a feature is currently enabled."""
        return self.feature_flags.get(feature_name, False)
    
    def get_system_health(self) -> Dict[str, Any]:
        """Get overall system health status."""
        healthy_services = sum(1 for h in self.service_health.values() if h.is_healthy)
        total_services = len(self.service_health)
        enabled_features = sum(1 for f in self.feature_flags.values() if f)
        total_features = len(self.feature_flags)
        
        return {
            "healthy_services": f"{healthy_services}/{total_services}",
            "enabled_features": f"{enabled_features}/{total_features}",
            "services": {name: {"healthy": h.is_healthy, "errors": h.error_count} 
                        for name, h in self.service_health.items()},
            "features": self.feature_flags
        }

class ResilientService:
    """Comprehensive service that combines all error recovery strategies."""
    
    def __init__(self):
        self.retry_strategy = RetryStrategy()
        self.circuit_breaker = CircuitBreaker()
        self.fallback_strategy = FallbackStrategy()
        self.degradation_manager = GracefulDegradationManager()
        
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Initialize services and features
        self._setup_services()
    
    def _setup_services(self):
        """Initialize service monitoring and fallback strategies."""
        # Register services
        self.degradation_manager.register_service("database")
        self.degradation_manager.register_service("external_api")
        self.degradation_manager.register_service("cache")
        
        # Register features
        self.degradation_manager.register_feature("advanced_analytics", True)
        self.degradation_manager.register_feature("real_time_updates", True)
        self.degradation_manager.register_feature("personalization", True)
        
        # Setup degradation rules
        self.degradation_manager.add_degradation_rule("database", ["advanced_analytics"])
        self.degradation_manager.add_degradation_rule("external_api", ["real_time_updates"])
        self.degradation_manager.add_degradation_rule("cache", ["personalization"])
        
        # Register fallback functions
        self.fallback_strategy.register_fallback_function(
            "user_data", self._get_default_user_data
        )
        self.fallback_strategy.register_default_value("weather", "Sunny, 72°F")
    
    def _get_default_user_data(self, user_id: str) -> Dict[str, Any]:
        """Fallback function for user data."""
        return {
            "id": user_id,
            "name": "Guest User",
            "preferences": {"theme": "default"},
            "source": "fallback"
        }
    
    def process_with_recovery(self, operation: str, *args, **kwargs) -> Any:
        """Process operation with full error recovery strategies."""
        service_name = kwargs.get('service', 'unknown')
        
        try:
            # Check if feature is enabled
            if 'feature' in kwargs:
                feature = kwargs['feature']
                if not self.degradation_manager.is_feature_enabled(feature):
                    self.logger.info(f"Feature {feature} is disabled, using degraded response")
                    return self._get_degraded_response(operation)
            
            # Execute with circuit breaker and retry
            result = self._execute_with_protection(operation, *args, **kwargs)
            
            # Report success
            if service_name != 'unknown':
                self.degradation_manager.report_service_success(service_name)
            
            return result
            
        except Exception as e:
            # Report failure
            if service_name != 'unknown':
                self.degradation_manager.report_service_error(service_name, str(e))
            
            # Try fallback strategies
            try:
                return self.fallback_strategy.execute_with_fallback(
                    self._execute_operation,
                    operation,
                    f"{operation}_{hash(str(args) + str(kwargs))}",
                    operation, *args, **kwargs
                )
            except Exception:
                # Final fallback - return degraded response
                self.logger.error(f"All recovery strategies failed for {operation}")
                return self._get_degraded_response(operation)
    
    def _execute_with_protection(self, operation: str, *args, **kwargs) -> Any:
        """Execute operation with circuit breaker and retry protection."""
        @retry_with_backoff(self.retry_strategy)
        def protected_operation():
            return self.circuit_breaker.call(self._execute_operation, operation, *args, **kwargs)
        
        return protected_operation()
    
    def _execute_operation(self, operation: str, *args, **kwargs) -> Any:
        """Simulate different operations that might fail."""
        # Simulate random failures for demonstration
        if random.random() < 0.3:  # 30% failure rate
            raise Exception(f"Simulated failure in {operation}")
        
        # Simulate different operations
        if operation == "get_user_data":
            user_id = args[0] if args else "unknown"
            return {
                "id": user_id,
                "name": f"User {user_id}",
                "preferences": {"theme": "dark", "language": "en"},
                "source": "primary"
            }
        elif operation == "get_weather":
            return "Partly cloudy, 68°F"
        elif operation == "get_analytics":
            return {"page_views": 1234, "unique_visitors": 567}
        else:
            return f"Result for {operation}"
    
    def _get_degraded_response(self, operation: str) -> Any:
        """Provide degraded response when all else fails."""
        degraded_responses = {
            "get_user_data": {"id": "guest", "name": "Guest", "source": "degraded"},
            "get_weather": "Weather unavailable",
            "get_analytics": {"message": "Analytics temporarily unavailable"}
        }
        return degraded_responses.get(operation, f"Service temporarily unavailable for {operation}")
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get comprehensive system status."""
        return {
            "circuit_breaker": {
                "state": self.circuit_breaker.state.value,
                "failure_count": self.circuit_breaker.failure_count
            },
            "system_health": self.degradation_manager.get_system_health(),
            "cache_size": len(self.fallback_strategy.cache.cache)
        }

def demonstrate_error_recovery():
    """Comprehensive demonstration of error recovery strategies."""
    print("=" * 80)
    print("ERROR RECOVERY STRATEGIES DEMONSTRATION")
    print("=" * 80)
    
    # Create resilient service
    service = ResilientService()
    
    print("\n1. Testing normal operation:")
    print("-" * 40)
    try:
        result = service.process_with_recovery("get_user_data", "user123")
        print(f"✓ User data: {result}")
    except Exception as e:
        print(f"✗ Failed: {e}")
    
    print("\n2. Testing with service failures:")
    print("-" * 40)
    for i in range(5):
        try:
            result = service.process_with_recovery("get_weather", service="external_api")
            print(f"✓ Attempt {i+1}: {result}")
        except Exception as e:
            print(f"✗ Attempt {i+1} failed: {e}")
    
    print("\n3. System health status:")
    print("-" * 40)
    status = service.get_system_status()
    print(f"Circuit breaker state: {status['circuit_breaker']['state']}")
    print(f"System health: {status['system_health']}")
    
    print("\n4. Testing individual strategies:")
    print("-" * 40)
    
    # Test retry mechanism
    @retry_with_backoff(RetryStrategy(max_attempts=3, base_delay=0.1))
    def flaky_function():
        if random.random() < 0.7:
            raise Exception("Random failure")
        return "Success!"
    
    try:
        result = flaky_function()
        print(f"✓ Retry test: {result}")
    except Exception as e:
        print(f"✗ Retry test failed: {e}")
    
    # Test circuit breaker
    breaker = CircuitBreaker(failure_threshold=2, recovery_timeout=1.0)
    
    def failing_service():
        raise Exception("Service down")
    
    print("\n5. Circuit breaker test:")
    for i in range(5):
        try:
            breaker.call(failing_service)
            print(f"✓ Call {i+1}: Success")
        except CircuitBreakerOpenException:
            print(f"⚡ Call {i+1}: Circuit breaker is OPEN")
        except Exception as e:
            print(f"✗ Call {i+1}: {e}")
    
    print("\n6. Fallback strategy test:")
    print("-" * 40)
    fallback = FallbackStrategy()
    fallback.register_default_value("test", "Default response")
    
    def unreliable_service():
        raise Exception("Service unavailable")
    
    try:
        result = fallback.execute_with_fallback(unreliable_service, "test")
        print(f"✓ Fallback result: {result}")
    except Exception as e:
        print(f"✗ Fallback failed: {e}")
    
    print("\n" + "=" * 80)
    print("DEMONSTRATION COMPLETE")
    print("=" * 80)

# Example usage and testing
if __name__ == "__main__":
    demonstrate_error_recovery()

# What we accomplished in this step:
# - Created comprehensive demonstration of all error recovery strategies
# - Provided practical examples of retry, circuit breaker, fallback, and degradation
# - Showed how to combine all strategies in a resilient service
# - Added testing examples for individual components
