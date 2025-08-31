class WeaponProcessor:
    def __init__(self, weapon_list_path):
        weapon_list = []
        with open(weapon_list_path, encoding='utf-8') as f:
            for line in f:
                weapon = line.strip()
                if weapon:
                    weapon_list.append(weapon)
        self.weapon_list = weapon_list

    def find_weapons(self, clean_text: str) -> list[str]:

        text = ' '.join(clean_text.split())
        tokens = set(text.split())
        padded = f" {text} "

        found = []
        for weapon in self.weapon_list:
            if ' ' in weapon:
                if f" {weapon} " in padded:
                    found.append(weapon)
            else:
                if weapon in tokens:
                    found.append(weapon)
        return found
