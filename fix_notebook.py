import json

file_path = 'promotion_prediction.ipynb'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
        json_content = json.loads(data)
        
    # If successful, save it back formatted correctly
    print("Success! The JSON is valid. Re-saving with proper formatting...")
    with open('fixed_notebook.ipynb', 'w', encoding='utf-8') as f:
        json.dump(json_content, f, indent=1)
    print("Saved as 'fixed_notebook.ipynb'. Try opening this file.")

except json.JSONDecodeError as e:
    print(f"\n❌ JSON Error found at line {e.lineno}, column {e.colno}:")
    print(f"Error message: {e.msg}")
    
    # Print the specific line causing trouble
    lines = data.splitlines()
    if e.lineno <= len(lines):
        print(f"\nProblematic line content:\n{lines[e.lineno - 1]}")
        print("-" * 20)
        print("Tip: Look for a missing comma, extra comma, or unclosed quote.")
