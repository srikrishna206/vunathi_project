# Safe fix: Comment out the problematic section
with open('backend/ai_backend/app.py', 'r') as f:
    lines = f.readlines()

# Comment out lines 7755-7760 (the problematic area)
start_line = 7754  # 0-based index
end_line = 7760

for i in range(start_line, min(end_line, len(lines))):
    if not lines[i].strip().startswith('#'):
        lines[i] = "# " + lines[i]

with open('backend/ai_backend/app.py', 'w') as f:
    f.writelines(lines)

print("✅ Commented out problematic section (lines 7755-7760)")
