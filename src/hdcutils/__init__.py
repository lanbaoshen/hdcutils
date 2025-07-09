from hdcutils._device import HDCDevice
from hdcutils._hdc import HDC

__all__ = [
    'HDCDevice',
    'HDCClient',
]


class HDCClient(HDC):
    def list_targets(self, *, detail: bool = False) -> list[str]:
        cmd = ['list', 'targets']
        if detail:
            cmd.append('-v')
        out, _ = self.cmd(cmd, timeout=5)
        return out.splitlines()

    def device(self, connect_key: str = None) -> HDCDevice:
        return HDCDevice(connect_key=connect_key, hdc=self)
