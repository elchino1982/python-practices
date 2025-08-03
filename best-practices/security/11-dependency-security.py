"""Question: Implement comprehensive dependency security practices to protect applications from vulnerable dependencies.

Create a dependency security system that can scan, validate, and manage dependencies
with security best practices.

Requirements:
1. Create a dependency scanner that checks for known vulnerabilities
2. Implement dependency validation and verification
3. Create a secure dependency manager with version pinning
4. Implement license compliance checking
5. Demonstrate security monitoring and alerting

Example usage:
    scanner = DependencyScanner()
    vulnerabilities = scanner.scan_dependencies("requirements.txt")
    manager = SecureDependencyManager()
    manager.validate_and_install(dependencies)
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
# - What data structures represent dependencies and vulnerabilities?
# - How do you parse and validate dependency files?
# - What security checks should be performed?
# - How do you implement secure version management?
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


# Step 1: Import modules and create basic dependency data structures
# ===============================================================================

# Explanation:
# We start by creating data structures to represent dependencies and vulnerabilities.
# This forms the foundation for our security system.

import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import urlparse
import warnings

class SeverityLevel(Enum):
    """Severity levels for vulnerabilities."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class Dependency:
    """Represents a software dependency."""
    name: str
    version: str
    source: str = "pypi"
    hash_value: Optional[str] = None
    license: Optional[str] = None
    
    def __str__(self):
        return f"{self.name}=={self.version}"

@dataclass
class Vulnerability:
    """Represents a security vulnerability."""
    id: str
    title: str
    description: str
    severity: SeverityLevel
    affected_versions: List[str]
    fixed_version: Optional[str] = None
    cve_id: Optional[str] = None
    published_date: Optional[datetime] = None

# What we accomplished in this step:
# - Created enums and data classes for dependencies and vulnerabilities
# - Established the foundation data structures for our security system


# Step 2: Create dependency parser for requirements files
# ===============================================================================

# Explanation:
# We need to parse dependency files (like requirements.txt) to extract
# dependency information for security analysis.

import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import urlparse
import warnings

class SeverityLevel(Enum):
    """Severity levels for vulnerabilities."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class Dependency:
    """Represents a software dependency."""
    name: str
    version: str
    source: str = "pypi"
    hash_value: Optional[str] = None
    license: Optional[str] = None
    
    def __str__(self):
        return f"{self.name}=={self.version}"

@dataclass
class Vulnerability:
    """Represents a security vulnerability."""
    id: str
    title: str
    description: str
    severity: SeverityLevel
    affected_versions: List[str]
    fixed_version: Optional[str] = None
    cve_id: Optional[str] = None
    published_date: Optional[datetime] = None

class DependencyParser:
    """Parses dependency files and extracts dependency information."""
    
    def __init__(self):
        self.version_pattern = re.compile(r'^([a-zA-Z0-9_-]+)\s*([><=!~]+)\s*([0-9\.]+.*?)(?:\s*#.*)?$')
        self.simple_pattern = re.compile(r'^([a-zA-Z0-9_-]+)(?:\s*#.*)?$')
    
    def parse_requirements_file(self, file_path: str) -> List[Dependency]:
        """Parse a requirements.txt file and return list of dependencies."""
        dependencies = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, 1):
                    line = line.strip()
                    
                    # Skip empty lines and comments
                    if not line or line.startswith('#'):
                        continue
                    
                    # Skip -r, -e, and other pip options
                    if line.startswith('-'):
                        continue
                    
                    dependency = self._parse_dependency_line(line, line_num)
                    if dependency:
                        dependencies.append(dependency)
        
        except FileNotFoundError:
            raise FileNotFoundError(f"Requirements file not found: {file_path}")
        except Exception as e:
            raise ValueError(f"Error parsing requirements file: {e}")
        
        return dependencies
    
    def _parse_dependency_line(self, line: str, line_num: int) -> Optional[Dependency]:
        """Parse a single dependency line."""
        # Try versioned dependency first
        match = self.version_pattern.match(line)
        if match:
            name, operator, version = match.groups()
            # For security, we prefer exact versions
            if operator == '==':
                return Dependency(name=name.lower(), version=version)
            else:
                warnings.warn(f"Line {line_num}: Non-exact version '{operator}' detected for {name}. "
                            f"Consider pinning to exact version for security.")
                return Dependency(name=name.lower(), version=version)
        
        # Try simple dependency without version
        match = self.simple_pattern.match(line)
        if match:
            name = match.group(1)
            warnings.warn(f"Line {line_num}: No version specified for {name}. "
                        f"This is a security risk - always pin versions.")
            return Dependency(name=name.lower(), version="latest")
        
        warnings.warn(f"Line {line_num}: Could not parse dependency line: {line}")
        return None
    
    def parse_installed_packages(self) -> List[Dependency]:
        """Get list of currently installed packages."""
        try:
            result = subprocess.run([sys.executable, '-m', 'pip', 'list', '--format=json'], 
                                  capture_output=True, text=True, check=True)
            packages = json.loads(result.stdout)
            
            dependencies = []
            for package in packages:
                dependencies.append(Dependency(
                    name=package['name'].lower(),
                    version=package['version']
                ))
            
            return dependencies
        
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to get installed packages: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Failed to parse pip output: {e}")

# What we accomplished in this step:
# - Created dependency parser for requirements.txt files
# - Added support for different dependency formats and version operators
# - Implemented warnings for insecure dependency specifications
# - Added functionality to parse currently installed packages


# Step 3: Create vulnerability scanner with mock vulnerability database
# ===============================================================================

# Explanation:
# We create a vulnerability scanner that checks dependencies against a database
# of known vulnerabilities. In production, this would connect to real databases.

import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import urlparse
import warnings

class SeverityLevel(Enum):
    """Severity levels for vulnerabilities."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class Dependency:
    """Represents a software dependency."""
    name: str
    version: str
    source: str = "pypi"
    hash_value: Optional[str] = None
    license: Optional[str] = None
    
    def __str__(self):
        return f"{self.name}=={self.version}"

@dataclass
class Vulnerability:
    """Represents a security vulnerability."""
    id: str
    title: str
    description: str
    severity: SeverityLevel
    affected_versions: List[str]
    fixed_version: Optional[str] = None
    cve_id: Optional[str] = None
    published_date: Optional[datetime] = None

class DependencyParser:
    """Parses dependency files and extracts dependency information."""
    
    def __init__(self):
        self.version_pattern = re.compile(r'^([a-zA-Z0-9_-]+)\s*([><=!~]+)\s*([0-9\.]+.*?)(?:\s*#.*)?$')
        self.simple_pattern = re.compile(r'^([a-zA-Z0-9_-]+)(?:\s*#.*)?$')
    
    def parse_requirements_file(self, file_path: str) -> List[Dependency]:
        """Parse a requirements.txt file and return list of dependencies."""
        dependencies = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, 1):
                    line = line.strip()
                    
                    # Skip empty lines and comments
                    if not line or line.startswith('#'):
                        continue
                    
                    # Skip -r, -e, and other pip options
                    if line.startswith('-'):
                        continue
                    
                    dependency = self._parse_dependency_line(line, line_num)
                    if dependency:
                        dependencies.append(dependency)
        
        except FileNotFoundError:
            raise FileNotFoundError(f"Requirements file not found: {file_path}")
        except Exception as e:
            raise ValueError(f"Error parsing requirements file: {e}")
        
        return dependencies
    
    def _parse_dependency_line(self, line: str, line_num: int) -> Optional[Dependency]:
        """Parse a single dependency line."""
        # Try versioned dependency first
        match = self.version_pattern.match(line)
        if match:
            name, operator, version = match.groups()
            # For security, we prefer exact versions
            if operator == '==':
                return Dependency(name=name.lower(), version=version)
            else:
                warnings.warn(f"Line {line_num}: Non-exact version '{operator}' detected for {name}. "
                            f"Consider pinning to exact version for security.")
                return Dependency(name=name.lower(), version=version)
        
        # Try simple dependency without version
        match = self.simple_pattern.match(line)
        if match:
            name = match.group(1)
            warnings.warn(f"Line {line_num}: No version specified for {name}. "
                        f"This is a security risk - always pin versions.")
            return Dependency(name=name.lower(), version="latest")
        
        warnings.warn(f"Line {line_num}: Could not parse dependency line: {line}")
        return None
    
    def parse_installed_packages(self) -> List[Dependency]:
        """Get list of currently installed packages."""
        try:
            result = subprocess.run([sys.executable, '-m', 'pip', 'list', '--format=json'], 
                                  capture_output=True, text=True, check=True)
            packages = json.loads(result.stdout)
            
            dependencies = []
            for package in packages:
                dependencies.append(Dependency(
                    name=package['name'].lower(),
                    version=package['version']
                ))
            
            return dependencies
        
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to get installed packages: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Failed to parse pip output: {e}")

@dataclass
class ScanResult:
    """Results of a dependency security scan."""
    dependency: Dependency
    vulnerabilities: List[Vulnerability] = field(default_factory=list)
    is_vulnerable: bool = False
    risk_score: float = 0.0

class VulnerabilityDatabase:
    """Mock vulnerability database for demonstration."""
    
    def __init__(self):
        # In production, this would connect to real vulnerability databases
        # like OSV, CVE, PyUp, etc.
        self.vulnerabilities = {
            "requests": [
                Vulnerability(
                    id="VULN-001",
                    title="Server-Side Request Forgery in requests",
                    description="Requests library vulnerable to SSRF attacks in versions < 2.31.0",
                    severity=SeverityLevel.HIGH,
                    affected_versions=["2.25.0", "2.26.0", "2.27.0", "2.28.0", "2.29.0", "2.30.0"],
                    fixed_version="2.31.0",
                    cve_id="CVE-2025-32681"
                )
            ],
            "django": [
                Vulnerability(
                    id="VULN-002",
                    title="SQL Injection in Django ORM",
                    description="Django ORM vulnerable to SQL injection in versions < 4.2.7",
                    severity=SeverityLevel.CRITICAL,
                    affected_versions=["4.0.0", "4.1.0", "4.2.0", "4.2.1", "4.2.2", "4.2.3", "4.2.4", "4.2.5", "4.2.6"],
                    fixed_version="4.2.7",
                    cve_id="CVE-2025-43665"
                )
            ],
            "flask": [
                Vulnerability(
                    id="VULN-003",
                    title="Session Cookie Security Issue",
                    description="Flask session cookies not properly secured in versions < 2.3.3",
                    severity=SeverityLevel.MEDIUM,
                    affected_versions=["2.0.0", "2.1.0", "2.2.0", "2.3.0", "2.3.1", "2.3.2"],
                    fixed_version="2.3.3",
                    cve_id="CVE-2025-30861"
                )
            ]
        }
    
    def get_vulnerabilities(self, package_name: str) -> List[Vulnerability]:
        """Get vulnerabilities for a specific package."""
        return self.vulnerabilities.get(package_name.lower(), [])

class DependencyScanner:
    """Scans dependencies for security vulnerabilities."""
    
    def __init__(self):
        self.parser = DependencyParser()
        self.vuln_db = VulnerabilityDatabase()
        self.severity_scores = {
            SeverityLevel.LOW: 1.0,
            SeverityLevel.MEDIUM: 3.0,
            SeverityLevel.HIGH: 7.0,
            SeverityLevel.CRITICAL: 10.0
        }
    
    def scan_dependencies(self, dependencies: List[Dependency]) -> List[ScanResult]:
        """Scan a list of dependencies for vulnerabilities."""
        results = []
        
        for dependency in dependencies:
            result = self._scan_single_dependency(dependency)
            results.append(result)
        
        return results
    
    def scan_requirements_file(self, file_path: str) -> List[ScanResult]:
        """Scan dependencies from a requirements file."""
        dependencies = self.parser.parse_requirements_file(file_path)
        return self.scan_dependencies(dependencies)
    
    def _scan_single_dependency(self, dependency: Dependency) -> ScanResult:
        """Scan a single dependency for vulnerabilities."""
        vulnerabilities = self.vuln_db.get_vulnerabilities(dependency.name)
        applicable_vulns = []
        
        for vuln in vulnerabilities:
            if self._is_version_affected(dependency.version, vuln.affected_versions):
                applicable_vulns.append(vuln)
        
        is_vulnerable = len(applicable_vulns) > 0
        risk_score = self._calculate_risk_score(applicable_vulns)
        
        return ScanResult(
            dependency=dependency,
            vulnerabilities=applicable_vulns,
            is_vulnerable=is_vulnerable,
            risk_score=risk_score
        )
    
    def _is_version_affected(self, version: str, affected_versions: List[str]) -> bool:
        """Check if a version is in the list of affected versions."""
        # Simplified version comparison - in production use proper version parsing
        if version == "latest":
            return True  # Latest version might be vulnerable
        return version in affected_versions
    
    def _calculate_risk_score(self, vulnerabilities: List[Vulnerability]) -> float:
        """Calculate risk score based on vulnerabilities."""
        if not vulnerabilities:
            return 0.0
        
        total_score = sum(self.severity_scores[vuln.severity] for vuln in vulnerabilities)
        return min(total_score, 10.0)  # Cap at 10.0

# What we accomplished in this step:
# - Created vulnerability database with mock data
# - Implemented dependency scanner that checks for vulnerabilities
# - Added risk scoring based on vulnerability severity
# - Created scan results structure for reporting


# Step 4: Create secure dependency manager with license compliance
# ===============================================================================

# Explanation:
# We create a secure dependency manager that validates dependencies,
# checks licenses, and manages secure installations.

import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import urlparse
import warnings

class SeverityLevel(Enum):
    """Severity levels for vulnerabilities."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class LicenseType(Enum):
    """License types for compliance checking."""
    APPROVED = "approved"
    RESTRICTED = "restricted"
    FORBIDDEN = "forbidden"
    UNKNOWN = "unknown"

@dataclass
class Dependency:
    """Represents a software dependency."""
    name: str
    version: str
    source: str = "pypi"
    hash_value: Optional[str] = None
    license: Optional[str] = None
    
    def __str__(self):
        return f"{self.name}=={self.version}"

@dataclass
class Vulnerability:
    """Represents a security vulnerability."""
    id: str
    title: str
    description: str
    severity: SeverityLevel
    affected_versions: List[str]
    fixed_version: Optional[str] = None
    cve_id: Optional[str] = None
    published_date: Optional[datetime] = None

class DependencyParser:
    """Parses dependency files and extracts dependency information."""
    
    def __init__(self):
        self.version_pattern = re.compile(r'^([a-zA-Z0-9_-]+)\s*([><=!~]+)\s*([0-9\.]+.*?)(?:\s*#.*)?$')
        self.simple_pattern = re.compile(r'^([a-zA-Z0-9_-]+)(?:\s*#.*)?$')
    
    def parse_requirements_file(self, file_path: str) -> List[Dependency]:
        """Parse a requirements.txt file and return list of dependencies."""
        dependencies = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, 1):
                    line = line.strip()
                    
                    # Skip empty lines and comments
                    if not line or line.startswith('#'):
                        continue
                    
                    # Skip -r, -e, and other pip options
                    if line.startswith('-'):
                        continue
                    
                    dependency = self._parse_dependency_line(line, line_num)
                    if dependency:
                        dependencies.append(dependency)
        
        except FileNotFoundError:
            raise FileNotFoundError(f"Requirements file not found: {file_path}")
        except Exception as e:
            raise ValueError(f"Error parsing requirements file: {e}")
        
        return dependencies
    
    def _parse_dependency_line(self, line: str, line_num: int) -> Optional[Dependency]:
        """Parse a single dependency line."""
        # Try versioned dependency first
        match = self.version_pattern.match(line)
        if match:
            name, operator, version = match.groups()
            # For security, we prefer exact versions
            if operator == '==':
                return Dependency(name=name.lower(), version=version)
            else:
                warnings.warn(f"Line {line_num}: Non-exact version '{operator}' detected for {name}. "
                            f"Consider pinning to exact version for security.")
                return Dependency(name=name.lower(), version=version)
        
        # Try simple dependency without version
        match = self.simple_pattern.match(line)
        if match:
            name = match.group(1)
            warnings.warn(f"Line {line_num}: No version specified for {name}. "
                        f"This is a security risk - always pin versions.")
            return Dependency(name=name.lower(), version="latest")
        
        warnings.warn(f"Line {line_num}: Could not parse dependency line: {line}")
        return None
    
    def parse_installed_packages(self) -> List[Dependency]:
        """Get list of currently installed packages."""
        try:
            result = subprocess.run([sys.executable, '-m', 'pip', 'list', '--format=json'], 
                                  capture_output=True, text=True, check=True)
            packages = json.loads(result.stdout)
            
            dependencies = []
            for package in packages:
                dependencies.append(Dependency(
                    name=package['name'].lower(),
                    version=package['version']
                ))
            
            return dependencies
        
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to get installed packages: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Failed to parse pip output: {e}")

@dataclass
class ScanResult:
    """Results of a dependency security scan."""
    dependency: Dependency
    vulnerabilities: List[Vulnerability] = field(default_factory=list)
    is_vulnerable: bool = False
    risk_score: float = 0.0

class VulnerabilityDatabase:
    """Mock vulnerability database for demonstration."""
    
    def __init__(self):
        # In production, this would connect to real vulnerability databases
        # like OSV, CVE, PyUp, etc.
        self.vulnerabilities = {
            "requests": [
                Vulnerability(
                    id="VULN-001",
                    title="Server-Side Request Forgery in requests",
                    description="Requests library vulnerable to SSRF attacks in versions < 2.31.0",
                    severity=SeverityLevel.HIGH,
                    affected_versions=["2.25.0", "2.26.0", "2.27.0", "2.28.0", "2.29.0", "2.30.0"],
                    fixed_version="2.31.0",
                    cve_id="CVE-2025-32681"
                )
            ],
            "django": [
                Vulnerability(
                    id="VULN-002",
                    title="SQL Injection in Django ORM",
                    description="Django ORM vulnerable to SQL injection in versions < 4.2.7",
                    severity=SeverityLevel.CRITICAL,
                    affected_versions=["4.0.0", "4.1.0", "4.2.0", "4.2.1", "4.2.2", "4.2.3", "4.2.4", "4.2.5", "4.2.6"],
                    fixed_version="4.2.7",
                    cve_id="CVE-2025-43665"
                )
            ],
            "flask": [
                Vulnerability(
                    id="VULN-003",
                    title="Session Cookie Security Issue",
                    description="Flask session cookies not properly secured in versions < 2.3.3",
                    severity=SeverityLevel.MEDIUM,
                    affected_versions=["2.0.0", "2.1.0", "2.2.0", "2.3.0", "2.3.1", "2.3.2"],
                    fixed_version="2.3.3",
                    cve_id="CVE-2025-30861"
                )
            ]
        }
    
    def get_vulnerabilities(self, package_name: str) -> List[Vulnerability]:
        """Get vulnerabilities for a specific package."""
        return self.vulnerabilities.get(package_name.lower(), [])

class DependencyScanner:
    """Scans dependencies for security vulnerabilities."""
    
    def __init__(self):
        self.parser = DependencyParser()
        self.vuln_db = VulnerabilityDatabase()
        self.severity_scores = {
            SeverityLevel.LOW: 1.0,
            SeverityLevel.MEDIUM: 3.0,
            SeverityLevel.HIGH: 7.0,
            SeverityLevel.CRITICAL: 10.0
        }
    
    def scan_dependencies(self, dependencies: List[Dependency]) -> List[ScanResult]:
        """Scan a list of dependencies for vulnerabilities."""
        results = []
        
        for dependency in dependencies:
            result = self._scan_single_dependency(dependency)
            results.append(result)
        
        return results
    
    def scan_requirements_file(self, file_path: str) -> List[ScanResult]:
        """Scan dependencies from a requirements file."""
        dependencies = self.parser.parse_requirements_file(file_path)
        return self.scan_dependencies(dependencies)
    
    def _scan_single_dependency(self, dependency: Dependency) -> ScanResult:
        """Scan a single dependency for vulnerabilities."""
        vulnerabilities = self.vuln_db.get_vulnerabilities(dependency.name)
        applicable_vulns = []
        
        for vuln in vulnerabilities:
            if self._is_version_affected(dependency.version, vuln.affected_versions):
                applicable_vulns.append(vuln)
        
        is_vulnerable = len(applicable_vulns) > 0
        risk_score = self._calculate_risk_score(applicable_vulns)
        
        return ScanResult(
            dependency=dependency,
            vulnerabilities=applicable_vulns,
            is_vulnerable=is_vulnerable,
            risk_score=risk_score
        )
    
    def _is_version_affected(self, version: str, affected_versions: List[str]) -> bool:
        """Check if a version is in the list of affected versions."""
        # Simplified version comparison - in production use proper version parsing
        if version == "latest":
            return True  # Latest version might be vulnerable
        return version in affected_versions
    
    def _calculate_risk_score(self, vulnerabilities: List[Vulnerability]) -> float:
        """Calculate risk score based on vulnerabilities."""
        if not vulnerabilities:
            return 0.0
        
        total_score = sum(self.severity_scores[vuln.severity] for vuln in vulnerabilities)
        return min(total_score, 10.0)  # Cap at 10.0

class LicenseChecker:
    """Checks license compliance for dependencies."""
    
    def __init__(self):
        # Define license classifications
        self.license_classifications = {
            # Approved open source licenses
            "MIT": LicenseType.APPROVED,
            "Apache-2.0": LicenseType.APPROVED,
            "BSD-3-Clause": LicenseType.APPROVED,
            "BSD-2-Clause": LicenseType.APPROVED,
            "ISC": LicenseType.APPROVED,
            "Python Software Foundation License": LicenseType.APPROVED,
            
            # Restricted licenses (require legal review)
            "GPL-3.0": LicenseType.RESTRICTED,
            "GPL-2.0": LicenseType.RESTRICTED,
            "LGPL-3.0": LicenseType.RESTRICTED,
            "AGPL-3.0": LicenseType.RESTRICTED,
            
            # Forbidden licenses
            "WTFPL": LicenseType.FORBIDDEN,
            "Unlicense": LicenseType.FORBIDDEN,
        }
        
        # Mock license database
        self.package_licenses = {
            "requests": "Apache-2.0",
            "django": "BSD-3-Clause",
            "flask": "BSD-3-Clause",
            "numpy": "BSD-3-Clause",
            "pandas": "BSD-3-Clause",
            "matplotlib": "Python Software Foundation License",
            "scipy": "BSD-3-Clause",
            "pillow": "PIL Software License",  # Custom license
        }
    
    def check_license(self, dependency: Dependency) -> Tuple[Optional[str], LicenseType]:
        """Check license for a dependency."""
        license_name = self.package_licenses.get(dependency.name.lower())
        
        if not license_name:
            return None, LicenseType.UNKNOWN
        
        license_type = self.license_classifications.get(license_name, LicenseType.UNKNOWN)
        return license_name, license_type
    
    def check_licenses(self, dependencies: List[Dependency]) -> Dict[str, Tuple[Optional[str], LicenseType]]:
        """Check licenses for multiple dependencies."""
        results = {}
        for dependency in dependencies:
            license_name, license_type = self.check_license(dependency)
            results[dependency.name] = (license_name, license_type)
        return results

@dataclass
class ValidationResult:
    """Result of dependency validation."""
    dependency: Dependency
    is_valid: bool = True
    issues: List[str] = field(default_factory=list)
    license_info: Optional[Tuple[str, LicenseType]] = None

class SecureDependencyManager:
    """Manages dependencies with security and compliance checks."""
    
    def __init__(self):
        self.scanner = DependencyScanner()
        self.license_checker = LicenseChecker()
        self.parser = DependencyParser()
        
        # Security policies
        self.max_risk_score = 7.0  # Don't allow high-risk dependencies
        self.allowed_license_types = {LicenseType.APPROVED}
        self.require_exact_versions = True
    
    def validate_dependencies(self, dependencies: List[Dependency]) -> List[ValidationResult]:
        """Validate dependencies against security and compliance policies."""
        results = []
        
        # Scan for vulnerabilities
        scan_results = self.scanner.scan_dependencies(dependencies)
        scan_dict = {result.dependency.name: result for result in scan_results}
        
        # Check licenses
        license_results = self.license_checker.check_licenses(dependencies)
        
        for dependency in dependencies:
            validation_result = ValidationResult(dependency=dependency)
            
            # Check vulnerabilities
            scan_result = scan_dict.get(dependency.name)
            if scan_result and scan_result.is_vulnerable:
                if scan_result.risk_score > self.max_risk_score:
                    validation_result.is_valid = False
                    validation_result.issues.append(
                        f"High risk vulnerability (score: {scan_result.risk_score:.1f})"
                    )
                else:
                    validation_result.issues.append(
                        f"Low risk vulnerability (score: {scan_result.risk_score:.1f})"
                    )
            
            # Check license compliance
            license_name, license_type = license_results.get(dependency.name, (None, LicenseType.UNKNOWN))
            validation_result.license_info = (license_name, license_type)
            
            if license_type == LicenseType.FORBIDDEN:
                validation_result.is_valid = False
                validation_result.issues.append(f"Forbidden license: {license_name}")
            elif license_type == LicenseType.RESTRICTED:
                validation_result.issues.append(f"Restricted license requires review: {license_name}")
            elif license_type == LicenseType.UNKNOWN:
                validation_result.issues.append("Unknown license - requires investigation")
            
            # Check version pinning
            if self.require_exact_versions and dependency.version == "latest":
                validation_result.is_valid = False
                validation_result.issues.append("Version not pinned - security risk")
            
            results.append(validation_result)
        
        return results
    
    def generate_secure_requirements(self, dependencies: List[Dependency]) -> str:
        """Generate a secure requirements.txt with hash verification."""
        lines = []
        lines.append("# Secure requirements file generated by SecureDependencyManager")
        lines.append("# All versions are pinned for security")
        lines.append("")
        
        validation_results = self.validate_dependencies(dependencies)
        
        for result in validation_results:
            if result.is_valid:
                dep = result.dependency
                line = f"{dep.name}=={dep.version}"
                
                # Add hash if available (in production, fetch from PyPI)
                if dep.hash_value:
                    line += f" --hash=sha256:{dep.hash_value}"
                
                lines.append(line)
                
                # Add comments for issues
                if result.issues:
                    for issue in result.issues:
                        lines.append(f"    # WARNING: {issue}")
            else:
                lines.append(f"# BLOCKED: {result.dependency.name}=={result.dependency.version}")
                for issue in result.issues:
                    lines.append(f"#   REASON: {issue}")
        
        return "\n".join(lines)
    
    def install_secure(self, requirements_file: str, dry_run: bool = True) -> bool:
        """Securely install dependencies with validation."""
        try:
            dependencies = self.parser.parse_requirements_file(requirements_file)
            validation_results = self.validate_dependencies(dependencies)
            
            # Check if all dependencies are valid
            invalid_deps = [r for r in validation_results if not r.is_valid]
            if invalid_deps:
                print("❌ Installation blocked due to security/compliance issues:")
                for result in invalid_deps:
                    print(f"  - {result.dependency.name}: {', '.join(result.issues)}")
                return False
            
            # Show warnings for valid but concerning dependencies
            warning_deps = [r for r in validation_results if r.is_valid and r.issues]
            if warning_deps:
                print("⚠️  Warnings for dependencies:")
                for result in warning_deps:
                    print(f"  - {result.dependency.name}: {', '.join(result.issues)}")
            
            if dry_run:
                print("✅ Dry run: All dependencies passed validation")
                return True
            
            # In production, this would actually install the packages
            print("✅ Installing validated dependencies...")
            return True
            
        except Exception as e:
            print(f"❌ Installation failed: {e}")
            return False

# What we accomplished in this step:
# - Created license checker with compliance classifications
# - Implemented secure dependency manager with validation policies
# - Added secure requirements file generation with hash verification
# - Created secure installation process with dry-run capability


# Step 5: Create security monitoring and alerting system
# ===============================================================================

# Explanation:
# We create a monitoring system that tracks dependency security over time
# and provides alerting for new vulnerabilities.

import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import urlparse
import warnings

class SeverityLevel(Enum):
    """Severity levels for vulnerabilities."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class LicenseType(Enum):
    """License types for compliance checking."""
    APPROVED = "approved"
    RESTRICTED = "restricted"
    FORBIDDEN = "forbidden"
    UNKNOWN = "unknown"

class AlertLevel(Enum):
    """Alert levels for monitoring."""
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"

@dataclass
class Dependency:
    """Represents a software dependency."""
    name: str
    version: str
    source: str = "pypi"
    hash_value: Optional[str] = None
    license: Optional[str] = None
    
    def __str__(self):
        return f"{self.name}=={self.version}"

@dataclass
class Vulnerability:
    """Represents a security vulnerability."""
    id: str
    title: str
    description: str
    severity: SeverityLevel
    affected_versions: List[str]
    fixed_version: Optional[str] = None
    cve_id: Optional[str] = None
    published_date: Optional[datetime] = None

class DependencyParser:
    """Parses dependency files and extracts dependency information."""
    
    def __init__(self):
        self.version_pattern = re.compile(r'^([a-zA-Z0-9_-]+)\s*([><=!~]+)\s*([0-9\.]+.*?)(?:\s*#.*)?$')
        self.simple_pattern = re.compile(r'^([a-zA-Z0-9_-]+)(?:\s*#.*)?$')
    
    def parse_requirements_file(self, file_path: str) -> List[Dependency]:
        """Parse a requirements.txt file and return list of dependencies."""
        dependencies = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, 1):
                    line = line.strip()
                    
                    # Skip empty lines and comments
                    if not line or line.startswith('#'):
                        continue
                    
                    # Skip -r, -e, and other pip options
                    if line.startswith('-'):
                        continue
                    
                    dependency = self._parse_dependency_line(line, line_num)
                    if dependency:
                        dependencies.append(dependency)
        
        except FileNotFoundError:
            raise FileNotFoundError(f"Requirements file not found: {file_path}")
        except Exception as e:
            raise ValueError(f"Error parsing requirements file: {e}")
        
        return dependencies
    
    def _parse_dependency_line(self, line: str, line_num: int) -> Optional[Dependency]:
        """Parse a single dependency line."""
        # Try versioned dependency first
        match = self.version_pattern.match(line)
        if match:
            name, operator, version = match.groups()
            # For security, we prefer exact versions
            if operator == '==':
                return Dependency(name=name.lower(), version=version)
            else:
                warnings.warn(f"Line {line_num}: Non-exact version '{operator}' detected for {name}. "
                            f"Consider pinning to exact version for security.")
                return Dependency(name=name.lower(), version=version)
        
        # Try simple dependency without version
        match = self.simple_pattern.match(line)
        if match:
            name = match.group(1)
            warnings.warn(f"Line {line_num}: No version specified for {name}. "
                        f"This is a security risk - always pin versions.")
            return Dependency(name=name.lower(), version="latest")
        
        warnings.warn(f"Line {line_num}: Could not parse dependency line: {line}")
        return None
    
    def parse_installed_packages(self) -> List[Dependency]:
        """Get list of currently installed packages."""
        try:
            result = subprocess.run([sys.executable, '-m', 'pip', 'list', '--format=json'], 
                                  capture_output=True, text=True, check=True)
            packages = json.loads(result.stdout)
            
            dependencies = []
            for package in packages:
                dependencies.append(Dependency(
                    name=package['name'].lower(),
                    version=package['version']
                ))
            
            return dependencies
        
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to get installed packages: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Failed to parse pip output: {e}")

@dataclass
class ScanResult:
    """Results of a dependency security scan."""
    dependency: Dependency
    vulnerabilities: List[Vulnerability] = field(default_factory=list)
    is_vulnerable: bool = False
    risk_score: float = 0.0

class VulnerabilityDatabase:
    """Mock vulnerability database for demonstration."""
    
    def __init__(self):
        # In production, this would connect to real vulnerability databases
        # like OSV, CVE, PyUp, etc.
        self.vulnerabilities = {
            "requests": [
                Vulnerability(
                    id="VULN-001",
                    title="Server-Side Request Forgery in requests",
                    description="Requests library vulnerable to SSRF attacks in versions < 2.31.0",
                    severity=SeverityLevel.HIGH,
                    affected_versions=["2.25.0", "2.26.0", "2.27.0", "2.28.0", "2.29.0", "2.30.0"],
                    fixed_version="2.31.0",
                    cve_id="CVE-2025-32681"
                )
            ],
            "django": [
                Vulnerability(
                    id="VULN-002",
                    title="SQL Injection in Django ORM",
                    description="Django ORM vulnerable to SQL injection in versions < 4.2.7",
                    severity=SeverityLevel.CRITICAL,
                    affected_versions=["4.0.0", "4.1.0", "4.2.0", "4.2.1", "4.2.2", "4.2.3", "4.2.4", "4.2.5", "4.2.6"],
                    fixed_version="4.2.7",
                    cve_id="CVE-2025-43665"
                )
            ],
            "flask": [
                Vulnerability(
                    id="VULN-003",
                    title="Session Cookie Security Issue",
                    description="Flask session cookies not properly secured in versions < 2.3.3",
                    severity=SeverityLevel.MEDIUM,
                    affected_versions=["2.0.0", "2.1.0", "2.2.0", "2.3.0", "2.3.1", "2.3.2"],
                    fixed_version="2.3.3",
                    cve_id="CVE-2025-30861"
                )
            ]
        }
    
    def get_vulnerabilities(self, package_name: str) -> List[Vulnerability]:
        """Get vulnerabilities for a specific package."""
        return self.vulnerabilities.get(package_name.lower(), [])

class DependencyScanner:
    """Scans dependencies for security vulnerabilities."""
    
    def __init__(self):
        self.parser = DependencyParser()
        self.vuln_db = VulnerabilityDatabase()
        self.severity_scores = {
            SeverityLevel.LOW: 1.0,
            SeverityLevel.MEDIUM: 3.0,
            SeverityLevel.HIGH: 7.0,
            SeverityLevel.CRITICAL: 10.0
        }
    
    def scan_dependencies(self, dependencies: List[Dependency]) -> List[ScanResult]:
        """Scan a list of dependencies for vulnerabilities."""
        results = []
        
        for dependency in dependencies:
            result = self._scan_single_dependency(dependency)
            results.append(result)
        
        return results
    
    def scan_requirements_file(self, file_path: str) -> List[ScanResult]:
        """Scan dependencies from a requirements file."""
        dependencies = self.parser.parse_requirements_file(file_path)
        return self.scan_dependencies(dependencies)
    
    def _scan_single_dependency(self, dependency: Dependency) -> ScanResult:
        """Scan a single dependency for vulnerabilities."""
        vulnerabilities = self.vuln_db.get_vulnerabilities(dependency.name)
        applicable_vulns = []
        
        for vuln in vulnerabilities:
            if self._is_version_affected(dependency.version, vuln.affected_versions):
                applicable_vulns.append(vuln)
        
        is_vulnerable = len(applicable_vulns) > 0
        risk_score = self._calculate_risk_score(applicable_vulns)
        
        return ScanResult(
            dependency=dependency,
            vulnerabilities=applicable_vulns,
            is_vulnerable=is_vulnerable,
            risk_score=risk_score
        )
    
    def _is_version_affected(self, version: str, affected_versions: List[str]) -> bool:
        """Check if a version is in the list of affected versions."""
        # Simplified version comparison - in production use proper version parsing
        if version == "latest":
            return True  # Latest version might be vulnerable
        return version in affected_versions
    
    def _calculate_risk_score(self, vulnerabilities: List[Vulnerability]) -> float:
        """Calculate risk score based on vulnerabilities."""
        if not vulnerabilities:
            return 0.0
        
        total_score = sum(self.severity_scores[vuln.severity] for vuln in vulnerabilities)
        return min(total_score, 10.0)  # Cap at 10.0

class LicenseChecker:
    """Checks license compliance for dependencies."""
    
    def __init__(self):
        # Define license classifications
        self.license_classifications = {
            # Approved open source licenses
            "MIT": LicenseType.APPROVED,
            "Apache-2.0": LicenseType.APPROVED,
            "BSD-3-Clause": LicenseType.APPROVED,
            "BSD-2-Clause": LicenseType.APPROVED,
            "ISC": LicenseType.APPROVED,
            "Python Software Foundation License": LicenseType.APPROVED,
            
            # Restricted licenses (require legal review)
            "GPL-3.0": LicenseType.RESTRICTED,
            "GPL-2.0": LicenseType.RESTRICTED,
            "LGPL-3.0": LicenseType.RESTRICTED,
            "AGPL-3.0": LicenseType.RESTRICTED,
            
            # Forbidden licenses
            "WTFPL": LicenseType.FORBIDDEN,
            "Unlicense": LicenseType.FORBIDDEN,
        }
        
        # Mock license database
        self.package_licenses = {
            "requests": "Apache-2.0",
            "django": "BSD-3-Clause",
            "flask": "BSD-3-Clause",
            "numpy": "BSD-3-Clause",
            "pandas": "BSD-3-Clause",
            "matplotlib": "Python Software Foundation License",
            "scipy": "BSD-3-Clause",
            "pillow": "PIL Software License",  # Custom license
        }
    
    def check_license(self, dependency: Dependency) -> Tuple[Optional[str], LicenseType]:
        """Check license for a dependency."""
        license_name = self.package_licenses.get(dependency.name.lower())
        
        if not license_name:
            return None, LicenseType.UNKNOWN
        
        license_type = self.license_classifications.get(license_name, LicenseType.UNKNOWN)
        return license_name, license_type
    
    def check_licenses(self, dependencies: List[Dependency]) -> Dict[str, Tuple[Optional[str], LicenseType]]:
        """Check licenses for multiple dependencies."""
        results = {}
        for dependency in dependencies:
            license_name, license_type = self.check_license(dependency)
            results[dependency.name] = (license_name, license_type)
        return results

@dataclass
class ValidationResult:
    """Result of dependency validation."""
    dependency: Dependency
    is_valid: bool = True
    issues: List[str] = field(default_factory=list)
    license_info: Optional[Tuple[str, LicenseType]] = None

class SecureDependencyManager:
    """Manages dependencies with security and compliance checks."""
    
    def __init__(self):
        self.scanner = DependencyScanner()
        self.license_checker = LicenseChecker()
        self.parser = DependencyParser()
        
        # Security policies
        self.max_risk_score = 7.0  # Don't allow high-risk dependencies
        self.allowed_license_types = {LicenseType.APPROVED}
        self.require_exact_versions = True
    
    def validate_dependencies(self, dependencies: List[Dependency]) -> List[ValidationResult]:
        """Validate dependencies against security and compliance policies."""
        results = []
        
        # Scan for vulnerabilities
        scan_results = self.scanner.scan_dependencies(dependencies)
        scan_dict = {result.dependency.name: result for result in scan_results}
        
        # Check licenses
        license_results = self.license_checker.check_licenses(dependencies)
        
        for dependency in dependencies:
            validation_result = ValidationResult(dependency=dependency)
            
            # Check vulnerabilities
            scan_result = scan_dict.get(dependency.name)
            if scan_result and scan_result.is_vulnerable:
                if scan_result.risk_score > self.max_risk_score:
                    validation_result.is_valid = False
                    validation_result.issues.append(
                        f"High risk vulnerability (score: {scan_result.risk_score:.1f})"
                    )
                else:
                    validation_result.issues.append(
                        f"Low risk vulnerability (score: {scan_result.risk_score:.1f})"
                    )
            
            # Check license compliance
            license_name, license_type = license_results.get(dependency.name, (None, LicenseType.UNKNOWN))
            validation_result.license_info = (license_name, license_type)
            
            if license_type == LicenseType.FORBIDDEN:
                validation_result.is_valid = False
                validation_result.issues.append(f"Forbidden license: {license_name}")
            elif license_type == LicenseType.RESTRICTED:
                validation_result.issues.append(f"Restricted license requires review: {license_name}")
            elif license_type == LicenseType.UNKNOWN:
                validation_result.issues.append("Unknown license - requires investigation")
            
            # Check version pinning
            if self.require_exact_versions and dependency.version == "latest":
                validation_result.is_valid = False
                validation_result.issues.append("Version not pinned - security risk")
            
            results.append(validation_result)
        
        return results
    
    def generate_secure_requirements(self, dependencies: List[Dependency]) -> str:
        """Generate a secure requirements.txt with hash verification."""
        lines = []
        lines.append("# Secure requirements file generated by SecureDependencyManager")
        lines.append("# All versions are pinned for security")
        lines.append("")
        
        validation_results = self.validate_dependencies(dependencies)
        
        for result in validation_results:
            if result.is_valid:
                dep = result.dependency
                line = f"{dep.name}=={dep.version}"
                
                # Add hash if available (in production, fetch from PyPI)
                if dep.hash_value:
                    line += f" --hash=sha256:{dep.hash_value}"
                
                lines.append(line)
                
                # Add comments for issues
                if result.issues:
                    for issue in result.issues:
                        lines.append(f"    # WARNING: {issue}")
            else:
                lines.append(f"# BLOCKED: {result.dependency.name}=={result.dependency.version}")
                for issue in result.issues:
                    lines.append(f"#   REASON: {issue}")
        
        return "\n".join(lines)
    
    def install_secure(self, requirements_file: str, dry_run: bool = True) -> bool:
        """Securely install dependencies with validation."""
        try:
            dependencies = self.parser.parse_requirements_file(requirements_file)
            validation_results = self.validate_dependencies(dependencies)
            
            # Check if all dependencies are valid
            invalid_deps = [r for r in validation_results if not r.is_valid]
            if invalid_deps:
                print("❌ Installation blocked due to security/compliance issues:")
                for result in invalid_deps:
                    print(f"  - {result.dependency.name}: {', '.join(result.issues)}")
                return False
            
            # Show warnings for valid but concerning dependencies
            warning_deps = [r for r in validation_results if r.is_valid and r.issues]
            if warning_deps:
                print("⚠️  Warnings for dependencies:")
                for result in warning_deps:
                    print(f"  - {result.dependency.name}: {', '.join(result.issues)}")
            
            if dry_run:
                print("✅ Dry run: All dependencies passed validation")
                return True
            
            # In production, this would actually install the packages
            print("✅ Installing validated dependencies...")
            return True
            
        except Exception as e:
            print(f"❌ Installation failed: {e}")
            return False

@dataclass
class SecurityAlert:
    """Represents a security alert."""
    id: str
    timestamp: datetime
    level: AlertLevel
    title: str
    description: str
    affected_dependencies: List[str]
    recommended_action: str

@dataclass
class MonitoringReport:
    """Security monitoring report."""
    timestamp: datetime
    total_dependencies: int
    vulnerable_dependencies: int
    critical_vulnerabilities: int
    high_vulnerabilities: int
    medium_vulnerabilities: int
    low_vulnerabilities: int
    license_issues: int
    overall_risk_score: float
    alerts: List[SecurityAlert] = field(default_factory=list)

class SecurityMonitor:
    """Monitors dependency security and generates alerts."""
    
    def __init__(self):
        self.scanner = DependencyScanner()
        self.manager = SecureDependencyManager()
        self.alert_history: List[SecurityAlert] = []
        self.last_scan_results: Optional[List[ScanResult]] = None
    
    def monitor_dependencies(self, dependencies: List[Dependency]) -> MonitoringReport:
        """Monitor dependencies and generate security report."""
        timestamp = datetime.now()
        
        # Scan for vulnerabilities
        scan_results = self.scanner.scan_dependencies(dependencies)
        validation_results = self.manager.validate_dependencies(dependencies)
        
        # Generate statistics
        total_deps = len(dependencies)
        vulnerable_deps = sum(1 for result in scan_results if result.is_vulnerable)
        
        # Count vulnerabilities by severity
        critical_vulns = 0
        high_vulns = 0
        medium_vulns = 0
        low_vulns = 0
        
        for result in scan_results:
            for vuln in result.vulnerabilities:
                if vuln.severity == SeverityLevel.CRITICAL:
                    critical_vulns += 1
                elif vuln.severity == SeverityLevel.HIGH:
                    high_vulns += 1
                elif vuln.severity == SeverityLevel.MEDIUM:
                    medium_vulns += 1
                elif vuln.severity == SeverityLevel.LOW:
                    low_vulns += 1
        
        # Count license issues
        license_issues = sum(1 for result in validation_results if not result.is_valid)
        
        # Calculate overall risk score
        total_risk = sum(result.risk_score for result in scan_results)
        overall_risk = total_risk / max(total_deps, 1)
        
        # Generate alerts
        alerts = self._generate_alerts(scan_results, validation_results)
        
        # Store scan results for comparison
        self.last_scan_results = scan_results
        
        return MonitoringReport(
            timestamp=timestamp,
            total_dependencies=total_deps,
            vulnerable_dependencies=vulnerable_deps,
            critical_vulnerabilities=critical_vulns,
            high_vulnerabilities=high_vulns,
            medium_vulnerabilities=medium_vulns,
            low_vulnerabilities=low_vulns,
            license_issues=license_issues,
            overall_risk_score=overall_risk,
            alerts=alerts
        )
    
    def _generate_alerts(self, scan_results: List[ScanResult], 
                        validation_results: List[ValidationResult]) -> List[SecurityAlert]:
        """Generate security alerts based on scan results."""
        alerts = []
        
        # Critical vulnerability alerts
        critical_deps = []
        for result in scan_results:
            for vuln in result.vulnerabilities:
                if vuln.severity == SeverityLevel.CRITICAL:
                    critical_deps.append(result.dependency.name)
        
        if critical_deps:
            alert = SecurityAlert(
                id=f"CRIT-{datetime.now().strftime('%Y%m%d%H%M%S')}",
                timestamp=datetime.now(),
                level=AlertLevel.CRITICAL,
                title="Critical Vulnerabilities Detected",
                description=f"Found critical vulnerabilities in {len(critical_deps)} dependencies",
                affected_dependencies=critical_deps,
                recommended_action="Immediately update affected dependencies or remove them"
            )
            alerts.append(alert)
        
        # High-risk dependency alerts
        high_risk_deps = []
        for result in scan_results:
            if result.risk_score >= 7.0:
                high_risk_deps.append(result.dependency.name)
        
        if high_risk_deps:
            alert = SecurityAlert(
                id=f"HIGH-{datetime.now().strftime('%Y%m%d%H%M%S')}",
                timestamp=datetime.now(),
                level=AlertLevel.ERROR,
                title="High-Risk Dependencies Detected",
                description=f"Found {len(high_risk_deps)} high-risk dependencies",
                affected_dependencies=high_risk_deps,
                recommended_action="Review and update high-risk dependencies"
            )
            alerts.append(alert)
        
        # License compliance alerts
        license_violation_deps = []
        for result in validation_results:
            if not result.is_valid and any("license" in issue.lower() for issue in result.issues):
                license_violation_deps.append(result.dependency.name)
        
        if license_violation_deps:
            alert = SecurityAlert(
                id=f"LIC-{datetime.now().strftime('%Y%m%d%H%M%S')}",
                timestamp=datetime.now(),
                level=AlertLevel.WARNING,
                title="License Compliance Issues",
                description=f"Found license issues in {len(license_violation_deps)} dependencies",
                affected_dependencies=license_violation_deps,
                recommended_action="Review license compliance and replace problematic dependencies"
            )
            alerts.append(alert)
        
        return alerts
    
    def generate_security_report(self, report: MonitoringReport) -> str:
        """Generate a formatted security report."""
        lines = []
        lines.append("=" * 60)
        lines.append("DEPENDENCY SECURITY MONITORING REPORT")
        lines.append("=" * 60)
        lines.append(f"Generated: {report.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("")
        
        # Summary statistics
        lines.append("SUMMARY:")
        lines.append(f"  Total Dependencies: {report.total_dependencies}")
        lines.append(f"  Vulnerable Dependencies: {report.vulnerable_dependencies}")
        lines.append(f"  Overall Risk Score: {report.overall_risk_score:.2f}/10.0")
        lines.append("")
        
        # Vulnerability breakdown
        lines.append("VULNERABILITIES BY SEVERITY:")
        lines.append(f"  Critical: {report.critical_vulnerabilities}")
        lines.append(f"  High: {report.high_vulnerabilities}")
        lines.append(f"  Medium: {report.medium_vulnerabilities}")
        lines.append(f"  Low: {report.low_vulnerabilities}")
        lines.append("")
        
        # License issues
        lines.append(f"LICENSE ISSUES: {report.license_issues}")
        lines.append("")
        
        # Alerts
        if report.alerts:
            lines.append("SECURITY ALERTS:")
            for alert in report.alerts:
                lines.append(f"  [{alert.level.value.upper()}] {alert.title}")
                lines.append(f"    {alert.description}")
                lines.append(f"    Affected: {', '.join(alert.affected_dependencies)}")
                lines.append(f"    Action: {alert.recommended_action}")
                lines.append("")
        else:
            lines.append("✅ No security alerts")
        
        lines.append("=" * 60)
        
        return "\n".join(lines)

# What we accomplished in this step:
# - Created security monitoring system with alerting
# - Implemented comprehensive reporting with statistics
# - Added alert generation for different security issues
# - Created formatted security reports for stakeholders


# Step 6: Test the complete dependency security system
# ===============================================================================

# Explanation:
# Let's test our complete dependency security system with sample data
# to demonstrate all the security features working together.

import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import urlparse
import warnings

class SeverityLevel(Enum):
    """Severity levels for vulnerabilities."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class LicenseType(Enum):
    """License types for compliance checking."""
    APPROVED = "approved"
    RESTRICTED = "restricted"
    FORBIDDEN = "forbidden"
    UNKNOWN = "unknown"

class AlertLevel(Enum):
    """Alert levels for monitoring."""
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"

@dataclass
class Dependency:
    """Represents a software dependency."""
    name: str
    version: str
    source: str = "pypi"
    hash_value: Optional[str] = None
    license: Optional[str] = None
    
    def __str__(self):
        return f"{self.name}=={self.version}"

@dataclass
class Vulnerability:
    """Represents a security vulnerability."""
    id: str
    title: str
    description: str
    severity: SeverityLevel
    affected_versions: List[str]
    fixed_version: Optional[str] = None
    cve_id: Optional[str] = None
    published_date: Optional[datetime] = None

class DependencyParser:
    """Parses dependency files and extracts dependency information."""
    
    def __init__(self):
        self.version_pattern = re.compile(r'^([a-zA-Z0-9_-]+)\s*([><=!~]+)\s*([0-9\.]+.*?)(?:\s*#.*)?$')
        self.simple_pattern = re.compile(r'^([a-zA-Z0-9_-]+)(?:\s*#.*)?$')
    
    def parse_requirements_file(self, file_path: str) -> List[Dependency]:
        """Parse a requirements.txt file and return list of dependencies."""
        dependencies = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, 1):
                    line = line.strip()
                    
                    # Skip empty lines and comments
                    if not line or line.startswith('#'):
                        continue
                    
                    # Skip -r, -e, and other pip options
                    if line.startswith('-'):
                        continue
                    
                    dependency = self._parse_dependency_line(line, line_num)
                    if dependency:
                        dependencies.append(dependency)
        
        except FileNotFoundError:
            raise FileNotFoundError(f"Requirements file not found: {file_path}")
        except Exception as e:
            raise ValueError(f"Error parsing requirements file: {e}")
        
        return dependencies
    
    def _parse_dependency_line(self, line: str, line_num: int) -> Optional[Dependency]:
        """Parse a single dependency line."""
        # Try versioned dependency first
        match = self.version_pattern.match(line)
        if match:
            name, operator, version = match.groups()
            # For security, we prefer exact versions
            if operator == '==':
                return Dependency(name=name.lower(), version=version)
            else:
                warnings.warn(f"Line {line_num}: Non-exact version '{operator}' detected for {name}. "
                            f"Consider pinning to exact version for security.")
                return Dependency(name=name.lower(), version=version)
        
        # Try simple dependency without version
        match = self.simple_pattern.match(line)
        if match:
            name = match.group(1)
            warnings.warn(f"Line {line_num}: No version specified for {name}. "
                        f"This is a security risk - always pin versions.")
            return Dependency(name=name.lower(), version="latest")
        
        warnings.warn(f"Line {line_num}: Could not parse dependency line: {line}")
        return None
    
    def parse_installed_packages(self) -> List[Dependency]:
        """Get list of currently installed packages."""
        try:
            result = subprocess.run([sys.executable, '-m', 'pip', 'list', '--format=json'], 
                                  capture_output=True, text=True, check=True)
            packages = json.loads(result.stdout)
            
            dependencies = []
            for package in packages:
                dependencies.append(Dependency(
                    name=package['name'].lower(),
                    version=package['version']
                ))
            
            return dependencies
        
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to get installed packages: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Failed to parse pip output: {e}")

@dataclass
class ScanResult:
    """Results of a dependency security scan."""
    dependency: Dependency
    vulnerabilities: List[Vulnerability] = field(default_factory=list)
    is_vulnerable: bool = False
    risk_score: float = 0.0

class VulnerabilityDatabase:
    """Mock vulnerability database for demonstration."""
    
    def __init__(self):
        # In production, this would connect to real vulnerability databases
        # like OSV, CVE, PyUp, etc.
        self.vulnerabilities = {
            "requests": [
                Vulnerability(
                    id="VULN-001",
                    title="Server-Side Request Forgery in requests",
                    description="Requests library vulnerable to SSRF attacks in versions < 2.31.0",
                    severity=SeverityLevel.HIGH,
                    affected_versions=["2.25.0", "2.26.0", "2.27.0", "2.28.0", "2.29.0", "2.30.0"],
                    fixed_version="2.31.0",
                    cve_id="CVE-2025-32681"
                )
            ],
            "django": [
                Vulnerability(
                    id="VULN-002",
                    title="SQL Injection in Django ORM",
                    description="Django ORM vulnerable to SQL injection in versions < 4.2.7",
                    severity=SeverityLevel.CRITICAL,
                    affected_versions=["4.0.0", "4.1.0", "4.2.0", "4.2.1", "4.2.2", "4.2.3", "4.2.4", "4.2.5", "4.2.6"],
                    fixed_version="4.2.7",
                    cve_id="CVE-2025-43665"
                )
            ],
            "flask": [
                Vulnerability(
                    id="VULN-003",
                    title="Session Cookie Security Issue",
                    description="Flask session cookies not properly secured in versions < 2.3.3",
                    severity=SeverityLevel.MEDIUM,
                    affected_versions=["2.0.0", "2.1.0", "2.2.0", "2.3.0", "2.3.1", "2.3.2"],
                    fixed_version="2.3.3",
                    cve_id="CVE-2025-30861"
                )
            ]
        }
    
    def get_vulnerabilities(self, package_name: str) -> List[Vulnerability]:
        """Get vulnerabilities for a specific package."""
        return self.vulnerabilities.get(package_name.lower(), [])

class DependencyScanner:
    """Scans dependencies for security vulnerabilities."""
    
    def __init__(self):
        self.parser = DependencyParser()
        self.vuln_db = VulnerabilityDatabase()
        self.severity_scores = {
            SeverityLevel.LOW: 1.0,
            SeverityLevel.MEDIUM: 3.0,
            SeverityLevel.HIGH: 7.0,
            SeverityLevel.CRITICAL: 10.0
        }
    
    def scan_dependencies(self, dependencies: List[Dependency]) -> List[ScanResult]:
        """Scan a list of dependencies for vulnerabilities."""
        results = []
        
        for dependency in dependencies:
            result = self._scan_single_dependency(dependency)
            results.append(result)
        
        return results
    
    def scan_requirements_file(self, file_path: str) -> List[ScanResult]:
        """Scan dependencies from a requirements file."""
        dependencies = self.parser.parse_requirements_file(file_path)
        return self.scan_dependencies(dependencies)
    
    def _scan_single_dependency(self, dependency: Dependency) -> ScanResult:
        """Scan a single dependency for vulnerabilities."""
        vulnerabilities = self.vuln_db.get_vulnerabilities(dependency.name)
        applicable_vulns = []
        
        for vuln in vulnerabilities:
            if self._is_version_affected(dependency.version, vuln.affected_versions):
                applicable_vulns.append(vuln)
        
        is_vulnerable = len(applicable_vulns) > 0
        risk_score = self._calculate_risk_score(applicable_vulns)
        
        return ScanResult(
            dependency=dependency,
            vulnerabilities=applicable_vulns,
            is_vulnerable=is_vulnerable,
            risk_score=risk_score
        )
    
    def _is_version_affected(self, version: str, affected_versions: List[str]) -> bool:
        """Check if a version is in the list of affected versions."""
        # Simplified version comparison - in production use proper version parsing
        if version == "latest":
            return True  # Latest version might be vulnerable
        return version in affected_versions
    
    def _calculate_risk_score(self, vulnerabilities: List[Vulnerability]) -> float:
        """Calculate risk score based on vulnerabilities."""
        if not vulnerabilities:
            return 0.0
        
        total_score = sum(self.severity_scores[vuln.severity] for vuln in vulnerabilities)
        return min(total_score, 10.0)  # Cap at 10.0

class LicenseChecker:
    """Checks license compliance for dependencies."""
    
    def __init__(self):
        # Define license classifications
        self.license_classifications = {
            # Approved open source licenses
            "MIT": LicenseType.APPROVED,
            "Apache-2.0": LicenseType.APPROVED,
            "BSD-3-Clause": LicenseType.APPROVED,
            "BSD-2-Clause": LicenseType.APPROVED,
            "ISC": LicenseType.APPROVED,
            "Python Software Foundation License": LicenseType.APPROVED,
            
            # Restricted licenses (require legal review)
            "GPL-3.0": LicenseType.RESTRICTED,
            "GPL-2.0": LicenseType.RESTRICTED,
            "LGPL-3.0": LicenseType.RESTRICTED,
            "AGPL-3.0": LicenseType.RESTRICTED,
            
            # Forbidden licenses
            "WTFPL": LicenseType.FORBIDDEN,
            "Unlicense": LicenseType.FORBIDDEN,
        }
        
        # Mock license database
        self.package_licenses = {
            "requests": "Apache-2.0",
            "django": "BSD-3-Clause",
            "flask": "BSD-3-Clause",
            "numpy": "BSD-3-Clause",
            "pandas": "BSD-3-Clause",
            "matplotlib": "Python Software Foundation License",
            "scipy": "BSD-3-Clause",
            "pillow": "PIL Software License",  # Custom license
        }
    
    def check_license(self, dependency: Dependency) -> Tuple[Optional[str], LicenseType]:
        """Check license for a dependency."""
        license_name = self.package_licenses.get(dependency.name.lower())
        
        if not license_name:
            return None, LicenseType.UNKNOWN
        
        license_type = self.license_classifications.get(license_name, LicenseType.UNKNOWN)
        return license_name, license_type
    
    def check_licenses(self, dependencies: List[Dependency]) -> Dict[str, Tuple[Optional[str], LicenseType]]:
        """Check licenses for multiple dependencies."""
        results = {}
        for dependency in dependencies:
            license_name, license_type = self.check_license(dependency)
            results[dependency.name] = (license_name, license_type)
        return results

@dataclass
class ValidationResult:
    """Result of dependency validation."""
    dependency: Dependency
    is_valid: bool = True
    issues: List[str] = field(default_factory=list)
    license_info: Optional[Tuple[str, LicenseType]] = None

class SecureDependencyManager:
    """Manages dependencies with security and compliance checks."""
    
    def __init__(self):
        self.scanner = DependencyScanner()
        self.license_checker = LicenseChecker()
        self.parser = DependencyParser()
        
        # Security policies
        self.max_risk_score = 7.0  # Don't allow high-risk dependencies
        self.allowed_license_types = {LicenseType.APPROVED}
        self.require_exact_versions = True
    
    def validate_dependencies(self, dependencies: List[Dependency]) -> List[ValidationResult]:
        """Validate dependencies against security and compliance policies."""
        results = []
        
        # Scan for vulnerabilities
        scan_results = self.scanner.scan_dependencies(dependencies)
        scan_dict = {result.dependency.name: result for result in scan_results}
        
        # Check licenses
        license_results = self.license_checker.check_licenses(dependencies)
        
        for dependency in dependencies:
            validation_result = ValidationResult(dependency=dependency)
            
            # Check vulnerabilities
            scan_result = scan_dict.get(dependency.name)
            if scan_result and scan_result.is_vulnerable:
                if scan_result.risk_score > self.max_risk_score:
                    validation_result.is_valid = False
                    validation_result.issues.append(
                        f"High risk vulnerability (score: {scan_result.risk_score:.1f})"
                    )
                else:
                    validation_result.issues.append(
                        f"Low risk vulnerability (score: {scan_result.risk_score:.1f})"
                    )
            
            # Check license compliance
            license_name, license_type = license_results.get(dependency.name, (None, LicenseType.UNKNOWN))
            validation_result.license_info = (license_name, license_type)
            
            if license_type == LicenseType.FORBIDDEN:
                validation_result.is_valid = False
                validation_result.issues.append(f"Forbidden license: {license_name}")
            elif license_type == LicenseType.RESTRICTED:
                validation_result.issues.append(f"Restricted license requires review: {license_name}")
            elif license_type == LicenseType.UNKNOWN:
                validation_result.issues.append("Unknown license - requires investigation")
            
            # Check version pinning
            if self.require_exact_versions and dependency.version == "latest":
                validation_result.is_valid = False
                validation_result.issues.append("Version not pinned - security risk")
            
            results.append(validation_result)
        
        return results
    
    def generate_secure_requirements(self, dependencies: List[Dependency]) -> str:
        """Generate a secure requirements.txt with hash verification."""
        lines = []
        lines.append("# Secure requirements file generated by SecureDependencyManager")
        lines.append("# All versions are pinned for security")
        lines.append("")
        
        validation_results = self.validate_dependencies(dependencies)
        
        for result in validation_results:
            if result.is_valid:
                dep = result.dependency
                line = f"{dep.name}=={dep.version}"
                
                # Add hash if available (in production, fetch from PyPI)
                if dep.hash_value:
                    line += f" --hash=sha256:{dep.hash_value}"
                
                lines.append(line)
                
                # Add comments for issues
                if result.issues:
                    for issue in result.issues:
                        lines.append(f"    # WARNING: {issue}")
            else:
                lines.append(f"# BLOCKED: {result.dependency.name}=={result.dependency.version}")
                for issue in result.issues:
                    lines.append(f"#   REASON: {issue}")
        
        return "\n".join(lines)
    
    def install_secure(self, requirements_file: str, dry_run: bool = True) -> bool:
        """Securely install dependencies with validation."""
        try:
            dependencies = self.parser.parse_requirements_file(requirements_file)
            validation_results = self.validate_dependencies(dependencies)
            
            # Check if all dependencies are valid
            invalid_deps = [r for r in validation_results if not r.is_valid]
            if invalid_deps:
                print("❌ Installation blocked due to security/compliance issues:")
                for result in invalid_deps:
                    print(f"  - {result.dependency.name}: {', '.join(result.issues)}")
                return False
            
            # Show warnings for valid but concerning dependencies
            warning_deps = [r for r in validation_results if r.is_valid and r.issues]
            if warning_deps:
                print("⚠️  Warnings for dependencies:")
                for result in warning_deps:
                    print(f"  - {result.dependency.name}: {', '.join(result.issues)}")
            
            if dry_run:
                print("✅ Dry run: All dependencies passed validation")
                return True
            
            # In production, this would actually install the packages
            print("✅ Installing validated dependencies...")
            return True
            
        except Exception as e:
            print(f"❌ Installation failed: {e}")
            return False

@dataclass
class SecurityAlert:
    """Represents a security alert."""
    id: str
    timestamp: datetime
    level: AlertLevel
    title: str
    description: str
    affected_dependencies: List[str]
    recommended_action: str

@dataclass
class MonitoringReport:
    """Security monitoring report."""
    timestamp: datetime
    total_dependencies: int
    vulnerable_dependencies: int
    critical_vulnerabilities: int
    high_vulnerabilities: int
    medium_vulnerabilities: int
    low_vulnerabilities: int
    license_issues: int
    overall_risk_score: float
    alerts: List[SecurityAlert] = field(default_factory=list)

class SecurityMonitor:
    """Monitors dependency security and generates alerts."""
    
    def __init__(self):
        self.scanner = DependencyScanner()
        self.manager = SecureDependencyManager()
        self.alert_history: List[SecurityAlert] = []
        self.last_scan_results: Optional[List[ScanResult]] = None
    
    def monitor_dependencies(self, dependencies: List[Dependency]) -> MonitoringReport:
        """Monitor dependencies and generate security report."""
        timestamp = datetime.now()
        
        # Scan for vulnerabilities
        scan_results = self.scanner.scan_dependencies(dependencies)
        validation_results = self.manager.validate_dependencies(dependencies)
        
        # Generate statistics
        total_deps = len(dependencies)
        vulnerable_deps = sum(1 for result in scan_results if result.is_vulnerable)
        
        # Count vulnerabilities by severity
        critical_vulns = 0
        high_vulns = 0
        medium_vulns = 0
        low_vulns = 0
        
        for result in scan_results:
            for vuln in result.vulnerabilities:
                if vuln.severity == SeverityLevel.CRITICAL:
                    critical_vulns += 1
                elif vuln.severity == SeverityLevel.HIGH:
                    high_vulns += 1
                elif vuln.severity == SeverityLevel.MEDIUM:
                    medium_vulns += 1
                elif vuln.severity == SeverityLevel.LOW:
                    low_vulns += 1
        
        # Count license issues
        license_issues = sum(1 for result in validation_results if not result.is_valid)
        
        # Calculate overall risk score
        total_risk = sum(result.risk_score for result in scan_results)
        overall_risk = total_risk / max(total_deps, 1)
        
        # Generate alerts
        alerts = self._generate_alerts(scan_results, validation_results)
        
        # Store scan results for comparison
        self.last_scan_results = scan_results
        
        return MonitoringReport(
            timestamp=timestamp,
            total_dependencies=total_deps,
            vulnerable_dependencies=vulnerable_deps,
            critical_vulnerabilities=critical_vulns,
            high_vulnerabilities=high_vulns,
            medium_vulnerabilities=medium_vulns,
            low_vulnerabilities=low_vulns,
            license_issues=license_issues,
            overall_risk_score=overall_risk,
            alerts=alerts
        )
    
    def _generate_alerts(self, scan_results: List[ScanResult], 
                        validation_results: List[ValidationResult]) -> List[SecurityAlert]:
        """Generate security alerts based on scan results."""
        alerts = []
        
        # Critical vulnerability alerts
        critical_deps = []
        for result in scan_results:
            for vuln in result.vulnerabilities:
                if vuln.severity == SeverityLevel.CRITICAL:
                    critical_deps.append(result.dependency.name)
        
        if critical_deps:
            alert = SecurityAlert(
                id=f"CRIT-{datetime.now().strftime('%Y%m%d%H%M%S')}",
                timestamp=datetime.now(),
                level=AlertLevel.CRITICAL,
                title="Critical Vulnerabilities Detected",
                description=f"Found critical vulnerabilities in {len(critical_deps)} dependencies",
                affected_dependencies=critical_deps,
                recommended_action="Immediately update affected dependencies or remove them"
            )
            alerts.append(alert)
        
        # High-risk dependency alerts
        high_risk_deps = []
        for result in scan_results:
            if result.risk_score >= 7.0:
                high_risk_deps.append(result.dependency.name)
        
        if high_risk_deps:
            alert = SecurityAlert(
                id=f"HIGH-{datetime.now().strftime('%Y%m%d%H%M%S')}",
                timestamp=datetime.now(),
                level=AlertLevel.ERROR,
                title="High-Risk Dependencies Detected",
                description=f"Found {len(high_risk_deps)} high-risk dependencies",
                affected_dependencies=high_risk_deps,
                recommended_action="Review and update high-risk dependencies"
            )
            alerts.append(alert)
        
        # License compliance alerts
        license_violation_deps = []
        for result in validation_results:
            if not result.is_valid and any("license" in issue.lower() for issue in result.issues):
                license_violation_deps.append(result.dependency.name)
        
        if license_violation_deps:
            alert = SecurityAlert(
                id=f"LIC-{datetime.now().strftime('%Y%m%d%H%M%S')}",
                timestamp=datetime.now(),
                level=AlertLevel.WARNING,
                title="License Compliance Issues",
                description=f"Found license issues in {len(license_violation_deps)} dependencies",
                affected_dependencies=license_violation_deps,
                recommended_action="Review license compliance and replace problematic dependencies"
            )
            alerts.append(alert)
        
        return alerts
    
    def generate_security_report(self, report: MonitoringReport) -> str:
        """Generate a formatted security report."""
        lines = []
        lines.append("=" * 60)
        lines.append("DEPENDENCY SECURITY MONITORING REPORT")
        lines.append("=" * 60)
        lines.append(f"Generated: {report.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("")
        
        # Summary statistics
        lines.append("SUMMARY:")
        lines.append(f"  Total Dependencies: {report.total_dependencies}")
        lines.append(f"  Vulnerable Dependencies: {report.vulnerable_dependencies}")
        lines.append(f"  Overall Risk Score: {report.overall_risk_score:.2f}/10.0")
        lines.append("")
        
        # Vulnerability breakdown
        lines.append("VULNERABILITIES BY SEVERITY:")
        lines.append(f"  Critical: {report.critical_vulnerabilities}")
        lines.append(f"  High: {report.high_vulnerabilities}")
        lines.append(f"  Medium: {report.medium_vulnerabilities}")
        lines.append(f"  Low: {report.low_vulnerabilities}")
        lines.append("")
        
        # License issues
        lines.append(f"LICENSE ISSUES: {report.license_issues}")
        lines.append("")
        
        # Alerts
        if report.alerts:
            lines.append("SECURITY ALERTS:")
            for alert in report.alerts:
                lines.append(f"  [{alert.level.value.upper()}] {alert.title}")
                lines.append(f"    {alert.description}")
                lines.append(f"    Affected: {', '.join(alert.affected_dependencies)}")
                lines.append(f"    Action: {alert.recommended_action}")
                lines.append("")
        else:
            lines.append("✅ No security alerts")
        
        lines.append("=" * 60)
        
        return "\n".join(lines)

# Test the complete dependency security system
print("=== Testing Dependency Security System ===\n")

# Create sample dependencies with various security issues
test_dependencies = [
    Dependency("requests", "2.28.0"),  # Vulnerable version
    Dependency("django", "4.2.3"),    # Vulnerable version
    Dependency("flask", "2.3.3"),     # Safe version
    Dependency("numpy", "1.24.0"),    # Safe version
    Dependency("pandas", "2.0.0"),    # Safe version
    Dependency("pillow", "9.5.0"),    # Unknown license
]

print("1. Testing Dependency Scanner:")
scanner = DependencyScanner()
scan_results = scanner.scan_dependencies(test_dependencies)

for result in scan_results:
    status = "🔴 VULNERABLE" if result.is_vulnerable else "✅ SAFE"
    print(f"  {result.dependency.name} {result.dependency.version}: {status} (Risk: {result.risk_score:.1f})")
    for vuln in result.vulnerabilities:
        print(f"    - {vuln.title} ({vuln.severity.value.upper()})")

print("\n2. Testing License Checker:")
license_checker = LicenseChecker()
license_results = license_checker.check_licenses(test_dependencies)

for dep_name, (license_name, license_type) in license_results.items():
    status_icon = {
        LicenseType.APPROVED: "✅",
        LicenseType.RESTRICTED: "⚠️",
        LicenseType.FORBIDDEN: "🔴",
        LicenseType.UNKNOWN: "❓"
    }[license_type]
    print(f"  {dep_name}: {license_name or 'Unknown'} {status_icon}")

print("\n3. Testing Secure Dependency Manager:")
manager = SecureDependencyManager()
validation_results = manager.validate_dependencies(test_dependencies)

for result in validation_results:
    status = "✅ VALID" if result.is_valid else "🔴 BLOCKED"
    print(f"  {result.dependency.name}: {status}")
    for issue in result.issues:
        print(f"    - {issue}")

print("\n4. Testing Security Monitor:")
monitor = SecurityMonitor()
report = monitor.monitor_dependencies(test_dependencies)

print(monitor.generate_security_report(report))

print("\n5. Testing Secure Requirements Generation:")
secure_requirements = manager.generate_secure_requirements(test_dependencies)
print("Generated secure requirements.txt:")
print("-" * 40)
print(secure_requirements)

# What we accomplished in this step:
# - Tested all components of the dependency security system
# - Demonstrated vulnerability scanning with sample data
# - Showed license compliance checking in action
# - Generated security monitoring reports with alerts
# - Created secure requirements files with validation


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Dependency vulnerability scanning and risk assessment
# - License compliance checking and policy enforcement
# - Secure dependency management with validation
# - Security monitoring and alerting systems
# - Requirements file parsing and secure generation
# - Integration of multiple security components
#
# Security best practices covered:
# - Always pin exact dependency versions
# - Regularly scan for vulnerabilities
# - Implement license compliance policies
# - Use hash verification for package integrity
# - Monitor dependencies continuously
# - Generate security reports for stakeholders
# - Block high-risk dependencies automatically
# - Maintain audit trails of security decisions
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each security check is necessary
# 4. Experiment with different vulnerability scenarios
# 5. Try integrating with real vulnerability databases
#
# Production considerations:
# - Connect to real vulnerability databases (OSV, CVE, PyUp)
# - Implement proper version comparison logic
# - Add support for different package managers
# - Integrate with CI/CD pipelines
# - Set up automated security scanning
# - Configure alerting to security teams
# - Implement dependency update automation
# - Add support for private package repositories
#
# Remember: Dependency security is an ongoing process, not a one-time check!
# ===============================================================================

