import pandas as pd
import pytest
from utils import tratar_premiered

def test_tratar_premiered_splits_correctly():
    # Define input DataFrame
    df = pd.DataFrame({'PREMIERED': ['Spring 2022', 'Summer 2021']})

    # Call the function
    result = tratar_premiered(df)

    # Check if the result DataFrame has the expected columns
    assert 'PREMIERED_SEASON' in result.columns
    assert 'PREMIERED_YEAR' in result.columns

    # Check if the function correctly splits the 'PREMIERED' column
    assert result['PREMIERED_SEASON'].tolist() == ['Spring', 'Summer']
    assert result['PREMIERED_YEAR'].tolist() == ['2022', '2021']
    
def test_tratar_premiered_drops_column():
    # Define input DataFrame
    df = pd.DataFrame({'PREMIERED': ['Spring 2022', 'Summer 2021']})

    # Call the function
    result = tratar_premiered(df)

    # Check if the 'PREMIERED' column is not present in the result DataFrame
    assert 'PREMIERED' not in result.columns
    
def test_tratar_premiered_empty_dataframe():
    # Define an empty DataFrame
    df = pd.DataFrame()

    # Call the function and expect a ValueError
    with pytest.raises(ValueError):
        tratar_premiered(df)