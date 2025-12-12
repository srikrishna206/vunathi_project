# Fix the f-string syntax error in AI backend
with open('backend/ai_backend/app.py', 'r') as f:
    lines = f.readlines()

# Fix line 7758 - escape the quotes properly
if len(lines) >= 7758:
    old_line = lines[7757]  # Python uses 0-based indexing
    print(f"Original line 7758: {old_line}")
    
    # Fix the f-string by escaping the inner quotes
    new_line = '    logger.error(f"   Question markers found: {text.count(\\"question\\")}")\n'
    lines[7757] = new_line
    print(f"Fixed line 7758: {new_line}")
    
    # Write back
    with open('backend/ai_backend/app.py', 'w') as f:
        f.writelines(lines)
    print("✅ Fixed the f-string syntax error")
else:
    print("❌ File doesn't have 7758 lines")
