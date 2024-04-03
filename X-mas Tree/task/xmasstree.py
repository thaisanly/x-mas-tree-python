decorator = 'O'
symbol = '*'


def get_post_card_canvas(line, column):
    greeting = 'Merry Xmas'
    greeting_start_at = column // 2 - len(greeting) // 2

    _lines = [column * "-"]
    for i in range(1, line - 1):
        _line = "|" + " " * (column - 2) + "|"

        if i == line - 3:

            _line = list(_line)

            for char in list(greeting):
                _line[greeting_start_at] = char
                greeting_start_at += 1

            _line = "".join(_line)

        _lines.append(_line)

    _lines.append(column * "-")

    return _lines


def create_xmas_tree(tree_height, decoration_interval):
    rows = 0
    current_row = 1
    space = tree_height - 1

    xmas_tree = [' ' * space + "X", ' ' * space + "^"]

    current_decoration = 1

    while rows < tree_height - 1:

        row = str(current_row * symbol)

        decorator_row = list(row)

        if rows == 1:
            decorator_row[1] = decorator
        else:

            for index, char in enumerate(decorator_row):
                if index > 0 and index % 2 == 1:

                    if current_decoration == decoration_interval:
                        decorator_row[index] = decorator
                        current_decoration = 1
                    else:
                        current_decoration += 1

        xmas_tree.append(' ' * (space - 1) + '/' + "".join(decorator_row) + "\\")

        current_row += 2
        rows += 1
        space -= 1

    xmas_tree.append((tree_height - 2) * " " + "| |")

    return xmas_tree


user_input = [int(x) for x in input().split()]
# user_input = [int(x) for x in "7 3 7 37".split()]

post_card_width = 30
post_card_height = 50

if len(user_input) == 2:
    tree = create_xmas_tree(user_input[0], user_input[1])

    for i in tree:
        print(i)
else:
    trees = [user_input[i:i + 4] for i in range(0, len(user_input), 4)]

    postcard = get_post_card_canvas(post_card_width, post_card_height)

    for _tree in trees:
        height, decorator_interval, line, column = _tree
        tree = create_xmas_tree(height, decorator_interval)

        for i in range(len(tree)):

            postcard_line = list(postcard[line + i])

            for j in range(len(tree[i])):
                if tree[i][j] != ' ':
                    head_cord = len(tree[0]) - 1
                    postcard_line[column - head_cord + j] = tree[i][j]

            postcard[line + i] = ''.join(postcard_line)

    # avoid tree overflow
    for index, item in enumerate(postcard):
        if 0 < index < post_card_width - 1:
            _item = list(postcard[index])
            _item[post_card_height - 1] = '|'
            postcard[index] = "".join(_item)

    for i in postcard:
        print(i)
