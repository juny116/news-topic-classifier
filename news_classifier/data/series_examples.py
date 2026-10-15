"""Compatibility entry points for dataframe rows and dictionary records."""
from torchtext.data import Example

class SeriesExample(Example):
    @classmethod
    def fromSeries(cls, data, fields):
        return cls.fromdict(data.to_dict(), fields)

    @classmethod
    def fromdict(cls, data, fields):
        mapping = list(fields.items())
        missing = set(fields).difference(data)
        if missing:
            raise ValueError(f"Missing dataframe columns: {sorted(missing)}")
        return cls.fromlist([data[name] for name, _ in mapping], mapping)
