# This is a simple Python script for controlling high current relay with
# Nordpool electricity price data.

# UNDER ACTIVE DEVELOPMENT

# Author @mrMikoma

# Thanks to
# - https://github.com/kipe/nordpool


"""
Improvement ideas:
- DO ALL :)
-
"""
import nordPoolAPI


# APPLICATION


# MAIN
if __name__ == '__main__':
    # Starting program
    print(f'\nHi, this is a really simple application for controlling high current relay '
          + f'with Nordpool electricity price data\n')

    # Running program
    nordPoolAPI.getNordPoolPrices()

    # Ending program
    print(f'\nThank you for using this program! :)')

# eof