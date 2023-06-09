import os
import random
from datetime import date, time, datetime
import datetime

total_day = 30 #total days back
commit_frequency = 10 #commit time per day
repo_link = "https://github.com/miracletalent/techbot.git"

tl = total_day #time day
ctr = 1

now = datetime.datetime.now()

f = open("commit.txt", "w")
os.system("git config user.name")
os.system("git config user.email")
os.system("git init")

pointer = 60

def randtime(start_time = datetime.time(9, 0, 0), end_time = datetime.time(17, 0, 0)):
    time_range = datetime.datetime.combine(datetime.date.today(), end_time) - datetime.datetime.combine(datetime.date.today(), start_time)
    random_seconds = random.randint(0, time_range.seconds)
    return (
        datetime.datetime.combine(datetime.date.today(), start_time)
        + datetime.timedelta(seconds=random_seconds)
    ).time()

while tl > 0:
    ct = random.randint(0, 6)
    while ct > 0 and random.randint(0,2):
        with open("commit.txt", "a+") as f:
            l_date = now + datetime.timedelta(days=-pointer)
            if l_date.weekday() == 5 and random.randint(0, 7) != 5:
                break
            if l_date.weekday() == 6 and random.randint(0, 12) != 5:
                break
            formatdate = l_date.strftime("%Y-%m-%d")
            formattime = randtime()
            f.write(f"commit ke {ctr}: {formatdate}\n")
        os.system("git add .")
        os.system(f"git commit --date=\"{formatdate} {formattime}\" -m \"commit ke {ctr}\"")
        print(f"commit ke {ctr}: {formatdate}")
        ct-=1
        ctr+=1
    pointer+=1
    tl-=1

os.system(f"git remote add origin {repo_link}")
os.system(f"git remote set-url origin {repo_link}")
os.system("git branch -M main")
os.system("git push -u origin main -f")