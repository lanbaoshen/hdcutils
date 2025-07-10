# HDC Utils
Pure python hdc library for harmony hdc service.

**Support querying corresponding hdc commands and documentation via adb command.**

<img width="1135" alt="Screenshot 2025-07-09 at 17 02 36" src="https://github.com/user-attachments/assets/8eac7cf2-8e20-490e-ad47-9c1ec388bdf3" />

## Requires
- Python 3.11+
- [hdc](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hdc#environment-setup)

<details>
<summary>Install hdc without DevEco Studio</summary>

1. Find `command-line-tools` in [Download Center](https://developer.huawei.com/consumer/en/download/), and choose a release version to download.
If the path is zh, you need to log in to your Huawei account first.
2. Unzip the downloaded file to a directory, e.g `~/Library/Harmony/command-line-tools`
3. Set environment variable like:
```shell
export HARMONY_HOME=~/Library/Harmony
export PATH=${HARMONY_HOME}/command-line-tools/bin:${HARMONY_HOME}/command-line-tools/sdk/default/openharmony/toolchains:${PATH}
```
4. Run `hdc` command to check if it works:
```shell
hdc checkserver
# Client version:Ver: 3.1.0e, server version:Ver: 3.1.0e
```

</details>

## Install

```shell
pip3 install hdcutils
```

## Usage

### Search method & doc via adb command
```python
from hdcutils import adb_mapping
result = adb_mapping.search_cmd(cmd='adb logcat -c')
print(result['example'])  # HDCClient().device().hilog.remove_buffer_log
print(result['doc'])  # https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hilog#clearing-the-log-buffer

# Print full mapping
print(adb_mapping.mapping)
```

### List all the devices and get device object
```python
from hdcutils import HDCClient

# hdc = HDCClient(hdc='/path/to/hdc')
# If you don't set `hdc` path, it will try to find it in $PATH.
hdc = HDCClient()
for target in hdc.list_targets():
    d = hdc.device(connect_key=target)
```

### Run shell command
```python
from hdcutils import HDCClient
hdc = HDCClient()
# d = hdc.device(connect_key='device_connect_key')
# If you only have one device, you can use `hdc.device()` without arguments.
d = hdc.device()
out, err = d.shell(['echo', 'Hello World!'])
print(out)
```

## License
Licensed under MIT - see [LICENSE](LICENSE) file. This is not an official Harmony product.
