# Python Security Best Practices

This directory contains comprehensive examples and implementations of essential security practices for Python applications. Each file demonstrates real-world security scenarios with step-by-step solutions and best practices.

## 📋 Table of Contents

1. [Input Validation and Sanitization](#1-input-validation-and-sanitization)
2. [SQL Injection Prevention](#2-sql-injection-prevention)
3. [XSS Prevention](#3-xss-prevention)
4. [Authentication and Authorization](#4-authentication-and-authorization)
5. [Password Hashing](#5-password-hashing)
6. [Cryptography Basics](#6-cryptography-basics)
7. [Secure File Handling](#7-secure-file-handling)
8. [Environment Variables](#8-environment-variables)
9. [Secure Communication](#9-secure-communication)
10. [Code Injection Prevention](#10-code-injection-prevention)
11. [Dependency Security](#11-dependency-security)
12. [Logging Security](#12-logging-security)

---

## 1. Input Validation and Sanitization

**File:** `01-input-validation-sanitization.py`

Learn how to properly validate and sanitize user inputs to prevent various security vulnerabilities.

### Key Topics Covered:
- **Data Type Validation**: Ensuring inputs match expected types
- **Length and Range Validation**: Preventing buffer overflows and DoS attacks
- **Format Validation**: Using regex patterns for emails, URLs, etc.
- **Sanitization Techniques**: Removing dangerous characters and content
- **Whitelist vs Blacklist**: Implementing secure validation strategies

### Example Use Cases:
```python
validator = InputValidator()
# Email validation
is_valid = validator.validate_email("user@example.com")
# Sanitize HTML content
clean_html = validator.sanitize_html("<script>alert('xss')</script>")
# Validate file uploads
validator.validate_file_upload(filename, content, max_size=5*1024*1024)
```

### Security Benefits:
- Prevents XSS attacks through input sanitization
- Blocks SQL injection via parameterized validation
- Mitigates file upload vulnerabilities
- Reduces application crashes from malformed input

---

## 2. SQL Injection Prevention

**File:** `02-sql-injection-prevention.py`

Comprehensive guide to preventing SQL injection attacks through secure database practices.

### Key Topics Covered:
- **Parameterized Queries**: Using placeholders instead of string concatenation
- **Stored Procedures**: Implementing secure database procedures
- **Input Validation**: Validating data before database operations
- **ORM Security**: Secure usage of Object-Relational Mapping tools
- **Database Permissions**: Principle of least privilege

### Example Use Cases:
```python
db_manager = SecureDatabaseManager()
# Safe user authentication
user = db_manager.authenticate_user(username, password)
# Secure data retrieval with parameters
results = db_manager.get_user_data(user_id, filters)
# Safe dynamic query building
query_builder = SecureQueryBuilder()
query = query_builder.select("users").where("age", ">", 18).build()
```

### Security Benefits:
- Eliminates SQL injection vulnerabilities
- Protects sensitive database information
- Ensures data integrity and confidentiality
- Provides audit trails for database access

---

## 3. XSS Prevention

**File:** `03-xss-prevention.py`

Learn to prevent Cross-Site Scripting (XSS) attacks in web applications.

### Key Topics Covered:
- **Output Encoding**: Properly encoding data for different contexts
- **Content Security Policy (CSP)**: Implementing browser-level protection
- **Input Sanitization**: Removing malicious scripts from user input
- **Template Security**: Secure templating practices
- **DOM Manipulation**: Safe client-side scripting

### Example Use Cases:
```python
xss_protector = XSSProtector()
# Sanitize user content for display
safe_content = xss_protector.sanitize_html(user_input)
# Generate CSP headers
csp_header = xss_protector.generate_csp_header()
# Validate and encode URLs
safe_url = xss_protector.validate_and_encode_url(user_url)
```

### Security Benefits:
- Prevents malicious script execution
- Protects user sessions and data
- Maintains application integrity
- Reduces risk of account takeover

---

## 4. Authentication and Authorization

**File:** `04-authentication-authorization.py`

Implement robust authentication and authorization systems.

### Key Topics Covered:
- **Multi-Factor Authentication (MFA)**: Adding extra security layers
- **Session Management**: Secure session handling and timeout
- **Role-Based Access Control (RBAC)**: Implementing permission systems
- **JWT Security**: Secure token-based authentication
- **Account Lockout**: Preventing brute force attacks

### Example Use Cases:
```python
auth_system = AuthenticationSystem()
# User registration with validation
auth_system.register_user(username, password, email)
# Multi-factor authentication
auth_system.setup_mfa(user_id, phone_number)
# Role-based authorization
auth_system.authorize_action(user_id, resource, action)
```

### Security Benefits:
- Prevents unauthorized access
- Implements defense in depth
- Provides audit trails for access attempts
- Supports compliance requirements

---

## 5. Password Hashing

**File:** `05-password-hashing.py`

Modern password hashing techniques using cryptographically secure methods.

### Key Topics Covered:
- **bcrypt Hashing**: Industry-standard password hashing
- **Salt Generation**: Preventing rainbow table attacks
- **Key Derivation Functions**: Using PBKDF2, scrypt, and Argon2
- **Password Policies**: Implementing strong password requirements
- **Secure Comparison**: Timing-attack resistant verification

### Example Use Cases:
```python
password_manager = SecurePasswordManager()
# Hash password with automatic salt
hashed = password_manager.hash_password("user_password")
# Verify password securely
is_valid = password_manager.verify_password("user_password", hashed)
# Generate secure passwords
strong_password = password_manager.generate_secure_password()
```

### Security Benefits:
- Protects passwords even if database is compromised
- Prevents rainbow table attacks
- Implements industry best practices
- Provides configurable security levels

---

## 6. Cryptography Basics

**File:** `06-cryptography-basics.py`

Essential cryptographic operations for data protection.

### Key Topics Covered:
- **Symmetric Encryption**: AES encryption for data at rest
- **Asymmetric Encryption**: RSA for secure key exchange
- **Digital Signatures**: Ensuring data integrity and authenticity
- **Key Management**: Secure key generation and storage
- **Hashing**: Cryptographic hash functions for integrity

### Example Use Cases:
```python
crypto_manager = CryptographyManager()
# Encrypt sensitive data
encrypted_data = crypto_manager.encrypt_data("sensitive information")
# Generate digital signatures
signature = crypto_manager.sign_data(data, private_key)
# Secure key exchange
shared_key = crypto_manager.generate_shared_key()
```

### Security Benefits:
- Protects data confidentiality
- Ensures data integrity
- Provides non-repudiation
- Enables secure communication

---

## 7. Secure File Handling

**File:** `07-secure-file-handling.py`

Secure practices for file operations and uploads.

### Key Topics Covered:
- **File Upload Security**: Validating file types and content
- **Path Traversal Prevention**: Preventing directory traversal attacks
- **File Permissions**: Setting appropriate access controls
- **Virus Scanning**: Integrating malware detection
- **Secure Storage**: Encrypted file storage solutions

### Example Use Cases:
```python
file_handler = SecureFileHandler()
# Secure file upload processing
file_handler.process_upload(file_data, allowed_types=['jpg', 'png'])
# Safe file path operations
safe_path = file_handler.sanitize_file_path(user_path)
# Encrypted file storage
file_handler.store_encrypted_file(file_data, encryption_key)
```

### Security Benefits:
- Prevents malicious file uploads
- Protects against path traversal attacks
- Ensures file integrity
- Maintains confidentiality of stored files

---

## 8. Environment Variables

**File:** `08-environment-variables.py`

Secure management of configuration and sensitive data.

### Key Topics Covered:
- **Secret Management**: Storing API keys and passwords securely
- **Environment Separation**: Different configs for dev/staging/prod
- **Encryption at Rest**: Encrypting sensitive configuration data
- **Access Control**: Limiting access to environment variables
- **Audit Logging**: Tracking configuration access

### Example Use Cases:
```python
env_manager = SecureEnvironmentManager()
# Secure secret storage
env_manager.store_secret("API_KEY", api_key_value)
# Encrypted configuration loading
config = env_manager.load_encrypted_config("production")
# Audit configuration access
env_manager.audit_config_access(user_id, config_key)
```

### Security Benefits:
- Protects sensitive configuration data
- Prevents credential exposure in code
- Enables secure deployment practices
- Provides configuration audit trails

---

## 9. Secure Communication

**File:** `09-secure-communication.py`

Implementing secure network communication protocols.

### Key Topics Covered:
- **TLS/SSL Configuration**: Secure transport layer setup
- **Certificate Validation**: Proper certificate verification
- **API Security**: Securing REST and GraphQL APIs
- **Message Encryption**: End-to-end encryption for messaging
- **Network Security**: Firewall and network-level protection

### Example Use Cases:
```python
comm_manager = SecureCommunicationManager()
# Secure HTTP client with certificate validation
response = comm_manager.secure_request(url, verify_cert=True)
# Encrypted messaging
encrypted_msg = comm_manager.encrypt_message(message, recipient_key)
# API authentication and rate limiting
comm_manager.authenticate_api_request(request, api_key)
```

### Security Benefits:
- Ensures data confidentiality in transit
- Prevents man-in-the-middle attacks
- Provides authentication and integrity
- Protects against eavesdropping

---

## 10. Code Injection Prevention

**File:** `10-code-injection-prevention.py`

Preventing various forms of code injection attacks.

### Key Topics Covered:
- **Command Injection**: Preventing OS command execution
- **Template Injection**: Securing template engines
- **Deserialization Attacks**: Safe object deserialization
- **Dynamic Code Execution**: Avoiding eval() and exec()
- **Input Validation**: Comprehensive input sanitization

### Example Use Cases:
```python
injection_preventer = CodeInjectionPreventer()
# Safe command execution
result = injection_preventer.safe_execute_command(command, args)
# Secure template rendering
output = injection_preventer.safe_template_render(template, data)
# Safe deserialization
obj = injection_preventer.safe_deserialize(serialized_data)
```

### Security Benefits:
- Prevents arbitrary code execution
- Protects system integrity
- Maintains application security
- Reduces attack surface

---

## 11. Dependency Security

**File:** `11-dependency-security.py`

Managing and securing third-party dependencies.

### Key Topics Covered:
- **Vulnerability Scanning**: Automated dependency vulnerability detection
- **License Compliance**: Ensuring legal compliance with dependencies
- **Version Pinning**: Securing dependency versions
- **Supply Chain Security**: Protecting against compromised packages
- **Security Monitoring**: Continuous dependency security monitoring

### Example Use Cases:
```python
dependency_scanner = DependencyScanner()
# Scan for vulnerabilities
vulnerabilities = dependency_scanner.scan_dependencies("requirements.txt")
# Validate licenses
license_checker = LicenseChecker()
compliance = license_checker.check_licenses(dependencies)
# Generate secure requirements
secure_manager = SecureDependencyManager()
secure_reqs = secure_manager.generate_secure_requirements(deps)
```

### Security Benefits:
- Identifies vulnerable dependencies
- Ensures license compliance
- Provides supply chain security
- Enables proactive security management

---

## 12. Logging Security

**File:** `12-logging-security.py`

Secure logging practices to protect sensitive information.

### Key Topics Covered:
- **PII Protection**: Detecting and masking personally identifiable information
- **Log Injection Prevention**: Preventing log tampering and injection
- **Audit Logging**: Comprehensive security event logging
- **Secure Storage**: Encrypted and access-controlled log storage
- **Log Rotation**: Secure log rotation and archival

### Example Use Cases:
```python
secure_logger = SecureLogger()
# Log with PII sanitization
secure_logger.log_user_action(user_id, action, metadata)
# Audit security events
audit_logger = AuditLogger()
audit_logger.log_authentication_event(user, event, success, ip)
# Secure log management
log_manager = SecureLogManager()
log_manager.archive_old_logs(days_to_keep=90)
```

### Security Benefits:
- Protects user privacy in logs
- Prevents log injection attacks
- Provides comprehensive audit trails
- Ensures secure log storage and rotation

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Required packages (install via pip):
  ```bash
  pip install cryptography bcrypt requests sqlalchemy
  ```

### Running the Examples
Each file is self-contained and can be run independently:

```bash
# Run a specific security example
python 01-input-validation-sanitization.py

# Run all examples (if you have a test runner)
python -m pytest security/
```

### Learning Path
1. **Start with fundamentals**: Input validation and SQL injection prevention
2. **Progress to authentication**: Password hashing and auth systems
3. **Advanced topics**: Cryptography and secure communication
4. **Operational security**: Logging, dependencies, and file handling

---

## 🛡️ Security Principles

### Defense in Depth
Implement multiple layers of security controls rather than relying on a single mechanism.

### Principle of Least Privilege
Grant minimal necessary permissions and access rights.

### Fail Securely
Ensure that security failures result in a secure state, not an open one.

### Input Validation
Validate all inputs at the boundary of trust zones.

### Security by Design
Integrate security considerations from the beginning of development.

---

## 📚 Additional Resources

### Official Documentation
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security Guidelines](https://python.org/dev/security/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

### Security Tools
- **Static Analysis**: bandit, semgrep
- **Dependency Scanning**: safety, pip-audit
- **Code Quality**: pylint, flake8 with security plugins

### Best Practices
- Regular security assessments and code reviews
- Automated security testing in CI/CD pipelines
- Continuous monitoring and incident response
- Security training and awareness programs

---

## 🤝 Contributing

When contributing to security examples:

1. **Follow secure coding practices** demonstrated in the examples
2. **Include comprehensive documentation** explaining security implications
3. **Add test cases** that verify security controls
4. **Update this README** if adding new security topics

---

## ⚠️ Important Notes

- **Educational Purpose**: These examples are for learning and should be adapted for production use
- **Stay Updated**: Security practices evolve; keep examples current with latest threats
- **Test Thoroughly**: Always test security implementations in your specific environment
- **Professional Review**: Have security implementations reviewed by security professionals

---

## 📄 License

This educational content is provided under the MIT License. See the main repository LICENSE file for details.

---

*Remember: Security is not a destination but a journey. Stay informed, stay vigilant, and always prioritize the protection of user data and system integrity.*