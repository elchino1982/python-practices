"""Question: Implement the Adapter pattern to make incompatible interfaces work together.

Create a media player system that can play different audio formats (MP3, MP4, VLC)
by adapting third-party libraries with incompatible interfaces.

Requirements:
1. Create MediaPlayer interface with play method
2. Implement AdvancedMediaPlayer for MP4 and VLC
3. Create MediaAdapter to adapt incompatible interfaces
4. Implement AudioPlayer that uses adapter when needed
5. Demonstrate playing different formats through unified interface
6. Show both object and class adapter approaches

Example usage:
    player = AudioPlayer()
    player.play("mp3", "song.mp3")
    player.play("mp4", "video.mp4")
    player.play("vlc", "movie.vlc")
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
# - What is the target interface you want to use?
# - What are the incompatible interfaces you need to adapt?
# - How can an adapter translate between interfaces?
# - What are the differences between object and class adapters?
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


# Step 1: Create the target interface and basic implementation
# ===============================================================================

# Explanation:
# The Adapter pattern starts with a target interface that the client expects.
# We'll create a MediaPlayer interface and a basic implementation for MP3.

from abc import ABC, abstractmethod

class MediaPlayer(ABC):
    """Target interface that clients expect to use."""
    
    @abstractmethod
    def play(self, audio_type: str, filename: str):
        """Play audio file of specified type."""
        pass

class Mp3Player:
    """Basic MP3 player implementation."""
    
    def play_mp3(self, filename: str):
        """Play MP3 file."""
        print(f"Playing MP3 file: {filename}")

# What we accomplished in this step:
# - Created the target MediaPlayer interface
# - Implemented basic MP3 player functionality


# Step 2: Create incompatible third-party interfaces
# ===============================================================================

# Explanation:
# These represent third-party libraries with incompatible interfaces
# that we need to adapt to work with our MediaPlayer interface.

from abc import ABC, abstractmethod

class MediaPlayer(ABC):
    """Target interface that clients expect to use."""
    
    @abstractmethod
    def play(self, audio_type: str, filename: str):
        """Play audio file of specified type."""
        pass

class Mp3Player:
    """Basic MP3 player implementation."""
    
    def play_mp3(self, filename: str):
        """Play MP3 file."""
        print(f"Playing MP3 file: {filename}")

class AdvancedMediaPlayer(ABC):
    """Interface for advanced media players (third-party)."""
    
    @abstractmethod
    def play_vlc(self, filename: str):
        """Play VLC file."""
        pass
    
    @abstractmethod
    def play_mp4(self, filename: str):
        """Play MP4 file."""
        pass

class VlcPlayer(AdvancedMediaPlayer):
    """VLC player implementation (third-party library)."""
    
    def play_vlc(self, filename: str):
        """Play VLC file."""
        print(f"Playing VLC file: {filename}")
    
    def play_mp4(self, filename: str):
        """VLC doesn't support MP4 directly."""
        # Do nothing - VLC player doesn't support MP4
        pass

class Mp4Player(AdvancedMediaPlayer):
    """MP4 player implementation (third-party library)."""
    
    def play_vlc(self, filename: str):
        """MP4 player doesn't support VLC."""
        # Do nothing - MP4 player doesn't support VLC
        pass
    
    def play_mp4(self, filename: str):
        """Play MP4 file."""
        print(f"Playing MP4 file: {filename}")

# What we accomplished in this step:
# - Created incompatible third-party interfaces
# - Implemented VLC and MP4 players with different method signatures


# Step 3: Create the object adapter
# ===============================================================================

# Explanation:
# The adapter translates calls from the target interface to the incompatible
# interface. Object adapter uses composition to wrap the adaptee.

from abc import ABC, abstractmethod

class MediaPlayer(ABC):
    """Target interface that clients expect to use."""
    
    @abstractmethod
    def play(self, audio_type: str, filename: str):
        """Play audio file of specified type."""
        pass

class Mp3Player:
    """Basic MP3 player implementation."""
    
    def play_mp3(self, filename: str):
        """Play MP3 file."""
        print(f"Playing MP3 file: {filename}")

class AdvancedMediaPlayer(ABC):
    """Interface for advanced media players (third-party)."""
    
    @abstractmethod
    def play_vlc(self, filename: str):
        """Play VLC file."""
        pass
    
    @abstractmethod
    def play_mp4(self, filename: str):
        """Play MP4 file."""
        pass

class VlcPlayer(AdvancedMediaPlayer):
    """VLC player implementation (third-party library)."""
    
    def play_vlc(self, filename: str):
        """Play VLC file."""
        print(f"Playing VLC file: {filename}")
    
    def play_mp4(self, filename: str):
        """VLC doesn't support MP4 directly."""
        # Do nothing - VLC player doesn't support MP4
        pass

class Mp4Player(AdvancedMediaPlayer):
    """MP4 player implementation (third-party library)."""
    
    def play_vlc(self, filename: str):
        """MP4 player doesn't support VLC."""
        # Do nothing - MP4 player doesn't support VLC
        pass
    
    def play_mp4(self, filename: str):
        """Play MP4 file."""
        print(f"Playing MP4 file: {filename}")

class MediaAdapter(MediaPlayer):
    """Object adapter that adapts AdvancedMediaPlayer to MediaPlayer interface."""
    
    def __init__(self, audio_type: str):
        """Initialize adapter with specific audio type."""
        self.audio_type = audio_type.lower()
        
        if self.audio_type == "vlc":
            self.advanced_player = VlcPlayer()
        elif self.audio_type == "mp4":
            self.advanced_player = Mp4Player()
        else:
            self.advanced_player = None
    
    def play(self, audio_type: str, filename: str):
        """Adapt the play method to use advanced media players."""
        audio_type = audio_type.lower()
        
        if audio_type == "vlc":
            self.advanced_player.play_vlc(filename)
        elif audio_type == "mp4":
            self.advanced_player.play_mp4(filename)

# What we accomplished in this step:
# - Created object adapter using composition
# - Adapter translates MediaPlayer.play() to appropriate AdvancedMediaPlayer methods
# - Supports both VLC and MP4 formats through adaptation


# Step 4: Create the main AudioPlayer that uses the adapter
# ===============================================================================

# Explanation:
# The AudioPlayer is the client that uses the adapter when needed.
# It handles MP3 directly and uses the adapter for other formats.

from abc import ABC, abstractmethod

class MediaPlayer(ABC):
    """Target interface that clients expect to use."""
    
    @abstractmethod
    def play(self, audio_type: str, filename: str):
        """Play audio file of specified type."""
        pass

class Mp3Player:
    """Basic MP3 player implementation."""
    
    def play_mp3(self, filename: str):
        """Play MP3 file."""
        print(f"Playing MP3 file: {filename}")

class AdvancedMediaPlayer(ABC):
    """Interface for advanced media players (third-party)."""
    
    @abstractmethod
    def play_vlc(self, filename: str):
        """Play VLC file."""
        pass
    
    @abstractmethod
    def play_mp4(self, filename: str):
        """Play MP4 file."""
        pass

class VlcPlayer(AdvancedMediaPlayer):
    """VLC player implementation (third-party library)."""
    
    def play_vlc(self, filename: str):
        """Play VLC file."""
        print(f"Playing VLC file: {filename}")
    
    def play_mp4(self, filename: str):
        """VLC doesn't support MP4 directly."""
        # Do nothing - VLC player doesn't support MP4
        pass

class Mp4Player(AdvancedMediaPlayer):
    """MP4 player implementation (third-party library)."""
    
    def play_vlc(self, filename: str):
        """MP4 player doesn't support VLC."""
        # Do nothing - MP4 player doesn't support VLC
        pass
    
    def play_mp4(self, filename: str):
        """Play MP4 file."""
        print(f"Playing MP4 file: {filename}")

class MediaAdapter(MediaPlayer):
    """Object adapter that adapts AdvancedMediaPlayer to MediaPlayer interface."""
    
    def __init__(self, audio_type: str):
        """Initialize adapter with specific audio type."""
        self.audio_type = audio_type.lower()
        
        if self.audio_type == "vlc":
            self.advanced_player = VlcPlayer()
        elif self.audio_type == "mp4":
            self.advanced_player = Mp4Player()
        else:
            self.advanced_player = None
    
    def play(self, audio_type: str, filename: str):
        """Adapt the play method to use advanced media players."""
        audio_type = audio_type.lower()
        
        if audio_type == "vlc":
            self.advanced_player.play_vlc(filename)
        elif audio_type == "mp4":
            self.advanced_player.play_mp4(filename)

class AudioPlayer(MediaPlayer):
    """Main audio player that uses adapter for unsupported formats."""
    
    def __init__(self):
        """Initialize the audio player."""
        self.mp3_player = Mp3Player()
        self.media_adapter = None
    
    def play(self, audio_type: str, filename: str):
        """Play audio file, using adapter for unsupported formats."""
        audio_type = audio_type.lower()
        
        if audio_type == "mp3":
            # Handle MP3 directly
            self.mp3_player.play_mp3(filename)
        elif audio_type in ["mp4", "vlc"]:
            # Use adapter for other formats
            self.media_adapter = MediaAdapter(audio_type)
            self.media_adapter.play(audio_type, filename)
        else:
            print(f"Invalid media. {audio_type} format not supported")

# What we accomplished in this step:
# - Created AudioPlayer that acts as the client
# - Handles MP3 directly and uses adapter for MP4/VLC
# - Provides unified interface for all supported formats


# Step 5: Implement class adapter approach
# ===============================================================================

# Explanation:
# Class adapter uses inheritance instead of composition.
# In Python, we can use multiple inheritance to create class adapters.

from abc import ABC, abstractmethod

class MediaPlayer(ABC):
    """Target interface that clients expect to use."""
    
    @abstractmethod
    def play(self, audio_type: str, filename: str):
        """Play audio file of specified type."""
        pass

class Mp3Player:
    """Basic MP3 player implementation."""
    
    def play_mp3(self, filename: str):
        """Play MP3 file."""
        print(f"Playing MP3 file: {filename}")

class AdvancedMediaPlayer(ABC):
    """Interface for advanced media players (third-party)."""
    
    @abstractmethod
    def play_vlc(self, filename: str):
        """Play VLC file."""
        pass
    
    @abstractmethod
    def play_mp4(self, filename: str):
        """Play MP4 file."""
        pass

class VlcPlayer(AdvancedMediaPlayer):
    """VLC player implementation (third-party library)."""
    
    def play_vlc(self, filename: str):
        """Play VLC file."""
        print(f"Playing VLC file: {filename}")
    
    def play_mp4(self, filename: str):
        """VLC doesn't support MP4 directly."""
        # Do nothing - VLC player doesn't support MP4
        pass

class Mp4Player(AdvancedMediaPlayer):
    """MP4 player implementation (third-party library)."""
    
    def play_vlc(self, filename: str):
        """MP4 player doesn't support VLC."""
        # Do nothing - MP4 player doesn't support VLC
        pass
    
    def play_mp4(self, filename: str):
        """Play MP4 file."""
        print(f"Playing MP4 file: {filename}")

class MediaAdapter(MediaPlayer):
    """Object adapter that adapts AdvancedMediaPlayer to MediaPlayer interface."""
    
    def __init__(self, audio_type: str):
        """Initialize adapter with specific audio type."""
        self.audio_type = audio_type.lower()
        
        if self.audio_type == "vlc":
            self.advanced_player = VlcPlayer()
        elif self.audio_type == "mp4":
            self.advanced_player = Mp4Player()
        else:
            self.advanced_player = None
    
    def play(self, audio_type: str, filename: str):
        """Adapt the play method to use advanced media players."""
        audio_type = audio_type.lower()
        
        if audio_type == "vlc":
            self.advanced_player.play_vlc(filename)
        elif audio_type == "mp4":
            self.advanced_player.play_mp4(filename)

class VlcClassAdapter(MediaPlayer, VlcPlayer):
    """Class adapter for VLC player using multiple inheritance."""
    
    def play(self, audio_type: str, filename: str):
        """Adapt VLC player to MediaPlayer interface."""
        if audio_type.lower() == "vlc":
            self.play_vlc(filename)

class Mp4ClassAdapter(MediaPlayer, Mp4Player):
    """Class adapter for MP4 player using multiple inheritance."""
    
    def play(self, audio_type: str, filename: str):
        """Adapt MP4 player to MediaPlayer interface."""
        if audio_type.lower() == "mp4":
            self.play_mp4(filename)

class AudioPlayer(MediaPlayer):
    """Main audio player that uses adapter for unsupported formats."""
    
    def __init__(self):
        """Initialize the audio player."""
        self.mp3_player = Mp3Player()
        self.media_adapter = None
    
    def play(self, audio_type: str, filename: str):
        """Play audio file, using adapter for unsupported formats."""
        audio_type = audio_type.lower()
        
        if audio_type == "mp3":
            # Handle MP3 directly
            self.mp3_player.play_mp3(filename)
        elif audio_type in ["mp4", "vlc"]:
            # Use adapter for other formats
            self.media_adapter = MediaAdapter(audio_type)
            self.media_adapter.play(audio_type, filename)
        else:
            print(f"Invalid media. {audio_type} format not supported")

class EnhancedAudioPlayer(MediaPlayer):
    """Enhanced audio player that demonstrates class adapters."""
    
    def __init__(self):
        """Initialize the enhanced audio player."""
        self.mp3_player = Mp3Player()
        self.vlc_adapter = VlcClassAdapter()
        self.mp4_adapter = Mp4ClassAdapter()
    
    def play(self, audio_type: str, filename: str):
        """Play audio file using class adapters."""
        audio_type = audio_type.lower()
        
        if audio_type == "mp3":
            self.mp3_player.play_mp3(filename)
        elif audio_type == "vlc":
            self.vlc_adapter.play(audio_type, filename)
        elif audio_type == "mp4":
            self.mp4_adapter.play(audio_type, filename)
        else:
            print(f"Invalid media. {audio_type} format not supported")

# What we accomplished in this step:
# - Created class adapters using multiple inheritance
# - Demonstrated alternative approach to object adapter
# - Added enhanced audio player using class adapters


# Step 6: Test the complete implementation
# ===============================================================================

# Explanation:
# Let's test both object and class adapter approaches with different media formats.

from abc import ABC, abstractmethod

class MediaPlayer(ABC):
    """Target interface that clients expect to use."""
    
    @abstractmethod
    def play(self, audio_type: str, filename: str):
        """Play audio file of specified type."""
        pass

class Mp3Player:
    """Basic MP3 player implementation."""
    
    def play_mp3(self, filename: str):
        """Play MP3 file."""
        print(f"Playing MP3 file: {filename}")

class AdvancedMediaPlayer(ABC):
    """Interface for advanced media players (third-party)."""
    
    @abstractmethod
    def play_vlc(self, filename: str):
        """Play VLC file."""
        pass
    
    @abstractmethod
    def play_mp4(self, filename: str):
        """Play MP4 file."""
        pass

class VlcPlayer(AdvancedMediaPlayer):
    """VLC player implementation (third-party library)."""
    
    def play_vlc(self, filename: str):
        """Play VLC file."""
        print(f"Playing VLC file: {filename}")
    
    def play_mp4(self, filename: str):
        """VLC doesn't support MP4 directly."""
        # Do nothing - VLC player doesn't support MP4
        pass

class Mp4Player(AdvancedMediaPlayer):
    """MP4 player implementation (third-party library)."""
    
    def play_vlc(self, filename: str):
        """MP4 player doesn't support VLC."""
        # Do nothing - MP4 player doesn't support VLC
        pass
    
    def play_mp4(self, filename: str):
        """Play MP4 file."""
        print(f"Playing MP4 file: {filename}")

class MediaAdapter(MediaPlayer):
    """Object adapter that adapts AdvancedMediaPlayer to MediaPlayer interface."""
    
    def __init__(self, audio_type: str):
        """Initialize adapter with specific audio type."""
        self.audio_type = audio_type.lower()
        
        if self.audio_type == "vlc":
            self.advanced_player = VlcPlayer()
        elif self.audio_type == "mp4":
            self.advanced_player = Mp4Player()
        else:
            self.advanced_player = None
    
    def play(self, audio_type: str, filename: str):
        """Adapt the play method to use advanced media players."""
        audio_type = audio_type.lower()
        
        if audio_type == "vlc":
            self.advanced_player.play_vlc(filename)
        elif audio_type == "mp4":
            self.advanced_player.play_mp4(filename)

class VlcClassAdapter(MediaPlayer, VlcPlayer):
    """Class adapter for VLC player using multiple inheritance."""
    
    def play(self, audio_type: str, filename: str):
        """Adapt VLC player to MediaPlayer interface."""
        if audio_type.lower() == "vlc":
            self.play_vlc(filename)

class Mp4ClassAdapter(MediaPlayer, Mp4Player):
    """Class adapter for MP4 player using multiple inheritance."""
    
    def play(self, audio_type: str, filename: str):
        """Adapt MP4 player to MediaPlayer interface."""
        if audio_type.lower() == "mp4":
            self.play_mp4(filename)

class AudioPlayer(MediaPlayer):
    """Main audio player that uses adapter for unsupported formats."""
    
    def __init__(self):
        """Initialize the audio player."""
        self.mp3_player = Mp3Player()
        self.media_adapter = None
    
    def play(self, audio_type: str, filename: str):
        """Play audio file, using adapter for unsupported formats."""
        audio_type = audio_type.lower()
        
        if audio_type == "mp3":
            # Handle MP3 directly
            self.mp3_player.play_mp3(filename)
        elif audio_type in ["mp4", "vlc"]:
            # Use adapter for other formats
            self.media_adapter = MediaAdapter(audio_type)
            self.media_adapter.play(audio_type, filename)
        else:
            print(f"Invalid media. {audio_type} format not supported")

class EnhancedAudioPlayer(MediaPlayer):
    """Enhanced audio player that demonstrates class adapters."""
    
    def __init__(self):
        """Initialize the enhanced audio player."""
        self.mp3_player = Mp3Player()
        self.vlc_adapter = VlcClassAdapter()
        self.mp4_adapter = Mp4ClassAdapter()
    
    def play(self, audio_type: str, filename: str):
        """Play audio file using class adapters."""
        audio_type = audio_type.lower()
        
        if audio_type == "mp3":
            self.mp3_player.play_mp3(filename)
        elif audio_type == "vlc":
            self.vlc_adapter.play(audio_type, filename)
        elif audio_type == "mp4":
            self.mp4_adapter.play(audio_type, filename)
        else:
            print(f"Invalid media. {audio_type} format not supported")

print("=== Testing Adapter Pattern ===\n")

# Test object adapter approach
print("1. Testing Object Adapter Approach:")
print("-" * 40)
player = AudioPlayer()
player.play("mp3", "beyond_the_horizon.mp3")
player.play("mp4", "alone.mp4")
player.play("vlc", "far_far_away.vlc")
player.play("avi", "mind_me.avi")
print()

# Test class adapter approach
print("2. Testing Class Adapter Approach:")
print("-" * 40)
enhanced_player = EnhancedAudioPlayer()
enhanced_player.play("mp3", "my_favorite_song.mp3")
enhanced_player.play("mp4", "action_movie.mp4")
enhanced_player.play("vlc", "documentary.vlc")
enhanced_player.play("wav", "sound_effect.wav")
print()

# Test individual adapters
print("3. Testing Individual Adapters:")
print("-" * 40)
vlc_adapter = VlcClassAdapter()
vlc_adapter.play("vlc", "classic_movie.vlc")

mp4_adapter = Mp4ClassAdapter()
mp4_adapter.play("mp4", "music_video.mp4")

object_adapter = MediaAdapter("mp4")
object_adapter.play("mp4", "trailer.mp4")

# What we accomplished in this step:
# - Tested both object and class adapter approaches
# - Demonstrated unified interface for different media formats
# - Showed error handling for unsupported formats
# - Verified adapter functionality with various file types


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Adapter pattern structure and purpose
# - Object adapter using composition
# - Class adapter using multiple inheritance
# - Target interface and adaptee interfaces
# - Client code that uses adapters transparently
# - Making incompatible interfaces work together
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding AAC or FLAC support!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
