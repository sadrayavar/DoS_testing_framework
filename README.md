# DoS Testing Local Tool [(Click)](https://github.com/sadrayavar/DoS_testing_framework)

I developed this simple tool to test DoS mitigation tools.<br>
This tool has 2 parts:

- Target website
- StressTester

<br>

### Usage

Execute the following commands in the given order (for the first time):

- `python manage.py makemigrations`
- `python manage.py migrate`
- `pip3 install gunicorn`

<br>

Then you can start the server each time using the following command:

- `gunicorn DoS_testing_website.wsgi:application --config gunicorn.py`

<br>
<br>

### Recommendation

I suggest you run this project as a `docker-compose` service and limit its resources using the `cpus` and `mem_limit` attributes so your system does not crash.

<br>
<br>
<br>

## StressTester

The StressTester tool is a Python code that uses the "requests" library and has 2 classes:

- `Get`
- `Ui`

### Get

Is for getting files from a specific URL and saving them to the "downloads" directory.

### Ui

Is for getting the URL and selecting the attack type and value through a Python command.

<br>
<br>
<br>

## Website

The website has 3 pages for the hardware resources involved in a typical DoS attack:

- Bandwidth
- CPU
- RAM

<br>

### Bandwidth (http://localhost/bw)

Displays a list of the files in the "static" folder of the Django project. After you select one of them, it will redirect you to "http://localhost/bw/&lt;fileName&gt;" to download the respective file.

<br>

### CPU (http://localhost/cpu)

It will ask you for a number and then redirect you to "http://localhost/cpu/&lt;givenNumber&gt;". After that, it will calculate its runtime, digits, and result itself.

If a non-integer value is given, it will redirect you to "http://localhost/cpu" so you can enter a new value.

<br>

### RAM (http://localhost/ram)

Just like the CPU section, it will ask you for a number and then redirect you to "http://localhost/ram/&lt;givenNumber&gt;". After that, it will load 100MB every &lt;givenNumber&gt; seconds.<br>
Be aware to stop it before your RAM fills up using the Django terminal.

If a non-number is given, it will redirect you to "http://localhost/ram" so you can enter a new value.
