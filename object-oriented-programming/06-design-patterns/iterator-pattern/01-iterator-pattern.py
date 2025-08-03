"""Question: Implement the Iterator pattern to provide sequential access to elements without exposing structure.

Create a playlist system where songs can be iterated in different orders
(sequential, shuffle, repeat) without exposing the internal collection structure.

Requirements:
1. Create Iterator interface with has_next() and next() methods
2. Implement concrete iterators (Sequential, Shuffle, Repeat)
3. Create Aggregate interface with create_iterator() method
4. Implement Playlist class that creates different iterators
5. Demonstrate different iteration strategies
6. Show how Python's iterator protocol can be used

Example usage:
    playlist = Playlist()
    playlist.add_song("Song 1")
    playlist.add_song("Song 2")
    iterator = playlist.create_iterator("shuffle")
    while iterator.has_next():
        print(iterator.next())
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!

# Try to implement your solution here:
# (Write your code below this line)


















































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


# Step 1: Import modules and create the Song class
# ===============================================================================

# Explanation:
# The Iterator pattern starts with the objects we want to iterate over.
# We'll create a Song class to represent individual songs in our playlist.

from abc import ABC, abstractmethod
from typing import List, Optional
import random

class Song:
    """Represents a song in the playlist."""
    
    def __init__(self, title: str, artist: str = "Unknown", duration: int = 180):
        self.title = title
        self.artist = artist
        self.duration = duration  # duration in seconds
    
    def __str__(self):
        """String representation of the song."""
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{self.title} by {self.artist} ({minutes}:{seconds:02d})"
    
    def __repr__(self):
        return f"Song('{self.title}', '{self.artist}', {self.duration})"

# What we accomplished in this step:
# - Created the Song class with title, artist, and duration
# - Added string representation for easy display
# - This will be the element type our iterators will work with


# Step 2: Create the abstract iterator interface
# ===============================================================================

# Explanation:
# The Iterator interface defines the contract for all concrete iterators.
# It provides methods to check if there are more elements and to get the next element.

from abc import ABC, abstractmethod
from typing import List, Optional
import random

class Song:
    """Represents a song in the playlist."""
    
    def __init__(self, title: str, artist: str = "Unknown", duration: int = 180):
        self.title = title
        self.artist = artist
        self.duration = duration  # duration in seconds
    
    def __str__(self):
        """String representation of the song."""
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{self.title} by {self.artist} ({minutes}:{seconds:02d})"
    
    def __repr__(self):
        return f"Song('{self.title}', '{self.artist}', {self.duration})"

class Iterator(ABC):
    """Abstract iterator interface."""
    
    @abstractmethod
    def has_next(self) -> bool:
        """Check if there are more elements to iterate over."""
        pass
    
    @abstractmethod
    def next(self) -> Song:
        """Get the next element in the iteration."""
        pass
    
    @abstractmethod
    def reset(self):
        """Reset the iterator to the beginning."""
        pass

# What we accomplished in this step:
# - Created abstract Iterator interface with essential methods
# - has_next() checks if more elements are available
# - next() returns the next element in sequence
# - reset() allows restarting iteration from the beginning


# Step 3: Create concrete sequential iterator
# ===============================================================================

# Explanation:
# The SequentialIterator iterates through songs in their original order.
# It maintains a current position and moves forward one song at a time.

from abc import ABC, abstractmethod
from typing import List, Optional
import random

class Song:
    """Represents a song in the playlist."""
    
    def __init__(self, title: str, artist: str = "Unknown", duration: int = 180):
        self.title = title
        self.artist = artist
        self.duration = duration  # duration in seconds
    
    def __str__(self):
        """String representation of the song."""
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{self.title} by {self.artist} ({minutes}:{seconds:02d})"
    
    def __repr__(self):
        return f"Song('{self.title}', '{self.artist}', {self.duration})"

class Iterator(ABC):
    """Abstract iterator interface."""
    
    @abstractmethod
    def has_next(self) -> bool:
        """Check if there are more elements to iterate over."""
        pass
    
    @abstractmethod
    def next(self) -> Song:
        """Get the next element in the iteration."""
        pass
    
    @abstractmethod
    def reset(self):
        """Reset the iterator to the beginning."""
        pass

class SequentialIterator(Iterator):
    """Iterator that goes through songs in sequential order."""
    
    def __init__(self, songs: List[Song]):
        self.songs = songs
        self.current_index = 0
    
    def has_next(self) -> bool:
        """Check if there are more songs to play."""
        return self.current_index < len(self.songs)
    
    def next(self) -> Song:
        """Get the next song in sequence."""
        if not self.has_next():
            raise StopIteration("No more songs in the playlist")
        
        song = self.songs[self.current_index]
        self.current_index += 1
        return song
    
    def reset(self):
        """Reset to the beginning of the playlist."""
        self.current_index = 0

# What we accomplished in this step:
# - Created SequentialIterator that iterates in original order
# - Maintains current_index to track position
# - Implements all abstract methods from Iterator interface
# - Raises StopIteration when no more elements available


# Step 4: Create concrete shuffle iterator
# ===============================================================================

# Explanation:
# The ShuffleIterator randomizes the order of songs but still visits each song exactly once.
# It creates a shuffled copy of the song indices to maintain randomness.

from abc import ABC, abstractmethod
from typing import List, Optional
import random

class Song:
    """Represents a song in the playlist."""
    
    def __init__(self, title: str, artist: str = "Unknown", duration: int = 180):
        self.title = title
        self.artist = artist
        self.duration = duration  # duration in seconds
    
    def __str__(self):
        """String representation of the song."""
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{self.title} by {self.artist} ({minutes}:{seconds:02d})"
    
    def __repr__(self):
        return f"Song('{self.title}', '{self.artist}', {self.duration})"

class Iterator(ABC):
    """Abstract iterator interface."""
    
    @abstractmethod
    def has_next(self) -> bool:
        """Check if there are more elements to iterate over."""
        pass
    
    @abstractmethod
    def next(self) -> Song:
        """Get the next element in the iteration."""
        pass
    
    @abstractmethod
    def reset(self):
        """Reset the iterator to the beginning."""
        pass

class SequentialIterator(Iterator):
    """Iterator that goes through songs in sequential order."""
    
    def __init__(self, songs: List[Song]):
        self.songs = songs
        self.current_index = 0
    
    def has_next(self) -> bool:
        """Check if there are more songs to play."""
        return self.current_index < len(self.songs)
    
    def next(self) -> Song:
        """Get the next song in sequence."""
        if not self.has_next():
            raise StopIteration("No more songs in the playlist")
        
        song = self.songs[self.current_index]
        self.current_index += 1
        return song
    
    def reset(self):
        """Reset to the beginning of the playlist."""
        self.current_index = 0

class ShuffleIterator(Iterator):
    """Iterator that goes through songs in random order."""
    
    def __init__(self, songs: List[Song]):
        self.songs = songs
        self.shuffled_indices = list(range(len(songs)))
        random.shuffle(self.shuffled_indices)
        self.current_index = 0
    
    def has_next(self) -> bool:
        """Check if there are more songs to play."""
        return self.current_index < len(self.shuffled_indices)
    
    def next(self) -> Song:
        """Get the next song in shuffled order."""
        if not self.has_next():
            raise StopIteration("No more songs in the playlist")
        
        song_index = self.shuffled_indices[self.current_index]
        song = self.songs[song_index]
        self.current_index += 1
        return song
    
    def reset(self):
        """Reset and reshuffle the playlist."""
        random.shuffle(self.shuffled_indices)
        self.current_index = 0

# What we accomplished in this step:
# - Created ShuffleIterator that randomizes song order
# - Uses shuffled_indices to maintain random but complete iteration
# - Reset method reshuffles for different random order each time
# - Still visits each song exactly once per iteration cycle


# Step 5: Create concrete repeat iterator
# ===============================================================================

# Explanation:
# The RepeatIterator cycles through songs infinitely, starting over when it reaches the end.
# It can be configured to repeat a certain number of times or infinitely.

from abc import ABC, abstractmethod
from typing import List, Optional
import random

class Song:
    """Represents a song in the playlist."""
    
    def __init__(self, title: str, artist: str = "Unknown", duration: int = 180):
        self.title = title
        self.artist = artist
        self.duration = duration  # duration in seconds
    
    def __str__(self):
        """String representation of the song."""
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{self.title} by {self.artist} ({minutes}:{seconds:02d})"
    
    def __repr__(self):
        return f"Song('{self.title}', '{self.artist}', {self.duration})"

class Iterator(ABC):
    """Abstract iterator interface."""
    
    @abstractmethod
    def has_next(self) -> bool:
        """Check if there are more elements to iterate over."""
        pass
    
    @abstractmethod
    def next(self) -> Song:
        """Get the next element in the iteration."""
        pass
    
    @abstractmethod
    def reset(self):
        """Reset the iterator to the beginning."""
        pass

class SequentialIterator(Iterator):
    """Iterator that goes through songs in sequential order."""
    
    def __init__(self, songs: List[Song]):
        self.songs = songs
        self.current_index = 0
    
    def has_next(self) -> bool:
        """Check if there are more songs to play."""
        return self.current_index < len(self.songs)
    
    def next(self) -> Song:
        """Get the next song in sequence."""
        if not self.has_next():
            raise StopIteration("No more songs in the playlist")
        
        song = self.songs[self.current_index]
        self.current_index += 1
        return song
    
    def reset(self):
        """Reset to the beginning of the playlist."""
        self.current_index = 0

class ShuffleIterator(Iterator):
    """Iterator that goes through songs in random order."""
    
    def __init__(self, songs: List[Song]):
        self.songs = songs
        self.shuffled_indices = list(range(len(songs)))
        random.shuffle(self.shuffled_indices)
        self.current_index = 0
    
    def has_next(self) -> bool:
        """Check if there are more songs to play."""
        return self.current_index < len(self.shuffled_indices)
    
    def next(self) -> Song:
        """Get the next song in shuffled order."""
        if not self.has_next():
            raise StopIteration("No more songs in the playlist")
        
        song_index = self.shuffled_indices[self.current_index]
        song = self.songs[song_index]
        self.current_index += 1
        return song
    
    def reset(self):
        """Reset and reshuffle the playlist."""
        random.shuffle(self.shuffled_indices)
        self.current_index = 0

class RepeatIterator(Iterator):
    """Iterator that repeats the playlist a specified number of times or infinitely."""
    
    def __init__(self, songs: List[Song], repeat_count: Optional[int] = None):
        self.songs = songs
        self.repeat_count = repeat_count  # None means infinite repeat
        self.current_index = 0
        self.cycles_completed = 0
    
    def has_next(self) -> bool:
        """Check if there are more songs to play."""
        if not self.songs:
            return False
        
        # If repeat_count is None, always has next (infinite)
        if self.repeat_count is None:
            return True
        
        # Check if we've completed all requested cycles
        return self.cycles_completed < self.repeat_count
    
    def next(self) -> Song:
        """Get the next song, cycling through the playlist."""
        if not self.has_next():
            raise StopIteration("Playlist repetition completed")
        
        song = self.songs[self.current_index]
        self.current_index += 1
        
        # Check if we've reached the end of the playlist
        if self.current_index >= len(self.songs):
            self.current_index = 0
            self.cycles_completed += 1
        
        return song
    
    def reset(self):
        """Reset to the beginning of the playlist."""
        self.current_index = 0
        self.cycles_completed = 0

# What we accomplished in this step:
# - Created RepeatIterator that cycles through songs multiple times
# - Supports both finite repeat count and infinite repetition
# - Tracks cycles_completed to know when to stop
# - Automatically wraps around to beginning when reaching end


# Step 6: Create aggregate interface and Playlist class
# ===============================================================================

# Explanation:
# The Aggregate interface defines how to create iterators. The Playlist class
# implements this interface and can create different types of iterators for the same data.

from abc import ABC, abstractmethod
from typing import List, Optional
import random

class Song:
    """Represents a song in the playlist."""
    
    def __init__(self, title: str, artist: str = "Unknown", duration: int = 180):
        self.title = title
        self.artist = artist
        self.duration = duration  # duration in seconds
    
    def __str__(self):
        """String representation of the song."""
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{self.title} by {self.artist} ({minutes}:{seconds:02d})"
    
    def __repr__(self):
        return f"Song('{self.title}', '{self.artist}', {self.duration})"

class Iterator(ABC):
    """Abstract iterator interface."""
    
    @abstractmethod
    def has_next(self) -> bool:
        """Check if there are more elements to iterate over."""
        pass
    
    @abstractmethod
    def next(self) -> Song:
        """Get the next element in the iteration."""
        pass
    
    @abstractmethod
    def reset(self):
        """Reset the iterator to the beginning."""
        pass

class SequentialIterator(Iterator):
    """Iterator that goes through songs in sequential order."""
    
    def __init__(self, songs: List[Song]):
        self.songs = songs
        self.current_index = 0
    
    def has_next(self) -> bool:
        """Check if there are more songs to play."""
        return self.current_index < len(self.songs)
    
    def next(self) -> Song:
        """Get the next song in sequence."""
        if not self.has_next():
            raise StopIteration("No more songs in the playlist")
        
        song = self.songs[self.current_index]
        self.current_index += 1
        return song
    
    def reset(self):
        """Reset to the beginning of the playlist."""
        self.current_index = 0

class ShuffleIterator(Iterator):
    """Iterator that goes through songs in random order."""
    
    def __init__(self, songs: List[Song]):
        self.songs = songs
        self.shuffled_indices = list(range(len(songs)))
        random.shuffle(self.shuffled_indices)
        self.current_index = 0
    
    def has_next(self) -> bool:
        """Check if there are more songs to play."""
        return self.current_index < len(self.shuffled_indices)
    
    def next(self) -> Song:
        """Get the next song in shuffled order."""
        if not self.has_next():
            raise StopIteration("No more songs in the playlist")
        
        song_index = self.shuffled_indices[self.current_index]
        song = self.songs[song_index]
        self.current_index += 1
        return song
    
    def reset(self):
        """Reset and reshuffle the playlist."""
        random.shuffle(self.shuffled_indices)
        self.current_index = 0

class RepeatIterator(Iterator):
    """Iterator that repeats the playlist a specified number of times or infinitely."""
    
    def __init__(self, songs: List[Song], repeat_count: Optional[int] = None):
        self.songs = songs
        self.repeat_count = repeat_count  # None means infinite repeat
        self.current_index = 0
        self.cycles_completed = 0
    
    def has_next(self) -> bool:
        """Check if there are more songs to play."""
        if not self.songs:
            return False
        
        # If repeat_count is None, always has next (infinite)
        if self.repeat_count is None:
            return True
        
        # Check if we've completed all requested cycles
        return self.cycles_completed < self.repeat_count
    
    def next(self) -> Song:
        """Get the next song, cycling through the playlist."""
        if not self.has_next():
            raise StopIteration("Playlist repetition completed")
        
        song = self.songs[self.current_index]
        self.current_index += 1
        
        # Check if we've reached the end of the playlist
        if self.current_index >= len(self.songs):
            self.current_index = 0
            self.cycles_completed += 1
        
        return song
    
    def reset(self):
        """Reset to the beginning of the playlist."""
        self.current_index = 0
        self.cycles_completed = 0

class Aggregate(ABC):
    """Abstract aggregate interface for creating iterators."""
    
    @abstractmethod
    def create_iterator(self, iterator_type: str = "sequential") -> Iterator:
        """Create an iterator for the collection."""
        pass

class Playlist(Aggregate):
    """Playlist that can create different types of iterators."""
    
    def __init__(self, name: str = "My Playlist"):
        self.name = name
        self.songs: List[Song] = []
    
    def add_song(self, song: Song):
        """Add a song to the playlist."""
        self.songs.append(song)
    
    def remove_song(self, song: Song):
        """Remove a song from the playlist."""
        if song in self.songs:
            self.songs.remove(song)
    
    def get_song_count(self) -> int:
        """Get the number of songs in the playlist."""
        return len(self.songs)
    
    def create_iterator(self, iterator_type: str = "sequential", **kwargs) -> Iterator:
        """Create an iterator based on the specified type."""
        if iterator_type.lower() == "sequential":
            return SequentialIterator(self.songs.copy())
        elif iterator_type.lower() == "shuffle":
            return ShuffleIterator(self.songs.copy())
        elif iterator_type.lower() == "repeat":
            repeat_count = kwargs.get("repeat_count", None)
            return RepeatIterator(self.songs.copy(), repeat_count)
        else:
            raise ValueError(f"Unknown iterator type: {iterator_type}")
    
    def __str__(self):
        """String representation of the playlist."""
        return f"Playlist '{self.name}' with {len(self.songs)} songs"

# What we accomplished in this step:
# - Created Aggregate interface for iterator creation
# - Implemented Playlist class that manages songs and creates iterators
# - Added methods to add/remove songs and get song count
# - Factory method create_iterator() supports different iterator types
# - Uses copy() to prevent external modification of internal song list


# Step 7: Add Python's iterator protocol support
# ===============================================================================

# Explanation:
# Python has built-in iterator protocol using __iter__() and __next__() methods.
# We'll create a Pythonic iterator that works with for loops and other Python constructs.

from abc import ABC, abstractmethod
from typing import List, Optional
import random

class Song:
    """Represents a song in the playlist."""
    
    def __init__(self, title: str, artist: str = "Unknown", duration: int = 180):
        self.title = title
        self.artist = artist
        self.duration = duration  # duration in seconds
    
    def __str__(self):
        """String representation of the song."""
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{self.title} by {self.artist} ({minutes}:{seconds:02d})"
    
    def __repr__(self):
        return f"Song('{self.title}', '{self.artist}', {self.duration})"

class Iterator(ABC):
    """Abstract iterator interface."""
    
    @abstractmethod
    def has_next(self) -> bool:
        """Check if there are more elements to iterate over."""
        pass
    
    @abstractmethod
    def next(self) -> Song:
        """Get the next element in the iteration."""
        pass
    
    @abstractmethod
    def reset(self):
        """Reset the iterator to the beginning."""
        pass

class SequentialIterator(Iterator):
    """Iterator that goes through songs in sequential order."""
    
    def __init__(self, songs: List[Song]):
        self.songs = songs
        self.current_index = 0
    
    def has_next(self) -> bool:
        """Check if there are more songs to play."""
        return self.current_index < len(self.songs)
    
    def next(self) -> Song:
        """Get the next song in sequence."""
        if not self.has_next():
            raise StopIteration("No more songs in the playlist")
        
        song = self.songs[self.current_index]
        self.current_index += 1
        return song
    
    def reset(self):
        """Reset to the beginning of the playlist."""
        self.current_index = 0

class ShuffleIterator(Iterator):
    """Iterator that goes through songs in random order."""
    
    def __init__(self, songs: List[Song]):
        self.songs = songs
        self.shuffled_indices = list(range(len(songs)))
        random.shuffle(self.shuffled_indices)
        self.current_index = 0
    
    def has_next(self) -> bool:
        """Check if there are more songs to play."""
        return self.current_index < len(self.shuffled_indices)
    
    def next(self) -> Song:
        """Get the next song in shuffled order."""
        if not self.has_next():
            raise StopIteration("No more songs in the playlist")
        
        song_index = self.shuffled_indices[self.current_index]
        song = self.songs[song_index]
        self.current_index += 1
        return song
    
    def reset(self):
        """Reset and reshuffle the playlist."""
        random.shuffle(self.shuffled_indices)
        self.current_index = 0

class RepeatIterator(Iterator):
    """Iterator that repeats the playlist a specified number of times or infinitely."""
    
    def __init__(self, songs: List[Song], repeat_count: Optional[int] = None):
        self.songs = songs
        self.repeat_count = repeat_count  # None means infinite repeat
        self.current_index = 0
        self.cycles_completed = 0
    
    def has_next(self) -> bool:
        """Check if there are more songs to play."""
        if not self.songs:
            return False
        
        # If repeat_count is None, always has next (infinite)
        if self.repeat_count is None:
            return True
        
        # Check if we've completed all requested cycles
        return self.cycles_completed < self.repeat_count
    
    def next(self) -> Song:
        """Get the next song, cycling through the playlist."""
        if not self.has_next():
            raise StopIteration("Playlist repetition completed")
        
        song = self.songs[self.current_index]
        self.current_index += 1
        
        # Check if we've reached the end of the playlist
        if self.current_index >= len(self.songs):
            self.current_index = 0
            self.cycles_completed += 1
        
        return song
    
    def reset(self):
        """Reset to the beginning of the playlist."""
        self.current_index = 0
        self.cycles_completed = 0

class Aggregate(ABC):
    """Abstract aggregate interface for creating iterators."""
    
    @abstractmethod
    def create_iterator(self, iterator_type: str = "sequential") -> Iterator:
        """Create an iterator for the collection."""
        pass

class Playlist(Aggregate):
    """Playlist that can create different types of iterators."""
    
    def __init__(self, name: str = "My Playlist"):
        self.name = name
        self.songs: List[Song] = []
    
    def add_song(self, song: Song):
        """Add a song to the playlist."""
        self.songs.append(song)
    
    def remove_song(self, song: Song):
        """Remove a song from the playlist."""
        if song in self.songs:
            self.songs.remove(song)
    
    def get_song_count(self) -> int:
        """Get the number of songs in the playlist."""
        return len(self.songs)
    
    def create_iterator(self, iterator_type: str = "sequential", **kwargs) -> Iterator:
        """Create an iterator based on the specified type."""
        if iterator_type.lower() == "sequential":
            return SequentialIterator(self.songs.copy())
        elif iterator_type.lower() == "shuffle":
            return ShuffleIterator(self.songs.copy())
        elif iterator_type.lower() == "repeat":
            repeat_count = kwargs.get("repeat_count", None)
            return RepeatIterator(self.songs.copy(), repeat_count)
        else:
            raise ValueError(f"Unknown iterator type: {iterator_type}")
    
    def __str__(self):
        """String representation of the playlist."""
        return f"Playlist '{self.name}' with {len(self.songs)} songs"

class PythonicPlaylistIterator:
    """Python-style iterator that works with for loops and built-in functions."""
    
    def __init__(self, iterator: Iterator):
        self.iterator = iterator
    
    def __iter__(self):
        """Return self as the iterator object."""
        return self
    
    def __next__(self):
        """Get the next item using Python's iterator protocol."""
        if self.iterator.has_next():
            return self.iterator.next()
        else:
            raise StopIteration

class PythonicPlaylist(Playlist):
    """Enhanced playlist that supports Python's iterator protocol."""
    
    def __iter__(self):
        """Return a Python-style iterator for the playlist."""
        return PythonicPlaylistIterator(self.create_iterator("sequential"))
    
    def iter_shuffle(self):
        """Return a shuffled Python-style iterator."""
        return PythonicPlaylistIterator(self.create_iterator("shuffle"))
    
    def iter_repeat(self, repeat_count: Optional[int] = None):
        """Return a repeating Python-style iterator."""
        return PythonicPlaylistIterator(self.create_iterator("repeat", repeat_count=repeat_count))

# What we accomplished in this step:
# - Created PythonicPlaylistIterator that implements __iter__ and __next__
# - Enhanced PythonicPlaylist to work with Python's for loops
# - Added convenience methods for different iteration types
# - Now supports: for song in playlist, list(playlist), etc.


# Step 8: Test the complete implementation
# ===============================================================================

# Explanation:
# Let's test our Iterator pattern implementation with different iteration strategies
# and demonstrate both custom iterators and Python's built-in iterator protocol.

from abc import ABC, abstractmethod
from typing import List, Optional
import random

class Song:
    """Represents a song in the playlist."""
    
    def __init__(self, title: str, artist: str = "Unknown", duration: int = 180):
        self.title = title
        self.artist = artist
        self.duration = duration  # duration in seconds
    
    def __str__(self):
        """String representation of the song."""
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{self.title} by {self.artist} ({minutes}:{seconds:02d})"
    
    def __repr__(self):
        return f"Song('{self.title}', '{self.artist}', {self.duration})"

class Iterator(ABC):
    """Abstract iterator interface."""
    
    @abstractmethod
    def has_next(self) -> bool:
        """Check if there are more elements to iterate over."""
        pass
    
    @abstractmethod
    def next(self) -> Song:
        """Get the next element in the iteration."""
        pass
    
    @abstractmethod
    def reset(self):
        """Reset the iterator to the beginning."""
        pass

class SequentialIterator(Iterator):
    """Iterator that goes through songs in sequential order."""
    
    def __init__(self, songs: List[Song]):
        self.songs = songs
        self.current_index = 0
    
    def has_next(self) -> bool:
        """Check if there are more songs to play."""
        return self.current_index < len(self.songs)
    
    def next(self) -> Song:
        """Get the next song in sequence."""
        if not self.has_next():
            raise StopIteration("No more songs in the playlist")
        
        song = self.songs[self.current_index]
        self.current_index += 1
        return song
    
    def reset(self):
        """Reset to the beginning of the playlist."""
        self.current_index = 0

class ShuffleIterator(Iterator):
    """Iterator that goes through songs in random order."""
    
    def __init__(self, songs: List[Song]):
        self.songs = songs
        self.shuffled_indices = list(range(len(songs)))
        random.shuffle(self.shuffled_indices)
        self.current_index = 0
    
    def has_next(self) -> bool:
        """Check if there are more songs to play."""
        return self.current_index < len(self.shuffled_indices)
    
    def next(self) -> Song:
        """Get the next song in shuffled order."""
        if not self.has_next():
            raise StopIteration("No more songs in the playlist")
        
        song_index = self.shuffled_indices[self.current_index]
        song = self.songs[song_index]
        self.current_index += 1
        return song
    
    def reset(self):
        """Reset and reshuffle the playlist."""
        random.shuffle(self.shuffled_indices)
        self.current_index = 0

class RepeatIterator(Iterator):
    """Iterator that repeats the playlist a specified number of times or infinitely."""
    
    def __init__(self, songs: List[Song], repeat_count: Optional[int] = None):
        self.songs = songs
        self.repeat_count = repeat_count  # None means infinite repeat
        self.current_index = 0
        self.cycles_completed = 0
    
    def has_next(self) -> bool:
        """Check if there are more songs to play."""
        if not self.songs:
            return False
        
        # If repeat_count is None, always has next (infinite)
        if self.repeat_count is None:
            return True
        
        # Check if we've completed all requested cycles
        return self.cycles_completed < self.repeat_count
    
    def next(self) -> Song:
        """Get the next song, cycling through the playlist."""
        if not self.has_next():
            raise StopIteration("Playlist repetition completed")
        
        song = self.songs[self.current_index]
        self.current_index += 1
        
        # Check if we've reached the end of the playlist
        if self.current_index >= len(self.songs):
            self.current_index = 0
            self.cycles_completed += 1
        
        return song
    
    def reset(self):
        """Reset to the beginning of the playlist."""
        self.current_index = 0
        self.cycles_completed = 0

class Aggregate(ABC):
    """Abstract aggregate interface for creating iterators."""
    
    @abstractmethod
    def create_iterator(self, iterator_type: str = "sequential") -> Iterator:
        """Create an iterator for the collection."""
        pass

class Playlist(Aggregate):
    """Playlist that can create different types of iterators."""
    
    def __init__(self, name: str = "My Playlist"):
        self.name = name
        self.songs: List[Song] = []
    
    def add_song(self, song: Song):
        """Add a song to the playlist."""
        self.songs.append(song)
    
    def remove_song(self, song: Song):
        """Remove a song from the playlist."""
        if song in self.songs:
            self.songs.remove(song)
    
    def get_song_count(self) -> int:
        """Get the number of songs in the playlist."""
        return len(self.songs)
    
    def create_iterator(self, iterator_type: str = "sequential", **kwargs) -> Iterator:
        """Create an iterator based on the specified type."""
        if iterator_type.lower() == "sequential":
            return SequentialIterator(self.songs.copy())
        elif iterator_type.lower() == "shuffle":
            return ShuffleIterator(self.songs.copy())
        elif iterator_type.lower() == "repeat":
            repeat_count = kwargs.get("repeat_count", None)
            return RepeatIterator(self.songs.copy(), repeat_count)
        else:
            raise ValueError(f"Unknown iterator type: {iterator_type}")
    
    def __str__(self):
        """String representation of the playlist."""
        return f"Playlist '{self.name}' with {len(self.songs)} songs"

class PythonicPlaylistIterator:
    """Python-style iterator that works with for loops and built-in functions."""
    
    def __init__(self, iterator: Iterator):
        self.iterator = iterator
    
    def __iter__(self):
        """Return self as the iterator object."""
        return self
    
    def __next__(self):
        """Get the next item using Python's iterator protocol."""
        if self.iterator.has_next():
            return self.iterator.next()
        else:
            raise StopIteration

class PythonicPlaylist(Playlist):
    """Enhanced playlist that supports Python's iterator protocol."""
    
    def __iter__(self):
        """Return a Python-style iterator for the playlist."""
        return PythonicPlaylistIterator(self.create_iterator("sequential"))
    
    def iter_shuffle(self):
        """Return a shuffled Python-style iterator."""
        return PythonicPlaylistIterator(self.create_iterator("shuffle"))
    
    def iter_repeat(self, repeat_count: Optional[int] = None):
        """Return a repeating Python-style iterator."""
        return PythonicPlaylistIterator(self.create_iterator("repeat", repeat_count=repeat_count))

# Create sample playlist
playlist = Playlist("Rock Classics")
playlist.add_song(Song("Bohemian Rhapsody", "Queen", 355))
playlist.add_song(Song("Stairway to Heaven", "Led Zeppelin", 482))
playlist.add_song(Song("Hotel California", "Eagles", 391))
playlist.add_song(Song("Sweet Child O' Mine", "Guns N' Roses", 356))

print("=== Testing Iterator Pattern ===\\n")
print(f"Created {playlist}\\n")

# Test 1: Sequential Iterator
print("1. Sequential Iterator:")
sequential_iter = playlist.create_iterator("sequential")
while sequential_iter.has_next():
    song = sequential_iter.next()
    print(f"   Playing: {song}")
print()

# Test 2: Shuffle Iterator
print("2. Shuffle Iterator:")
shuffle_iter = playlist.create_iterator("shuffle")
while shuffle_iter.has_next():
    song = shuffle_iter.next()
    print(f"   Playing: {song}")
print()

# Test 3: Repeat Iterator (limited)
print("3. Repeat Iterator (2 cycles):")
repeat_iter = playlist.create_iterator("repeat", repeat_count=2)
count = 0
while repeat_iter.has_next() and count < 6:  # Limit output for demo
    song = repeat_iter.next()
    print(f"   Playing: {song}")
    count += 1
print("   ... (continues cycling)")
print()

# Test 4: Python Iterator Protocol
print("4. Python Iterator Protocol:")
pythonic_playlist = PythonicPlaylist("Python Playlist")
pythonic_playlist.add_song(Song("Code Monkey", "Jonathan Coulton", 180))
pythonic_playlist.add_song(Song("Still Alive", "Portal Soundtrack", 178))
pythonic_playlist.add_song(Song("The Internet is for Porn", "Avenue Q", 195))

print("   Using for loop:")
for song in pythonic_playlist:
    print(f"   Playing: {song}")
print()

print("   Using list comprehension:")
song_titles = [song.title for song in pythonic_playlist]
print(f"   Titles: {song_titles}")
print()

# Test 5: Different Python iterators
print("5. Shuffled Python Iterator:")
for song in pythonic_playlist.iter_shuffle():
    print(f"   Playing: {song}")
print()

print("6. Repeat Python Iterator (1 cycle):")
for i, song in enumerate(pythonic_playlist.iter_repeat(1)):
    if i >= 4:  # Limit output
        print("   ... (continues)")
        break
    print(f"   Playing: {song}")

# What we accomplished in this step:
# - Tested all iterator types with comprehensive examples
# - Demonstrated custom iterator interface usage
# - Showed Python's iterator protocol integration
# - Proved iterators work with for loops, list comprehensions, etc.
# - Illustrated different iteration strategies on the same data


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step Iterator pattern solution!
#
# Key concepts learned:
# - Iterator pattern structure and purpose
# - Abstract iterator interface and concrete implementations
# - Aggregate interface for creating different iterators
# - Sequential, shuffle, and repeat iteration strategies
# - Python's iterator protocol (__iter__ and __next__)
# - Integration with Python's built-in iteration constructs
# - Separation of iteration logic from data structure
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each component is necessary
# 4. Experiment with modifications (try adding a reverse iterator!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================