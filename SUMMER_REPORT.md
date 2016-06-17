Отчет о реализации проекта "Имиджборд"
========================================

Выполнил
--------------
Студент группы БПМИ146 2-го курса ПМИ ФКН ВШЭ  
Илья Соловьев  
(В рамках полугодового проекта, расчитанного на второй семестр)

Итоговый результат
--------------
Реализован полноценный форум, удовлетворяющий поставленным требованиям.  
С результатом можно ознакомиться, перейдя по ссылке ниже:  

[Ссылка] []
[Ссылка]: http://iluhandric.pythonanywhere.com/


Формальная постановка задачи
-----------------
_Цитата из wiki.cs.hse.ru:_
>Система анонимных форумов с возможностью прикреплять к сообщениям изображения (аналоги: iichan.hk). Сервис состоит из набора разделов (досок), в которых пользователи могут начать обсуждение (тред) и писать комментарии в существующих тредах. Экран доски отображает список тредов и последние N комментариев, треды отсортированы по дате обновления. Пользователь идентифицируется по IP и cookie, но для неадминистратора не должно быть возможности ассоциировать сообщения с одним пользователем. Администратор должен иметь возможность создавать/удалять доски, редактировать и удалять сообщениях, также должна быть возможность удалить разом все сообщения определенного пользователя и запретить ему писать новые.


Реализация формальных критериев
-------------------------------
**Минимальная функциональность:**

    + В приложении можно создавать треды и комментарии.
    + Можно прикреплять к сообщениям изображения.
    + Приложение защищено от инъекций к базе, XSS-атак.
**На хорошо:**

    + Находясь на странице треда, можно подгрузить новые ответы, если они есть без перезагрузки страницы.

**На отлично:**

    + Реализованы все функции, доступные администратору (см. описание)
    + В реальном времени отображается количество просматривающих доску или тред
    +/- Сервис готов к запуску (по чеклисту выполнено все или почти все)

Работа над проектом
-------------------


### Модели

Следуя стандартам Django, классы моделей, испульзуемые в проекте блыли реализованы в файле models.py.

Список реализованых моделей (каждая из которых унаследована от класса _django.db.models.Model_):

* Tag - тег, опциональная особенность каждого треда, все теги уникальны;  
* Topic - топик, модель, определяющая обширную тематику обсуждений в содержащихся тредах;
* Thread - тред, задающий главную проблематику обсуждения, может содержать название, текст, теги и изображение;
* Comment - комментарий, оставленный под определенным тредом и закрепленный за ним (может содержать изображение);
* Blocked - содержит IP заблокированных пользователей (при отправлении каждого запроса проверяется, содержится ли ip-адрес клиента в данной таблице);
* UserIp - содержит ip и время последнего отклика на определенном треде, используя содержимое этой таблицы, вычисляется количество ip-адресов, просматривающих тот или иной тред;
    
___
В качестве примера можно взглянуть на реализацию класса модели Thread:

    class Thread(models.Model):
        title = models.CharField(max_length=60)
        text = models.TextField(blank=True, max_length=500)
        parent = models.BigIntegerField(blank=False)
        comments = models.ManyToManyField(Comment, blank=True)
        tags = models.CharField(max_length=100, blank=True)
        parsed_tags = models.ManyToManyField(Tag, blank=True)
        time_posted = models.DateTimeField(default=timezone.now)
        image = models.ImageField(upload_to=get_unique_path, blank=True)
        users = models.ManyToManyField(UserIp, blank=True)
        author_ip = models.CharField(max_length=100, default='unknown')

Более подробно схему базы данных и отношения между моделями можно узнать из файла _DBscheme.png_, находящегося в репозитории.
    
### Шаблоны 
 
 
    base.html - оболочка для остальных страниц, содержащая navbar и подключаемая с помощью "{% extends ... %}" 
    
    blocked.html - страница, гласящая о том, что ip клиента заблокирован
    
    home_page.html - landing page, домашняя страница, представляющая основную информацию о продукте
    
    new_thread.html - страница с формой для создания нового треда	
    
    search.html	- результаты поиска по запросу
    
    tag_results.html - список всех тредов, содержащих запрашиваемый тег
    
    tags.html - список тегов с количесвом раз использования для каждого
    
    thread.html - страница треда, содержащая тело треда и посление 10 комментариев (можно пролистывать на более ранние)
    
    topic_content.html - список всех тредов в топике с отображением даты создания и количества комментариев для каждого
    
    topics.html - сетка топиков в виде карточек
    
    topics_list.html - список топиков (альтернативное представление предыдущего экрана)


### Фронтенд и дизайн

В ходе работы было спроектирвано и отвергнуто множество вариантов интерфейса сайта. Работа над внешней составляющей и удобством использования продолжалась в течение всего срока разработки форума. HTML5 дал много возможностей для оптимальной разметки сайта.

Для достижения конечного результата испольовались внешние ресурсы:

* Twitter Bootstrap  -  удобная CSS библиотека, предоставляющая множество resizable элементов  
    * navigation bar  - для навигации по разделам home_page/topics/tags
    * cards - для видуализации топиков в представлении сеткой
    * cols and rows - для разбиения страницы на колонки адаптивной ширины
* Icons - некоторая часть интерфейса выполнена в виде кликабельных иконок
    * Font Awesome Icons 
    * Glyphicons 
* Google Fonts - подключение шрифтов  

Для введения новых особенностей использовалась анимация на CSS, стандартные фильтры изображений (увеличение яркости при наведении) (Неоптимально объемно символами описывать весь дизайн проекта, картинка скажет сама за себя)

### Работа бекенда

Для получения обратной связи клиентом посланный им запрос идентифицируется с помощью паттернов в файле urls.py. Далее необходимые аругменты передаются на вход некоторому "вью" (функции из view.py), которая, в свою очередь, выполняя, если необходимо GET/POST методы, возвращает, если требуется, новую страницу.

Приведем пример.  
Пусть пользователь находится в списке тредов какого-то топика. Теперь он хочет перейти в определенный тред и кликает на соответвующую ссылку.

Данная ссылка в коде шаблона задается так:

```python
href="{% url 'thread'  par=cur_topic.pk pk=thread.pk%}"
```

Она удовлетворяет следующему паттерну:

```python
url(r'^topics/(?P<par>[0-9]+)/threads/(?P<pk>[0-9]+)$', views.thread, name='thread')
```
    
Соответсвенно, далее вызывается функция `thread(request, par, pk)`:
```python
def thread(request, par, pk):
    cur_thread = get_object_or_404(Thread, pk=pk)
    comments = cur_thread.comments.all().order_by('-time_posted')
    cp = get_object_or_404(Topic, pk=cur_thread.parent)
    form = CommentForm()
    return render(request, get_template('thread'), {'cur_thread': cur_thread, 
                                                    'comments': comments, 
                                                    'form': form,
                                                    'cur_parent': cp})

```
Пользователю возвращается шаблон для данного треда с формой, и подгружаются все комментарии.
Таким образом, юзер перешел на запрашиваемую страницу. Заметим, что ее url удовлетворяет регулярному выражению  

`^topics/(?P<par>[0-9]+)/threads/(?P<pk>[0-9]+)`, где par - id топика, а pk - id треда.


### Features

#### Фоны топиков

Для каждого топика определен тематический фон (файл которого хранится по переменной logo класса Topic), отображающийся в карточках при выборе топика. При просмотре списка тредов данного топика и любого треда внутри него это изображение будет являться фоном всей страницы.  
Таким образом, выбирая ненавязчивые, но оптимальные по тематике изображение для топиков, можно добиться разбиения форума на разделы с индивидуальной "атмосферой" минимальными средствами, свзяв его с топиком, по при этом не уменьшая общности и шаблонности вссех страниц сайта.


#### Имена для файлов изображений

Для удобства обращения все файлы изображений, загруженных как прикрепленные к тредам/комментариям или как лого топиков, хранятся в одной директории. Проблема заключается в случае, если пользователь загружает разные фотографии с одинаковым именем файла, например "1.jpg". Для решения этой задачи было предпринято следующее. Каждому загружаемому изображению дается случайное имя (повторяющееся с пренебрежимо малой вероятностью)генерируемое в функции:
```python
def get_unique_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('./', filename)
```

#### Администрирование и блокировка  
Django предоставляет администрирование для созданных админов. Используя данную возможность, войдя со специального url, можно просматривать и исправлять все поля всех объектов.  

Соответственно, администратор может изменять и удалять весь контент на форуме.
Класс комментария содержит поле author_ip (в данную переменную записывается ip-адрес отправителя), невидимое для любого, кто использует обычную версию сайта. Значение данного поля можно посмотреть через вышеупомянутое djangoadministration. 
Далее, если необходимо заблокировать пользователя, данное строковое значение помещается в новый объект класса Blocked.
Теперь, как было сказано ранее, 
> Blocked - содержит IP заблокированных пользователей (при отправлении каждого запроса проверяется, содержится ли ip-адрес клиента в данной таблице)

За это отвечают следующие строчки при обработке запроса:
```python
if is_blocked(request):
       return render(request, get_template('blocked'))
```
где 
```python
def is_blocked(request):
    user_ip = get_client_ip(request)
    try:
        response = Blocked.objects.get(address=user_ip)
        return True
    except Blocked.DoesNotExist:
        return False
    except Blocked.MultipleObjectsReturned:
        return True
```

#### Количество просматривающих

Функция, проверяющая наличие пользовотеля по ip в таблице UserIP и истечение таймаута, таким образом считает количество подключенных пользователей:
```python
def counter(request):
    if is_blocked(request):
        return render(request, get_template('blocked'))
    thread_pk = request.GET["pk"]
    cur_ip = get_client_ip(request)
    cur_thread = Thread.objects.get(pk=thread_pk)
    is_new = True
    for user in cur_thread.users.all():
        if user.ip == cur_ip:
            user.last_request = timezone.now()
            user.save()
            is_new = False
        else:
            if (timezone.now() - user.last_request).total_seconds() > 10:
                user.delete()
    if is_new:
        new_user = UserIp(ip=cur_ip, last_request=timezone.now())
        new_user.save()
        cur_thread.users.add(new_user)
        cur_thread.save()
    count = len(cur_thread.users.all())
    data = dict()
    data["count"] = count
    return HttpResponse(json.dumps(data), content_type='application/json')
```

Для ее вызова используется функция на js

```javascript
$.fn.updateCounter = function (){
    $.getJSON("/api/counter.json?pk=" + pk).done(function(json){
        $("#counter").html("People viewing: " + json["count"])
    });
};
```

#### Отправка комментария

Оправка комментария осуществляется через апи вью, вызываемым ajax-запросом:
```javascript
$('#post_comment').submit(function(e){
    $('#image').src = "";
    var info  = new FormData($(this)[0]);
    $.ajax({
        url: "/api/post_comment.json?pk=" + pk,
        data: info,
        processData: false,
        contentType: false,
        type: 'POST',
        dataType:'json',
        success: function (data) {
             if (data) {
                 $.fn.reloadComments();
             } else {
                 alert('You cannot send empty comment or comment with not image files!');
             }
        },
    });
    e.preventDefault();
    $(this).closest('form').find("input[type=text], textarea").val("");
    $('#file').trigger("change");
    $.fn.reloadComments();
    $('#image').src = "";
});
```
Где вызываемое вью:
```python
@api_view(['GET', 'POST', 'FILES'])
def new_comment(request):
    form = CommentForm(request.POST, request.FILES)
    if form.is_valid():
        comment = Comment(text=request.POST.get('text', False).replace('<', '&lt'), 
                            image=request.FILES.get('image'))
        comment.parent = request.GET["pk"]
        comment.time_posted = timezone.now()
        comment.author_ip = get_client_ip(request)
        comment.save()
        thread_pk = request.GET["pk"]
        cur_thread = Thread.objects.get(pk=thread_pk)
        cur_topic = Topic.objects.get(pk=cur_thread.parent)
        cur_topic.comments.add(comment)
        cur_thread.comments.add(comment)
    return Response(form.is_valid())
```

#### Подгрузка комментариев

При нажатиии на кнопку перезагрузки(а также при отправке комментария, загрузке страницы и тд) вызывается функция, возвращающая комментарии через json
```python
@api_view(['GET', 'POST'])
def get_comments(request):
    if is_blocked(request):
        return render(request, get_template('blocked'))
    if not is_blocked(request):
        thread_pk = request.GET["pk"]
        cur_thread = Thread.objects.get(pk=thread_pk)
        comments = cur_thread.comments.all().order_by('-time_posted')
        data = []
        for com in comments:
            new_obj = model_to_dict(com)
            for field in new_obj:
                if field == 'time_posted':
                    new_obj[field] = new_obj[field].strftime("%Y/%m/%d %H:%M:%S")
                if field and field != 'time_posted':
                    new_obj[field] = str(new_obj[field])

            data.append(new_obj)
    else:
        data = [{'text': 'YOU ARE BLOCKED AND NOT ALLOWED TO VIEW OR POST ANYTHING', 'time_posted': ''}]
    return Response(json.dumps(data), content_type='application/json')
```
### Ещё:

* Можно прикреплять к треду/комментарию изображения
* Перед отправкой треда/комментария отображается превью загруженных изображений
* Работает поиск (whoosh) по словам из названия, тела, тегов треда (при добавлении треда его индексация происходит автоматически)
* Если в треде > 10 комментариев, то их можно пролистывать вперед/назад без перезакрузки страницы
* Сортировка тредов и комментариев по новизне
* Вложены душа, время и силы
