# ============================================
# PYTHON BASICS: Variables & Data Types
# ============================================

print("=" * 40)
print("PYTHON VARIABLES & DATA TYPES")
print("=" * 40)

# ---------- INTEGER (int) ----------
print("\n1. INTEGER (Whole Numbers)")

age = 25
score = 100
temperature = -5

print("Age:", age)
print("Score:", score)
print("Temperature:", temperature)
print("Type of age:", type(age))

# ---------- FLOAT (float) ----------
print("\n2. FLOAT (Decimal Numbers)")

price = 19.99
pi = 3.14
percentage = 75.5

print("Price:", price)
print("PI:", pi)
print("Percentage:", percentage)
print("Type of price:", type(price))

# ---------- STRING (str) ----------
print("\n3. STRING (Text)")

name = "Rahul"
city = "Delhi"
message = "Hello World"

print("Name:", name)
print("City:", city)
print("Message:", message)
print("Type of name:", type(name))

# ---------- BOOLEAN (bool) ----------
print("\n4. BOOLEAN (True/False)")

is_student = True
has_license = False

print("Is Student:", is_student)
print("Has License:", has_license)
print("Type of is_student:", type(is_student))

# ---------- TYPE CONVERSION ----------
print("\n5. TYPE CONVERSION (Changing Types)")

num_str = "123"
num_int = int(num_str)
num_float = float(num_str)
str_num = str(100)

print("String to Integer:", num_int)
print("String to Float:", num_float)
print("Integer to String:", str_num)

print("\n" + "=" * 40)
print("CODE FINISHED!")
