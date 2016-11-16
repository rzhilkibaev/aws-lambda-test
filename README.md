# AWS Lambda tests

## Initial setup

Run `$ sudo ./setup.sh` to install the build tools (`cfgen`, `awscli`, `terraform`).
Create a versioned S3 bucket in the same region where lambda will be.

## How to build individual service

```
$ cd infra/<resource_group>
$ ./init.sh
$ terraform apply
```

## Directory Layout

Directory | Description
----------|----------------
lambda | Lambda source code (python)
infra | Infrastructure source code (terraform)
util | Various utilities (bash, python)
cfg | Configuration files

All lambda functions are packaged into a single wheel. With minimal cold lambda penalty we don't need to worry about separating them yet.

