
class SongWrapper():
    """
    Parent class of song file wrapper sub-classes.
    Defines the methods that should be implemented in
    subclasses. This class should not be instantiated.
    """
    def __init__(self, path):
        self.path = None
        self.decoder = None
    def get_decoder(self):
        return None
    def deinit(self):
        return None
    def get_song(self):
        return None

class MP3Wrapper(SongWrapper):
    """
    Wrapper for MP3 audio files.
    """
    def __init__(self, path):
        self.path = path
        self.decoder = None
    def get_decoder(self):
        self.decoder = audiomp3.MP3Decoder(self.path)
    def deinit(self):
        if self.decoder is not None:
            self.decoder.deinit()
    def get_song(self):
        return self.path

class WavWrapper(SongWrapper):
    """
    Wrapper for WAV audio files.
    """
    def __init__(self, path):
        self.path = path
        self.decoder = None
    def get_decoder(self):
        self.decoder = audiocore.WaveFile(self.path)
        return self.decoder
    def deinit(self):
        if self.decoder is not None:
            self.decoder.deinit()
    def get_song(self):
        return self.path