for sgw in schlagwoerter:
    for sw in sgw:

        if sw.endswith("ung"):
            continue
        elif sw == "Digitalisierung":
            break

        print(sw)