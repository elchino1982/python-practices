"""Question: Implement comprehensive XSS (Cross-Site Scripting) prevention techniques.

Create a secure web input handler that can sanitize and validate user inputs
to prevent XSS attacks in web applications.

Requirements:
1. Create input sanitization functions for different contexts
2. Implement HTML entity encoding
3. Create content security policy helpers
4. Implement input validation with whitelisting
5. Demonstrate safe output rendering techniques

Example usage:
    sanitizer = XSSSanitizer()
    safe_html = sanitizer.sanitize_html(user_input)
    safe_js = sanitizer.sanitize_javascript(user_script)
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
# - What are the different contexts where XSS can occur? (HTML, JavaScript, CSS, URLs)
# - How do you encode special characters safely?
# - What input validation strategies prevent malicious scripts?
# - How can Content Security Policy help?
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


# Step 1: Import modules and create basic HTML entity encoding
# ===============================================================================

# Explanation:
# XSS prevention starts with proper encoding of special characters.
# We'll create functions to encode HTML entities and handle basic sanitization.

import html
import re
import urllib.parse
from typing import Dict, List, Optional, Set
from enum import Enum

class OutputContext(Enum):
    """Enumeration of different output contexts for XSS prevention."""
    HTML_CONTENT = "html_content"
    HTML_ATTRIBUTE = "html_attribute"
    JAVASCRIPT = "javascript"
    CSS = "css"
    URL = "url"

def html_encode(text: str) -> str:
    """
    Encode HTML entities to prevent XSS in HTML content.
    
    Args:
        text: Input text that may contain HTML special characters
        
    Returns:
        HTML-encoded safe string
        
    Example:
        >>> html_encode('<script>alert("xss")</script>')
        '&lt;script&gt;alert(&quot;xss&quot;)&lt;/script&gt;'
    """
    if not isinstance(text, str):
        text = str(text)
    return html.escape(text, quote=True)

# Test the basic encoding
if __name__ == "__main__":
    print("=== Step 1: Basic HTML Encoding ===")
    malicious_input = '<script>alert("XSS Attack!")</script>'
    safe_output = html_encode(malicious_input)
    print(f"Original: {malicious_input}")
    print(f"Encoded:  {safe_output}")
    print()


# Step 2: Add JavaScript and URL encoding functions
# ===============================================================================

# Explanation:
# Different contexts require different encoding strategies.
# JavaScript context needs different escaping than HTML, and URLs need percent encoding.

def javascript_encode(text: str) -> str:
    """
    Encode text for safe inclusion in JavaScript context.
    
    Args:
        text: Input text that may contain JavaScript special characters
        
    Returns:
        JavaScript-encoded safe string
        
    Example:
        >>> javascript_encode('"; alert("xss"); "')
        '\\"; alert(\\"xss\\"); \\"'
    """
    if not isinstance(text, str):
        text = str(text)
    
    # Escape JavaScript special characters
    replacements = {
        '\\': '\\\\',  # Backslash must be first
        '"': '\\"',    # Double quote
        "'": "\\'",    # Single quote
        '\n': '\\n',   # Newline
        '\r': '\\r',   # Carriage return
        '\t': '\\t',   # Tab
        '\b': '\\b',   # Backspace
        '\f': '\\f',   # Form feed
        '/': '\\/',    # Forward slash (prevents </script> injection)
    }
    
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    
    return text

def url_encode(text: str) -> str:
    """
    Encode text for safe inclusion in URLs.
    
    Args:
        text: Input text that may contain URL special characters
        
    Returns:
        URL-encoded safe string
        
    Example:
        >>> url_encode('javascript:alert("xss")')
        'javascript%3Aalert%28%22xss%22%29'
    """
    if not isinstance(text, str):
        text = str(text)
    return urllib.parse.quote(text, safe='')

def css_encode(text: str) -> str:
    """
    Encode text for safe inclusion in CSS context.
    
    Args:
        text: Input text that may contain CSS special characters
        
    Returns:
        CSS-encoded safe string
    """
    if not isinstance(text, str):
        text = str(text)
    
    # Remove or escape CSS special characters
    # Only allow alphanumeric characters and safe symbols
    safe_chars = re.compile(r'[^a-zA-Z0-9\s\-_]')
    return safe_chars.sub('', text)

# Test the encoding functions
if __name__ == "__main__":
    print("=== Step 1: Basic HTML Encoding ===")
    malicious_input = '<script>alert("XSS Attack!")</script>'
    safe_output = html_encode(malicious_input)
    print(f"Original: {malicious_input}")
    print(f"Encoded:  {safe_output}")
    print()
    
    print("=== Step 2: Context-Specific Encoding ===")
    js_payload = '"; alert("XSS"); "'
    url_payload = 'javascript:alert("XSS")'
    css_payload = 'expression(alert("XSS"))'
    
    print(f"JavaScript payload: {js_payload}")
    print(f"JS encoded: {javascript_encode(js_payload)}")
    print()
    
    print(f"URL payload: {url_payload}")
    print(f"URL encoded: {url_encode(url_payload)}")
    print()
    
    print(f"CSS payload: {css_payload}")
    print(f"CSS encoded: {css_encode(css_payload)}")
    print()


# Step 3: Add input validation and whitelisting
# ===============================================================================

# Explanation:
# Beyond encoding, we need input validation to reject malicious content entirely.
# Whitelisting approaches are more secure than blacklisting.

class InputValidator:
    """Validates user input against whitelists and patterns."""
    
    def __init__(self):
        # Define allowed patterns for different input types
        self.allowed_html_tags = {
            'p', 'br', 'strong', 'em', 'u', 'ol', 'ul', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'
        }
        self.allowed_protocols = {'http', 'https', 'mailto'}
        
    def validate_email(self, email: str) -> bool:
        """
        Validate email format using whitelist approach.
        
        Args:
            email: Email address to validate
            
        Returns:
            True if email is valid, False otherwise
        """
        if not isinstance(email, str):
            return False
            
        # Simple but effective email validation
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        return bool(email_pattern.match(email)) and len(email) <= 254
    
    def validate_url(self, url: str) -> bool:
        """
        Validate URL using protocol whitelist.
        
        Args:
            url: URL to validate
            
        Returns:
            True if URL is safe, False otherwise
        """
        if not isinstance(url, str):
            return False
            
        try:
            parsed = urllib.parse.urlparse(url.lower())
            return parsed.scheme in self.allowed_protocols
        except Exception:
            return False
    
    def validate_alphanumeric(self, text: str, allow_spaces: bool = True) -> bool:
        """
        Validate that text contains only safe alphanumeric characters.
        
        Args:
            text: Text to validate
            allow_spaces: Whether to allow spaces
            
        Returns:
            True if text is safe, False otherwise
        """
        if not isinstance(text, str):
            return False
            
        if allow_spaces:
            pattern = re.compile(r'^[a-zA-Z0-9\s]+$')
        else:
            pattern = re.compile(r'^[a-zA-Z0-9]+$')
            
        return bool(pattern.match(text))
    
    def sanitize_html_tags(self, html: str) -> str:
        """
        Remove all HTML tags except those in the whitelist.
        
        Args:
            html: HTML content to sanitize
            
        Returns:
            Sanitized HTML with only allowed tags
        """
        if not isinstance(html, str):
            html = str(html)
        
        # Remove all tags not in whitelist
        def replace_tag(match):
            tag_name = match.group(1).lower()
            if tag_name in self.allowed_html_tags:
                return match.group(0)  # Keep allowed tags
            else:
                return ''  # Remove disallowed tags
        
        # Pattern to match HTML tags
        tag_pattern = re.compile(r'<(/?)([a-zA-Z][a-zA-Z0-9]*)[^>]*>', re.IGNORECASE)
        sanitized = tag_pattern.sub(replace_tag, html)
        
        return sanitized

def detect_xss_patterns(text: str) -> List[str]:
    """
    Detect common XSS attack patterns in input.
    
    Args:
        text: Text to analyze for XSS patterns
        
    Returns:
        List of detected XSS patterns
    """
    if not isinstance(text, str):
        text = str(text)
    
    text_lower = text.lower()
    detected_patterns = []
    
    # Common XSS patterns
    xss_patterns = [
        r'<script[^>]*>',
        r'javascript:',
        r'on\w+\s*=',  # Event handlers like onclick, onload
        r'expression\s*\(',  # CSS expressions
        r'vbscript:',
        r'data:text/html',
        r'<iframe[^>]*>',
        r'<object[^>]*>',
        r'<embed[^>]*>',
        r'<link[^>]*>',
        r'<meta[^>]*>',
    ]
    
    for pattern in xss_patterns:
        if re.search(pattern, text_lower):
            detected_patterns.append(pattern)
    
    return detected_patterns

# Test input validation
if __name__ == "__main__":
    print("=== Step 1: Basic HTML Encoding ===")
    malicious_input = '<script>alert("XSS Attack!")</script>'
    safe_output = html_encode(malicious_input)
    print(f"Original: {malicious_input}")
    print(f"Encoded:  {safe_output}")
    print()
    
    print("=== Step 2: Context-Specific Encoding ===")
    js_payload = '"; alert("XSS"); "'
    url_payload = 'javascript:alert("XSS")'
    css_payload = 'expression(alert("XSS"))'
    
    print(f"JavaScript payload: {js_payload}")
    print(f"JS encoded: {javascript_encode(js_payload)}")
    print()
    
    print(f"URL payload: {url_payload}")
    print(f"URL encoded: {url_encode(url_payload)}")
    print()
    
    print(f"CSS payload: {css_payload}")
    print(f"CSS encoded: {css_encode(css_payload)}")
    print()
    
    print("=== Step 3: Input Validation ===")
    validator = InputValidator()
    
    # Test email validation
    emails = ["user@example.com", "invalid-email", "test@test.co.uk"]
    for email in emails:
        is_valid = validator.validate_email(email)
        print(f"Email '{email}': {'Valid' if is_valid else 'Invalid'}")
    
    # Test URL validation
    urls = ["https://example.com", "javascript:alert('xss')", "http://safe-site.org"]
    for url in urls:
        is_safe = validator.validate_url(url)
        print(f"URL '{url}': {'Safe' if is_safe else 'Unsafe'}")
    
    # Test XSS pattern detection
    test_inputs = [
        "Hello world",
        "<script>alert('xss')</script>",
        "<p onclick='alert()'>Click me</p>",
        "Normal text with <strong>bold</strong> formatting"
    ]
    
    for test_input in test_inputs:
        patterns = detect_xss_patterns(test_input)
        print(f"Input: '{test_input}'")
        print(f"XSS patterns detected: {patterns if patterns else 'None'}")
        print()
    print()


# Step 4: Create comprehensive XSS sanitizer class
# ===============================================================================

# Explanation:
# Now we'll combine all our techniques into a comprehensive sanitizer class
# that can handle different contexts and provide Content Security Policy helpers.

class XSSSanitizer:
    """Comprehensive XSS prevention and sanitization toolkit."""
    
    def __init__(self):
        self.validator = InputValidator()
        self.max_input_length = 10000  # Prevent DoS attacks
        
    def sanitize_for_context(self, text: str, context: OutputContext) -> str:
        """
        Sanitize text based on the output context.
        
        Args:
            text: Input text to sanitize
            context: The context where the text will be used
            
        Returns:
            Sanitized text safe for the specified context
        """
        if not isinstance(text, str):
            text = str(text)
            
        # Prevent DoS attacks with overly long inputs
        if len(text) > self.max_input_length:
            raise ValueError(f"Input too long. Maximum length: {self.max_input_length}")
        
        # Apply context-specific sanitization
        if context == OutputContext.HTML_CONTENT:
            return html_encode(text)
        elif context == OutputContext.HTML_ATTRIBUTE:
            return html_encode(text)
        elif context == OutputContext.JAVASCRIPT:
            return javascript_encode(text)
        elif context == OutputContext.CSS:
            return css_encode(text)
        elif context == OutputContext.URL:
            return url_encode(text)
        else:
            # Default to HTML encoding for unknown contexts
            return html_encode(text)
    
    def sanitize_html(self, html: str, allow_tags: Optional[Set[str]] = None) -> str:
        """
        Sanitize HTML content by removing dangerous tags and encoding content.
        
        Args:
            html: HTML content to sanitize
            allow_tags: Set of allowed HTML tags (uses default if None)
            
        Returns:
            Sanitized HTML content
        """
        if not isinstance(html, str):
            html = str(html)
        
        # First, detect and reject obvious XSS attempts
        xss_patterns = detect_xss_patterns(html)
        if xss_patterns:
            # Log the attempt (in real applications)
            print(f"Warning: XSS patterns detected: {xss_patterns}")
        
        # Use custom allowed tags if provided
        if allow_tags:
            original_tags = self.validator.allowed_html_tags
            self.validator.allowed_html_tags = allow_tags
            sanitized = self.validator.sanitize_html_tags(html)
            self.validator.allowed_html_tags = original_tags
        else:
            sanitized = self.validator.sanitize_html_tags(html)
        
        return sanitized
    
    def validate_and_sanitize_url(self, url: str) -> Optional[str]:
        """
        Validate and sanitize a URL.
        
        Args:
            url: URL to validate and sanitize
            
        Returns:
            Sanitized URL if valid, None if invalid
        """
        if not self.validator.validate_url(url):
            return None
        return url_encode(url)
    
    def create_safe_html_template(self, template: str, **kwargs) -> str:
        """
        Create safe HTML by substituting sanitized values into a template.
        
        Args:
            template: HTML template with {variable} placeholders
            **kwargs: Variables to substitute (will be sanitized)
            
        Returns:
            Safe HTML with sanitized substitutions
        """
        safe_kwargs = {}
        for key, value in kwargs.items():
            safe_kwargs[key] = self.sanitize_for_context(str(value), OutputContext.HTML_CONTENT)
        
        return template.format(**safe_kwargs)

class ContentSecurityPolicy:
    """Helper class for generating Content Security Policy headers."""
    
    def __init__(self):
        self.directives = {
            'default-src': ["'self'"],
            'script-src': ["'self'"],
            'style-src': ["'self'", "'unsafe-inline'"],
            'img-src': ["'self'", "data:", "https:"],
            'font-src': ["'self'"],
            'connect-src': ["'self'"],
            'frame-src': ["'none'"],
            'object-src': ["'none'"],
            'base-uri': ["'self'"],
            'form-action': ["'self'"],
        }
    
    def add_source(self, directive: str, source: str) -> None:
        """Add a source to a CSP directive."""
        if directive in self.directives:
            if source not in self.directives[directive]:
                self.directives[directive].append(source)
        else:
            self.directives[directive] = [source]
    
    def remove_source(self, directive: str, source: str) -> None:
        """Remove a source from a CSP directive."""
        if directive in self.directives and source in self.directives[directive]:
            self.directives[directive].remove(source)
    
    def generate_header(self) -> str:
        """Generate the CSP header string."""
        policy_parts = []
        for directive, sources in self.directives.items():
            if sources:  # Only include directives with sources
                policy_parts.append(f"{directive} {' '.join(sources)}")
        
        return "; ".join(policy_parts)
    
    def get_strict_policy(self) -> str:
        """Get a strict CSP policy for maximum security."""
        strict_directives = {
            'default-src': ["'none'"],
            'script-src': ["'self'"],
            'style-src': ["'self'"],
            'img-src': ["'self'"],
            'font-src': ["'self'"],
            'connect-src': ["'self'"],
            'frame-src': ["'none'"],
            'object-src': ["'none'"],
            'base-uri': ["'none'"],
            'form-action': ["'self'"],
        }
        
        policy_parts = []
        for directive, sources in strict_directives.items():
            policy_parts.append(f"{directive} {' '.join(sources)}")
        
        return "; ".join(policy_parts)

# Test the comprehensive sanitizer
if __name__ == "__main__":
    print("=== Step 1: Basic HTML Encoding ===")
    malicious_input = '<script>alert("XSS Attack!")</script>'
    safe_output = html_encode(malicious_input)
    print(f"Original: {malicious_input}")
    print(f"Encoded:  {safe_output}")
    print()
    
    print("=== Step 2: Context-Specific Encoding ===")
    js_payload = '"; alert("XSS"); "'
    url_payload = 'javascript:alert("XSS")'
    css_payload = 'expression(alert("XSS"))'
    
    print(f"JavaScript payload: {js_payload}")
    print(f"JS encoded: {javascript_encode(js_payload)}")
    print()
    
    print(f"URL payload: {url_payload}")
    print(f"URL encoded: {url_encode(url_payload)}")
    print()
    
    print(f"CSS payload: {css_payload}")
    print(f"CSS encoded: {css_encode(css_payload)}")
    print()
    
    print("=== Step 3: Input Validation ===")
    validator = InputValidator()
    
    # Test email validation
    emails = ["user@example.com", "invalid-email", "test@test.co.uk"]
    for email in emails:
        is_valid = validator.validate_email(email)
        print(f"Email '{email}': {'Valid' if is_valid else 'Invalid'}")
    
    # Test URL validation
    urls = ["https://example.com", "javascript:alert('xss')", "http://safe-site.org"]
    for url in urls:
        is_safe = validator.validate_url(url)
        print(f"URL '{url}': {'Safe' if is_safe else 'Unsafe'}")
    
    # Test XSS pattern detection
    test_inputs = [
        "Hello world",
        "<script>alert('xss')</script>",
        "<p onclick='alert()'>Click me</p>",
        "Normal text with <strong>bold</strong> formatting"
    ]
    
    for test_input in test_inputs:
        patterns = detect_xss_patterns(test_input)
        print(f"Input: '{test_input}'")
        print(f"XSS patterns detected: {patterns if patterns else 'None'}")
        print()
    print()
    
    print("=== Step 4: Comprehensive XSS Sanitizer ===")
    sanitizer = XSSSanitizer()
    
    # Test context-specific sanitization
    user_input = '<script>alert("xss")</script>Hello & "World"'
    
    contexts = [
        (OutputContext.HTML_CONTENT, "HTML Content"),
        (OutputContext.JAVASCRIPT, "JavaScript"),
        (OutputContext.URL, "URL"),
        (OutputContext.CSS, "CSS")
    ]
    
    for context, name in contexts:
        sanitized = sanitizer.sanitize_for_context(user_input, context)
        print(f"{name}: {sanitized}")
    
    # Test HTML sanitization
    html_input = '<p>Safe content</p><script>alert("xss")</script><strong>Bold text</strong>'
    sanitized_html = sanitizer.sanitize_html(html_input)
    print(f"\nHTML Input: {html_input}")
    print(f"Sanitized HTML: {sanitized_html}")
    
    # Test safe template rendering
    template = "<h1>Welcome {username}!</h1><p>Your email: {email}</p>"
    safe_html = sanitizer.create_safe_html_template(
        template,
        username='<script>alert("xss")</script>John',
        email='user@example.com'
    )
    print(f"\nSafe template result: {safe_html}")
    
    # Test CSP
    csp = ContentSecurityPolicy()
    print(f"\nDefault CSP: {csp.generate_header()}")
    print(f"Strict CSP: {csp.get_strict_policy()}")
    print()


# Step 5: Advanced security features and real-world examples
# ===============================================================================

# Explanation:
# Let's add advanced features like nonce generation, rate limiting,
# and demonstrate real-world usage patterns for web applications.

import secrets
import time
from collections import defaultdict, deque

class AdvancedXSSSanitizer(XSSSanitizer):
    """Advanced XSS sanitizer with additional security features."""
    
    def __init__(self):
        super().__init__()
        self.rate_limiter = RateLimiter()
        self.nonce_cache = set()
        
    def generate_nonce(self) -> str:
        """
        Generate a cryptographically secure nonce for CSP.
        
        Returns:
            Base64-encoded nonce string
        """
        import base64
        nonce_bytes = secrets.token_bytes(16)
        nonce = base64.b64encode(nonce_bytes).decode('ascii')
        self.nonce_cache.add(nonce)
        return nonce
    
    def validate_nonce(self, nonce: str) -> bool:
        """
        Validate that a nonce was previously generated.
        
        Args:
            nonce: Nonce to validate
            
        Returns:
            True if nonce is valid, False otherwise
        """
        return nonce in self.nonce_cache
    
    def sanitize_with_rate_limit(self, text: str, client_id: str, 
                                context: OutputContext) -> str:
        """
        Sanitize text with rate limiting to prevent abuse.
        
        Args:
            text: Text to sanitize
            client_id: Identifier for the client (IP, user ID, etc.)
            context: Output context
            
        Returns:
            Sanitized text
            
        Raises:
            ValueError: If rate limit is exceeded
        """
        if not self.rate_limiter.allow_request(client_id):
            raise ValueError("Rate limit exceeded. Please try again later.")
        
        return self.sanitize_for_context(text, context)
    
    def create_secure_form_token(self) -> str:
        """
        Create a secure token for form submissions (CSRF protection).
        
        Returns:
            Secure form token
        """
        return secrets.token_urlsafe(32)

class RateLimiter:
    """Simple rate limiter to prevent abuse."""
    
    def __init__(self, max_requests: int = 100, time_window: int = 3600):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = defaultdict(deque)
    
    def allow_request(self, client_id: str) -> bool:
        """
        Check if a request should be allowed based on rate limits.
        
        Args:
            client_id: Identifier for the client
            
        Returns:
            True if request is allowed, False otherwise
        """
        now = time.time()
        client_requests = self.requests[client_id]
        
        # Remove old requests outside the time window
        while client_requests and client_requests[0] < now - self.time_window:
            client_requests.popleft()
        
        # Check if under the limit
        if len(client_requests) < self.max_requests:
            client_requests.append(now)
            return True
        
        return False

class SecureWebRenderer:
    """Example web application renderer with XSS protection."""
    
    def __init__(self):
        self.sanitizer = AdvancedXSSSanitizer()
        self.csp = ContentSecurityPolicy()
    
    def render_user_profile(self, user_data: Dict[str, str]) -> str:
        """
        Render a user profile page with XSS protection.
        
        Args:
            user_data: Dictionary containing user information
            
        Returns:
            Safe HTML for user profile
        """
        # Generate nonce for inline scripts
        nonce = self.sanitizer.generate_nonce()
        
        # Update CSP to include the nonce
        self.csp.add_source('script-src', f"'nonce-{nonce}'")
        
        # Sanitize all user data
        safe_data = {}
        for key, value in user_data.items():
            safe_data[key] = self.sanitizer.sanitize_for_context(
                value, OutputContext.HTML_CONTENT
            )
        
        # Create safe HTML template
        template = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta http-equiv="Content-Security-Policy" content="{csp}">
            <title>User Profile</title>
        </head>
        <body>
            <h1>Welcome, {username}!</h1>
            <div class="profile">
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Bio:</strong> {bio}</p>
                <p><strong>Website:</strong> 
                   <a href="{website}" target="_blank">{website}</a>
                </p>
            </div>
            <script nonce="{nonce}">
                console.log('Profile loaded for: {username}');
            </script>
        </body>
        </html>
        """
        
        return template.format(
            csp=self.csp.generate_header(),
            nonce=nonce,
            **safe_data
        )
    
    def render_comment_section(self, comments: List[Dict[str, str]]) -> str:
        """
        Render a comment section with XSS protection.
        
        Args:
            comments: List of comment dictionaries
            
        Returns:
            Safe HTML for comments
        """
        safe_comments = []
        
        for comment in comments:
            # Sanitize comment content
            safe_comment = {
                'author': self.sanitizer.sanitize_for_context(
                    comment.get('author', ''), OutputContext.HTML_CONTENT
                ),
                'content': self.sanitizer.sanitize_html(
                    comment.get('content', ''),
                    allow_tags={'p', 'br', 'strong', 'em'}
                ),
                'timestamp': self.sanitizer.sanitize_for_context(
                    comment.get('timestamp', ''), OutputContext.HTML_CONTENT
                )
            }
            safe_comments.append(safe_comment)
        
        # Build comments HTML
        comments_html = []
        for comment in safe_comments:
            comment_html = f"""
            <div class="comment">
                <h4>{comment['author']}</h4>
                <div class="content">{comment['content']}</div>
                <small class="timestamp">{comment['timestamp']}</small>
            </div>
            """
            comments_html.append(comment_html)
        
        return '<div class="comments">' + ''.join(comments_html) + '</div>'

def demonstrate_xss_attacks_and_prevention():
    """Demonstrate common XSS attacks and how to prevent them."""
    
    print("=== XSS Attack Demonstrations ===")
    
    # Common XSS payloads
    xss_payloads = [
        '<script>alert("Basic XSS")</script>',
        '<img src="x" onerror="alert(\'Image XSS\')">',
        '<a href="javascript:alert(\'Link XSS\')">Click me</a>',
        '<div onmouseover="alert(\'Event XSS\')">Hover me</div>',
        '"><script>alert("Attribute escape")</script>',
        "'; alert('SQL-like injection'); //",
        '<iframe src="javascript:alert(\'Frame XSS\')"></iframe>',
    ]
    
    sanitizer = AdvancedXSSSanitizer()
    
    for i, payload in enumerate(xss_payloads, 1):
        print(f"\n--- Attack {i} ---")
        print(f"Payload: {payload}")
        
        # Show how different contexts handle the payload
        html_safe = sanitizer.sanitize_for_context(payload, OutputContext.HTML_CONTENT)
        js_safe = sanitizer.sanitize_for_context(payload, OutputContext.JAVASCRIPT)
        
        print(f"HTML Context: {html_safe}")
        print(f"JS Context: {js_safe}")
        
        # Detect XSS patterns
        patterns = detect_xss_patterns(payload)
        print(f"Detected patterns: {patterns}")

# Final comprehensive test
if __name__ == "__main__":
    print("=== Step 1: Basic HTML Encoding ===")
    malicious_input = '<script>alert("XSS Attack!")</script>'
    safe_output = html_encode(malicious_input)
    print(f"Original: {malicious_input}")
    print(f"Encoded:  {safe_output}")
    print()
    
    print("=== Step 2: Context-Specific Encoding ===")
    js_payload = '"; alert("XSS"); "'
    url_payload = 'javascript:alert("XSS")'
    css_payload = 'expression(alert("XSS"))'
    
    print(f"JavaScript payload: {js_payload}")
    print(f"JS encoded: {javascript_encode(js_payload)}")
    print()
    
    print(f"URL payload: {url_payload}")
    print(f"URL encoded: {url_encode(url_payload)}")
    print()
    
    print(f"CSS payload: {css_payload}")
    print(f"CSS encoded: {css_encode(css_payload)}")
    print()
    
    print("=== Step 3: Input Validation ===")
    validator = InputValidator()
    
    # Test email validation
    emails = ["user@example.com", "invalid-email", "test@test.co.uk"]
    for email in emails:
        is_valid = validator.validate_email(email)
        print(f"Email '{email}': {'Valid' if is_valid else 'Invalid'}")
    
    # Test URL validation
    urls = ["https://example.com", "javascript:alert('xss')", "http://safe-site.org"]
    for url in urls:
        is_safe = validator.validate_url(url)
        print(f"URL '{url}': {'Safe' if is_safe else 'Unsafe'}")
    
    # Test XSS pattern detection
    test_inputs = [
        "Hello world",
        "<script>alert('xss')</script>",
        "<p onclick='alert()'>Click me</p>",
        "Normal text with <strong>bold</strong> formatting"
    ]
    
    for test_input in test_inputs:
        patterns = detect_xss_patterns(test_input)
        print(f"Input: '{test_input}'")
        print(f"XSS patterns detected: {patterns if patterns else 'None'}")
        print()
    print()
    
    print("=== Step 4: Comprehensive XSS Sanitizer ===")
    sanitizer = XSSSanitizer()
    
    # Test context-specific sanitization
    user_input = '<script>alert("xss")</script>Hello & "World"'
    
    contexts = [
        (OutputContext.HTML_CONTENT, "HTML Content"),
        (OutputContext.JAVASCRIPT, "JavaScript"),
        (OutputContext.URL, "URL"),
        (OutputContext.CSS, "CSS")
    ]
    
    for context, name in contexts:
        sanitized = sanitizer.sanitize_for_context(user_input, context)
        print(f"{name}: {sanitized}")
    
    # Test HTML sanitization
    html_input = '<p>Safe content</p><script>alert("xss")</script><strong>Bold text</strong>'
    sanitized_html = sanitizer.sanitize_html(html_input)
    print(f"\nHTML Input: {html_input}")
    print(f"Sanitized HTML: {sanitized_html}")
    
    # Test safe template rendering
    template = "<h1>Welcome {username}!</h1><p>Your email: {email}</p>"
    safe_html = sanitizer.create_safe_html_template(
        template,
        username='<script>alert("xss")</script>John',
        email='user@example.com'
    )
    print(f"\nSafe template result: {safe_html}")
    
    # Test CSP
    csp = ContentSecurityPolicy()
    print(f"\nDefault CSP: {csp.generate_header()}")
    print(f"Strict CSP: {csp.get_strict_policy()}")
    print()
    
    print("=== Step 5: Advanced Security Features ===")
    advanced_sanitizer = AdvancedXSSSanitizer()
    
    # Test nonce generation
    nonce1 = advanced_sanitizer.generate_nonce()
    nonce2 = advanced_sanitizer.generate_nonce()
    print(f"Generated nonces: {nonce1}, {nonce2}")
    print(f"Nonce validation: {advanced_sanitizer.validate_nonce(nonce1)}")
    
    # Test rate limiting
    try:
        result = advanced_sanitizer.sanitize_with_rate_limit(
            "Test input", "client123", OutputContext.HTML_CONTENT
        )
        print(f"Rate limited sanitization: {result}")
    except ValueError as e:
        print(f"Rate limit error: {e}")
    
    # Test secure web renderer
    renderer = SecureWebRenderer()
    
    user_data = {
        'username': '<script>alert("xss")</script>John Doe',
        'email': 'john@example.com',
        'bio': 'I love <script>alert("bio xss")</script> programming!',
        'website': 'https://johndoe.com'
    }
    
    profile_html = renderer.render_user_profile(user_data)
    print(f"\nSecure profile HTML (truncated): {profile_html[:200]}...")
    
    # Demonstrate XSS attacks and prevention
    demonstrate_xss_attacks_and_prevention()
    
    print("\n=== Security Best Practices Summary ===")
    print("1. Always encode output based on context (HTML, JS, CSS, URL)")
    print("2. Use input validation with whitelisting approaches")
    print("3. Implement Content Security Policy (CSP)")
    print("4. Use nonces for inline scripts when necessary")
    print("5. Apply rate limiting to prevent abuse")
    print("6. Sanitize HTML content by removing dangerous tags")
    print("7. Never trust user input - validate and sanitize everything")
    print("8. Use secure templating systems that auto-escape by default")
    print("9. Regularly update security libraries and frameworks")
    print("10. Test your application with various XSS payloads")

