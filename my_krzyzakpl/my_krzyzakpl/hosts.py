from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(r"", "my_krzyzakpl.urls", name=" "),
    host(r"panel", "panel.urls", name="panel"),
)
