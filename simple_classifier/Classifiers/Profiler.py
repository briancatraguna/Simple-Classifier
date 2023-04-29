from simple_classifier.Classifiers.ClassifierProfiler import ClassifierProfiler


class Profiler(ClassifierProfiler):
    def __init__(self, metrics):
        self.metrics = metrics

    def run(self, classifier):
        # Run profiler on given classifier
        pass