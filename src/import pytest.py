import pytest
from algokit_utils.testing import (
    AlgorandTest,
    get_account,
    get_app_id
)

@pytest.fixture
def birth_registry_app(algorand_test: AlgorandTest):
    """Fixture to deploy the application for each test."""
    app_id, app_address = algorand_test.deploy(
        'contracts/BirthRegistry.py',
        'contracts/BirthRegistry.py'
    )
    return app_id, app_address

def test_register_new_birth(algorand_test: AlgorandTest, birth_registry_app):
    """Test that a new birth can be registered successfully."""
    app_id, app_address = birth_registry_app
    creator = algorand_test.get_funded_account()
    
    did = b'did:example:12345'
    data_hash = b'some_data_hash'

 
    algorand_test.call_app(
        app_id,
        sender=creator,
        args=[b'register_birth', did, data_hash],
    )
    
  
    app_state = algorand_test.get_application_state(app_id)
    
    assert app_state.get(did) == data_hash
    
def test_register_duplicate_birth_fails(algorand_test: AlgorandTest, birth_registry_app):
    """Test that registering a duplicate birth fails."""
    app_id, app_address = birth_registry_app
    creator = algorand_test.get_funded_account()
    
    did = b'did:example:67890'
    data_hash = b'first_data_hash'
    
   
    algorand_test.call_app(
        app_id,
        sender=creator,
        args=[b'register_birth', did, data_hash],
    )

    with pytest.raises(Exception):
        algorand_test.call_app(
            app_id,
            sender=creator,
            args=[b'register_birth', did, b'second_data_hash']
        )