import os

for i in range(1, 101):
    day_folder = f"day_{i:02d}"
    os.makedirs(day_folder, exist_ok=True)
    with open(os.path.join(day_folder, "notes.md"), "w") as f:
        f.write(f"# Day {i:02d} Notes\n")
    open(os.path.join(day_folder, "code.py"), "w").close()
