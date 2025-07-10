from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hdcutils._device import HDCDevice


class ExtensionBase(ABC):
    def __init__(self, device: 'HDCDevice'):
        self._device = device

    @abstractmethod
    def cmd(self, cmd: list[str], timeout: int) -> tuple[str, str]:
        pass
