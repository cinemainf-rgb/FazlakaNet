name: Build APK

on:
  workflow_dispatch:
  push:

jobs:

  build:

    runs-on: ubuntu-22.04

    steps:

      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Install Dependencies
        run: |
          sudo apt update

          sudo apt install -y \
          git \
          zip \
          unzip \
          openjdk-17-jdk \
          python3-pip \
          autoconf \
          automake \
          libtool \
          pkg-config \
          zlib1g-dev \
          libncurses5-dev \
          libffi-dev \
          libssl-dev \
          cmake

          python3 -m pip install --upgrade pip
          pip3 install buildozer cython

      - name: Accept Android Licenses
        run: |
          mkdir -p ~/.android
          touch ~/.android/repositories.cfg

      - name: Build APK
        run: |
          buildozer android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: APK
          path: bin/*.apk
