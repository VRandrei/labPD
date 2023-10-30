import os
import random
import shutil
import csv

def copy_dataset_with_random_numbers(src_dataset_path, dest_dataset_path):
    os.makedirs(dest_dataset_path, exist_ok=True)

    annotation_file = 'annotation.csv'
    annotation_path = os.path.join(dest_dataset_path, annotation_file)

    new_data_list = []

    for root, dirs, files in os.walk(src_dataset_path):
        for file in files:
            class_label = os.path.basename(root)
            random_number = random.randint(0, 10000)
            new_file_name = f'{random_number}.jpg'

            rel_path = os.path.join(dest_dataset_path, new_file_name)
            abs_path = os.path.join(os.getcwd(), rel_path)

            new_data_list.append([abs_path, rel_path, class_label])

            src_file_path = os.path.join(root, file)
            dest_file_path = os.path.join(dest_dataset_path, new_file_name)

            shutil.copy(src_file_path, dest_file_path)

    with open(annotation_path, mode='w', newline='') as annotation_csv:
        annotation_writer = csv.writer(annotation_csv)
        annotation_writer.writerow(['Absolute Path', 'Relative Path', 'Class Label'])
        annotation_writer.writerows(new_data_list)

    print(f"Файл-аннотация {annotation_file} успешно создан.")


src_dataset_path = '../lab2/dataset'
dest_dataset_path = 'random_dataset'

copy_dataset_with_random_numbers(src_dataset_path, dest_dataset_path)
