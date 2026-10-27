string_to_process = "   sMitH, aLeX    "

string_to_process = string_to_process.lstrip()
list_to_process = string_to_process.split(",")
string_to_process = list_to_process[1] + list_to_process[0]
string_to_process = string_to_process.strip()
string_to_process = string_to_process.title()
list_to_process = string_to_process.split("   ")
string_to_process = "".join(list_to_process)

print(string_to_process)
# Expected output: "Alex Smith"