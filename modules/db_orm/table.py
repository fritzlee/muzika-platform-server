BOARD_TYPE_LIST = (
    'community',
    'video',
    'music',
)


class Table:
    USERS = 'users'
    SIGN_MESSAGES = 'sign_messages'
    FILES = 'files'
    MUSIC_FILES = 'music_files'
    MUSIC_FILES_PRIVATE = 'music_files_private'

    MUSIC_CONTRACTS = 'music_contracts'

    IPFS_FILES = 'ipfs_files'
    IPFS_FILES_PRIVATE = 'ipfs_files_private'

    @staticmethod
    def board(board_type):
        if board_type not in BOARD_TYPE_LIST:
            return None
        else:
            return '{}_board'.format(board_type)

    @staticmethod
    def comment(board_type):
        if board_type not in BOARD_TYPE_LIST:
            return None
        else:
            return '{}_comments'.format(board_type)

    @staticmethod
    def tags(board_type):
        if board_type not in BOARD_TYPE_LIST:
            return None
        else:
            return '{}_tags'.format(board_type)

    @staticmethod
    def like(board_type):
        if board_type not in BOARD_TYPE_LIST:
            return None
        else:
            return '{}_likes'.format(board_type)

    @staticmethod
    def comment_like(board_type):
        if board_type not in BOARD_TYPE_LIST:
            return None
        else:
            return '{}_comment_likes'.format(board_type)
