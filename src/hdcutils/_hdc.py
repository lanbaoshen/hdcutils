import os
import platform
import subprocess
from pathlib import Path
from shutil import which
from tempfile import SpooledTemporaryFile

from loguru import logger


class HDC:
    def __init__(self, hdc: str | Path = None):
        self._hdc = hdc or which('hdc')
        if not self._hdc:
            raise FileNotFoundError('No HDC provided, and not configured in $PATH')

        if not os.access(self._hdc, os.X_OK):
            raise PermissionError(f'"{self._hdc}" is not executable')

        logger.debug(f'HDC initialized with path: {self._hdc}')

    def cmd(self, cmd: list[str], timeout: float | int = 5 * 60, *, redirect: bool = False) -> tuple[str, str]:
        close_fds = False if platform.system() == 'Darwin' else True

        if redirect:
            temp = SpooledTemporaryFile(max_size=1024 * 10)
            file_no = temp.fileno()
            output_kwargs = {'stdout': file_no, 'stderr': file_no}
        else:
            output_kwargs = {'stdout': subprocess.PIPE, 'stderr': subprocess.STDOUT}

        cmd = [self._hdc] + cmd
        logger.debug(f'Executing command: {cmd}')

        proc = subprocess.run(
            cmd, text=True, errors='replace', close_fds=close_fds, timeout=timeout, check=True, **output_kwargs
        )
        out = proc.stdout.strip() if proc.stdout else ''
        err = proc.stderr.strip() if proc.stderr else ''

        return out, err
