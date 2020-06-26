#!/usr/local/bin/python3
import os,argparse
print("Install go program for multiple OS and multiple architectures")
parser = argparse.ArgumentParser()
parser.add_argument("--os",
help="The target OS. Eg. all,linux,darwin,windows,etc",
choices=["all","linux","darwin","windows","dragonfly","android","freebsd",
         "netbsd","openbsd","plan9","solaris","aix""js"],
)

parser.add_argument("--arch",
help="The target's architecture. Eg. all,amd64,386,etc",
choices=["all","amd64","386","arm","ppc64","arm64","ppc64le", "mips", "mipsle",
"mips64", "mips64le", "s390x"],
)
parser.add_argument("--source",
help="The directory where source source is present",
default=".",
)
parser.add_argument("--target",
help="The target dir where the binary needs to be stored",
default=".",
)

args = parser.parse_args()
print("OS: ",args.os)
print("Arch: ",args.arch)
print("Source: ",args.source)
print("Target: ",args.target)
# source for the envs- https://golang.org/doc/install/source#environment
envs = {}
envs["aix"]=["ppc64"]
envs["android"]= ["386","amd64","arm","arm64"]
envs["darwin"]=["386","amd64","arm", "arm64"]
envs["dragonfly"]=["amd64"]
envs["freebsd"]=["386","amd64","arm", "amd64"]
envs["js"]=["wasm"]
envs["linux"]=["386","amd64", "arm", "arm64", "ppc64", "ppc64le", "mips", "mipsle", "mips64", "mips64le", "s390x"]
envs["netbsd"]=["386","amd64", "arm"]
envs["openbsd"]=["386","amd64", "arm", "arm64"]
envs["plan9"]=["386","amd64","arm"]
envs["solaris"]=["amd64"]
envs["windows"]=["386","amd64"]
#for key,value in envs.items():
#    print(key,value)

