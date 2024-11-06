import pandas as pd
import numpy as np


def infer_and_convert_data_types(df: pd.DataFrame) -> dict:
    for col in df.columns:
        # Attempt to convert to numeric first
        df_converted = pd.to_numeric(df[col], errors='coerce')
        if not df_converted.isna().all():  # If at least one value is numeric
            df[col] = df_converted
            continue

        # Attempt to convert to datetime
        try:
            df[col] = pd.to_datetime(df[col])
            continue
        except (ValueError, TypeError):
            pass

        # Attempt to convert to timedelta
        try:
            df[col] = pd.to_timedelta(df[col])
            if not df[col].isna().all():  # If at least one value is a valid timedelta
                continue
        except ValueError:
            pass

        # Check if the column should be categorical
        if len(df[col].unique()) / len(df[col]) < 0.5:  # Example threshold for categorization
            df[col] = pd.Categorical(df[col])

    df = df.replace({np.nan: None})

    result = df.to_dict(orient='split', index=False)
    result['data_types'] = [str(dtype) for dtype in df.dtypes]
    return result
