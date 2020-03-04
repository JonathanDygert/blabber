FROM python:3

# Configure apt and install packages
RUN apt-get -q update \
    && apt-get -yq install --no-install-recommends apt-utils dialog 2>&1 \
    && DEBIAN_FRONTEND=noninteractive apt-get -yq install \
    git \
    iproute2 \
    lsb-release \
    openssh-client \
    procps \
    && apt-get autoremove -yq \
    && apt-get clean -yq \
    && rm -rf /var/lib/apt/lists/*

# Update Python environment based on requirements.txt
COPY requirements.txt /tmp/pip-tmp/
RUN pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

# Install python packages for development
RUN pip --disable-pip-version-check --no-cache-dir install pylint black

# Create a non-root user to use
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME

WORKDIR /workspace

# Set up flask configuration
ENV FLASK_APP=src/app.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=80 \
    FLASK_ENV=development

EXPOSE 80/tcp

CMD ["flask", "run"]