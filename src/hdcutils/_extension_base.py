from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hdcutils._device import HDCDevice


class ExtensionBase:
    def __init__(self, device: 'HDCDevice'):
        self._device = device
