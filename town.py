from Equipment import EquipmentFactory, RareEquipmentFactory

class Town:
    def __init__(self):
        self.items = [EquipmentFactory(), EquipmentFactory(),
                      RareEquipmentFactory()]

    def refresh(self):
        self.items = [EquipmentFactory(), EquipmentFactory(),
                      RareEquipmentFactory()]
