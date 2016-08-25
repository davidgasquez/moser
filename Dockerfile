FROM debian:jessie

RUN apt-get update -y && \
    apt-get install --no-install-recommends -y -q \
        curl python3 python-dev python-setuptools bzip2

EXPOSE 5000

# Install conda
RUN curl -LO http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash Miniconda3-latest-Linux-x86_64.sh -p /miniconda -b
RUN rm Miniconda3-latest-Linux-x86_64.sh
ENV PATH=/miniconda/bin:${PATH}
RUN conda update -y conda

# Set conda environment
COPY requirements.yml /tmp/requirements.yml
RUN conda env update -f=/tmp/requirements.yml

# Add the application
COPY skflask /app
WORKDIR /app

ENTRYPOINT ["python"]
CMD ["app.py"]
