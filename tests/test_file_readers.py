import csv
from unittest.mock import patch, mock_open, MagicMock
import pandas as pd
from scr.file_readers import read_transactions_from_csv, read_transactions_from_excel


def test_read_csv_success(sample_csv_data):
    with patch('builtins.open', mock_open(read_data=sample_csv_data['content'])):
        result = read_transactions_from_csv('test_file.csv')
    
    assert result == sample_csv_data['expected']
    assert len(result) == 2


def test_read_csv_file_not_found():
    with patch('builtins.open', side_effect=FileNotFoundError()):
        result = read_transactions_from_csv('nonexistent_file.csv')
    
    assert result == []


def test_read_csv_error():
    with patch('builtins.open', mock_open(read_data="invalid,csv\n")):
        with patch('csv.DictReader', side_effect=csv.Error("CSV error")):
            result = read_transactions_from_csv('invalid_file.csv')
    
    assert result == []


def test_read_csv_general_exception():
    with patch('builtins.open', side_effect=Exception("Unexpected error")):
        result = read_transactions_from_csv('error_file.csv')
    
    assert result == []


def test_read_csv_empty_file():
    empty_content = "id,amount,currency\n"
    with patch('builtins.open', mock_open(read_data=empty_content)):
        result = read_transactions_from_csv('empty_file.csv')
    
    assert result == []


def test_read_csv_with_encoding():
    csv_content = "id,description\n1,Тест с русскими символами"
    
    with patch('builtins.open', mock_open(read_data=csv_content)) as mock_file:
        result = read_transactions_from_csv('test_utf8.csv')

    mock_file.assert_called_once_with('test_utf8.csv', 'r', encoding='utf-8')
    assert len(result) == 1
    assert result[0]['id'] == '1'


def test_csv_dict_reader_iteration():
    csv_content = "id,amount\n1,100\n2,200\n3,300"
    
    with patch('builtins.open', mock_open(read_data=csv_content)):
        result = read_transactions_from_csv('multi_row.csv')
    
    assert len(result) == 3
    assert result[0]['id'] == '1'
    assert result[1]['id'] == '2' 
    assert result[2]['id'] == '3'


# Тесты для Excel функции
@patch('pandas.read_excel')
def test_read_excel_success(mock_read_excel):
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [
        {'id': 1, 'amount': 100.50, 'currency': 'RUB'},
        {'id': 2, 'amount': 200.00, 'currency': 'USD'}
    ]
    mock_read_excel.return_value = mock_df
    
    result = read_transactions_from_excel('test_file.xlsx')
    
    assert len(result) == 2
    assert result[0]['id'] == 1
    mock_read_excel.assert_called_once_with('test_file.xlsx')


@patch('pandas.read_excel')
def test_read_excel_file_not_found(mock_read_excel):
    mock_read_excel.side_effect = FileNotFoundError()
    
    result = read_transactions_from_excel('nonexistent_file.xlsx')
    
    assert result == []


@patch('pandas.read_excel')
def test_read_excel_error(mock_read_excel):
    mock_read_excel.side_effect = Exception("Excel error")
    result = read_transactions_from_excel('error_file.xlsx')
    assert result == []


@patch('pandas.read_excel')
def test_read_excel_empty_data_error(mock_read_excel):
    mock_read_excel.side_effect = pd.errors.EmptyDataError()
    result = read_transactions_from_excel('empty_file.xlsx')
    assert result == []


@patch('pandas.read_excel')
def test_read_excel_empty_dataframe(mock_read_excel):
    mock_df = MagicMock()
    mock_df.to_dict.return_value = []  # Пустой список
    mock_read_excel.return_value = mock_df
    
    result = read_transactions_from_excel('empty_excel.xlsx')
    
    assert result == []
    mock_df.to_dict.assert_called_once_with('records')
