import random


class RandomStringGenerator(object):
    def __init__(self, **kwargs):
        self.probability = kwargs.get("probability", 0)
        self.keyword = kwargs.get("keyword")

    def generate_random_string(self):
        if self.probability > 0 and self.keyword:
            if random.random() < self.probability:
                return self.keyword
        return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=random.randint(1, 20)))


