class ColorDict:
    def __init__(self,is_empty = False):
        self.dict_with_colors = self.cost = {"red": 7, "blue": 7, "black": 7,
                                             "white": 7, "green": 7, "special": 5}
        if is_empty:
            self.dict_with_colors = self.cost = {"red": 0, "blue": 0, "black": 0,
                                                 "white": 0, "green": 0, "special": 0}

    def get_dict(self):
        return self.dict_with_colors

    def increase_color_value(self, color, value):
        self.dict_with_colors[color] += value

    def set_value(self, color, value):
        self.dict_with_colors[color] = value

    def increse_by_color_dict(self,second_color_dict):
        for key, value in second_color_dict.get_dict:
            self.increase_color_value(key,value)

