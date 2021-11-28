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
    params = {'start': start, 'limit': limit}

    response = await test_app.get(f'/employees', params=params)
    response_data = response.json()

    assert response.status_code == expected
    assert isinstance(response_data, list)
    assert len(response_data) == limit


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'test_input, expected',
    [
        ((60, 63), 200),
        ((50, 100), 200),
        ((0, 1), 200),
    ],
)
async def test_travel_get_filter_age(test_app, test_input, expected):

    start, end = test_input

    params = {'start_age': start, 'end_age': end}
    response = await test_app.get(f'/employees', params=params)
    response_data = response.json()

    assert response.status_code == expected
    assert isinstance(response_data, list)
    assert all(start <= user['age'] <= end for user in response_data)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'test_input, expected',
    [
        ((1000, 2500), 200),
        ((3400, 9000), 200),
        ((100, 999), 200),
    ],
)
async def test_travel_get_filter_salary(test_app, test_input, expected):

    start, end = test_input

    params = {'start_salary': start, 'end_salary': end}
    response = await test_app.get(f'/employees', params=params)
    response_data = response.json()

    assert response.status_code == expected
    assert isinstance(response_data, list)
    assert all(start <= user['salary'] <= end for user in response_data)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'test_input, expected',
    [
        (('2012-12-29T03:00:10', '2018-12-29T03:00:10'), 200),
        (('2000-12-29T03:00:10', '2005-12-29T03:00:10'), 200),
    ],
)
async def test_travel_get_filter_join_date(test_app, test_input, expected):

    start, end = test_input

    params = {'start_join_date': start, 'end_join_date': end}
    response = await test_app.get(f'/employees', params=params)
    response_data = response.json()

    assert response.status_code == expected
    assert isinstance(response_data, list)
    assert all(start <= user['join_date'] <= end for user in response_data)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'test_input, expected',
    [
        ((['Twitter', 'Yandex']), 200),
        ((['Twitter']), 200),
        ((['Amazon']), 200),
    ],
)
async def test_travel_get_filter_company(test_app, test_input, expected):

    list_of_companies = test_input

    params = {'company': list_of_companies}
    response = await test_app.get(f'/employees', params=params)
    response_data = response.json()

    assert response.status_code == expected
    assert isinstance(response_data, list)
    assert all(user['company'] in list_of_companies for user in response_data)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'test_input, expected',
    [
        ((['janitor', 'manager']), 200),
        ((['manager']), 200)
    ],
)
async def test_travel_get_filter_job_title(test_app, test_input, expected):

    list_of_companies = test_input

    params = {'job_title': list_of_companies}
    response = await test_app.get(f'/employees', params=params)
    response_data = response.json()

    assert response.status_code == expected
    assert isinstance(response_data, list)
    assert all(user['job_title'] in list_of_companies for user in response_data)