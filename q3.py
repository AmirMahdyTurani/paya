digits = list(input("Please enter your number: "))

dict = {
    '0': [
        ' *** ',
        '*   *',
        '*   *',
        '*   *',
        ' *** '
    ],
    '1': [
        '  *  ',
        '  *  ',
        '  *  ',
        '  *  ',
        '  *  ',
        '  *  ',
        '  *  ',
        '  *  ',
        '  *  ',
        '  *  '
    ],
    '2': [
        '****',
        '*   *',
        '    *',
        '    *',
        '*****'
    ],
    '3': [
        ' *** ',
        '    *',
        '  ** ',
        '    *',
        ' *** '
    ],
    '4': [
        '   * ',
        '  ** ',
        ' * * ',
        '*****',
        '   * '
    ],
    '5': [
        '*****',
        '*    ',
        '**** ',
        '    *',
        '**** '
    ],
    '6': [
        ' *** ',
        '*    ',
        '**** ',
        '*   *',
        ' *** '
    ],
    '7': [
        '*****',
        '   * ',
        '  *  ',
        ' *   ',
        '*    '
    ],
    '8': [
        ' *** ',
        '*   *',
        ' *** ',
        '*   *',
        ' *** '
    ],
    '9': [
        ' ****',
        '*   *',
        ' ****',
        '    *',
        ' *** '
    ]
}

for i in range(10):
    for digit in digits:
        print(dict[digit][i], end='\t')
    print("\n", end="")