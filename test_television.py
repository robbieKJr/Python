import pytest
from televison import televison  # import statement needed to gain access to Television class


class Test:
    def __init__(self):
        self.tvl = None
        self.__mute = False
        self.__volume = 0
        self.__channel = 0
        self.__power = False

    def teardown_method(self):
        del self.tvl

    def test_init(self):
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        self.tvl.power()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tvl.power()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        self.tvl.power()
        self.tvl.volume_up()
        self.tvl.volume_down()
        self.tvl.mute()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tvl.mute()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 5'

    def test_channel_up(self):
        self.tvl.channel_up()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tvl.power()
        self.tvl.channel_up()
        assert self.tvl.__str__() == 'Power = True, Channel = 1, Volume = 0'

        self.tvl.channel_up()
        self.tvl.channel_up()
        self.tvl.channel_up()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        self.tvl.channel_down()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tvl.power()
        self.tvl.channel_down()
        assert self.tvl.__str__() == 'Power = True, Channel = 3, Volume = 0'

        self.tvl.power()
        self.tvl.channel_down()
        assert self.tvl.__str__() == 'Power = True, Channel = 2, Volume = 0'


    def test_volume_up(self):
        self.tvl.volume_up()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 1'

        for _ in range(20):
            self.tvl.volume_up()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 20'

    def test_volume_down(self):
        self.tvl.volume_down()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tvl.power()
        self.tvl.volume_up()
        self.tvl.volume_up()
        self.tvl.volume_up()
        self.tvl.volume_down()
        self.tvl.volume_down()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tvl.volume_down()
        self.tvl.volume_down()
        self.tvl.volume_down()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 0'

