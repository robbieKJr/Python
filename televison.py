class Televison:
    MIN_VOLUME = 0
    MAX_VOLUME = 20 #max level of volume
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3 #only 3 channels


    def __init__(self):
        """
        Television starts with default value.
        """
        self._status = None
        self._muted = False
        self._volume = Television.MIN_VOLUME
        self._channel = Television.MIN_CHANNEL

    def power(self):
        """
        Turns TV on and off
        """
        self._status = self.power

    def mute(self):
        """
        Turns volume off or returns it to previous volume level
        """
        if self._status:
            self._status = self._muted

    def channel_up (self):
        """
        increases the channel by 1. When top channel reached, loops to the bottom channel.
        """
        if self._status:
            self._channel = (self._channel + 1) % (Televison.MAX_CHANNEL + 1)

    def channel_down(self):
        """
        decreases the channel by 1. When bottom channel reached, loops to the top channel.
        """
        if self._status:
            if self._channel > Television.MIN_CHANNEL:
                self._channel -= 1
            else:
                self._channel = Television.MAX_CHANNEL
    def volume_up(self):
        """
        Increase the volume. Unmuted if the TV was muted.
        """
        if self._status:
            self._muted = False
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1

    def volume_down(self):
        """
        Decrease the volume.Unmute if the TV was muted.
        """
        if self._status:
            self._muted = False
            if self._volume > Televison.MIN_VOLUME:
                self._volume -= 1


    def __str__(self):
        if self._muted:
            return f'Volume = {Televison.MIN_VOLUME}'
        else:
            return f'Power = {self._status}, Volume = {self._volume}, Channel = {self._channel}'







#Channel logic
##################################################################
# Default  -  NFL  -  Cartoon Network    -    Discovery Channel
#   0           1             2                        3

#Volume Logic
##############################
#   0           1            2