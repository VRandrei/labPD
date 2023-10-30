import os


def find_directories_recursive(start_directory, target_directory_name_):
    found_directories = []

    for root, dirs, files in os.walk(start_directory):
        if target_directory_name_ in dirs:
            found_directories.append(os.path.join(root, target_directory_name_))

    return found_directories


project_directory = '../lab2/dataset'
target_directory_name = 'tiger'

results = find_directories_recursive(project_directory, target_directory_name)

if results:
    print(f"Найдены директории '{target_directory_name}':")
    for result in results:
        print(result)
else:
    print(f"Директории '{target_directory_name}' не найдены в проекте.")