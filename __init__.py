from .filterwords import start_filtering

# Додаємо пункт у меню Anki для запуску фільтрації
from aqt import mw
from aqt.qt import QAction

action = QAction("Фільтрація за відомими словами та фразами", mw)
action.triggered.connect(start_filtering)
mw.form.menuTools.addAction(action)