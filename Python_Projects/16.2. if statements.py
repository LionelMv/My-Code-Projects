is_Male = False
is_Tall = False
if is_Male or is_Tall:
    print("You are either male or tall or both")
else:
    print("You are neither male or tall")

if is_Male and is_Tall:
    print("You are a tall male")
elif is_Male and not(is_Tall):
    print("You are a male but not tall")
elif not(is_Male) and is_Tall:
    print("You are tall but not male")
else:
    print("You are neither male or tall")