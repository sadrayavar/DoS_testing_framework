# DoS testing local tool [(Click)](https://github.com/sadrayavar/DoS_testing_framework)

I developed this simple tool to test the DoS mitigation tools.<br>
This tool has 2 parts which are:

- Target website
- Attacker

<br>

### Usage

Execute following commands in given order (for the first time):

- `python manage.py makemigrations`
- `python manage.py migrate`
- `pip3 install gunicorn`

<br>

Then you can start server each time using below command:

- `gunicorn DoS_testing_website.wsgi:application --config gunicorn.py`

<br>
<br>

### Recommendation

I suggest you run this Project as a `docker-compose` service and limit its resources using `cpus` and `mem_limit` attributes so your system does not crash.

<br>
<br>
<br>

## Attacker

The attacker tool is a python code that uses "request" library and it has 2 classes which are:

- `Get`
- `Ui`

### Get

Is for getting files from specific URL and save it to "downloades" directory.

### Ui

Is for getting url and selecting attack type and value thorugh python command.

<br>
<br>
<br>

## Website

The website has 3 pages for any Hardware resources that are involved in a typical DoS attack:

- Bandwidth
- CPU
- RAM

<br>

### Bandwidth (http://localhost/bw)

Displays list of the files that are in the "static" folder of django project. After you select one of them, It will redirect you to "http://localhost/bw/&lt;fileName&gt;" to download the respective file.

<br>

### CPU (http://localhost/cpu)

It will ask you a number and will redirect you to "http://localhost/cpu/&lt;givenNumber&gt;". After that it will calculate its runtime, digits and result itself.

If non integer value given, It will redirect you to "http://localhost/cpu" so you can enter a new value.

<br>

### RAM (http://localhost/ram)

Just like the CPU section, It will ask you a number and will redirect you to "http://localhost/ram/&lt;givenNumber&gt;". After that it will load 100MB every &lt;givenNumber&gt; seconds.<b>
Be aware to stop it before your RAM fills up using Django terminal.
</b>

If non number given, It will redirect you to "http://localhost/ram" so you can enter a new value.
