import difflib
from collections.abc import Callable
from typing import Any, TypeAlias

AnyFunction: TypeAlias = Callable[..., Any]


class ADBMapping:
    def __init__(self):
        self._mapping: dict[str, list[dict[str, str]]] = {}

    def __call__(self, cmd: str, refer_chain: str, desc: str = None, doc: str = None):
        if callable(cmd):
            raise TypeError(
                'The @adb_mapping decorator was used incorrectly. '
                'Did you forget to call it? Use @adb_mapping() instead of @adb_mapping'
            )

        def decorator(fn: AnyFunction) -> AnyFunction:
            info = {
                'example': f'{refer_chain}.{fn.__name__}',
            }
            if desc:
                info['desc'] = desc
            if doc:
                info['doc'] = doc
            self._mapping.setdefault(cmd, []).append(info)
            return fn

        return decorator

    def search_cmd(self, cmd: str) -> dict[str, list[dict[str, str]]] | str:
        """
        Search by an ADB command in the mapping.

        Args:
            cmd: ADB command

        Returns:
            A dictionary containing command information if found, otherwise None.
        """
        if closest_match := difflib.get_close_matches(cmd, self._mapping.keys(), n=1, cutoff=0.1):
            return {closest_match[0]: self._mapping[closest_match[0]]}
        return 'No match found, maybe you can use adb_mapping.mapping to check all commands.'

    @property
    def mapping(self) -> dict[str, Any]:
        """
        Get the full ADB command mapping.
        """
        return self._mapping


adb_mapping = ADBMapping()
