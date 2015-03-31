with open('invert-marks.vim', 'w') as f:
    for i in range(26):
        upper = unichr(i + ord('A'))
        lower = unichr(i + ord('a'))
        for a, b in [('m', 'm'), ('`', '\''), ('\'', '`')]:
            f.write("nnoremap {0}{1} {2}{3}\n".format(a, upper, b, lower))
            f.write("nnoremap {0}{1} {2}{3}\n".format(a, lower, b, upper))
