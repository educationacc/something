class Validator:
    def __init__(self):
        self.valid_integers = []

    def user_input(self, input_list):
        for user_input in input_list:
            if self.is_valid_positive_integer(user_input):
                self.valid_integers.append(int(user_input))
