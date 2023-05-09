import abc


class Splitter(abc.ABC):
    """
    A class that splits the dataset into train and test data
    """

    def __init__(self, test_size: float, random_state: int, shuffle: bool):
        """
        :param test_size: a fraction that defines the percentage of the test data split
        :param random_state: a Controller that controls shuffling. Pass an int for reproducible output across multiple
            function calls.
        """
        self.test_size = test_size
        self.random_state = random_state

    @abc.abstractmethod
    def split_data(self, X, y):
        """
        :param X: X is the feature matrix. It is typically two-dimensional array or matrix of
            shape (n_samples,n_features)
        :param y: y is the target variable. It is one-dimensional array of (n_samples)
        :return: The output of the split_data method will be a tuple of four arrays: X_train, X_test, y_train, and
            y_test.
        """
        pass
