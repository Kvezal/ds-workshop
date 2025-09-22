import pandas


class ModelAPI:
    THRESHOLD_CLASSIFICATION = 0.42

    def __init__(self, model):
        super().__init__()
        self._model = model


    def predict_from_df(self, df: pandas.DataFrame) -> pandas.DataFrame:
        df_for_predict = df.drop(['id'], axis=1)
        proba = self._model.predict_proba(df_for_predict)[:, 1]
        return  pandas.DataFrame({
            'id': df.id,
            'prediction': list(map(lambda x: 1 if x >= self.THRESHOLD_CLASSIFICATION else 0, proba)),
        })
