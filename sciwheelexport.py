"""User facing entry-point for sciwheel-export for those not using
PyPi.
"""

from src.export import sciwheelexport


def main():
    """Primary entry point for this script."""
    sciwheelexport.main()


if __name__ == "__main__":
    main()
