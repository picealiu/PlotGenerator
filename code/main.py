#!/usr/bin/env python
# coding: utf-8

# Necessary Packages
from utils import get_user_input
from plot_FTIR import user_input_FTIR
from imageJ_tool import image_processing


def main():
    while True:
        print("Welcome to the Image Processer!")

        # Ask the user which function they want to use
        print("\nOptions:\n1. Generate FTIR Plot")
        print("2. Use ImageJ")
        print("3. Exit.")

        choice = get_user_input("Enter the number of the function "
                                "you want to use: ", int)

        if choice == 1:          # FTIR PLOT Function
            user_input_FTIR()
        elif choice == 2:
            image_processing()  # Image J color change
        elif choice == 3:
            break


if __name__ == "__main__":
    main()
