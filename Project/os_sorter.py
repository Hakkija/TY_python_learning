with open("archs.txt", "r") as f:
    architectures = [line.strip() for line in f.readlines()]

unix_os = ["aix", "android", "darwin", "dragonfly", "freebsd", "hurd", "illumos", "ios", "linux", "netbsd", "openbsd", "solaris"]

def matching_architectures(os, arch, cgo, architectures):
    matches = []
    if os in unix_os:
        matches.append("unix")
    if cgo:
        matches.append("cgo")
    matches.extend([os, arch, f"{os}-{arch}"])
    if cgo:
        matches.append(f"{os}-{arch}-cgo")
    matches.append("all")
    return [arch for arch in architectures if arch in matches]

print(matching_architectures("linux", "arm64", False, architectures))
print(matching_architectures("windows", "386", True, architectures))
