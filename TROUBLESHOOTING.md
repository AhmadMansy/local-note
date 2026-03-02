# 🔧 دليل حل المشكلات | Troubleshooting Guide

حلول للمشاكل الشائعة أثناء التطوير
Solutions to common development issues

---

## 🌍 مشاكل البيئة | Environment Issues

### ❌ المشكلة: "python is not recognized"
**الحل | Solution:**
```bash
# Windows - أضف Python إلى PATH
# 1. ابحث عن "Environment Variables" في إعدادات Windows
# 2. عدل "Path" وأضف مسار Python

# تحقق من التثبيت
python --version
```

---

### ❌ المشكلة: "Virtual environment activation fails"
**الحل | Solution:**
```bash
# Windows PowerShell - سماح بتشغيل السكريبتات
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# macOS/Linux - صلاحيات التنفيذ
chmod +x .venv/bin/activate

# إعادة إنشاء البيئة
python -m venv .venv --clear
```

---

### ❌ المشكلة: "pip install fails"
**الحل | Solution:**
```bash
# تحديث pip
python -m pip install --upgrade pip

# استخدام مرآة أسرع
pip install -r requirements.txt -i https://pypi.org/simple

# تثبيت يدوي
pip install --no-cache-dir <package-name>
```

---

### ❌ المشكلة: "Module not found" على الرغم من التثبيت
**الحل | Solution:**
```bash
# تأكد من تفعيل البيئة الافتراضية
# Windows
echo $env:VIRTUAL_ENV

# macOS/Linux
echo $VIRTUAL_ENV

# إعادة تثبيت الحزمة
pip uninstall <package>
pip install <package>

# تحقق من المسار
python -c "import sys; print(sys.path)"
```

---

## 📦 مشاكل Git | Git Issues

### ❌ المشكلة: "Permission denied (publickey)"
**الحل | Solution:**
```bash
# إنشاء مفتاح SSH جديد
ssh-keygen -t ed25519 -C "your_email@example.com"

# إضافته إلى SSH agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# نسخ المفتاح العام
cat ~/.ssh/id_ed25519.pub
# أضفه إلى GitHub Settings > SSH Keys

# اختبار الاتصال
ssh -T git@github.com
```

---

### ❌ المشكلة: "Merge conflict"
**الحل | Solution:**
```bash
# 1. اسحب التغييرات
git pull origin main

# 2. افتح الملفات المتعارضة
# ابحث عن: <<<<<<<, =======, >>>>>>>

# 3. حل التعارض يدوياً
# احذف العلامات واختر الكود الصحيح

# 4. أضف الملفات
git add <resolved-files>

# 5. أكمل الدمج
git commit

# أو استخدم rebase
git pull --rebase origin main
# حل التعارضات
git rebase --continue
```

---

## 🧪 مشاكل الاختبارات | Testing Issues

### ❌ المشكلة: "No tests collected"
**الحل | Solution:**
```bash
# تأكد من تسمية الاختبارات
# يجب أن يبدأ بـ test_

# ✅ صحيح | Correct
def test_something():
    pass

# ❌ خطأ | Wrong
def something_test():
    pass

# تحقق من تكوين pytest
pytest --collect-only

# تشغيل من المجلد الصحيح
pytest tests/
```

---

### ❌ المشكلة: "ImportError"
**الحل | Solution:**
```bash
# تأكد من بنية المجلدات
your-project/
├── src/
│   └── local_note/
│       ├── __init__.py
│       └── core.py
└── tests/
    ├── __init__.py
    └── test_core.py

# أضف __init__.py لكل مجلد
touch src/__init__.py
touch src/local_note/__init__.py
touch tests/__init__.py

# أو أضف المسار إلى PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
```

---

## 🖥️ مشاكل GUI | GUI Issues

### ❌ المشكلة: "Tkinter not available"
**الحل | Solution:**
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# macOS (مع Homebrew)
brew install python-tk

# Windows - يجب أن يكون مثبتاً تلقائياً
```

---

### ❌ المشكلة: "Arabic text displays incorrectly (RTL)"
**الحل | Solution:**
```python
# استخدم مكتبة bidi
# pip install python-bidi

from bidi.algorithm import get_display

# عكس النص العربي
arabic_text = "مرحبا بالعالم"
display_text = get_display(arabic_text)
```

---

## 📁 مشاكل الملفات | File Issues

### ❌ المشكلة: "UnicodeDecodeError"
**الحل | Solution:**
```python
# ✅ صحيح - استخدم UTF-8
with open('file.md', 'r', encoding='utf-8') as f:
    content = f.read()

# ✅ مع معالجة الأخطاء
try:
    with open('file.md', 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    # جرب ترميزات أخرى
    with open('file.md', 'r', encoding='utf-8-sig') as f:
        content = f.read()
```

---

### ❌ المشكلة: "Path not found on different OS"
**الحل | Solution:**
```python
from pathlib import Path

# ✅ صحيح - استخدم pathlib
base_path = Path.home() / 'local-note'
notes_path = base_path / 'notes'

# لا تستخدم
# ❌ path = "C:\\Users\\..." # Windows only
# ❌ path = "/Users/..."     # macOS only

# لإنشاء المجلد
notes_path.mkdir(parents=True, exist_ok=True)
```

---

## 📞 الحصول على مساعدة إضافية | Getting Additional Help

### أين تسأل | Where to Ask:
1. 💬 Discord: https://discord.gg/local-note
2. 📧 Email: help@local-note.dev
3. 🐛 GitHub Issues: https://github.com/your-username/local-note/issues

---

**تذكر: لا توجد أسئلة غبية! السؤال هو بداية التعلم. 🌟**
**Remember: There are no silly questions! Asking is the start of learning. 🌟**
