# my-first-repo
# ============================================
# PYTHON BASICS: Variables & Data Types
# ============================================

print("=" * 50)
print("📚 PYTHON VARIABLES & DATA TYPES")
print("=" * 50)

# ---------- INTEGER (int) ----------
print("\n1️⃣ INTEGER (int) - Whole Numbers")
age = 25
score = 100
temperature = -5
print(f"Age: {age} (Type: {type(age)})")
print(f"Score: {score} (Type: {type(score)})")

# ---------- FLOAT (float) ----------
print("\n2️⃣ FLOAT (float) - Decimal Numbers")
price = 19.99
pi = 3.14159
percentage = 75.5
print(f"Price: {price} (Type: {type(price)})")
print(f"PI: {pi} (Type: {type(pi)})")

# ---------- STRING (str) ----------
print("\n3️⃣ STRING (str) - Text")
name = "Rahul Kumar"
city = 'Delhi'
multi_line = """This is a
multi-line string"""
print(f"Name: {name} (Type: {type(name)})")
print(f"City: {city} (Type: {type(city)})")

# ---------- BOOLEAN (bool) ----------
print("\n4️⃣ BOOLEAN (bool) - True/False")
is_student = True
has_license = False
print(f"Is Student: {is_student} (Type: {type(is_student)})")
print(f"Has License: {has_license} (Type: {type(has_license)})")

# ---------- TYPE CONVERSION ----------
print("\n5️⃣ TYPE CONVERSION (Type Casting)")
num_str = "123"
num_int = int(num_str)  # String to Integer
num_float = float(num_str)  # String to Float
str_num = str(100)  # Integer to String
print(f"String to Integer: {num_int} (Type: {type(num_int)})")
print(f"String to Float: {num_float} (Type: {type(num_float)})")
print(f"Integer to String: {str_num} (Type: {type(str_num)})")
