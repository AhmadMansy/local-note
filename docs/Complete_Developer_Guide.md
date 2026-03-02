# Local Note - Complete Developer Guide

---

## 📖 Table of Contents

1. [Introduction](#introduction)
2. [Project Overview](#project-overview)
3. [Phase 1: Core Backend](#phase-1-core-backend)
4. [Phase 2: Logic & Processing](#phase-2-logic--processing)
5. [Phase 3: GUI Development](#phase-3-gui-development)
6. [Phase 4: Polish & Release](#phase-4-polish--release)
7. [Best Practices](#best-practices)
8. [Conclusion](#conclusion)

---

## Introduction

Welcome to this comprehensive guide for developing the **Local Note** application. This book will teach you how to build a complete note-taking application that stores notes as Markdown files, using Python.

### 🎯 What You'll Learn

- Develop a complete desktop application with graphical user interface
- Manage files and folders programmatically
- Search and filter through text content
- Support Arabic language and RTL (Right-to-Left) text
- Professional software testing

### Prerequisites

- Basic Python knowledge
- Understanding of Object-Oriented Programming (OOP)
- Desire to learn and apply practical skills

---

## Project Overview

### What is Local Note?

Local Note is a personal note management application that saves notes as Markdown files on your computer. It's similar to apps like Obsidian and Notion but:
- ✅ Works offline (no internet required)
- ✅ Lightweight and fast
- ✅ Full Arabic language support
- ✅ Free and open source

### Technical Architecture

```
local-note/
├── src/                    # Main source code
│   ├── models.py          # Data models
│   ├── file_manager.py    # File management
│   ├── scanner.py         # Directory scanning
│   ├── search.py          # Search functionality
│   ├── tags.py            # Tag management
│   ├── parser.py          # Markdown parsing
│   └── main.py            # Main entry point
├── tests/                  # Test files
├── data/                   # Note storage
├── docs/                   # Documentation
├── requirements.txt        # Dependencies
└── README.md              # Readme file
```

---

## Phase 1: Core Backend

### Chapter 1: Setting Up Development Environment

#### Step 1: Install Python

First, ensure Python 3.8+ is installed:

```bash
# Check Python version
python --version
```

#### Step 2: Create Virtual Environment

Virtual environment isolates project dependencies:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**💡 Tip:** You'll know it's activated when you see (venv) in your prompt

#### Step 3: Create Project Structure

```bash
# Create directories
mkdir src tests data docs

# Create __init__.py files
touch src/__init__.py tests/__init__.py
```

#### Step 4: Install Dependencies

Create `requirements.txt`:

```text
pytest>=7.4.0
customtkinter>=5.2.0
markdown>=3.5.0
pymdown-extensions>=10.0
tkinterweb>=3.0
```

Install them:

```bash
pip install -r requirements.txt
```

---

### Chapter 2: Creating the Note Model

#### What is a Dataclass?

Dataclass is a concise way to create classes for storing data. Instead of writing repetitive code, use the `@dataclass` decorator.

#### Implementation

Create `src/models.py`:

```python
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Note:
    """Represents a single note.
    
    Contains all note information:
    - title: Note name
    - content: Note text in Markdown format
    - file_path: Location where note is saved
    - created_at: Creation timestamp
    - updated_at: Last modification timestamp
    """
    
    # Required fields
    title: str
    content: str
    file_path: str
    created_at: datetime
    updated_at: datetime
    
    # Optional fields
    tags: Optional[list[str]] = None
    
    def __str__(self) -> str:
        """String representation - useful for debugging."""
        return f"Note(title='{self.title}', path='{self.file_path}')"
    
    def to_dict(self) -> dict:
        """Convert note to dictionary."""
        return {
            'title': self.title,
            'content': self.content,
            'file_path': self.file_path,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'tags': self.tags or []
        }
    
    @property
    def word_count(self) -> int:
        """Calculate word count."""
        return len(self.content.split())
    
    @property
    def char_count(self) -> int:
        """Calculate character count."""
        return len(self.content)
```

#### Code Explanation:

1. **@dataclass**: Automatically generates:
   - `__init__` method
   - `__repr__` method
   - `__eq__` method

2. **Data Fields**:
   - `title`: Note title
   - `content`: Note text
   - `file_path`: File location
   - `created_at`, `updated_at`: Tracking timestamps

3. **Properties**:
   - `word_count`: Word count
   - `char_count`: Character count

#### Testing the Model

Create `tests/test_models.py`:

```python
import pytest
from datetime import datetime
from src.models import Note

def test_note_creation():
    """Test creating a new note."""
    note = Note(
        title="Test Note",
        content="This is a test note",
        file_path="test.md",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    
    assert note.title == "Test Note"
    assert "test note" in note.content.lower()
    assert note.word_count > 0

def test_note_with_tags():
    """Test note with tags."""
    note = Note(
        title="Programming",
        content="Learn Python",
        file_path="python.md",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        tags=["python", "programming", "learning"]
    )
    
    assert "python" in note.tags
    assert len(note.tags) == 3

def test_empty_note():
    """Test empty note."""
    note = Note(
        title="",
        content="",
        file_path="empty.md",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    
    assert note.word_count == 0
    assert note.char_count == 0
```

**Run tests:**

```bash
pytest tests/test_models.py -v
```

---

### Chapter 3: File Management

#### Create File Manager

Create `src/file_manager.py`:

```python
import os
from datetime import datetime
from pathlib import Path
from typing import Optional
from src.models import Note

def save_note(note: Note, root_dir: str = "./data") -> bool:
    """Save note to Markdown file.
    
    Args:
        note: Note object to save
        root_dir: Root directory for file storage
        
    Returns:
        True if saved successfully, False on failure
    """
    try:
        full_path = Path(root_dir) / note.file_path
        
        # Create directories if needed
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save with UTF-8 encoding for Arabic support
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(note.content)
        
        print(f"✅ Note saved: {note.title}")
        return True
        
    except Exception as e:
        print(f"❌ Error saving note: {e}")
        return False

def read_note(file_path: str, root_dir: str = "./data") -> Optional[Note]:
    """Read note from Markdown file.
    
    Args:
        file_path: File path
        root_dir: Root directory
        
    Returns:
        Note object or None if not found
    """
    try:
        full_path = Path(root_dir) / file_path
        
        if not full_path.exists():
            print(f"⚠️  File not found: {file_path}")
            return None
        
        # Read with UTF-8 encoding
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Get file info
        stat = full_path.stat()
        
        # Create note object
        note = Note(
            title=Path(file_path).stem,
            content=content,
            file_path=file_path,
            created_at=datetime.fromtimestamp(stat.st_ctime),
            updated_at=datetime.fromtimestamp(stat.st_mtime)
        )
        
        return note
        
    except Exception as e:
        print(f"❌ Error reading note: {e}")
        return None

def update_note(note: Note, root_dir: str = "./data") -> bool:
    """Update existing note.
    
    Args:
        note: Updated note object
        root_dir: Root directory
        
    Returns:
        True if updated successfully
    """
    note.updated_at = datetime.now()
    return save_note(note, root_dir)

def delete_note(file_path: str, root_dir: str = "./data") -> bool:
    """Delete note.
    
    Args:
        file_path: File path
        root_dir: Root directory
        
    Returns:
        True if deleted successfully
    """
    try:
        full_path = Path(root_dir) / file_path
        
        if not full_path.exists():
            print(f"⚠️  File not found: {file_path}")
            return False
        
        if not full_path.is_file():
            print(f"❌ Path is not a file: {file_path}")
            return False
        
        full_path.unlink()
        print(f"✅ Note deleted: {file_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error deleting note: {e}")
        return False
```

#### Code Explanation:

1. **save_note()**:
   - Creates full file path
   - Creates directories if needed
   - Saves content with UTF-8 encoding

2. **read_note()**:
   - Checks file existence
   - Reads content with UTF-8 encoding
   - Extracts file metadata (dates)

3. **update_note()**:
   - Updates `updated_at` timestamp
   - Re-saves note

4. **delete_note()**:
   - Checks file existence
   - Safely deletes file

---

### Chapter 4: Directory Scanning

#### Create Scanner

Create `src/scanner.py`:

```python
from pathlib import Path
from typing import List
from src.models import Note
from src.file_manager import read_note

def get_all_notes(root_dir: str = "./data") -> List[Note]:
    """Get all notes in directory.
    
    Scans all subdirectories and collects all Markdown files.
    
    Args:
        root_dir: Root directory to search
        
    Returns:
        List of all found notes
    """
    notes = []
    root_path = Path(root_dir)
    
    if not root_path.exists():
        print(f"⚠️  Directory not found: {root_dir}")
        return notes
    
    # Recursive scan for all files
    for md_file in root_path.rglob("*.md"):
        # Skip hidden files
        if md_file.name.startswith('.'):
            continue
        
        try:
            rel_path = md_file.relative_to(root_path)
            note = read_note(str(rel_path), root_dir)
            if note:
                notes.append(note)
                print(f"✅ Found: {note.title}")
                
        except Exception as e:
            print(f"⚠️  Error reading {md_file}: {e}")
            continue
    
    print(f"\n📊 Total: {len(notes)} notes")
    return notes

def get_notes_by_folder(root_dir: str = "./data") -> dict:
    """Organize notes by folder.
    
    Args:
        root_dir: Root directory
        
    Returns:
        Dictionary: {folder_name: [notes]}
    """
    notes_dict = {}
    notes = get_all_notes(root_dir)
    
    for note in notes:
        folder = str(Path(note.file_path).parent)
        if folder == ".":
            folder = "Root"
        
        if folder not in notes_dict:
            notes_dict[folder] = []
        
        notes_dict[folder].append(note)
    
    return notes_dict
```

---

## Phase 2: Logic & Processing

### Chapter 5: Markdown Parser

#### What is Markdown?

Markdown is a lightweight markup language for writing formatted text.

#### Create Parser

Create `src/parser.py`:

```python
import markdown
from typing import Optional

def render_html(markdown_text: str) -> str:
    """Convert Markdown text to HTML.
    
    Args:
        markdown_text: Markdown text to convert
        
    Returns:
        HTML output
    """
    try:
        md = markdown.Markdown(
            extensions=[
                'extra',
                'codehilite',
                'toc',
                'nl2br',
            ]
        )
        
        html = md.convert(markdown_text)
        return html
        
    except Exception as e:
        print(f"❌ Markdown parsing error: {e}")
        return f"<p>{markdown_text}</p>"

def preview_markdown(markdown_text: str, css_style: Optional[str] = None) -> str:
    """Create complete HTML preview.
    
    Args:
        markdown_text: Markdown text
        css_style: Additional CSS
        
    Returns:
        Complete HTML page
    """
    html_content = render_html(markdown_text)
    
    default_css = """
    <style>
        body {
            direction: rtl;
            text-align: right;
            font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
            line-height: 1.8;
        }
        h1, h2, h3 {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
        }
    </style>
    """
    
    final_css = css_style + default_css if css_style else default_css
    
    full_html = f"""
    <!DOCTYPE html>
    <html dir="rtl" lang="ar">
    <head>
        <meta charset="UTF-8">
        {final_css}
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    return full_html
```

---

### Chapter 6: Search Engine

#### Create Search Module

Create `src/search.py`:

```python
from typing import List
from src.models import Note

def search_notes(query: str, notes: List[Note]) -> List[Note]:
    """Search through notes.
    
    Args:
        query: Search keyword
        notes: List of notes
        
    Returns:
        Matching notes
    """
    if not query:
        return notes
    
    query_lower = query.lower()
    results = []
    
    for note in notes:
        # Search in title
        if query_lower in note.title.lower():
            results.append(note)
            continue
        
        # Search in content
        if query_lower in note.content.lower():
            results.append(note)
    
    return results
```

---

### Chapter 7: Tag Management

#### Create Tags Module

Create `src/tags.py`:

```python
import re
from typing import List, Set
from src.models import Note

def extract_tags(text: str) -> List[str]:
    """Extract tags from text.
    
    Tags are words starting with #
    Example: #python #programming #learning
    
    Args:
        text: Text to extract tags from
        
    Returns:
        Sorted list of unique tags
    """
    pattern = r'#([\w\u0600-\u06FF-]+)'
    tags = re.findall(pattern, text)
    
    unique_tags = sorted(set(tags))
    return unique_tags

def get_all_tags(notes: List[Note]) -> List[str]:
    """Get all tags from all notes.
    
    Args:
        notes: List of notes
        
    Returns:
        List of all unique tags
    """
    all_tags: Set[str] = set()
    
    for note in notes:
        tags = extract_tags(note.content)
        all_tags.update(tags)
    
    return sorted(all_tags)

def filter_by_tag(tag: str, notes: List[Note]) -> List[Note]:
    """Filter notes by tag.
    
    Args:
        tag: Tag to filter by
        notes: List of notes
        
    Returns:
        Notes containing the tag
    """
    filtered = []
    
    for note in notes:
        if tag in extract_tags(note.content):
            filtered.append(note)
    
    return filtered
```

---

## Phase 3: GUI Development

### Chapter 8: Main Window

#### Install CustomTkinter

```bash
pip install customtkinter
```

#### Create User Interface

Create `src/main.py`:

```python
import customtkinter as ctk
from src.scanner import get_all_notes

class LocalNoteApp:
    """Main application."""
    
    def __init__(self):
        """Initialize application."""
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.root = ctk.CTk()
        self.root.title("Local Note")
        self.root.minsize(900, 600)
        self.root.geometry("1100x700")
        
        self.setup_layout()
        self.notes = get_all_notes()
        self.create_widgets()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def setup_layout(self):
        """Setup window layout."""
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=3)
        self.root.grid_rowconfigure(0, weight=1)
    
    def create_widgets(self):
        """Create UI components."""
        self.sidebar = ctk.CTkFrame(self.root)
        self.sidebar.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        self.main_content = ctk.CTkFrame(self.root)
        self.main_content.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        
        self.create_sidebar_content()
        self.create_main_content()
    
    def create_sidebar_content(self):
        """Create sidebar content."""
        title = ctk.CTkLabel(
            self.sidebar,
            text="📝 Notes",
            font=("", 20, "bold")
        )
        title.pack(pady=10)
        
        self.search_var = ctk.StringVar()
        search_entry = ctk.CTkEntry(
            self.sidebar,
            placeholder_text="🔍 Search...",
            textvariable=self.search_var
        )
        search_entry.pack(fill="x", padx=10, pady=5)
        
        self.notes_listbox = ctk.CTkTextbox(
            self.sidebar,
            height=400
        )
        self.notes_listbox.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.update_notes_list()
    
    def create_main_content(self):
        """Create main content."""
        toolbar = ctk.CTkFrame(self.main_content)
        toolbar.pack(fill="x", padx=5, pady=5)
        
        new_btn = ctk.CTkButton(
            toolbar,
            text="➕ New",
            command=self.new_note
        )
        new_btn.pack(side="left", padx=5)
        
        save_btn = ctk.CTkButton(
            toolbar,
            text="💾 Save",
            command=self.save_note
        )
        save_btn.pack(side="left", padx=5)
        
        delete_btn = ctk.CTkButton(
            toolbar,
            text="🗑️ Delete",
            command=self.delete_note
        )
        delete_btn.pack(side="left", padx=5)
        
        self.editor = ctk.CTkTextbox(
            self.main_content,
            font=("Consolas", 14),
            wrap="word"
        )
        self.editor.pack(fill="both", expand=True, padx=5, pady=5)
    
    def update_notes_list(self):
        """Update notes list."""
        self.notes_listbox.delete("1.0", "end")
        
        for note in self.notes:
            self.notes_listbox.insert("end", f"📄 {note.title}\n")
    
    def new_note(self):
        print("New note...")
    
    def save_note(self):
        print("Save note...")
    
    def delete_note(self):
        print("Delete note...")
    
    def on_closing(self):
        self.root.destroy()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = LocalNoteApp()
    app.run()
```

---

## Phase 4: Polish & Release

### Chapter 9: Live Preview

### Chapter 10: Internal WikiLinks

### Chapter 11: Final Documentation

---

## Best Practices

### Clean Code

### Testing

### Version Control

---

## Conclusion

Congratulations on completing this guide! 🎉

You now have:
- ✅ Complete note-taking application
- ✅ Deep understanding of desktop app development
- ✅ Advanced Python programming skills

### Next Steps

1. Explore more features
2. Add custom functionality
3. Share with community

---

**This book was created to teach application development using Python**
**Author: Development Team**
**Date: 2024**

---

**Copyright:** This project is open source and free for everyone.
**License:** MIT License

---

*Contribute on GitHub: https://github.com/AhmadMansy/local-note*
