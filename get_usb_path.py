import subprocess

def get_usb_path():
    output = subprocess.check_output(["lsblk", "-o", "NAME,MOUNTPOINT"]).decode()
    lines = output.strip().split("\n")[1:]
    for line in lines:
        parts = line.split()
        if len(parts) == 2 and parts[1].startswith("/media"):
            return parts[1]
    return None
