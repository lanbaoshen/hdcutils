from hdcutils._adb_mapping import adb_mapping
from hdcutils._device import HDCDevice
from hdcutils._hdc import HDC

__all__ = [
    'HDCClient',
    'adb_mapping',
]

_REFER_CHAIN = 'HDCClient()'
_DOC = 'https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hdc#'


class HDCClient(HDC):
    @adb_mapping(cmd='adb devices', refer_chain=_REFER_CHAIN, doc=_DOC)
    def list_targets(self, *, detail: bool = False) -> list[str]:
        """
        List all connected devices or emulators.

        Args:
            detail: If True, returns detailed information about each target.

        Returns:
            A list of strings, each representing a target device or emulator.
            If `detail` is True, each string contains detailed information.
        """
        cmd = ['list', 'targets']
        if detail:
            cmd.append('-v')
        out, _ = self.cmd(cmd, timeout=5)
        return out.splitlines()

    def device(self, connect_key: str = None) -> HDCDevice:
        return HDCDevice(connect_key=connect_key, hdc=self)
