# Входит в репозиторий, а локал конфиг не будет входить
TOKEN = None

try:
    from .local_config import *
except ImportError:
    pass
