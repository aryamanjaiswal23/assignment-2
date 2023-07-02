import os
import shutil


def organize_files(dir):
    file_counts = {}
    total_files_moved = 0

    for filename in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, filename)):
            file_extension = os.path.splitext(filename)[1][1:].lower()
            destination_folder = os.path.join(dir, file_extension)

            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            source_file = os.path.join(dir, filename)
            destination_file = os.path.join(destination_folder, filename)

            try:
                shutil.move(source_file, destination_file)
                total_files_moved += 1
                if file_extension in file_counts:
                    file_counts[file_extension] += 1
                else:
                    file_counts[file_extension] = 1
            except Exception as e:
                print(f"Error moving file '{filename}': {str(e)}")

    print("Files organized successfully!")
    print("Total files moved:", total_files_moved)
    print("File counts by extension:")
    for extension, count in file_counts.items():
        print(f"{extension}: {count} occurences")


dir = input("Enter the dir path: ")
organize_files(dir)


# if __name__ == "__main__":
#     main()
