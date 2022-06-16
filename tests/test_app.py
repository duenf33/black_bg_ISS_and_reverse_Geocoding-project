import pytest

@pytest.mark.index
def test_index_page_load(client):
    res = client.get('/')
    assert res.status_code == 200

@pytest.mark.index
def test_index_address_post(client):

    res = client.post('/get_coor', 
        data=dict(address="630 Ninth Ave, Unit 901, New York, NY 10036"),
        follow_redirects=True
    )

    assert res.status_code == 200
    assert b'630 Ninth Ave, Unit 901, New York, NY 10036' in res.data