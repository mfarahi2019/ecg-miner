# Standard library imports

import os
import cv2
import csv
import matplotlib.pyplot as plt


def sort_filenames_by_number(directory):
    filenames = os.listdir(directory)

    def sort_by_number(filename):
        number = int("".join(filter(str.isdigit, filename)))
        return number

    sorted_filenames = sorted(filenames, key=sort_by_number)
    output_path = os.path.dirname(directory)
    output_path = os.path.join(output_path, "sorted_filenames.txt")
    """sorted_filenames_str = str(sorted_filenames)
    with open(output_path, "w") as file:
        file.write(sorted_filenames_str)"""
    return sorted_filenames


def read_csv_file(file_path):
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                i = 1

    except FileNotFoundError:
        print(f"File {file_path} not found!")


def extract_column_from_excel(file_path, label: str):
    try:
        column_data = []
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                column_data.append(row[label])  # extract data from a column
        return column_data
    except FileNotFoundError:
        print(f"File {file_path} not found!")


def show_image(image):
    try:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(
            image,
        )
        plt.axis("off")
        plt.show()
    except FileNotFoundError:
        print(f"File {image_path} not found!")


def save_signal_to_csv(signal, directory: str, file_name: str):
    os.makedirs(directory, exist_ok=True)  # make directory if does not exist
    file_path = os.path.join(directory, file_name)
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["II"])  # header
        for value in signal:
            writer.writerow([value])  # wrirte each value
    print(f"Signal saved to {file_name} successfully.")


def save_image(image, directory: str, file_name: str):
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, file_name)
    cv2.imwrite(file_path, image)


directory_signals = "/Users/maria/Idoven/Projects/002_ecg_paper_to_digit/ecg-miner/validation/LUDB/original/signal"
directory_images = "/Users/maria/Idoven/Projects/002_ecg_paper_to_digit/ecg-miner/validation/LUDB/original/img"

save_path_signals = "/Users/maria/Idoven/ProjectsData/002_ecg_paper_to_digit/20240213_LUDB_Lead2/signals"
save_path_images = (
    "/Users/maria/Idoven/ProjectsData/002_ecg_paper_to_digit/20240213_LUDB_Lead2/images"
)

signals = []
images = []

signals = sort_filenames_by_number(directory_signals)
images = sort_filenames_by_number(directory_images)


for index in range(len(images)):
    image_path = directory_images + "/" + images[index]
    signal_path = directory_signals + "/" + signals[index]

    image = cv2.imread(image_path)
    lead_II = image[700 : image.shape[0], 0 : image.shape[1]]
    # show_image(lead_II)
    save_image(lead_II, save_path_images, images[index])
    signal = extract_column_from_excel(signal_path, "II")
    save_signal_to_csv(signal, save_path_signals, signals[index])
