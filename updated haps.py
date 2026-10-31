import math

print("===HAPS Channel Quality Analyzer===")
distance = float(input("enter distance(km): "))
elevation = float(input("enter elevation angle: "))
frequency = float(input("enter frequency(Mhz): "))

if distance <= 0 or frequency <= 0 or not (0 <= elevation <= 90):
    print("invalid input! Check your values.")
else:
    # Corrected Free-Space Path Loss Formula (FSPL) using addition (+)
    path_loss = 32.44 + 20 * math.log10(distance) + 20 * math.log10(frequency)

    # Metric calculations
    distance_score = max(0, 100 - distance * 1.5)
    elevation_score = max(0, 100 - abs(elevation - 45) * 2)  # Fixed to use elevation
    frequency_score = max(0, 100 - abs(frequency - 29000) * 0.002)
    
    score = (distance_score + elevation_score + frequency_score) / 3

    if score >= 80:
        quality = "Good"
    elif score >= 60:
        quality = "moderate"
    else:
        quality = "poor"

    print("\n---Analysis Report---\n")
    print(f"Path loss: {path_loss:.2f} dB")
    print(f"Elevation score: {elevation_score:.1f}")
    print(f"Overall score: {score:.1f}%")
    print(f"Channel Quality: {quality}")

    if quality == "poor":
        print("suggestion: Review distance and link conditions.")
    elif quality == "moderate":
        print("suggestion: Further optimize link parameters.")
    else:
        print("suggestion: Conditions are favorable in this model.")