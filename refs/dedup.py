import sys
import re

def deduplicate_bib(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into entries
    entries = re.findall(r'(@[a-zA-Z]+\s*\{[^@]+)', content)
    
    seen_keys = set()
    unique_entries = []
    
    for entry in entries:
        # Extract citekey
        match = re.search(r'@[a-zA-Z]+\s*\{\s*([^,]+),', entry)
        if match:
            key = match.group(1).strip()
            if key not in seen_keys:
                seen_keys.add(key)
                unique_entries.append(entry.strip())
        else:
            unique_entries.append(entry.strip())
            
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(unique_entries))
        f.write("\n")
        
    print(f"Total entries: {len(entries)}, Unique entries: {len(unique_entries)}")

if __name__ == '__main__':
    deduplicate_bib(sys.argv[1], sys.argv[2])
