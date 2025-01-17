import pytest

from scr.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data() -> list[dict[str, str]]:
    return [
        {"state": "EXECUTED", "date": "2022-01-01"},
        {"state": "EXECUTED", "date": "2022-03-01"},
        {"state": "CANCELLED", "date": "2022-04-01"},
    ]


@pytest.mark.parametrize("state, expected_result", [
    ("EXECUTED", [
        {"state": "EXECUTED", "date": "2022-01-01"},
        {"state": "EXECUTED", "date": "2022-03-01"},
    ]),
    ("CANCELLED", [
        {"state": "CANCELLED", "date": "2022-04-01"},
    ]),
])
def test_filter_by_state(sample_data, state, expected_result):
    assert filter_by_state(sample_data, state) == expected_result


@pytest.mark.parametrize(
    "reverse, expected_result",
    [
        (
                True,
                [
                    {"state": "CANCELLED", "date": "2022-04-01"},
                    {"state": "EXECUTED", "date": "2022-03-01"},
                    {"state": "EXECUTED", "date": "2022-01-01"},
                ],
        ),
        (
                False,
                [
                    {"state": "EXECUTED", "date": "2022-01-01"},
                    {"state": "EXECUTED", "date": "2022-03-01"},
                    {"state": "CANCELLED", "date": "2022-04-01"},
                ],
        ),
    ],
)
def test_sort_by_date(sample_data: list, reverse: bool, expected_result: list[dict[str, str]]) -> None:
    assert sort_by_date(sample_data, reverse) == expected_result
