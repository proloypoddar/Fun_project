import ascii_magic
output = ascii_magic.from_image_file("yellow.jpeg", columns=60, char=".")
ascii_magic.to_terminal(output)