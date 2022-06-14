class KVDBError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__('ERROR => ' + msg)

class NoCommandProvidedError(KVDBError):
    def __init__(self) -> None:
        super().__init__(f'Command must be provided in request payload')

class NoParamsProvidedError(KVDBError):
    def __init__(self) -> None:
        super().__init__(f'Parameters must be provided in request payload')
        
class NoTemplateProvidedError(KVDBError):
    def __init__(self) -> None:
        super().__init__(f'request template must be provided in request payload')

class NoCommandError(KVDBError):
    def __init__(self, cmd: str) -> None:
        super().__init__(f'Unknown command {cmd}')
class NoCommandTemplateError(KVDBError):
    def __init__(self, cmd: str) -> None:
        super().__init__(f'Unknown command template {cmd}')
        
class NotMatchWithTemplateError(KVDBError):
    def __init__(self, cmd: str, template:str) -> None:
        super().__init__(f'the command {cmd} is not math with template {template}')
class BadArityError(KVDBError):
    def __init__(self, cmd: str, given: int, expected: int) -> None:
        super().__init__(f'Wrong number of arguments to command {cmd} ({given} given, expected {expected})')

class ConnError(KVDBError):
    def __init__(self, host: str, port: int) -> None:
        super().__init__(f'Unable to connect to {host} on port {port}')