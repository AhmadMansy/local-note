# 🚀 دليل البدء السريع | Quick Start Guide

مرحباً بك في Local Note! هذا الدليل سيساعدك على البدء بسرعة.
Welcome to Local Note! This guide will help you get started quickly.

---

## 📋 قبل أن تبدأ | Before You Start

### المتطلبات | Prerequisites

تأكد من تثبيت البرامج التالية:
Make sure you have the following installed:

- **Python** 3.8 أو أحدث | or later
  - تحقق | Check: `python --version`
  - تحميل | Download: https://python.org/downloads/

- **Git** 
  - تحقق | Check: `git --version`
  - تحميل | Download: https://git-scm.com/downloads

- **VS Code** (موصى به) | (Recommended)
  - تحميل | Download: https://code.visualstudio.com/

---

## 🎯 الخطوة 1: استنساخ المشروع | Clone the Project

```bash
# استنسخ المستودع | Clone the repository
git clone https://github.com/your-username/local-note.git
cd local-note
```

---

## 🔧 الخطوة 2: إعداد البيئة | Setup Environment

### على Windows | On Windows:
```bash
# إنشاء بيئة افتراضية | Create virtual environment
python -m venv .venv

# تفعيل البيئة | Activate environment
.venv\Scripts\activate

# تثبيت المتطلبات | Install requirements
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### على macOS/Linux | On macOS/Linux:
```bash
# إنشاء بيئة افتراضية | Create virtual environment
python3 -m venv .venv

# تفعيل البيئة | Activate environment
source .venv/bin/activate

# تثبيت المتطلبات | Install requirements
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

---

## 📚 الخطوة 3: فهم المشروع | Understand the Project

### هيكل المشروع | Project Structure
```
local-note/
├── docs/                    # الوثائق | Documentation
│   ├── GETTING_STARTED.md   # هذا الملف | This file
│   ├── WEEKLY_CHECKPOINTS.md # تتبع التقدم | Progress tracking
│   └── *.md                # أدلة المطورين | Developer guides
├── .github/                # قوالب GitHub | GitHub templates
│   ├── ISSUE_TEMPLATE/     # قوالب القضايا | Issue templates
│   └── workflows/          # سير العمل | Workflows
├── src/                    # الكود المصدري | Source code
├── tests/                  # الاختبارات | Tests
├── requirements.txt        # المتطلبات | Requirements
├── requirements-dev.txt    # متطلبات التطوير | Dev requirements
├── DEVELOPMENT.md          # دليل التطوير | Development guide
├── CONTRIBUTING.md         # دليل المساهمة | Contributing guide
└── TROUBLESHOOTING.md      # حل المشكلات | Troubleshooting
```

---

## 📖 الخطوة 4: اقرأ الوثائق | Read Documentation

### ترتيب القراءة الموصى به | Recommended Reading Order:

1. **README.md** - نظرة عامة | Overview
2. **docs/دليل_المطور_الكامل.md** - الدليل الكامل (عربي) | Complete guide (Arabic)
3. **docs/Complete_Developer_Guide.md** - English version
4. **DEVELOPMENT.md** - سير العمل | Workflow
5. **CONTRIBUTING.md** - كيفية المساهمة | How to contribute

---

## 🎮 الخطوة 5: أول مهمة | First Task

ابدأ بـ Issue #1: إعداد البيئة الافتراضية
Start with Issue #1: Virtual Environment Setup

### كيفية اختيار قضية | How to Pick an Issue:
```bash
# عرض جميع القضايا المفتوحة | List all open issues
gh issue list

# عرض القضايا المعينة لك | List issues assigned to you
gh issue list --assignee @me
```

---

## 🧪 الخطوة 6: تشغيل الاختبارات | Run Tests

```bash
# تشغيل جميع الاختبارات | Run all tests
pytest

# تشغيل مع تفاصيل أكثر | Run with more details
pytest -v

# تشغيل اختبار محدد | Run specific test
pytest tests/test_note.py

# تشغيل مع نسبة التغطية | Run with coverage
pytest --cov=. --cov-report=html
```

---

## 📝 الخطوة 7: أول التزام | First Commit

```bash
# أنشئ فرعاً جديداً | Create new branch
git checkout -b feature/my-first-feature

# أضف تغييراتك | Add your changes
git add .

# التزم | Commit
git commit -m "feat: add my first feature"

# ادفع | Push
git push origin feature/my-first-feature
```

---

## 🎓 نصائح للتعلم | Learning Tips

### ✅ افعل | Do:
- ابدأ بالقضايا الأسهل | Start with easier issues
- اقرأ الكود الموجود | Read existing code
- اسأل عندما تعلق | Ask when stuck
- التزم بشكل متكرر | Commit frequently
- اختبر دائماً | Always test

### ❌ لا تفعل | Don't:
- لا تخف من الأخطاء | Don't fear mistakes
- لا تنسخ بدون فهم | Don't copy without understanding
- لا تتردد في طلب المساعدة | Don't hesitate to ask for help
- لا تضغط很长时间 بدون التزام | Don't go long without committing

---

## 🆘 أين تجد المساعدة | Where to Get Help

### الموارد | Resources:
- **TROUBLESHOOTING.md** - حلول للمشاكل الشائعة | Solutions to common problems
- **DEVELOPMENT.md** - دليل التطوير | Development guide
- **GitHub Issues** - للأسئلة والمشاكل | For questions and problems

### التواصل | Communication:
- 💬 إنشاء GitHub Issue للأسئلة | Create a GitHub Issue for questions
- 📧 البريد الإلكتروني | Email: help@local-note.dev

---

## 📊 تتبع التقدم | Track Progress

استخدم ملف `docs/WEEKLY_CHECKPOINTS.md` لتتبع تقدمك الأسبوعي.
Use the `docs/WEEKLY_CHECKPOINTS.md` file to track your weekly progress.

---

## 🎉 الجدول الزمني | Timeline

| الأسبوع | Week | التركيز | Focus |
|---------|---------|-----------------|-------|
| 1 | 1 | الإعداد والأساسيات | Setup & Fundamentals |
| 2 | 2 | الملفات والاختبارات | Files & Testing |
| 3 | 3 | البحث والمعالجة | Search & Processing |
| 4 | 4 | واجهة المستخدم الأساسية | Basic GUI |
| 5 | 5 | واجهة المستخدم المتقدمة | Advanced GUI |
| 6 | 6 | الميزات والتحسين | Features & Polish |
| 7 | 7 | الوثائق والإصدار | Documentation & Release |

---

## 💻 اختصارات VS Code مفيدة | Useful VS Code Shortcuts

| الوظيفة | Function | Windows/Linux | macOS |
|----------|-----------|---------------|-------|
| حفظ | Save | Ctrl+S | Cmd+S |
| فتح Terminal | Open Terminal | Ctrl+` | Cmd+` |
| تنسيق الكود | Format Code | Shift+Alt+F | Shift+Opt+F |
| التنقل في الملفات | Navigate Files | Ctrl+P | Cmd+P |
| إغلاق Tab | Close Tab | Ctrl+W | Cmd+W |

---

## 🔗 روابط سريعة | Quick Links

- 📖 [Python Documentation](https://docs.python.org/3/)
- 🧪 [Pytest Documentation](https://docs.pytest.org/)
- 🎨 [CustomTkinter Docs](https://customtkinter.tomschimansky.com/)
- 📦 [PyPI Packages](https://pypi.org/)
- 📝 [GitHub Skills](https://skills.github.com/)

---

## ✨ ماذا بعد؟ | What's Next?

1. ✅ أكمل هذا الدليل | Complete this guide
2. 📖 اقرأ DEVELOPMENT.md | Read DEVELOPMENT.md
3. 🎯 اختر Issue #1 | Pick Issue #1
4. 🚀 ابدأ العمل! | Start working!

---

**تذكر | Remember:** هذا مشروع تعليمي! الهدف هو التعلم، لا تتحرج من ارتكاب الأخطاء.
**Remember:** This is a learning project! The goal is to learn. Don't be afraid to make mistakes.

**بالتوفيق! | Good luck! 🎉**
