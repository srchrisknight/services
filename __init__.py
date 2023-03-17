from .common.utils import detect_dcc

dcc_environment = detect_dcc()

if dcc_environment == "nuke":
    from .nuke import *
elif dcc_environment == "maya":
    from .maya import *
elif dcc_environment == "houdini":
    from .houdini import *
elif dcc_environment == "os_windows":
    from .os_windows import *
elif dcc_environment == "os_linux":
    from .os_linux import *
else:
    raise ImportError("DCC environment or OS not supported.")