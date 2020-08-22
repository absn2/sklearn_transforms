from sklearn.base import BaseEstimator, TransformerMixin
import pandas
# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        for labelColumn in self.columns:
            data = data.drop(labels=labelColumn, axis='columns')
        data = data.dropna()
        return data
        
