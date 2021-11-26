import pytest


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'test_input, expected',
    [
        ((0, 10), 200),
        ((0, 2), 200),
        ((100, 200), 200),
    ],
)
async def test_travel_get(test_app, test_input, expected):

    start, limit = test_input

    response = await test_app.get(f'/employees?start={start}&limit={limit}')
    response_data = response.json()

    assert response.status_code == expected
    assert type(response_data) == list
    assert len(response_data) == limit