from pick import pick


def print_console_menu():
    title = 'Please choose your favorite programming language (press SPACE to mark, ENTER to continue): '
    options = ['Update the Math Sorcerer\'s Amazon Index', 
               'Exit']
    selected = pick(options, title, multiselect=False, min_selection_count=1)
    return selected