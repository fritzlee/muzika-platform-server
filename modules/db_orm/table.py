BOARD_TYPE_LIST = (
    'community',
    'video',
    'sheet',
)

class Table:
    USERS = 'users'
    SIGN_MESSAGES = 'sign_messages'
    FILES = 'files'

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