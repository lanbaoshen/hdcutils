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

    @adb_mapping(cmd='adb start-server', refer_chain=_REFER_CHAIN, doc=_DOC)
    def start(self, *, restart: bool = False) -> tuple[str, str]:
        """
        Start the HDC Server.

        Args:
            restart: If True, restarts the HDC server if it is already running.

        Returns:
            stdout, stderr
        """
        cmd = ['start']
        if restart:
            cmd.append('-r')
        return self.cmd(cmd, timeout=10)

    @adb_mapping(cmd='adb kill-server', refer_chain=_REFER_CHAIN, doc=_DOC)
    def kill(self, *, restart: bool = False) -> tuple[str, str]:
        """
        Kill the HDC Server.

        Args:
            restart: If True, restarts the HDC server after killing it.

        Returns:
            stdout, stderr
        """
        cmd = ['kill']
        if restart:
            cmd.append('-r')
        return self.cmd(cmd, timeout=10)

    def device(self, connect_key: str = None) -> HDCDevice:
        """
        Create a device object for the specified connect key.

        Args:
            connect_key: The connect key of the device to connect to.

        Returns:
            HDCDevice: An instance of HDCDevice connected to the specified device.
        """
        return HDCDevice(connect_key=connect_key, hdc=self)
