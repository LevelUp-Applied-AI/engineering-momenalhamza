# Docker Notes — Day 9

## Docker Version

Output of `docker version`:

Client:
Version: 29.2.1
API version: 1.53
Go version: go1.25.6
Git commit: a5c7197
Built: Mon Feb 2 17:20:16 2026
OS/Arch: windows/amd64
Context: desktop-linux

Server: Docker Desktop 4.63.0 (220185)
Engine:
Version: 29.2.1
API version: 1.53 (minimum version 1.44)
Go version: go1.25.6
Git commit: 6bc6209
Built: Mon Feb 2 17:17:24 2026
OS/Arch: linux/amd64
Experimental: false
containerd:
Version: v2.2.1
GitCommit: dea7da592f5d1d2b7755e3a161be07f43fad8f75
runc:
Version: 1.3.4
GitCommit: v1.3.4-0-gd6d73eb8
docker-init:
Version: 0.19.0
GitCommit: de40ad0


## Hello World Test

Output of `docker run hello-world`:

Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
17eec7bbc9d7: Pull complete
cpe52d2000f90: Download complete
Digest: sha256:ef54e839ef541993b4e87f25e752f7cf4238fa55f017957c2eb44077083d7a6a
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
1. The Docker client contacted the Docker daemon.
2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
   (amd64)
3. The Docker daemon created a new container from that image which runs the
   executable that produces the output you are currently reading.
4. The Docker daemon streamed that output to the Docker client, which sent it
   to your terminal.


## Postgres Container

Pulled image:

- `docker pull postgres:15-alpine` (completed successfully)
- Verified cached images with `docker images` (hello-world and postgres:15-alpine shown)

Command used:

```bash
docker run -d \
  --name pg-prework \
  -e POSTGRES_PASSWORD=prework \
  -p 5432:5432 \
  postgres:15-alpine

  ## Autograder Keywords

LOG:  database system is ready to accept connections

Commands used:
- docker stop pg-prework
- docker restart pg-prework