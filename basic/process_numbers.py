string_to_process = "  18,27,35,20  "

string_to_process = string_to_process.strip()
list_to_process = string_to_process.split(",")

total = 0
for item in list_to_process:
    total = total + int(item)

avg = total / len(list_to_process)

print(f"Total: {total}")
print(f"Average: {avg}")
# Expected Output:
# "Total: 100"
# "Average: 25.0"