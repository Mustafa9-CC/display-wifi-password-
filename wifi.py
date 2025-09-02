import subprocess

# Get all Wi-Fi profiles
data = (
    subprocess.check_output(["netsh", "wlan", "show", "profiles"])
    .decode("utf-8", errors="ignore")
    .split("\n")
)

profiles = [i.split(":")[1].strip() for i in data if "All User Profile" in i]

# Extract passwords
for i in profiles:
    results = (
        subprocess
        .check_output(["netsh", "wlan", "show", "profile", i, "key=clear"])
        .decode("utf-8", errors="ignore")
        .split("\n")
    )
    results = [b.split(":")[1].strip() for b in results if "Key Content" in b]
    try:
        print("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30}|  {:<}".format(i, ""))
