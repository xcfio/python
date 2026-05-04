def is_number(value: str) -> bool:
    try:
        float(value.replace("%", ""))
        return True
    except ValueError:
        return False


def is_oklch(text: str) -> bool:
    if not text.startswith("oklch"):
        return False

    text = text[5:]

    if not text.startswith("(") or not text.endswith(")"):
        return False

    inner = text[1:-1]
    array = inner.split(" ")

    if len(array) not in (3, 5):
        return False

    if len(array) == 5 and array[3] != "/":
        return False

    lightness, chroma, hue, *rest = array
    slash, alpha = rest if rest else (None, None)

    for v in array:
        if v == "/":
            continue
        if v != "none" and not is_number(v):
            return False

    if lightness != "none":
        if "%" in lightness:
            l = float(lightness.replace("%", ""))
            if l < 0 or l > 100:
                return False
        else:
            l = float(lightness)
            if l < 0 or l > 1:
                return False

    if chroma != "none":
        if "%" in chroma:
            c = float(chroma.replace("%", ""))
            if c < 0 or c > 100:
                return False
        else:
            c = float(chroma)
            if c < 0 or c > 0.4:
                return False

    if hue != "none":
        if "%" in hue:
            return False
        h = float(hue)
        if h < 0 or h > 360:
            return False

    if slash is not None:
        if alpha is None or alpha == "none":
            return False

        if "%" in alpha:
            a = float(alpha.replace("%", ""))
            if a < 0 or a > 100:
                return False
        else:
            a = float(alpha)
            if a < 0 or a > 1:
                return False

    return True


print(is_oklch("oklch(0.5 0.2 180)"))  # True
print(is_oklch("oklch(50% 50% 180)"))  # True
print(is_oklch("oklch(0.5 0.2 180 / 0.5)"))  # True
print(is_oklch("oklch(0.5 0.2 180 / 50%)"))  # True
print(is_oklch("oklch(none 0.2 180)"))  # True
print(is_oklch("oklch(0.5 none 180)"))  # True
print(is_oklch("oklch(0.5 0.2 none)"))  # True
print(is_oklch("oklch(1 0 360)"))  # True
print(is_oklch("oklch(0 0 0)"))  # True

print(is_oklch("OKLCH(0.5 0.2 180)"))  # False - uppercase
print(is_oklch("oklch(1.1 0.2 180)"))  # False - L > 1
print(is_oklch("oklch(0.5 -0.1 180)"))  # False - C < 0
print(is_oklch("oklch(0.5 0.2 361)"))  # False - H > 360
print(is_oklch("oklch(0.5 0.2)"))  # False - missing H
print(is_oklch("oklch(0.5 0.2 180/0.5)"))  # False - bad / spacing
print(is_oklch("oklch(none none none / none)"))  # False - alpha can't be none
print(is_oklch("rgb(0, 0, 255)"))  # False - wrong format
print(is_oklch(""))  # False - empty
