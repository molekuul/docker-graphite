#!/bin/bash

j2 -f env /etc/templates/grafana.j2 > /etc/grafana/grafana.ini
j2 -f env /etc/templates/django_admin_init.exp.j2 > /tmp/django_admin_init.exp && \
    chmod a+x /tmp/django_admin_init.exp && \
    /tmp/django_admin_init.exp

mkdir -p /opt/graphite/storage/{log,rrd,whisper,lists} \
		 /opt/graphite/storage/log/webapp

chown graphite:graphite -R /opt/graphite/storage

exec /usr/bin/supervisord -c /etc/supervisord.conf -n
