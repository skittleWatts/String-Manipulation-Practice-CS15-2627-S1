string_to_process = "eggs,cheese,milk,bread,cereal"

string_to_process = string_to_process.replace(",", " | ")
string_to_process= string_to_process.upper()

print(string_to_process)
# Expected Output: "EGGS | CHEESE | MILK | BREAD | CEREAL"