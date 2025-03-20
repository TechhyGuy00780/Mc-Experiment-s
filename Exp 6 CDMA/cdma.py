import numpy as np

# Define Walsh codes
c1 = [1, 1, 1, 1]
c2 = [1, -1, 1, -1]
c3 = [1, 1, -1, -1]
c4 = [1, -1, -1, 1]

# Dictionary to store codes
codes = {1: c1, 2: c2, 3: c3, 4: c4}

# Get user input for data bits
print("Enter the data bits:")
d1 = int(input("Enter D1: "))
d2 = int(input("Enter D2: "))
d3 = int(input("Enter D3: "))
d4 = int(input("Enter D4: "))

# Encode the data using Walsh codes
r1 = np.multiply(c1, d1)
r2 = np.multiply(c2, d2)
r3 = np.multiply(c3, d3)
r4 = np.multiply(c4, d4)

# Sum all signals to create the transmitted signal
resultant_channel = r1 + r2 + r3 + r4
print("\nResultant Channel:", resultant_channel)

# Select a channel to decode
channel = int(input("\nEnter the station to listen for C1=1, C2=2, C3=3, C4=4: "))

if channel in codes:
    rc = codes[channel]
    
    # Decode the signal using the selected Walsh code
    inner_product = np.multiply(resultant_channel, rc)
    print("\nInner Product:", inner_product)

    # Compute the original data bit
    res1 = sum(inner_product)
    decoded_bit = res1 / len(inner_product)

    print("Data bit that was sent:", decoded_bit)
else:
    print("Invalid channel selection. Please enter a number between 1 and 4.")
