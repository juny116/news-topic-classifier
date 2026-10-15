"""Adapt dataframe records through torchtext's public Example/Dataset APIs."""
from torchtext.data import Dataset
from .series_examples import SeriesExample

class DataFrameDataset(Dataset):
    def __init__(self, examples, fields, filter_pred=None):
        mapping = dict(fields)
        records = [SeriesExample.fromdict(row, mapping)
                   for row in examples.to_dict(orient="records")]
        super().__init__(records, list(mapping.items()), filter_pred=filter_pred)

    @staticmethod
    def sort_key(example):
        return len(example.News)
