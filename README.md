# Local Website for DoS testing purposes

I developed this simple website to test DoS mitigation tools.

<br>
<br>

It has 3 pages for every Hardware resource that are involved in a typical DoS attack:

- Bandwidth
- CPU
- RAM

<br>

## Recomendation

I suggest you run this Django project as a docker-compose service and limit its resources using "cpus" and "mem_limit" attributes so your system does not crash.
