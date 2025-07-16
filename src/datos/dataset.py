import pandas as pd

def cargarData(year: int, month: int) -> pd.DataFrame:
    """Leer los datos de un año y mes determinados."""
    filename = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month:02}.parquet"
    return pd.read_parquet(filename)

