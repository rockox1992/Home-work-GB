class SpareParts:
    _warehouse = {"stack_1": {"cell_1_1": {}, "cell_1_2": {}, "cell_1_3": {}},
                  "stack_2": {"cell_2_1": {}, "cell_2_2": {}, "cell_2_3": {}},
                  "stack_3": {"cell_3_1": {}, "cell_3_2": {}, "cell_3_3": {}}}

    def __init__(self, name, price, quantity, new_param_val=False, new_param_key=False):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.new_param_val = new_param_val
        self.new_param_key = new_param_key

    def add_to_cell(self):
        item = {
            'Модель устройства': self.name,
            'Цена за ед': self.price,
            'Количество': self.quantity}
        if not self.new_param_val and self.new_param_key:
            num_stack = int(input("Введите номер стеллажа: "))
            stack = f'stack_{num_stack}'
            num_cell = int(input('Введите номер ячейки: '))
            cell = f'cell_{num_stack}_{num_cell}'
            self._warehouse[stack][cell].update(item)
            print(self._warehouse)
        else:
            param_key = f'{self.new_param_key}'
            param_val = f'{self.new_param_val}'
            item[param_key] = param_val
            num_stack = int(input("Введите номер стеллажа: "))
            stack = f'stack_{num_stack}'
            num_cell = int(input('Введите номер ячейки: '))
            cell = f'cell_{num_stack}_{num_cell}'
            self._warehouse[stack][cell].update(item)
            print(self._warehouse)

    def err(self):
        try:
            if self.price == int or self.quantity == int:
                pass
        except ValueError:
            print('Недопустимое значение!')


class InductiveSensors(SpareParts):

    def __init__(self, name, price, quantity, new_param_val):
        super().__init__(name, price, quantity, new_param_val, new_param_key="Способ переключения")


class OpticalSensors(SpareParts):
    def __init__(self, name, price, quantity, new_param_val):
        super().__init__(name, price, quantity, new_param_val, new_param_key="Отражение от")


class PressureSensors(SpareParts):
    def __init__(self, name, price, quantity, new_param_val):
        super().__init__(name, price, quantity, new_param_val, new_param_key="Резьба")



i_s = InductiveSensors('Sick', 175, 2, "PNP")
o_s = OpticalSensors("Leuze", 333, 4, "объекта")
p_s = PressureSensors("E+H", 708, 2, "G 1/2")
p_s_1 = PressureSensors("E+H", 135, 2, "G 1")

i_s.add_to_cell()
o_s.add_to_cell()
p_s.add_to_cell()
p_s_1.add_to_cell()
