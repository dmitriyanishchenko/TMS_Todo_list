<h1 align='center'> TODO List</h1>

<p> Данное приложение представляет собой планировщик задач </p>

<h2> Инструкция по установке </h2>

<p> Изначально необходимо клонировать источник локально:</p>
<pre>
    $ git clone https://github.com/dmitriyanishchenko/TMS_Todo_list.git
</pre>
<p> Далее нужно перейти в каталог с проектом, выполнив команду:</p>
<pre>
    $ cd TMS_Todo_list/
</pre>
<p> Обновите список пакетов и установите pip для Python 3:</p>
<pre>
      $ sudo apt update
      $ sudo apt install python3-pip
</pre>
<p> После завершения установки проверьте версию pip:</p>
<pre>
      $ pip3 --version
</pre>
<p> Вы по-прежнему находитесь в каталоге /TMS_Todo_list/, создайте и активируйте виртуальную среду:</p>
<pre>
      $ virtualenv -p python3.7 .venv
      $ source .venv/bin/activate
</pre>
<p> Далее установите все зависимости из файла requirements.txt, выполнив команду:</p>
<pre>
      $ pip install -r requirements.txt
</pre>
<p> Перейдите в каталог / todo /, инициализируйте базу данных и запустите сервер:</p>
<pre>
      $ cd todo/
      $ python manage.py migrate
      $ python manage.py runserver
</pre>
<p>Откройте Ваш браузер в новом окне и перейдите на localhost, для этого Вам необходимо ввести в строку ввода:</p>
<pre>
      http://127.0.0.1:8000/
</pre>