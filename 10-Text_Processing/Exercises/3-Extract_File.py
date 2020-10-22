file_path = input().split("\\")
file_name = file_path[-1].split(".")

print(f"""
File name: {file_name[0]}
File extension: {file_name[1]}
""")