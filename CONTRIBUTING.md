# 🤥 المساهمة في المشروع | Contributing to Local Note

نحن نرحب بالمساهمات! هذا دليل لكيفية المساهمة في المشروع.
We welcome contributions! This is a guide on how to contribute to the project.

---

## 📋 جدول المحتويات | Table of Contents
- [أنواع المساهمات](#أنواع-المساهمات--types-of-contributions)
- [كيفية البدء](#كيفية-البدء--how-to-get-started)
- [عملية التطوير](#عملية-التطوير--development-workflow)
- [معايير الكود](#معايير-الكود--code-standards)
- [اختبار الكود](#اختبار-الكود--testing)
- [إرسال Pull Request](#إرسال-pull-request--submitting-pull-requests)

---

## 🎯 أنواع المساهمات | Types of Contributions

### ما الذي يمكنك المساهمة به؟ | What can you contribute?

#### 🐛 تقارير الأخطاء | Bug Reports
- وجدت خطأ؟ أخبرنا! | Found a bug? Tell us!
- استخدم قالب "Bug Report" | Use the "Bug Report" template
- أضف تفاصيل تكرار الخطأ | Include reproduction details

#### ✨ اقتراحات الميزات | Feature Requests
- فكرة لميزة جديدة؟ | Idea for a new feature?
- استخدم قالب "Feature Request" | Use the "Feature Request" template
- اشرح حالة الاستخدام | Explain the use case

#### 📖 تحسينات الوثائق | Documentation Improvements
- أخطاء إملائية؟ | Typos?
- شروحات غير واضحة؟ | Unclear explanations?
- اقتراحات للتحسين؟ | Improvement suggestions?

#### 💻 تحسينات الكود | Code Contributions
- إصلاح الأخطاء | Bug fixes
- إضافة ميزات | Adding features
- تحسين الأداء | Performance improvements
- إعادة هيكلة | Refactoring

---

## 🚀 كيفية البدء | How to Get Started

### 1. استنساخ المشروع | Clone the Project
```bash
git clone https://github.com/your-username/local-note.git
cd local-note
```

### 2. إنشاء فرع | Create a Branch
```bash
git checkout -b feature/your-feature-name
# أو | or
git checkout -b fix/your-bug-fix
```

### 3. إعداد البيئة | Setup Environment
```bash
# إنشاء بيئة افتراضية | Create virtual environment
python -m venv .venv

# تفعيل البيئة | Activate environment
# Windows
.venv\\Scripts\\activate
# macOS/Linux
source .venv/bin/activate

# تثبيت المتطلبات | Install requirements
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 4. تشغيل الاختبارات | Run Tests
```bash
pytest
```

---

## 🔄 عملية التطوير | Development Workflow

### 1. اختر قضية | Pick an Issue
```bash
# عرض القضايا المفتوحة | List open issues
gh issue list

# تعيين قضية لنفسك (بعد الموافقة) | Assign issue to yourself
gh issue edit <issue-number> --add-assignee @me
```

### 2. ابدأ العمل | Start Working
```bash
# أنشئ فرع من main | Create branch from main
git checkout main
git pull origin main
git checkout -b feature/<issue-number>-short-description
```

### 3. اكتب الكود | Write Code
- اتبع معايير الكود | Follow code standards
- اكتب اختبارات | Write tests
- وثق التغييرات | Document changes
- التزم بشكل متكرر | Commit frequently

```bash
git add .
git commit -m "feat: implement feature description (#<issue-number>)"
```

### 4. اختبارات شاملة | Comprehensive Testing
```bash
# تشغيل جميع الاختبارات | Run all tests
pytest

# تشغيل مع تغطية الكود | Run with coverage
pytest --cov=. --cov-report=html

# فحص نوع الكود | Type check
mypy .
```

### 5. ادفع وأنشئ PR | Push and Create PR
```bash
git push origin feature/<issue-number>-short-description

# إنشاء Pull Request | Create PR
gh pr create --title "Issue #<issue-number>: Brief description" \\
    --body "Closes #<issue-number>"
```

---

## 📏 معايير الكود | Code Standards

### 🐍 Python Style Guide
نتبع PEP 8 مع بعض التعديلات:
We follow PEP 8 with some modifications:

```python
# ✅ جيد | Good
class NoteManager:
    def __init__(self, base_path: Path):
        self._base_path = base_path
    
    def create_note(self, title: str, content: str) -> Note:
        """إنشاء ملاحظة جديدة | Create a new note"""
        note = Note(title=title, content=content)
        self._save_note(note)
        return note

# ❌ سيء | Bad
class notemanager:
    def __init__(self,path):
        self.path=path
```

### قواعد التسمية | Naming Rules
- **Classes**: PascalCase (`NoteManager`)
- **Functions**: snake_case (`create_note`)
- **Constants**: UPPER_SNAKE_CASE (`MAX_NOTES`)
- **Private**: _leading_underscore (`_internal_method`)

### التنسيق | Formatting
```bash
# استخدام black للتنسيق | Use black for formatting
black .

# استخدام pylint للفحص | Use pylint for linting
pylint **/*.py
```

---

## 🧪 اختبار الكود | Testing

### كتابة الاختبارات | Writing Tests
```python
import pytest
from pathlib import Path
from local_note.core import Note

def test_note_creation():
    """اختبار إنشاء ملاحظة | Test note creation"""
    note = Note(title="Test", content="Content")
    assert note.title == "Test"
    assert note.content == "Content"

@pytest.mark.parametrize("title,content,expected_words", [
    ("Hello", "World test", 2),
    ("Test", "Single", 1),
])
def test_word_count(title, content, expected_words):
    """اختبار حساب الكلمات | Test word count"""
    note = Note(title=title, content=content)
    assert note.word_count == expected_words
```

### معايير الاختبار | Testing Standards
- ✅ تغطية 80% كحد أدنى | 80% coverage minimum
- ✅ اختبار جميع الوظائف العامة | Test all public functions
- ✅ اختبار الحالات الحدية | Test edge cases
- ✅ استخدام fixtures بذكاء | Use fixtures wisely

---

## 📤 إرسال Pull Request | Submitting Pull Requests

### قائمة التحقق | Checklist
قبل إرسال PR، تأكد من:
Before submitting a PR, make sure:

- [ ] ✨ جميع الاختبارات تمر | All tests pass
- [ ] 📝 الكود موثق | Code is documented
- [ ] 🎨 الكود منسق | Code is formatted
- [ ] 📖 الوثائق محدث | Documentation updated
- [ ] 🔗 يربط بقضية | Links to an issue
- [ ] 💬 واضح الوصف | Description is clear

### وصف PR الجيد | Good PR Description
```markdown
## 📋 Description | الوصف
إضافة وظيفة البحث في الملاحظات
Adds note search functionality

## 🎯 Related Issue | القضية المرتبطة
Closes #8

## ✅ Changes | التغييرات
- Added \`search_notes()\` function in \`core.py\`
- Added unit tests in \`test_search.py\`
- Updated README with usage examples

## 🧪 Testing | الاختبار
```bash
pytest tests/test_search.py -v
# All tests passing ✅
```

## 📸 Screenshots | لقطات الشاشة
![search-demo](screenshots/search.png)

## 📝 Notes | ملاحظات
- Uses case-insensitive matching
- Supports regex patterns
```

---

## 🎨 Code Review Process

### ما الذي نبحث عنه؟ | What We Look For?
1. **الصحة** | Correctness: Does it work?
2. **النمط** | Style: Does it follow standards?
3. **الاختبارات** | Tests: Are tests comprehensive?
4. **الوثائق** | Documentation: Is it documented?
5. **الأداء** | Performance: Is it efficient?

### التعامل مع التعليقات | Handling Feedback
- 🙏 استقبل التعليقات بصدر رحب | Accept feedback graciously
- 💬 ناقش إذا كان هناك خلاف | Discuss if disagree
- ✏️ عدل حسب الاقتراحات | Edit per suggestions
- 🎯 ركز على الهدف: كود أفضل | Focus on goal: better code

---

## 🎉 بعد الدمج | After Merging

### الخطوات التالية | Next Steps
1. 🗑️ احذف الفرع | Delete your branch
   ```bash
   git branch -d feature/your-feature
   ```

2. 🎉 احتفل! | Celebrate!
   - لقد ساهمت في مشروع مفتوح المصدر! | You contributed to open source!

3. 🔄 كرر! | Repeat!
   - اختر قضية أخرى | Pick another issue

---

## ❓ الأسئلة الشائعة | FAQ

### هل يمكنني المساهمة بدون خبرة؟ | Can I contribute without experience?
**نعم!** | **Yes!** هذا مشروع تعليمي، نرحب بالمبتدئين!
This is a learning project, beginners are welcome!

### كم من الوقت يستغرق مراجعة PR؟ | How long for PR review?
عادة 1-3 أيام | Usually 1-3 days

### ماذا لو رفض PR؟ | What if PR is rejected?
لا مشكلة! نوضح لك السبب ونساعدك في الإصلاح
No problem! We'll explain why and help you fix it

---

## 📞 التواصل | Contact

- 💬 Discord: https://discord.gg/local-note
- 📧 Email: contribute@local-note.dev
- 🐦 Twitter: @localnote_dev

---

**شكراً لاهتمامك بالمشاركة! 🙏**
**Thanks for your interest in contributing! 🙏**
