import pytest


@pytest.mark.api
def test_user_exist(github_api):
    user = github_api.get_user('vanpelt')
    assert user['login'] == 'vanpelt'


@pytest.mark.api
def test_user_not_exist(github_api):
    r = github_api.get_user('soikoroman')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 30
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('soikoroman_repo_non_exist')
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0