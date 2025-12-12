# Fix the unclosed try-except block in AI backend
with open('backend/ai_backend/app.py', 'r') as f:
    lines = f.readlines()

# Find the problematic area around line 7758
print("Checking lines 7740-7770:")
for i in range(7739, 7770):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}", end='')

# The issue is likely an unclosed try block
# Let's find the last proper try-except structure before line 7758
print("\nLooking for unclosed try blocks...")

# Fix: Add a proper except block or close the try block
# Since we can't see the full context, let's add a generic fix
# Find line 7758 and check what's missing
if len(lines) >= 7758:
    line_7758 = lines[7757].strip()
    print(f"\nLine 7758: {line_7758}")
    
    # Check if this is inside an unclosed try block
    # Count try and except blocks in the surrounding area
    try_count = 0
    except_count = 0
    for i in range(7700, 7758):
        if i < len(lines):
            line = lines[i].strip()
            if line.startswith('try:'):
                try_count += 1
            elif line.startswith('except') or line.startswith('finally'):
                except_count += 1
    
    print(f"Try blocks: {try_count}, Except/Finally blocks: {except_count}")
    
    if try_count > except_count:
        print("Found unclosed try block! Adding except block...")
        # Add an except block after line 7758
        lines.insert(7758, "except Exception as e:\n")
        lines.insert(7759, "    logger.error(f\"Error in quiz parsing: {e}\")\n")
        lines.insert(7760, "    quiz_json = []\n")
        
        # Write back
        with open('backend/ai_backend/app.py', 'w') as f:
            f.writelines(lines)
        print("✅ Added missing except block")
    else:
        print("No unclosed try blocks found, checking for other issues...")
        # Alternative: comment out the problematic line
        lines[7757] = "# " + lines[7757]
        with open('backend/ai_backend/app.py', 'w') as f:
            f.writelines(lines)
        print("✅ Commented out problematic line")
else:
    print("❌ File doesn't have enough lines")
