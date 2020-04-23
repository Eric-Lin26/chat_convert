#讀取及轉換對話

# 讀取檔案
def read(filename):
    lines = []
    with open(filename, "r", encoding="utf-8-sig") as f:
        for line in f:
            lines.append(line.strip())
    return lines

# 轉換對話格式
def convert(lines):
    new = []
    name = None
    for line in lines:
        if line == "Allen":
            name = "Allen"
            continue
        elif line == "Tom":
            name = "Tom"
            continue
        if name:
            new.append(name + ": " + line)
    return new

# 寫入檔案
def write_file(file, lines):
    with open(file, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

def main():
    lines = read("original.txt")
    lines = convert(lines)
    write_file("output.txt", lines)

main()