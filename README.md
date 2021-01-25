# Client for the HASTE Storage Engine

[![Build Status](https://travis-ci.org/HASTE-project/HasteStorageClient.svg?branch=master)](https://travis-ci.org/HASTE-project/HasteStorageClient)

Smart middleware for working with a variety of storage media with Scientific Computing datasets. 
Supports Python 2.7 and Python 3.*.


This tool was used in in this paper:
```
"Rapid development of cloud-native intelligent data pipelines for scientific data streams using the HASTE Toolkit"
https://www.biorxiv.org/content/10.1101/2020.09.13.274779v1
```
To reproduce the results from that paper, deploy and run the application according to the instructions at https://github.com/HASTE-project/k8s-deployments


## Installation

```
pip install haste-storage-client
```

To send blobs to Pachyderm, python-pachyderm is required.
Because of [this issue](https://github.com/pachyderm/python-pachyderm/issues/30), it needs to be installed manually:
```
git clone git@github.com:pachyderm/python-pachyderm.git
cd python-pachyderm
pip3 install -e .
```

Note that Pachyderm no longer supports Python 2.x

## Example
See [example.py](example.py).

## Tests

```
pip3 install -U pytest
pytest tests
```

## Config
Optionally, place `haste_storage_client_config.json` in ~/.haste/ (or windows equivalent),
instead of specifying config in constructor.

### Note
It isn't possible to connect to the database server from outside the SNIC cloud, so for local dev/testing you'll
need to use port forwarding from another machine. https://help.ubuntu.com/community/SSH/OpenSSH/PortForwarding


## Contributors
Ben Blamey, Andreas Hellander
