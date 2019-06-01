def test():
    import autosklearn.classification
    import sklearn.model_selection
    import sklearn.datasets
    import sklearn.metrics
    X, y = sklearn.datasets.load_digits(return_X_y=True)
    X_train, X_test, y_train, y_test = \
        sklearn.model_selection.train_test_split(X, y, random_state=1)
    automl = autosklearn.classification.AutoSklearnClassifier()
    automl.fit(X_train, y_train)

if __name__ == '__main__':
    if __name__ !="__mp_main__":
        test()
