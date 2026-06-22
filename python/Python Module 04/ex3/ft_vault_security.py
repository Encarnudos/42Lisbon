def secure_archive(
        filename: str, action: str = "read",
        content: str = ""
        ) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as f:
                data_read = f.read()
                return (True, data_read)
        else:
            with open(filename, "w") as f:
                f.write(content)
                return (True, "Content successfully written to file")
    except OSError as e:
        return (False, str(e))


def ft_vault_security() -> None:
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt"))
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", "write", "some content"))


if __name__ == "__main__":
    ft_vault_security()
