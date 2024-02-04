class SomeClass:
    def _hidden_method(self):
        return 0

    def public_method(self, x):
        return self._hidden_method() + x
