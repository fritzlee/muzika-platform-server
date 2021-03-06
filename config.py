"""
# Config.py

 Global constants for server configuration.
"""
import os


class AppConfig:
    """
    Global constants for Web backend server.
    """
    host = 'localhost'
    port = 7001
    timezone = 'UTC'
    issuer = 'https://muzika.network'

    # request that the content length is over it will be rejected
    max_content_length = 1024 * 1024 * 3    # 3 MB


class IPFSConfig:
    """
    Global constants for IPFS configuration.

    The server's IPFS must support websocket address. For supporting websocket address Edit IPFS config
    (the file path may be ~/.ipfs/config).
    reference : https://github.com/ipfs/js-ipfs/tree/master/examples/circuit-relaying
    """
    node_address = '127.0.0.1'
    port = 5001


class Web3ProviderConfig:
    """
    Global constants for web3 provider for interacting with ethereum block chain.
    """
    endpoint_url = {
        'production': 'https://mainnet.infura.io/' + os.environ.get('INFURA_API_KEY', ''),
        'stage': 'https://ropsten.infura.io/' + os.environ.get('INFURA_API_KEY', '')
    }.get(os.environ.get('ENV', 'dev'), 'http://localhost:8545')

    timeout = 5


class MuzikaContractConfig:
    """
    Global constants for Muzika contracts.
    """
    build_path = './muzika-contract/build/contracts'

    # The registered transactions are removed from the database if they are not mined over specific time.
    # @TODO Set long period on test/main network
    update_period = 10


class SignMessageConfig:
    """
    Global constants for sign message
    """
    unsigned_message_expired_time = 300  # 5 minute
    signed_message_expired_time = 24 * 60 * 60  # 1 day


class CacheConfig:
    """
    Global constants for redis
    """
    cache_type = 'redis' if os.environ.get('ENV') in ['production', 'stage'] else 'local'
    host = 'localhost'
    port = 6379  # ignored if local cache
    key_prefix = 'muzika-redis-cache'
