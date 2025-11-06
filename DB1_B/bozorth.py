import os
import subprocess

folder = "/Users/hugotrebert/Documents/Lju/ImageBasedBiometry_63554/LAB1/DB1_B/minutiae"
output_file = "/Users/hugotrebert/Documents/Lju/ImageBasedBiometry_63554/LAB1/DB1_B/results.txt"
files = sorted([f for f in os.listdir(folder) if f.endswith(".xyt")])
results_file = "/Users/hugotrebert/Documents/Lju/ImageBasedBiometry_63554/LAB1/DB1_B/results.txt"
impostors = []
genuines = []

scores = {}
if os.path.exists(results_file):
    with open(results_file, "r") as f:
        for line in f:
            a, b, s = line.strip().split()

            scores[(a, b)] = s

with open(output_file, "w") as f_out:
  for i in range(len(files)) :
    for j in range (i + 1, len(files)) :
      file1 = os.path.join(folder, files[i])
      file2 = os.path.join(folder, files[j])

      result = subprocess.run (
        ["bozorth3", file1, file2],
        capture_output=True,
        text=True
      )

      score = result.stdout.strip()
      line = f"{files[i]} {files[j]} {score}\n"
      print(line)
      f_out.write(line)