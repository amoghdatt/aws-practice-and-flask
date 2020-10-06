class Parent:

    def save(self):
        return self


class Child(Parent):

    username = 'test'

    def __init__(self, **kwargs):
        self.password = kwargs.get('password', '')

    def test_def(self):
        return self
