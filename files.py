with open(r"C:\Users\akash\Downloads\Logs\TC_logs.txt", "r") as file:

    for line in file:
       line = line.strip()
       

       if "FAIL" in line:
           tcid,reason = line.split(" ",1)
           print(f"{tcid} {reason}")

