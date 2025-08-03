"""Question: Implement a comprehensive changelog and versioning system.

Create a system that manages software versions and automatically generates
changelogs with proper semantic versioning.

Requirements:
1. Create a Version class that follows semantic versioning (MAJOR.MINOR.PATCH)
2. Create a ChangeEntry class to represent individual changes
3. Create a Changelog class to manage collections of changes
4. Implement automatic version bumping based on change types
5. Generate formatted changelog output in multiple formats

Example usage:
    changelog = Changelog("MyProject", "1.0.0")
    changelog.add_change("feat", "Add user authentication")
    changelog.add_change("fix", "Fix memory leak in parser")
    new_version = changelog.bump_version()
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
# - How to represent semantic versions (major.minor.patch)?
# - What information should each change entry contain?
# - How to categorize different types of changes?
# - How to automatically determine version bumps?
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


# Step 1: Import modules and create the Version class
# ===============================================================================

# Explanation:
# We start with a Version class that represents semantic versioning.
# Semantic versioning follows MAJOR.MINOR.PATCH format where:
# - MAJOR: incompatible API changes
# - MINOR: backwards-compatible functionality additions
# - PATCH: backwards-compatible bug fixes

from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum

class Version:
    """Represents a semantic version (MAJOR.MINOR.PATCH)."""
    
    def __init__(self, major: int = 0, minor: int = 0, patch: int = 0):
        self.major = major
        self.minor = minor
        self.patch = patch
    
    @classmethod
    def from_string(cls, version_string: str) -> 'Version':
        """Create Version from string like '1.2.3'."""
        parts = version_string.split('.')
        if len(parts) != 3:
            raise ValueError("Version must be in format 'MAJOR.MINOR.PATCH'")
        
        try:
            major, minor, patch = map(int, parts)
            return cls(major, minor, patch)
        except ValueError:
            raise ValueError("Version parts must be integers")
    
    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"
    
    def __repr__(self) -> str:
        return f"Version({self.major}, {self.minor}, {self.patch})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Version):
            return False
        return (self.major, self.minor, self.patch) == (other.major, other.minor, other.patch)
    
    def __lt__(self, other) -> bool:
        if not isinstance(other, Version):
            return NotImplemented
        return (self.major, self.minor, self.patch) < (other.major, other.minor, other.patch)


# Step 2: Create ChangeType enum and ChangeEntry class
# ===============================================================================

# Explanation:
# We need to categorize different types of changes and store information about each change.
# The ChangeType enum helps us determine how to bump versions automatically.

class ChangeType(Enum):
    """Types of changes that can be made to software."""
    BREAKING = "breaking"  # Major version bump
    FEATURE = "feat"       # Minor version bump
    FIX = "fix"           # Patch version bump
    DOCS = "docs"         # Patch version bump
    STYLE = "style"       # Patch version bump
    REFACTOR = "refactor" # Patch version bump
    PERF = "perf"         # Patch version bump
    TEST = "test"         # Patch version bump
    CHORE = "chore"       # Patch version bump

class ChangeEntry:
    """Represents a single change entry in the changelog."""
    
    def __init__(self, change_type: str, description: str, 
                 scope: Optional[str] = None, breaking: bool = False,
                 author: Optional[str] = None, date: Optional[datetime] = None):
        self.change_type = ChangeType(change_type) if isinstance(change_type, str) else change_type
        self.description = description
        self.scope = scope
        self.breaking = breaking or self.change_type == ChangeType.BREAKING
        self.author = author
        self.date = date or datetime.now()
    
    def get_version_impact(self) -> str:
        """Determine what type of version bump this change requires."""
        if self.breaking or self.change_type == ChangeType.BREAKING:
            return "major"
        elif self.change_type == ChangeType.FEATURE:
            return "minor"
        else:
            return "patch"
    
    def format_conventional(self) -> str:
        """Format as conventional commit style."""
        scope_part = f"({self.scope})" if self.scope else ""
        breaking_part = "!" if self.breaking else ""
        return f"{self.change_type.value}{scope_part}{breaking_part}: {self.description}"
    
    def __str__(self) -> str:
        return self.format_conventional()
    
    def __repr__(self) -> str:
        return f"ChangeEntry({self.change_type.value}, '{self.description}')"


# Step 3: Create the basic Changelog class structure
# ===============================================================================

# Explanation:
# The Changelog class manages collections of changes and handles version management.
# We'll start with basic functionality and build it up incrementally.

class Changelog:
    """Manages software changelog and versioning."""
    
    def __init__(self, project_name: str, initial_version: str = "0.1.0"):
        self.project_name = project_name
        self.current_version = Version.from_string(initial_version)
        self.unreleased_changes: List[ChangeEntry] = []
        self.releases: Dict[str, List[ChangeEntry]] = {}
        self.release_dates: Dict[str, datetime] = {}
    
    def add_change(self, change_type: str, description: str, 
                   scope: Optional[str] = None, breaking: bool = False,
                   author: Optional[str] = None) -> None:
        """Add a new change to the unreleased changes."""
        change = ChangeEntry(change_type, description, scope, breaking, author)
        self.unreleased_changes.append(change)
    
    def get_next_version(self) -> Version:
        """Calculate what the next version should be based on unreleased changes."""
        if not self.unreleased_changes:
            return self.current_version
        
        # Determine the highest impact change
        has_breaking = any(change.get_version_impact() == "major" for change in self.unreleased_changes)
        has_feature = any(change.get_version_impact() == "minor" for change in self.unreleased_changes)
        
        new_version = Version(self.current_version.major, self.current_version.minor, self.current_version.patch)
        
        if has_breaking:
            new_version.major += 1
            new_version.minor = 0
            new_version.patch = 0
        elif has_feature:
            new_version.minor += 1
            new_version.patch = 0
        else:
            new_version.patch += 1
        
        return new_version
    
    def release(self, version: Optional[str] = None) -> str:
        """Create a new release with the unreleased changes."""
        if not self.unreleased_changes:
            raise ValueError("No unreleased changes to release")
        
        if version:
            new_version = Version.from_string(version)
        else:
            new_version = self.get_next_version()
        
        version_str = str(new_version)
        self.releases[version_str] = self.unreleased_changes.copy()
        self.release_dates[version_str] = datetime.now()
        self.current_version = new_version
        self.unreleased_changes.clear()
        
        return version_str


# Step 4: Add formatting methods to the Changelog class
# ===============================================================================

# Explanation:
# Now we'll add methods to format the changelog in different styles.
# This includes Markdown format and conventional changelog format.

    def format_markdown(self, include_unreleased: bool = True) -> str:
        """Generate changelog in Markdown format."""
        lines = [f"# Changelog - {self.project_name}", ""]
        
        if include_unreleased and self.unreleased_changes:
            lines.extend(["## [Unreleased]", ""])
            lines.extend(self._format_changes_markdown(self.unreleased_changes))
            lines.append("")
        
        # Sort releases by version (newest first)
        sorted_releases = sorted(self.releases.keys(), 
                               key=lambda v: Version.from_string(v), reverse=True)
        
        for version in sorted_releases:
            release_date = self.release_dates.get(version, datetime.now())
            lines.append(f"## [{version}] - {release_date.strftime('%Y-%m-%d')}")
            lines.append("")
            lines.extend(self._format_changes_markdown(self.releases[version]))
            lines.append("")
        
        return "\n".join(lines)
    
    def _format_changes_markdown(self, changes: List[ChangeEntry]) -> List[str]:
        """Format a list of changes as Markdown."""
        if not changes:
            return ["No changes."]
        
        # Group changes by type
        grouped = {}
        for change in changes:
            change_type = change.change_type.value
            if change_type not in grouped:
                grouped[change_type] = []
            grouped[change_type].append(change)
        
        lines = []
        
        # Order: breaking, feat, fix, others
        type_order = ["breaking", "feat", "fix", "docs", "style", "refactor", "perf", "test", "chore"]
        type_headers = {
            "breaking": "### 💥 BREAKING CHANGES",
            "feat": "### ✨ Features",
            "fix": "### 🐛 Bug Fixes",
            "docs": "### 📚 Documentation",
            "style": "### 💄 Style",
            "refactor": "### ♻️ Code Refactoring",
            "perf": "### ⚡ Performance Improvements",
            "test": "### ✅ Tests",
            "chore": "### 🔧 Chores"
        }
        
        for change_type in type_order:
            if change_type in grouped:
                lines.append(type_headers[change_type])
                lines.append("")
                for change in grouped[change_type]:
                    scope_part = f"**{change.scope}**: " if change.scope else ""
                    lines.append(f"- {scope_part}{change.description}")
                lines.append("")
        
        return lines
    
    def format_conventional(self) -> str:
        """Generate changelog in conventional format."""
        lines = [f"# {self.project_name} Changelog", ""]
        
        if self.unreleased_changes:
            lines.extend(["## Unreleased", ""])
            for change in self.unreleased_changes:
                lines.append(f"- {change.format_conventional()}")
            lines.append("")
        
        sorted_releases = sorted(self.releases.keys(), 
                               key=lambda v: Version.from_string(v), reverse=True)
        
        for version in sorted_releases:
            release_date = self.release_dates.get(version, datetime.now())
            lines.append(f"## {version} ({release_date.strftime('%Y-%m-%d')})")
            lines.append("")
            for change in self.releases[version]:
                lines.append(f"- {change.format_conventional()}")
            lines.append("")
        
        return "\n".join(lines)


# Step 5: Add utility methods and complete the Changelog class
# ===============================================================================

# Explanation:
# Let's add some utility methods for managing the changelog and provide
# convenient ways to work with versions and changes.

    def bump_version(self, bump_type: Optional[str] = None) -> str:
        """Bump version and create a release. Returns the new version string."""
        if bump_type:
            if bump_type == "major":
                new_version = Version(self.current_version.major + 1, 0, 0)
            elif bump_type == "minor":
                new_version = Version(self.current_version.major, self.current_version.minor + 1, 0)
            elif bump_type == "patch":
                new_version = Version(self.current_version.major, self.current_version.minor, self.current_version.patch + 1)
            else:
                raise ValueError("bump_type must be 'major', 'minor', or 'patch'")
            
            return self.release(str(new_version))
        else:
            return self.release()
    
    def get_changes_since_version(self, version: str) -> List[ChangeEntry]:
        """Get all changes since a specific version."""
        target_version = Version.from_string(version)
        changes = []
        
        # Add unreleased changes
        changes.extend(self.unreleased_changes)
        
        # Add changes from releases newer than target version
        for release_version, release_changes in self.releases.items():
            if Version.from_string(release_version) > target_version:
                changes.extend(release_changes)
        
        return changes
    
    def get_statistics(self) -> Dict[str, int]:
        """Get statistics about the changelog."""
        stats = {
            "total_releases": len(self.releases),
            "unreleased_changes": len(self.unreleased_changes),
            "total_changes": len(self.unreleased_changes)
        }
        
        # Count changes by type
        all_changes = self.unreleased_changes.copy()
        for changes in self.releases.values():
            all_changes.extend(changes)
        
        for change in all_changes:
            change_type = change.change_type.value
            stats[f"{change_type}_count"] = stats.get(f"{change_type}_count", 0) + 1
            stats["total_changes"] += 1
        
        # Subtract the unreleased changes we counted twice
        stats["total_changes"] -= len(self.unreleased_changes)
        
        return stats
    
    def save_to_file(self, filename: str, format_type: str = "markdown") -> None:
        """Save changelog to a file."""
        if format_type == "markdown":
            content = self.format_markdown()
        elif format_type == "conventional":
            content = self.format_conventional()
        else:
            raise ValueError("format_type must be 'markdown' or 'conventional'")
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def __str__(self) -> str:
        return f"Changelog({self.project_name}, v{self.current_version}, {len(self.unreleased_changes)} unreleased)"
    
    def __repr__(self) -> str:
        return f"Changelog('{self.project_name}', '{self.current_version}')"


# Step 6: Demonstration and usage examples
# ===============================================================================

# Explanation:
# Let's demonstrate how to use our changelog and versioning system with
# practical examples that show all the features working together.

def demonstrate_changelog_system():
    """Demonstrate the complete changelog and versioning system."""
    print("=== Changelog and Versioning System Demo ===\n")
    
    # Create a new changelog
    changelog = Changelog("MyAwesomeProject", "1.0.0")
    print(f"Created changelog: {changelog}")
    print(f"Current version: {changelog.current_version}\n")
    
    # Add various types of changes
    print("Adding changes...")
    changelog.add_change("feat", "Add user authentication system", "auth")
    changelog.add_change("feat", "Implement password reset functionality", "auth")
    changelog.add_change("fix", "Fix memory leak in data parser", "core")
    changelog.add_change("docs", "Update API documentation")
    changelog.add_change("perf", "Optimize database queries", "db")
    
    print(f"Added {len(changelog.unreleased_changes)} unreleased changes")
    print(f"Next version will be: {changelog.get_next_version()}\n")
    
    # Create a release
    print("Creating release...")
    new_version = changelog.release()
    print(f"Released version: {new_version}")
    print(f"Current version: {changelog.current_version}\n")
    
    # Add more changes for next release
    print("Adding more changes...")
    changelog.add_change("breaking", "Remove deprecated API endpoints", "api")
    changelog.add_change("feat", "Add GraphQL support", "api")
    changelog.add_change("fix", "Fix race condition in cache", "cache")
    
    print(f"Next version will be: {changelog.get_next_version()}")
    
    # Create another release
    new_version = changelog.bump_version()
    print(f"Released version: {new_version}\n")
    
    # Show statistics
    stats = changelog.get_statistics()
    print("Changelog Statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
    print()
    
    # Generate different formats
    print("=== Markdown Format ===")
    print(changelog.format_markdown())
    print("\n=== Conventional Format ===")
    print(changelog.format_conventional())
    
    return changelog

# Step 7: Advanced features and utilities
# ===============================================================================

# Explanation:
# Let's add some advanced features like changelog parsing from files,
# integration with git, and automated version management.

class ChangelogManager:
    """Advanced changelog management with file operations and automation."""
    
    def __init__(self, changelog: Changelog):
        self.changelog = changelog
    
    def parse_conventional_commits(self, commit_messages: List[str]) -> None:
        """Parse conventional commit messages and add them as changes."""
        import re
        
        # Conventional commit pattern: type(scope): description
        pattern = r'^(\w+)(?:\(([^)]+)\))?(!)?: (.+)$'
        
        for message in commit_messages:
            match = re.match(pattern, message.strip())
            if match:
                change_type, scope, breaking_marker, description = match.groups()
                is_breaking = breaking_marker == '!' or change_type == 'breaking'
                
                try:
                    self.changelog.add_change(
                        change_type=change_type,
                        description=description,
                        scope=scope,
                        breaking=is_breaking
                    )
                except ValueError:
                    # Skip unknown change types
                    print(f"Warning: Unknown change type '{change_type}' in commit: {message}")
    
    def auto_release(self, dry_run: bool = False) -> Optional[str]:
        """Automatically create a release if there are unreleased changes."""
        if not self.changelog.unreleased_changes:
            print("No unreleased changes found.")
            return None
        
        next_version = self.changelog.get_next_version()
        
        if dry_run:
            print(f"Would create release: {next_version}")
            return str(next_version)
        else:
            return self.changelog.release()
    
    def generate_release_notes(self, version: Optional[str] = None) -> str:
        """Generate release notes for a specific version."""
        if version is None:
            # Use unreleased changes
            changes = self.changelog.unreleased_changes
            version_str = str(self.changelog.get_next_version())
        else:
            changes = self.changelog.releases.get(version, [])
            version_str = version
        
        if not changes:
            return f"# Release {version_str}\n\nNo changes in this release."
        
        lines = [f"# Release {version_str}", ""]
        
        # Group changes
        breaking_changes = [c for c in changes if c.breaking]
        features = [c for c in changes if c.change_type.value == "feat" and not c.breaking]
        fixes = [c for c in changes if c.change_type.value == "fix"]
        others = [c for c in changes if c.change_type.value not in ["feat", "fix"] and not c.breaking]
        
        if breaking_changes:
            lines.extend(["## 💥 BREAKING CHANGES", ""])
            for change in breaking_changes:
                lines.append(f"- {change.description}")
            lines.append("")
        
        if features:
            lines.extend(["## ✨ New Features", ""])
            for change in features:
                scope_part = f"**{change.scope}**: " if change.scope else ""
                lines.append(f"- {scope_part}{change.description}")
            lines.append("")
        
        if fixes:
            lines.extend(["## 🐛 Bug Fixes", ""])
            for change in fixes:
                scope_part = f"**{change.scope}**: " if change.scope else ""
                lines.append(f"- {scope_part}{change.description}")
            lines.append("")
        
        if others:
            lines.extend(["## 🔧 Other Changes", ""])
            for change in others:
                scope_part = f"**{change.scope}**: " if change.scope else ""
                lines.append(f"- {scope_part}{change.description}")
            lines.append("")
        
        return "\n".join(lines)



# Step 8: Complete example with main execution
# ===============================================================================

# Explanation:
# Let's create a complete working example that demonstrates all features
# and shows how everything works together in practice.

def demonstrate_advanced_features():
    """Demonstrate advanced changelog management features."""
    print("\n=== Advanced Features Demo ===\n")
    
    # Create changelog and manager
    changelog = Changelog("AdvancedProject", "0.1.0")
    manager = ChangelogManager(changelog)
    
    # Simulate parsing conventional commits
    commit_messages = [
        "feat(auth): add OAuth2 integration",
        "fix(db): resolve connection timeout issues",
        "feat!: redesign user interface",
        "docs: update installation guide",
        "perf(api): optimize response times",
        "test: add unit tests for user service"
    ]
    
    print("Parsing conventional commits...")
    manager.parse_conventional_commits(commit_messages)
    print(f"Parsed {len(changelog.unreleased_changes)} changes from commits\n")
    
    # Generate release notes
    print("=== Release Notes ===")
    release_notes = manager.generate_release_notes()
    print(release_notes)
    
    # Auto release
    print("\n=== Auto Release ===")
    print("Dry run:")
    manager.auto_release(dry_run=True)
    
    print("\nActual release:")
    new_version = manager.auto_release()
    print(f"Created release: {new_version}")
    
    return changelog, manager

def practical_usage_example():
    """Show practical usage patterns for real projects."""
    print("\n=== Practical Usage Example ===\n")
    
    # Initialize project changelog
    changelog = Changelog("MyWebApp", "1.2.3")
    
    # Add changes as development progresses
    changelog.add_change("feat", "Add dark mode support", "ui")
    changelog.add_change("feat", "Implement real-time notifications", "notifications")
    changelog.add_change("fix", "Fix responsive layout on mobile", "ui")
    changelog.add_change("fix", "Resolve memory leak in WebSocket connections", "websocket")
    changelog.add_change("perf", "Optimize image loading", "performance")
    changelog.add_change("docs", "Add API usage examples")
    
    # Check what the next version would be
    next_version = changelog.get_next_version()
    print(f"Current version: {changelog.current_version}")
    print(f"Next version: {next_version}")
    
    # Create release
    released_version = changelog.release()
    print(f"Released: {released_version}")
    
    # Add a breaking change
    changelog.add_change("breaking", "Remove deprecated v1 API endpoints", "api")
    changelog.add_change("feat", "Add v2 API with improved performance", "api")
    
    # This will bump major version
    next_major = changelog.bump_version()
    print(f"Major release: {next_major}")
    
    # Save changelog to file
    changelog.save_to_file("CHANGELOG.md", "markdown")
    print("Saved changelog to CHANGELOG.md")
    
    # Show final statistics
    stats = changelog.get_statistics()
    print(f"\nProject statistics: {stats}")
    
    return changelog

# Main execution
if __name__ == "__main__":
    print("Changelog and Versioning System")
    print("=" * 50)
    
    # Run basic demonstration
    basic_changelog = demonstrate_changelog_system()
    
    # Run advanced features
    advanced_changelog, manager = demonstrate_advanced_features()
    
    # Show practical usage
    practical_changelog = practical_usage_example()
    
    print("\n" + "=" * 50)
    print("All demonstrations completed successfully!")
    print("\nKey Features Demonstrated:")
    print("✅ Semantic versioning (MAJOR.MINOR.PATCH)")
    print("✅ Conventional commit parsing")
    print("✅ Automatic version bumping")
    print("✅ Multiple output formats (Markdown, Conventional)")
    print("✅ Release notes generation")
    print("✅ Change categorization and statistics")
    print("✅ File operations and persistence")
    print("✅ Advanced changelog management")


# ===============================================================================
#                              FINAL SUMMARY
# ===============================================================================
#
# WHAT WE'VE BUILT:
#
# 1. Version Class:
#    - Semantic versioning support (MAJOR.MINOR.PATCH)
#    - Version comparison and parsing
#    - String representation and validation
#
# 2. ChangeEntry Class:
#    - Represents individual changes with metadata
#    - Supports conventional commit format
#    - Determines version impact automatically
#
# 3. Changelog Class:
#    - Manages collections of changes and releases
#    - Automatic version bumping based on change types
#    - Multiple output formats (Markdown, Conventional)
#    - Statistics and utility methods
#
# 4. ChangelogManager Class:
#    - Advanced features for automation
#    - Conventional commit parsing
#    - Release notes generation
#    - Auto-release functionality
#
# 5. Complete Documentation System:
#    - Follows semantic versioning principles
#    - Supports conventional commits
#    - Generates professional changelogs
#    - Provides automation tools
#
# This system provides a comprehensive solution for managing software versions
# and generating changelogs, following industry best practices and standards.
#
# ===============================================================================
