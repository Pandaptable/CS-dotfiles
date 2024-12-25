from pathlib import Path

output_dir = "."
Path(output_dir).mkdir(exist_ok=True)

cumulative_sleep_duration = 50

for i in range(0, 11):
	content = f"sleep {cumulative_sleep_duration}\nn\n"
	new_line = "sleep 50\nn\n"

	n = int((1_000_000 - len(content)) / len(new_line))
	content += new_line * n
	cumulative_sleep_duration += 50 * n

	with open(Path(output_dir, f"tick{i}.cfg"), "w", encoding="utf-8") as file:
		file.write(content)
