import math

# Angle in degrees
degrees = 45

# The math functions expect radians, so we convert degrees to radians first
radians = math.radians(degrees)

# Calculating trigonometric values
sin_val = math.sin(radians)
cos_val = math.cos(radians)
tan_val = math.tan(radians)

print(f"Trigonometric values for {degrees} degrees:")
print(f"Sine: {sin_val:.4f}")
print(f"Cosine: {cos_val:.4f}")
print(f"Tangent: {tan_val:.4f}")