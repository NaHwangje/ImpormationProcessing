class Computer:
    def __init__(self, hdd, ram, is_graphics_card_enabled=False, is_bluetooth_enabled=False):
        self.hdd = hdd
        self.ram = ram
        self.is_graphics_card_enabled = is_graphics_card_enabled
        self.is_bluetooth_enabled = is_bluetooth_enabled

    def get_hdd(self):
        return self.hdd

    def get_ram(self):
        return self.ram

    def is_graphics_card_enabled(self):
        return self.is_graphics_card_enabled

    def is_bluetooth_enabled(self):
        return self.is_bluetooth_enabled
