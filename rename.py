import os

def replace_text_in_files(directory):
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)

            # Read the content of the file
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            # Replace the text
            new_content = content.replace("MUN_LOF33", "Monkey D. Luffy")
            # Write the modified content back to the file
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(new_content)

            print(f"Processed: {filename}")


replace_text_in_files("luffy_dataset_4")