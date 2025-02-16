import sys
from pathlib import Path
import re
import collections

def display_log_counts(counts: dict):
    st1 = "Рівень логування    |"
    st2 = "  Кількість  "
    print(st1+st2)
    print("-----------------------------------")
    for elem in counts.items():
        s_elem = re.split(",",str(elem))
        s_elem0 = re.sub(r"['(,\)]","",s_elem[0]).strip()
        s_elem1 = "|    " + re.sub(r"[())]","",s_elem[1]).strip()
        for i in range(len(st1)-len(s_elem0)-1):
            s_elem0 += " " 
        print(s_elem0 + s_elem1) 
    return

def filter_logs_by_level(logs: list, level: str) -> list:
    print("")
    print(f"Деталі логів для рівня {level}")
    list_level = [elem for elem in logs if str(elem["level"]) == str(level)]
    for elem in list_level:
        print(elem["data"] + "  " + elem["time"] + "  "+ elem["message"])
    return

def count_logs_by_level(logs: list) -> dict:
    kl_level = collections.Counter(logs)
    return kl_level

def parse_log_line(line: str) -> dict:
    log_lines = []
    #level = set()
    level_all = []
    for elem in line:
        el = re.split(' ',elem.strip())
        poz_message = len(el[0].strip()) + len(el[1].strip()) + len(el[2].strip()) + 3
        log_lines.append({"data": el[0], "time": el[1], "level": el[2], "message": elem[poz_message:].strip()})
        #level.add(el[2])   
        level_all.append(el[2])

    return log_lines,  count_logs_by_level(level_all) 

def load_logs(file_path: str) -> list:
    with open(file_path, "r") as file:
        return parse_log_line(file.readlines())    

def main():
    if len(sys.argv) > 1:
        logfile = Path(sys.argv[1])
        if logfile.exists():
           log_lines, kl_level = load_logs(logfile)
           display_log_counts(kl_level)
           if len(sys.argv) == 3:
              if sys.argv[2].upper() in kl_level:
                 filter_logs_by_level(log_lines, sys.argv[2].upper())  
              else:
                 print("Введений рівень логування не знайдено")    
        else:   
            print(f"{logfile} не знайдено.") 
    else:
        print("logfile не вказано.")   

if __name__ == "__main__":
     main()
# 
#    python task5_3.py  logfile.log 