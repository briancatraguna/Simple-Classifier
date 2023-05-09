from sklearn.model_selection import train_test_split

from src.Splitter.Splitter import Splitter


class PercentageSplitter(Splitter):
    """This class will cover split by percentage, as well as split by Random state. If you don't want to use random state
    set random_state = None. This will apply for every other subclasses also.

    :return: X_train : array-like or sparse matrix of shape (n_train_samples, n_features)
    The training input data.
    X_test : array-like or sparse matrix of shape (n_test_samples, n_features)
    The testing input data.
    y_train : array-like of shape (n_train_samples,)
    The training target labels.
    y_test : array-like of shape (n_test_samples,)
    The testing target labels.
    """

    def split_data(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size,
                                                            random_state=self.random_state, shuffle=False,
                                                            stratify=None)
        return X_train, X_test, y_train, y_test


class PercentageShuffleSplitter(Splitter):

    def split_data(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size,
                                                            random_state=self.random_state, shuffle=True, stratify=None)
        return X_train, X_test, y_train, y_test


class PercentageStratifiedSplitter(Splitter):
    """If stratify is not None, the function uses the target variable y to group the shuffled data by class. It then
    calculates the proportion of each class in the original dataset and ensures that the same proportion of each
    class is present in both the training and test sets. For example, if the original dataset has 70% of samples
    in class A and 30% in class B, the training and test sets will also have the same 70/30 split of classes.
    """

    def split_data(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size,
                                                            random_state=self.random_state, shuffle=True, stratify=y)
        return X_train, X_test, y_train, y_test


class PercentageCrossValSplitter(Splitter):
    """Splits a dataset into a training set, a validation set, and a testing set using scikit-learn's
    train_test_split() function.

    :return: X_val : array-like or sparse matrix of shape (n_val_samples, n_features)
    The validation input data.
    y_val : array-like of shape (n_val_samples,)
    The validation target labels.
    """

    def split_data(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size,
                                                            random_state=self.random_state)
        X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=self.test_size,
                                                          random_state=self.random_state)
        return X_train, X_test, y_train, y_test, X_val, y_val
