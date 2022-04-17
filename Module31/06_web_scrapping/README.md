## Задача 6. Web scraping
### Что нужно сделать
Дан несложный пример HTML-страницы: [Sample Web Page](http://www.columbia.edu/~fdc/sample.html).

Изучите код этой страницы и реализуйте программу, которая получает список всех подзаголовков сайта (они заключены в теги `h3`).

Ожидаемый результат:
```python
['CONTENTS', '1. Creating a Web Page', '2. HTML Syntax', '3. Special Characters', '4. Converting Plain Text to HTML', '5. Effects', '6. Lists', '7. Links', '8. Tables', '9. Viewing Your Web Page', '10. Installing Your Web Page on the Internet', '11. Where to go from here', '12. Postscript: Cell Phones']
```
Сделайте так, чтобы программа работала для любого сайта, где есть такие теги.
### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- Решение опирается на использование регулярных выражений и их методов.
- Переменные, функции и собственные методы классов имеют значащие имена, не `a`, `b`, `c`, `d`.
