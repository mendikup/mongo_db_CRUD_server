from models.soldier import Soldier
from tests import last_names, soldier


class SoldierBuilder:

    @staticmethod
    def build_soldier(soldier):
        soldier = Soldier(
            ID=soldier["ID"],
            first_name=soldier["first_name"],
            last_name=soldier["last_name"],
            phone_number=soldier["phone_number"],
            rank=soldier["rank"])

        return soldier
