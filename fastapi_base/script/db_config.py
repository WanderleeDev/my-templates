import sys
import os
import subprocess
import importlib.util

db_packages = {1: "psycopg2", 2: "aiomysql", 3: "aiosqlite"}


def config_db() -> None:
    declare_envs()
    # install_driver()


def install_driver():
    print(f"Select the database type:")
    print(f"1. PostgreSQL")
    print(f"2. MySQL")
    print(f"3. SQLite")
    print(f"4. Exit")

    while True:
        db_type = safe_input_int()

        if db_type == 4:
            exit_program()
            break

        if db_type not in db_packages:
            print(f"{db_type} Invalid option")
            continue

        try:
            pkg = validate_package(db_type)

            print(pkg)

            print(f"Configuring {db_packages[db_type]}...")
            subprocess.run(["uv", "add", pkg], check=True)
        except subprocess.CalledProcessError:
            print(f"Error installing {pkg}. Make sure UV is set up correctly.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            exit_program()


def declare_envs():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(current_dir, "..", ".env")

    print(env_path)

    if not os.path.isfile(env_path):
        print("Renombra el archivo .env.example a .env para usar las variables base")
        return

    with open(env_path, "r") as file:
        lines = file.readlines()

    print(lines)
    # for line in file:
    #     if line.startswith("DATABASE_URI"):
    # file.write('DDDDDDD="YOUR DATABASE URI"')


def safe_input_int() -> int:
    """Safe input for integer values."""
    while True:
        try:
            return int(input("\nEnter the number of the database type: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def validate_package(pkg_key: int) -> str:
    """Validate the package key and check if it exists."""
    pkg = db_packages.get(pkg_key)

    if pkg is None:
        raise ValueError(f"Package not found")

    if importlib.util.find_spec(pkg) is not None:
        raise RuntimeError(f"Package {pkg} already exists")

    return pkg


def declare_env() -> None:
    """Declare environment variables."""
    if not os.path.exists(".env"):
        print("Creating .env file")
        with open(".env", "w") as file:
            file.write('DATABASE_URI="YOUR DATABASE URI"')
    else:
        print(".env file already exists")


def exit_program() -> None:
    """Exit the program."""
    print(f"Exiting...")
    sys.exit()


if __name__ == "__main__":
    config_db()
