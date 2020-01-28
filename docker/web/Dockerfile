FROM continuumio/miniconda3
ENV PYTHONUNBUFFERED 1
#ENV C_FORCE_ROOT true
RUN mkdir /web
RUN mkdir /web/static

WORKDIR /web
ADD ./djangoVue.yml ./djangoVue.yml

RUN conda env create -f ./djangoVue.yml
RUN echo "source activate djangoVue" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH

CMD source activate djangoVue
