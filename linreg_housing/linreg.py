import numpy as np
from sklearn.model_selection import train_test_split


class GDRegressor:
    def __init__(self, alpha=0.001, n_iter=100, progress=True):
        # PUT YOUR CODE HERE
        pass


    def fit(self, X_train, y_train):
        """
        Подбирает коэффициенты линейной модели, ориентируясь на отклонение 
        предсказаний от реальных данных по MSE с помощью градиентного спуска.
        """
        # PUT YOUR CODE HERE
        pass


    def predict(self, X_test):
        """
        Считает предсказание, подставив в линейную модель найденные коэффициенты.
        """
        # PUT YOUR CODE HERE
        pass


def z_scaler(feature):
    """
    Проводит стандартизацию для X.
    Возвращает обновленную матрицу X.
    """
    # PUT YOUR CODE HERE
    pass


def min_max(feature):
    """
    Проводит минмаксную нормализацию (нормировку) для X.
    Возвращает обновленную матрицу X.
    """
    # PUT YOUR CODE HERE
    pass


def rmse(y_hat, y):
    """
    Считает и возвращает корень из среднеквадратичной ошибки.
    """
    # PUT YOUR CODE HERE
    pass


def r_squared(y_hat, y):
    """
    Считает и возвращает коэффициент детерминации.
    """
    # PUT YOUR CODE HERE
    pass


def find_optimal_params(X, y):
    """
    Подбирает лучшие гиперпараметры для поданных модели данных.
    Нужно разбить данные на тренировочную и тестовую выборки, 
    обучать модель с разными гиперпараметрами на тренировочной выборке, оценивать на тестовой.
    Вернуть нужно лучшие гиперпараметры: max_iter, alpha.
    Лучшие - это те, при которых на тестовой выборке R^2 ≥ 0.49, RMSE ≤ 6.45.
    При этом нельзя подгонять подбор гиперпараметров под тестовые данные. 
    В момент подбора оценка происходит на обучающей выборке.
    """
    # PUT YOUR CODE HERE
    pass
