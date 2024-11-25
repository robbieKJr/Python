class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2 #max level of volume
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3 #only 3 channels


    def __init__(self):
        """
        Television starts with default value.
        """
        self.__status = None
        self.__muted = None
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """
        Turns TV on and off
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Turns volume off or returns it to previous volume level
        """
        if self.__status:
            self.__status = not self.__muted

    def channel_up (self, televison = None):
        """
        increases the channel by 1. When top channel reached, loops to the bottom channel.
        """
        if self.__status:
            self.__channel = (self.__channel + 1) % (televison.MAX_CHANNEL + 1)

    def channel_down(self):
        """
        decreases the channel by 1. When bottom channel reached, loops to the top channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL
    def volume_up(self):
        """
        Increase the volume. Unmuted if the TV was muted.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self, televison = None):
        """
        Decrease the volume.Unmute if the TV was muted.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > televison.MIN_VOLUME:
                self.__volume -= 1


    def __str__(self, televison = None) -> str:
        """
        Method to show the tv status.
        :return:tv status.
        """
        if not self.__status:
            return f"Power = False, Channel = {self.__channel}, Volume = {self.__volume}"

        volume_display = Television.MIN_VOLUME if self.__muted else self.__volume
        return f"Power = True, Channel = {self.__channel}, Volume = {volume_display}"





#Channel logic
##################################################################
# Default  -  NFL  -  Cartoon Network    -    Discovery Channel
#   0           1             2                        3

#Volume Logic
##############################
#   0           1            2
