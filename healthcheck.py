"""Ping the healthcheck endpoint and expect a successful response."""

from urllib.request import urlopen

response = urlopen("http://localhost/api/healthcheck")
assert 200 <= response.status < 400, f"HTTP error code {response.status}"
