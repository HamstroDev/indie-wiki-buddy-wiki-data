# Indie Wiki Buddy Data

This repository defines data needed by the [Indie Wiki Buddy](https://getindie.wiki) extension.
The data defined here is updated rather frequently and thus fetched remotely by the extension, rather than being bundled with the extension itself.

This is still a work in progress!

## Format
The current data format version is `4.0-dev`.

There will be more documentation on the data format here soon, once it has been finalized.
See [indie-wiki-buddy#1449](https://github.com/KevinPayravi/indie-wiki-buddy/issues/1449) for the current plan!

## Deployment
The data from this repository's `main` branch is automatically bundled with `bundle.py` and committed to the `static` branch.

The contents of the `static` branch are currently made available at `https://hamstrodev.github.io/indie-wiki-buddy-data`.

Currently, the following two files are available:
- [`meta.json`](https://hamstrodev.github.io/indie-wiki-buddy-data/meta.json) – contains a hash of the `data.json` file and the current format version.
- [`data.json`](https://hamstrodev.github.io/indie-wiki-buddy-data/data.json) – contains all the data the extension needs, in particular:
  - Currently (known) available [BreezeWiki](https://gitdab.com/cadence/breezewiki) instances
  - List of wiki hosts
  - List of wiki redirects supported by the extension
