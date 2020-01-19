FROM continuumio/miniconda3
ENV PYTHONUNBUFFERED 1
#ENV C_FORCE_ROOT true
RUN mkdir /web
RUN mkdir /web/static

WORKDIR /web
ADD ./laurasBlog.yml ./laurasBlog.yml

RUN conda env create -f ./laurasBlog.yml
RUN echo "source activate laurasBlog" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH

CMD source activate laurasBlog
