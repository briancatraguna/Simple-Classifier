from simple_classifier.Splitter.Splitter import Splitter
from sklearn.model_selection import train_test_split


@Splitter.register("Percentage_split")
class PercentageSplitter(Splitter):
    """
    This class will cover split by percentage, as well as split by Random state. If you don't want to use random state
    set random_state = None. This will apply for every other subclasses also.

    """
    def split_data(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size,
                                                            random_state=self.random_state, shuffle=False,
                                                            stratify=None)
        return X_train, X_test, y_train, y_test


@Splitter.register("Percentage_split_w_shuffle")
class PercentageShuffleSplitter(Splitter):

    def split_data(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size,
                                                            random_state=self.random_state, shuffle=True, stratify=None)
        return X_train, X_test, y_train, y_test


@Splitter.register("Percentage_split_w_stratify")
class PercentageStratifiedSplitter(Splitter):
    """
    If stratify is not None, the function uses the target variable y to group the shuffled data by class. It then
    calculates the proportion of each class in the original dataset and ensures that the same proportion of each
    class is present in both the training and test sets. For example, if the original dataset has 70% of samples
    in class A and 30% in class B, the training and test sets will also have the same 70/30 split of classes.
    """

    def split_data(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size,
                                                            random_state=self.random_state, shuffle=True, stratify=y)
        return X_train, X_test, y_train, y_test


