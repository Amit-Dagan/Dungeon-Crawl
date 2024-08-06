from Equipment import EquipmentFactory

class Town:
    def __init__(self):
        self.items = [EquipmentFactory(type="normal"), EquipmentFactory(type="normal"),
                      EquipmentFactory(type="rare")]

    def refresh(self):
        self.items = [EquipmentFactory(type="normal"), EquipmentFactory(type="normal"),
                      EquipmentFactory(type="rare")]
