from ownercheck.db import generate_code, get_code, remove_code

TEST_DOMAIN = 'google.com'

def test_generate_code():
    assert generate_code(TEST_DOMAIN, 'TXT') != None
    assert generate_code(TEST_DOMAIN, 'TXT') != generate_code(
        TEST_DOMAIN, 'CNAME')
    assert generate_code(TEST_DOMAIN, 'TXT') == generate_code(
        TEST_DOMAIN, 'TXT')


def test_get_code():
    code = generate_code(TEST_DOMAIN, 'FILE')
    assert get_code(TEST_DOMAIN, 'FILE') == code
    assert get_code(TEST_DOMAIN, 'METATAG') == None


def test_remove_code():
    file_code = generate_code(TEST_DOMAIN, 'FILE')
    cname_code = generate_code(TEST_DOMAIN, 'CNAME')
    remove_code(TEST_DOMAIN, 'FILE')
    new_file_code = generate_code(TEST_DOMAIN, 'FILE')
    new_cname_code = generate_code(TEST_DOMAIN, 'CNAME')
    assert file_code != new_file_code
    assert cname_code == new_cname_code