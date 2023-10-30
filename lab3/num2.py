import csv
import os
import shutil

def copy_and_rename_dataset(src_dataset_path, dest_dataset_path):
    os.makedirs(dest_dataset_path, exist_ok=True)

    annotation_file = 'annotation.csv'
    annotation_path = os.path.join(dest_dataset_path, annotation_file)

    new_data_list = []

    for root, dirs, files in os.walk(src_dataset_path):
        for file in files:
            relative_path = os.path.join(root, file)
            class_label = os.path.basename(root)
            new_file_name = f'{class_label}_{file}'

            rel_path = os.path.join(dest_dataset_path, new_file_name)
            abs_path = os.path.join(os.getcwd(), rel_path)

            new_data_list.append([abs_path, rel_path, class_label])

            shutil.copy(relative_path, rel_path)

    with open(annotation_path, mode='w', newline='') as annotation_csv:
        annotation_writer = csv.writer(annotation_csv)
        annotation_writer.writerow(['Absolute Path', 'Relative Path', 'Class Label'])
        annotation_writer.writerows(new_data_list)

    print(f"Файл-аннотация {annotation_file} успешно создан.")


src_dataset_path = '../lab2/dataset'
dest_dataset_path = 'new_dataset'

copy_and_rename_dataset(src_dataset_path, dest_dataset_path)
