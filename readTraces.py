import csv


def readTrace(file_path, det_path):
    csvFile = open(det_path, 'w', newline='', encoding='utf-8')
    writer = csv.writer(csvFile)

    f = open(file_path, 'r', encoding='GB2312')
    for line in f:
        csvRow = line.split()
        writer.writerow(csvRow)

    f.close()
    csvFile.close()


def createFiles(file_path):
    temp_fid = set()
    temp_am = set()
    files = list()
    with open(file_path, encoding="utf-8") as fi:
        reader = csv.reader(fi)
        for row in reader:
            x = list()
            if row[4] == "R3" and (
                    row[7] == "read" or row[7] == "getattr" or row[7] == "access" or row[7] == "write") and len(
                    row) > 30:
                if row[7] == "write":
                    uid = int(row[22], 16)
                    gid = int(row[24], 16)
                    ftype = int(row[16])
                    fid = int(row[36], 16)
                    atime = round(float(row[38]))
                    mtime = round(float(row[40]))
                else:
                    uid = int(row[16], 16)
                    gid = int(row[18], 16)
                    ftype = int(row[10])
                    fid = int(row[30], 16)
                    atime = round(float(row[32]))
                    mtime = round(float(row[34]))
                sum = atime + mtime + fid
                x.append((fid, ftype, uid, gid, atime, mtime))
                if fid not in temp_fid:
                    temp_fid.add(fid)
                    temp_am.add(sum)
                    files.extend(x)
                else:
                    if sum not in temp_am:
                        temp_am.add(sum)
                        files.extend(x)
    return files


def createFiles_home(file_path):
    temp_fid = set()
    temp_am = set()
    files = list()
    with open(file_path, encoding="utf-8") as fi:
        reader = csv.reader(fi)
        for row in reader:
            x = list()
            if row[4] == "R3" and (
                    row[7] == "read" or row[7] == "getattr" or row[7] == "access" or row[7] == "write") and len(
                    row) > 30:
                uid = int(row[16], 16)
                gid = int(row[18], 16)
                ftype = int(row[10])
                fid = int(row[30], 16)  # home
                atime = round(float(row[32]))
                mtime = round(float(row[34]))
                sum = atime + mtime + fid
                x.append((fid, ftype, uid, gid, atime, mtime))
                if fid not in temp_fid:
                    temp_fid.add(fid)
                    temp_am.add(sum)
                    files.extend(x)
                else:
                    if sum not in temp_am:
                        temp_am.add(sum)
                        files.extend(x)
    return files


def writeFilesCSV(files, file_path):
    with open(file_path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, dialect="excel")
        for item in files:
            writer.writerow(item)


if __name__ == "__main__":
    old_txt_path = " "  # the original trace
    csv_path = " "  # convert the original trace file to a csv file
    core_data_path = " "  # the selected core data
    readTrace(old_txt_path, csv_path)
    writeFilesCSV(createFiles(csv_path), core_data_path)
    # writeFilesCSV(createFiles(csv_path), core_data_path) # if NFS trace is homexxx, use it
