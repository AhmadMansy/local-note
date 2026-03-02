# 🚀 دليل التطوير | Development Workflow Guide

## 📅 Weekly Learning Schedule | الجدول الأسبوعي للتعلم

### الأسبوع الأول | Week 1: Setup & Fundamentals | الإعداد والأساسيات
**الأهداف | Goals:**
- إعداد بيئة العمل | Setup development environment
- فهم البنية الأساسية | Understand basic structure
- أول مهمة برمجية | Complete first coding task

**المهام | Tasks:**
- [ ] Issue #1: Virtual Environment Setup
- [ ] Issue #2: Note Class Implementation
- [ ] Read: Chapters 1-3 from developer guide

**نقاط التحقق | Checkpoints:**
- 🎯 يوم الثلاثاء | Tuesday: Environment ready
- 🎯 يوم الخميس | Thursday: First test passing

---

### الأسبوع الثاني | Week 2: File System Operations | عمليات نظام الملفات
**الأهداف | Goals:**
- التعامل مع الملفات | File I/O operations
- كتابة الاختبارات | Writing tests
- فهم pathlib | Understanding pathlib

**المهام | Tasks:**
- [ ] Issue #3: File Manager (Create/Read)
- [ ] Issue #4: File Manager (Update/Delete)
- [ ] Issue #6: Unit Tests

**نقاط التحقق | Checkpoints:**
- 🎯 منتصف الأسبوع | Mid-week: File operations working
- 🎯 نهاية الأسبوع | Weekend: All tests passing

---

### الأسبوع الثالث | Week 3: Advanced Logic | المنطق المتقدم
**الأهداف | Goals:**
- معالجة Markdown | Markdown processing
- البحث والتصفية | Search and filtering
- التعبيرات النمطية | Regex patterns

**المهام | Tasks:**
- [ ] Issue #7: Markdown Parser
- [ ] Issue #8: Basic Search
- [ ] Issue #9: Advanced Search (Regex)
- [ ] Issue #10: Tag Extraction

**نقاط التحقق | Checkpoints:**
- 🎓 اجتماع منتصف الأسبوع | Mid-week meeting: Progress review
- 🎯 نهاية الأسبوع | Weekend: All backend features done

---

### الأسبوع الرابع | Week 4: GUI Basics | أساسيات الواجهة
**الأهداف | Goals:**
- بناء الواجهة الرئيسية | Build main window
- فهم CustomTkinter | Understand CustomTkinter
- ربط المكونات | Connect components

**المهام | Tasks:**
- [ ] Issue #11: Main Window Setup
- [ ] Issue #12: Sidebar File Tree
- [ ] Issue #13: Text Editor Widget

**نقاط التحقق | Checkpoints:**
- 🎯 يوم الأربعاء | Wednesday: Basic UI visible
- 🎯 نهاية الأسبوع | Weekend: Can open and edit notes

---

### الأسبوع الخامس | Week 5: GUI Advanced | الواجهة المتقدمة
**الأهداف | Goals:**
- ربط الواجهة بالمنطق | Connect UI to logic
- إضافة الوظائف | Add functionality
- تحسين تجربة المستخدم | Improve UX

**المهام | Tasks:**
- [ ] Issue #14: Connect Tree to Editor
- [ ] Issue #15: Save Functionality
- [ ] Issue #16: Create/Delete Actions

**نقاط التحقق | Checkpoints:**
- 🎓 اجتماع منتصف الأسبوع | Mid-week: Demo of working app
- 🎯 نهاية الأسبوع | Weekend: All CRUD operations working

---

### الأسبوع السادس | Week 6: Polish & Features | التحسين والميزات
**الأهداف | Goals:**
- إضافة الميزات المتقدمة | Add advanced features
- تحسين المظهر | Improve appearance
- اختبار شامل | Comprehensive testing

**المهام | Tasks:**
- [ ] Issue #17: Preview Pane
- [ ] Issue #18: Search UI
- [ ] Issue #19: WikiLinks
- [ ] Issue #20: Tag Cloud

**نقاط التحقق | Checkpoints:**
- 🎯 منتصف الأسبوع | Mid-week: All features implemented
- 🎯 نهاية الأسبوع | Weekend: Testing complete

---

### الأسبوع السابع | Week 7: Documentation & Release | الوثائق والإصدار
**الأهداف | Goals:**
- كتابة الوثائق | Write documentation
- إصلاح الأخطاء | Fix bugs
- التحضير للإصدار | Prepare for release

**المهام | Tasks:**
- [ ] Issue #21: Final Documentation
- [ ] Code review and cleanup
- [ ] Create release notes

**نقاط التحقق | Checkpoints:**
- 🎓 منتصف الأسبوع | Mid-week: Documentation complete
- 🎉 نهاية الأسبوع | Weekend: RELEASE! 🎉

---

## 🔄 Daily Workflow | روتين اليوم

### بداية اليوم | Start of Day
```bash
# 1. Check for updates | تحقق من التحديثات
git pull origin main

# 2. Check your assigned issues | تحقق من القضايا المسندة
gh issue list --assignee @me

# 3. Activate virtual environment | تفعيل البيئة الافتراضية
# Windows
.venv\\Scripts\\activate
# macOS/Linux
source .venv/bin/activate

# 4. Run tests | تشغيل الاختبارات
pytest
```

### أثناء العمل | During Work
```bash
# 1. Create feature branch | إنشاء فرع للميزة
git checkout -b feature/issue-number-description

# 2. Work on your task | العمل على المهمة
# Write code, test frequently

# 3. Run tests often | شغل الاختبارات بشكل متكرر
pytest -v

# 4. Commit frequently | التزم بشكل متكرر
git add .
git commit -m "feat: implement note class (#2)"
```

### نهاية اليوم | End of Day
```bash
# 1. Push your work | ادفع عملك
git push origin feature/issue-number-description

# 2. Create pull request | إنشاء طلب سحب
gh pr create --title "Implement Issue #X" --body "Closes #X"
```

---

## 📝 Commit Message Convention | اتفاقية رسائل الالتزام

### Format | التنسيق: `<type>: <description> (#issue-number)`

### الأنواع | Types:
- `feat`: ميزة جديدة | New feature
- `fix`: إصلاح خطأ | Bug fix
- `docs`: تحديث الوثائق | Documentation
- `style`: تنسيق الكود | Code formatting
- `refactor`: إعادة هيكلة | Code restructuring
- `test`: إضافة اختبارات | Adding tests
- `chore`: صيانة عامة | Maintenance

### أمثلة | Examples:
```bash
git commit -m "feat: add markdown parser (#7)"
git commit -m "fix: resolve file encoding issue (#3)"
git commit -m "docs: update README with screenshots (#21)"
```

---

## 🧪 Testing Guidelines | إرشادات الاختبار

### قبل الالتزام | Before Committing:
```bash
# Run all tests | شغل جميع الاختبارات
pytest

# Run specific test file | شغل ملف اختبار محدد
pytest tests/test_note.py

# Run with coverage | شغل مع نسبة التغطية
pytest --cov=. --cov-report=html

# View detailed output | عرض تفاصيل الإخراج
pytest -v -s
```

### كتابة الاختبارات | Writing Tests:
```python
def test_specific_feature():
    # Arrange - إعداد البيانات
    note = Note(title="Test", content="Content")
    
    # Act - تنفيذ العملية
    result = note.word_count
    
    # Assert - التحقق من النتيجة
    assert result == 1
```

---

## 📚 Learning Resources | موارد التعلم

### Python Basics:
- 📖 [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- 🎥 [Corey Schafer's Python Videos](https://youtube.com/user/schafer5)

### Testing:
- 📖 [Pytest Documentation](https://docs.pytest.org/)
- 🎥 [Armitage's Python Testing Course](https://youtube.com/)

### GUI Development:
- 📖 [CustomTkinter Docs](https://customtkinter.tomschimansky.com/)
- 📖 [Tkinter Docs](https://docs.python.org/3/library/tkinter.html)

### Git & GitHub:
- 📖 [Pro Git Book](https://git-scm.com/book)
- 🎥 [GitHub Skills](https://skills.github.com/)

---

## 💬 Communication Guidelines | إرشادات التواصل

### طلب المساعدة | Asking for Help:
1. 📝 اشرح المشكلة بوضوح | Clearly explain the problem
2. 💾 أضف لقطة شاشة | Include screenshots
3. 🔗 أضف رابط الكود | Share code link
4. 🏷️ استخدم التاغات المناسبة | Use appropriate tags

### اجتماعات أسبوعية | Weekly Meetings:
- **🎯 يوم الأحد | Sunday**: Plan week's tasks
- **📊 يوم الأربعاء | Wednesday**: Progress check
- **🎉 يوم الجمعة | Friday**: Demo completed work

---

## ⚠️ Troubleshooting | حل المشكلات

### مشكلة | Problem: Virtual environment not activating
**حل | Solution:**
```bash
# Windows
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# macOS/Linux
chmod +x .venv/bin/activate
```

### مشكلة | Problem: Tests failing
**حل | Solution:**
```bash
# Clear cache | مسح الذاكرة المؤقتة
find . -type d -name "__pycache__" -exec rm -r {} +

# Reinstall dependencies | إعادة تثبيت المتطلبات
pip install -r requirements.txt --force-reinstall
```

### مشكلة | Problem: Git conflicts
**حل | Solution:**
```bash
# Pull with rebase | السحب مع إعادة الأساس
git pull --rebase origin main

# Resolve conflicts manually | حل التعارضات يدوياً
# Then:
git add .
git rebase --continue
```

---

## 🌟 Pro Tips | نصائح احترافية

### للتعلم السريع | For Fast Learning:
1. 🎨 ارسم مخططاً قبل الكود | Draw diagrams before coding
2. 🧪 اكتب الاختبار أولاً | Write tests first (TDD)
3. 📖 اقرأ كود الآخرين | Read others' code
4. 🎥 شاهد دروس تعليمية | Watch tutorial videos
5. 🤝 اسأل عندما تعلق | Ask when stuck

### لتطوير أفضل | For Better Development:
1. 🔄 التزم بكثير | Commit frequently
2. 📝 اكتب رسائل واضحة | Write clear messages
3. 🧪 اختبر دائماً | Always test
4. 📚 وثق الكود | Document code
5. 🎯 ركز على مهمة واحدة | Focus on one task

---

**تذكر | Remember:** هذا مشروع تعليمي! الهدف هو التعلم، لا تتحرج من ارتكاب الأخطاء.
**Remember:** This is a learning project! The goal is to learn. Don't be afraid to make mistakes.
