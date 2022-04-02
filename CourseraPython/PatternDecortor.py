from abc import ABC, abstractmethod



class AbstractEffect(ABC, Hero):

    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass


class AbstractPositive(AbstractEffect, ABC):

    def __init__(self, base):
        super().__init__()
        self.base = base

    def get_positive_effects(self):
        return self.base.get_positive_effects()


class AbstractNegative(AbstractEffect, ABC):

    def __init__(self, base):
        super().__init__()
        self.base = base

    def get_negative_effects(self):
        return self.base.get_negative_effects()


class Berserk(AbstractPositive):

    def get_stats(self):
        """ Увеличивает характеристики: Сила, Выносливость, Ловкость, Удача на 7.
            Уменьшает характеристики: Восприятие, Харизма, Интеллект на 3ю
            Количество единиц здоровья увеличивается на 50."""
        health_decreasing_points = 50
        decreasing_points = 3
        increasing_points = 7

        health_stats = "HP"  # health points
        decreasing_stats = ["Perception", "Charisma", "Intelligence"]
        increasing_stats = ["Strength", "Endurance", "Agility", "Luck"]

        stats = self.base.get_stats()
        stats[health_stats] += health_decreasing_points
        for item in decreasing_stats:
            stats[item] -= decreasing_points
        for item in increasing_stats:
            stats[item] += increasing_points

        return stats

    def get_positive_effects(self):
        effect = self.base.get_positive_effects()
        effect.append("Berserk")
        return effect

    def get_negative_effects(self):
        return self.base.get_negative_effects()


class Blessing(AbstractPositive):

    def get_stats(self):
        """ Увеличивает все основные характеристики на 2."""
        increasing_points = 2
        increasing_stats = ["Strength", "Perception", "Endurance", "Charisma",
                            "Intelligence",  "Agility", "Luck"]
        stats = self.base.get_stats()

        for item in increasing_stats:
            stats[item] += increasing_points
        return stats

    def get_positive_effects(self):
        effect = self.base.get_positive_effects()
        effect.append("Blessing")
        return effect

    def get_negative_effects(self):
        return self.base.get_negative_effects()


class Weakness(AbstractNegative):
    def get_stats(self):
        """ Уменьшает характеристики: Сила, Выносливость, Ловкость на 4."""
        decreasing_points = 4
        decreasing_stats = ["Strength", "Endurance", "Agility"]

        stats = self.base.get_stats()
        for item in decreasing_stats:
            stats[item] -= decreasing_points
        return stats

    def get_negative_effects(self):
        effect = self.base.get_negative_effects()
        effect.append("Weakness")
        return effect

    def get_positive_effects(self):
        return self.base.get_positive_effects()


class EvilEye(AbstractNegative):

    def get_stats(self):
        """ Уменьшает  характеристику Удача на 10."""
        decreasing_points = 10
        decreasing_stats = "Luck"

        stats = self.base.get_stats()
        stats[decreasing_stats] -= decreasing_points

        return stats

    def get_negative_effects(self):
        effect = self.base.get_negative_effects()
        effect.append("EvilEye")
        return effect

    def get_positive_effects(self):
        return self.base.get_positive_effects()


class Curse(AbstractNegative):

    def get_stats(self):
        """ Уменьшает все основные характеристики на 2."""
        increasing_stats = ["Strength", "Perception", "Endurance", "Charisma",
                            "Intelligence", "Agility", "Luck"]
        increasing_points = 2
        stats = self.base.get_stats()

        for item in increasing_stats:
            stats[item] -= increasing_points
        return stats

    def get_negative_effects(self):
        effect = self.base.get_negative_effects()
        effect.append("Curse")
        return effect

    def get_positive_effects(self):
        return self.base.get_positive_effects()
