import abc


class Splitter(abc.ABC):

    def split_data(self, X, y):
        raise NotImplementedError(
            "Subclasses must implement split_data method")
