import subprocess


def run_apt_up():
    try:
        subprocess.run(["pip3", "install", "image"], check=True)
        subprocess.run(["pip3", "install", "piexif"], check=True)
        subprocess.run(["pip3", "install", "os"], check=True)
        subprocess.run(["pip3", "install", "Pillow"], check=True)
        subprocess.run(["pip3", "install", "termcolor"], check=True)
        subprocess.run(["sudo", "apt", "update"], check=True)
        print("Installed!")
    except subprocess.CalledProcessError:
        print("Error!")

if __name__ == "__main__":
    run_apt_up()
