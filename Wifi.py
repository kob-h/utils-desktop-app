import subprocess


def connect_to_wifi(ssid, password):
    # Create the network setup command
    command = f"networksetup -setairportnetwork en0 {ssid} {password}"

    try:
        # Execute the command
        #some additional comment
        res = subprocess.run(command, shell=True, check=True)
        print(f"Connected to {ssid} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to connect to {ssid}: {e}")


# Replace 'Your_SSID' with the name of the WiFi network you want to connect to
# Replace 'Your_Password' with the password for the WiFi network
passes = ['301751651', '301751651', '301751651', '301751657']
for passs in passes:
    connect_to_wifi('Kobi', passs)
