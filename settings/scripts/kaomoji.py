# Credit to aru because I hate writing code despite being perfectly capable :c (@arutonee on discord)

CFG = 'kaomoji'
CHAT = 'kaochat'
SAY = 'kaosay'
PRINT = 'kaoprint'
GHOST = 'kaoghost'
CS_PATH = "E:/SteamLibrary/steamapps/common/Counter-Strike Global Offensive/game/csgo/cfg/settings/"
CS_FILE = CS_PATH + CFG + '.cfg'
MESSAGES_FILE = CS_PATH + 'scripts/' + CFG + '.cfg'

LINES = 200


messages = []
with open(MESSAGES_FILE, 'r', encoding='utf-8') as f:
    messages = list(map(lambda s: s.strip(), f.readlines()))

num_messages = len(messages)
max_num_len = len(str(num_messages))

new_lines = []


new_lines.append(f'alias {PRINT} "{CHAT}1"')
new_lines.append(f'alias {GHOST} "{SAY}1"')
new_lines.append('')

for i, msg in enumerate(messages):
    num_spaces = max_num_len - len(str(i+1))
    spaces = ' ' * num_spaces
    new_msg = f'alias "{CHAT}{i+1}"{spaces} "say {msg}"'
    new_lines.append(new_msg)

new_lines.append('')

for i in range(num_messages):
    num_spaces = max_num_len - len(str(i+1))
    num_last_spaces = max_num_len - len(str((i+1) % num_messages + 1))
    spaces = ' ' * num_spaces
    last_spaces = ' ' * num_last_spaces
    roll_line = f'alias "{SAY}{i+1}"{spaces} "alias {PRINT} {CHAT}{i+1};{spaces} alias {GHOST} {SAY}{(i+1) % num_messages + 1}"'
    new_lines.append(roll_line)

with open(CS_FILE, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

def split_file(CS_FILE, CFG, LINES):
    with open(CS_FILE, 'r', encoding='utf-8') as infile:
        content = infile.readlines()

    non_empty_lines = [line.strip() for line in content if line.strip()]

    num_lines = len(non_empty_lines)
    num_files = (num_lines + LINES - 1) // LINES

    # Handle the first file separately without a number
    first_file = CS_PATH + f"{CFG}.cfg"
    with open(first_file, 'w', encoding='utf-8') as firstfile:
        firstfile.writelines('\n'.join(non_empty_lines[:LINES]))

    # Write the remaining lines to subsequent files
    for i in range(1, num_files):
        start_idx = i * LINES
        end_idx = (i + 1) * LINES
        output_file = CS_PATH + f"{CFG}{i}.cfg"

        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.writelines('\n'.join(non_empty_lines[start_idx:end_idx]))

#split_file(CS_FILE, CFG, LINES)