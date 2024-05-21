# Use an appropriate base image
FROM ubuntu:18.04

# Set environment variables for non-interactive installation
ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install necessary tools
RUN apt-get update && \
    apt-get install -y software-properties-common wget

# Add the necessary repository for g++ 7.4.0
RUN add-apt-repository ppa:ubuntu-toolchain-r/test && \
    apt-get update

# Manually download and install the specific g++ 7.4.0 packages
RUN apt-get install -y \
    gcc-7=7.4.0-1ubuntu2.3 \
    g++-7=7.4.0-1ubuntu2.3

# Configure the alternatives system to use g++-7
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 60 --slave /usr/bin/g++ g++ /usr/bin/g++-7

# Verify the installation
RUN g++ --version

# Specify the entrypoint to keep the container running
CMD ["/bin/bash"]
