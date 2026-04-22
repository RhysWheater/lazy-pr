import subprocess

def main():
    print("Hello from lazy-pr!")
    subprocess.call(["vim", "README.md"])
    print("exited vim back into python")

if __name__ == "__main__":
    main()
