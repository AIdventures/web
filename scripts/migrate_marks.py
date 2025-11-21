"""
Migrates legacy mark tags from posts to the new Highlight component.

Usage:
python scripts/migrate_marks.py
"""

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
    'rgba(216, 192, 175, 0.85)': 'brown',
    '#ba9375d9': 'brown'
}

POSTS_DIR = 'src/content/posts'

def migrate_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if file contains any mark or Underlined tags
    has_mark = '<mark' in content
    has_underlined = '<Underlined' in content

    if not has_mark and not has_underlined:
        return None

    # Add import if not present
    import_stmt = "import Highlight from '../../components/Highlight.astro';"
    import_added = False
    if import_stmt not in content:
        # Find end of frontmatter
        parts = content.split('---', 2)
        if len(parts) >= 3:
            # parts[0] is empty (before first ---), parts[1] is frontmatter, parts[2] is content
            parts[2] = '\n\n' + import_stmt + '\n' + parts[2]
            content = '---'.join(parts)
        else:
            # Fallback if no frontmatter found
            content = import_stmt + '\n\n' + content
        import_added = True

    mark_count = 0
    # Replace mark tags
    if has_mark:
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
        mark_pattern = re.compile(r'<mark style="background:\s*([^"]+)">((?:(?!</mark>).)*)</mark>', re.DOTALL)
        content, mark_count = mark_pattern.subn(replace_mark, content)

    underlined_count = 0
    # Replace Underlined tags
    if has_underlined:
        def replace_underlined(match):
            color = match.group(1)
            inner_content = match.group(2)
            
            if not color:
                color = 'yellow'
            
            return f'<Highlight color="{color}">{inner_content}</Highlight>'

        # Regex for Underlined tags with optional color attribute
        underlined_pattern = re.compile(r'<Underlined(?:\s+color=["\']([^"\']+)["\'])?\s*>((?:(?!</Underlined>).)*)</Underlined>', re.DOTALL)
        content, underlined_count = underlined_pattern.subn(replace_underlined, content)

    if mark_count > 0 or underlined_count > 0 or import_added:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return {
            'filepath': filepath,
            'marks': mark_count,
            'underlined': underlined_count,
            'import_added': import_added
        }
    
    return None

def print_stats(stats):
    if not stats:
        print("No files modified.")
        return

    print("\n" + "="*60)
    print(f"{'MIGRATION STATISTICS':^60}")
    print("="*60)
    print(f"{'File':<40} | {'Marks':<7} | {'Under':<7} | {'Import':<6}")
    print("-" * 60)
    
    total_marks = 0
    total_underlined = 0
    total_files = len(stats)

    for stat in stats:
        filename = os.path.basename(stat['filepath'])
        # Truncate filename if too long
        if len(filename) > 38:
            filename = filename[:35] + "..."
            
        print(f"{filename:<40} | {stat['marks']:<7} | {stat['underlined']:<7} | {'Yes' if stat['import_added'] else 'No':<6}")
        
        total_marks += stat['marks']
        total_underlined += stat['underlined']

    print("-" * 60)
    print(f"{'TOTALS':<40} | {total_marks:<7} | {total_underlined:<7} |")
    print("="*60)
    print(f"Total files modified: {total_files}")
    print("\n")

def main():
    all_stats = []
    for root, dirs, files in os.walk(POSTS_DIR):
        for file in files:
            if file.endswith('.mdx'):
                result = migrate_file(os.path.join(root, file))
                if result:
                    all_stats.append(result)
    
    print_stats(all_stats)

if __name__ == '__main__':
    main()
