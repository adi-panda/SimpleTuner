import os


def append_text_to_files(directory, text_to_append):
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)

            # Read the original content
            with open(file_path, "r", encoding="utf-8") as file:
                original_content = file.read()

            # Write the new content with the appended text
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text_to_append + original_content)

    print("Text appended to all .txt files in the directory.")


def remove_appended_text(directory, text_to_remove):
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)

            # Read the content
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            # Remove the appended text if it exists at the beginning
            if content.startswith(text_to_remove):
                new_content = content[len(text_to_remove) :]

                # Write the new content without the appended text
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(new_content)

    print("Text removed from all .txt files in the directory.")


# Usage
directory_path = (
    "GOJO_FULL_CROP"  # Replace with your actual directory path
)
text_to_append = "A scene from Jujutsu Kaisen. "

append_text_to_files(directory_path, text_to_append)
