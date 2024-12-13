# Credit to aru because I hate writing code despite being perfectly capable :c (@arutonee on discord)

CFG = 'trannies.cfg'
CHAT = 'chat'
SAY = 'say'
PRINT = 'print'
GHOST = 'ghost'
CS_PATH = "D:/SteamLibrary/steamapps/common/Counter-Strike Global Offensive/game/csgo/cfg/settings/"
CS_FILE = CS_PATH + CFG
MESSAGES_FILE = CS_PATH + 'scripts/' + CFG


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
