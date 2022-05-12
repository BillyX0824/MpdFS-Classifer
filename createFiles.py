import csv


# Extract feature combinations from traces
def createFiles(file_path):
    files = list()
    with open(file_path, encoding="UTF-8-sig") as fl:
        reader = csv.reader(fl)
        for row in reader:
            user_files = list()
            file_id = int(row[0])
            file_type = int(row[1])
            file_uid = int(row[2])
            file_gid = int(row[3])
            file_access = int(row[4])
            file_write = int(row[5])
            file_gap_time = (file_access - file_write) / 86400  # Last Access Time - Last Modified Time
            user_files.append((file_id, file_type, file_uid, file_gid, file_access, file_gap_time))
            files.extend(user_files)
    return files


def writeFilesCSV(files, file_path):
    with open(file_path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, dialect="excel")
        for item in files:
            writer.writerow(item)


if __name__ == "__main__":
    core_data_path = " "  # the selected core data from readTraces
    file_csv_path = " "  # a csv file to write files we created
    writeFilesCSV(createFiles(core_data_path), file_csv_path)
