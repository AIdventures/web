import os
import re

COLOR_MAP = {
    '#FFF3A3A6': 'yellow',
    '#BBFABBA6': 'green',
    '#D2B3FFA6': 'purple',
    '#FFB8EBA6': 'red',
    '#ABF7F7A6': 'cyan',
    '#ADCCFFA6': 'blue',
    '#FFB86CA6': 'orange',
    'rgba(216, 192, 175, 0.85)': 'brown'
}

POSTS_DIR = 'src/content/posts'

def migrate_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if file contains any mark tags
    if '<mark' not in content:
        return

    print(f"Migrating {filepath}...")

    # Add import if not present
    import_stmt = "import Highlight from '../../components/Highlight.astro';"
    if import_stmt not in content:
        # Find end of frontmatter
        parts = content.split('---', 2)
        if len(parts) >= 3:
            # parts[0] is empty (before first ---), parts[1] is frontmatter, parts[2] is content
            parts[2] = '\n\n' + import_stmt + parts[2]
            content = '---'.join(parts)
        else:
            # Fallback if no frontmatter found
            content = import_stmt + '\n\n' + content

    # Replace mark tags
    
    def replace_mark(match):
        style_content = match.group(1)
        inner_content = match.group(2)
        
        color = 'yellow' # Default fallback
        found_color = False
        
        for hex_code, name in COLOR_MAP.items():
            # Remove spaces to make matching robust
            clean_hex = hex_code.replace(' ', '').lower()
            clean_style = style_content.replace(' ', '').lower()
            
            if clean_hex in clean_style:
                color = name
                found_color = True
                break
        
        if not found_color:
            print(f"  Warning: Unknown color in style '{style_content}' in {filepath}")
            
        return f'<Highlight color="{color}">{inner_content}</Highlight>'

    # Regex updated to handle optional space after background:
    pattern = re.compile(r'<mark style="background:\s*([^"]+)">((?:(?!</mark>).)*)</mark>', re.DOTALL)
    
    new_content = pattern.sub(replace_mark, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    for root, dirs, files in os.walk(POSTS_DIR):
        for file in files:
            if file.endswith('.mdx'):
                migrate_file(os.path.join(root, file))

if __name__ == '__main__':
    main()

