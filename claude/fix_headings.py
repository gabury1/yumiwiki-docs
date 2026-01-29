
import os
import re

PRE_DOCS_DIR = r"c:\Users\장은수\OneDrive\바탕 화면\L Y S T\00. NOW\yumiwiki_docs\pre_docs"

def fix_headings():
    files = [f for f in os.listdir(PRE_DOCS_DIR) if f.endswith(".md")]
    
    for filename in files:
        filepath = os.path.join(PRE_DOCS_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace "## 기타: 알고 있으면 즐거운 TMI" with "## 기타"
        # and also "## 기타: 현실적인 구현의 아픔" or similar styles
        new_content = re.sub(r'## 기타:.*', '## 기타', content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {filename}")

if __name__ == "__main__":
    fix_headings()
