FROM python:3-slim@sha256:399ca82ae14b7c202285a74a41595040422cb9b186df3339c3b67d0882f00fdd

RUN useradd -d /opt/powerapi -m powerapi
WORKDIR /opt/powerapi
USER powerapi

COPY --chown=powerapi . /tmp/powerapi
RUN pip3 install --user --no-cache-dir "/tmp/powerapi[everything]" && rm -r /tmp/powerapi

ENTRYPOINT ["python", "readJson.py"]
