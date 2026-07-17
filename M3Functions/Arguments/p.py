import os

def shutdown_computer():
    # 'shutdown /s /t 1' means:
    # /s : Shutdown
    # /t 1 : Time delay of 1 second
    os.system("shutdown /s /t 1")

# Call the function to test it
# WARNING: Save all your work before running this!
shutdown_computer()