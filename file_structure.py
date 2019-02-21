class TrieNode(object):
    """
    Trie Node having two data members

    char: Name of the directory
    children: list of directories in a directory
    """
    def __init__(self, char):
        self.char = char
        self.children = []


class FileStructure(object):

    """
    File Structure involving Linux Path Traversal
    """

    def __init__(self):

        """
        File Structure starts from root directory and have 3 data members

        root: TrieNode having root directory
        current: Current path of a file from root
        point: Directory where currently file structure is
        """

        self.root = TrieNode('/')
        self.current = []
        self.point = self.root

    def get_pwd(self):

        """
        Method required to return the path of current directory from root
        """

        if self.point == self.root:
            return "PATH: " + self.point.char
        s = "/"
        return "PATH: /" + s.join(self.current)

    def process(self, cmd: str):

        """
        Method require to manage which method to call for particular command
        """
        if cmd == 'pwd':
            return self.get_pwd()

        cmd = cmd.strip().split()

        if cmd[0] in ['ls', 'dir']:
            return self.list_dir()
        elif cmd[0] == 'mkdir':
            return self.new_dir(cmd[1])
        elif cmd[0] == 'cd':
            return self.change_dir(cmd[1])
        elif cmd[0] == 'rm':
            return self.remove_dir(cmd[1])
        elif cmd[0].endswith('dir'):
            return self.list_dir(cmd)
        else:
            return "ERR: CANNOT RECOGNIZE INPUT"

    def list_dir(self, cmd=None):

        """
        Method required to return the list of all the directories
        present in a directory
        """
        childs = []
        start = "DIRS: "

        if cmd:
            dirs = cmd[0].split('/')
            node = self.point

            for char in dirs[:-1]:
                found_in_child = False
                for child in node.children:
                    if child.char == char:
                        found_in_child = True
                        node = child
                        break

            if not found_in_child:
                return "ERR: INVALID PATH"
            for child in node.children:
                childs.append(child.char)

        else:
            for child in self.point.children:
                childs.append(child.char)

        return start + "  ".join(childs)

    def new_dir(self, word):

        """
        Method required to return the response whether dirs bean created or not
        """

        word = word.strip().split('/')
        if len(word) == 1:

            for child in self.point.children:

                if child.char == word[0]:
                    return "ERR: DIRECTORY ALREADY EXISTS"

            new_node = TrieNode(word[0])
            self.point.children.append(new_node)
            return "SUCC: CREATED"

        node = self.point
        count = 0
        for char in word:

            found_in_child = False

            for child in node.children:

                if child.char == char:
                    count += 1
                    node = child
                    found_in_child = True
                    break

            if not found_in_child and count == len(word) - 1:
                new_node = TrieNode(char)
                node.children.append(new_node)
                count += 1
                break
        if count == len(word):
            return "SUCC: CREATED"
        return "ERR: DIRECTORY ALREADY EXISTS"

    def change_dir(self, word):

        """
        Method required to return whether file structure can be traverse
        through a particular path
        """

        word = word.strip().split('/')

        if len(word) == 1:

            for child in self.point.children:

                if child.char == word[0]:
                    self.point = child
                    self.current.append(child.char)
                    return "SUCC: REACHED"
            return "ERR: INVALID PATH"

        curr = self.current
        node = self.point

        for char in word:

            found_in_child = False

            for child in node.children:

                if child.char == char:
                    found_in_child = True
                    curr.append(child.char)
                    node = child
                    break

            if not found_in_child:
                return "ERR: INVALID PATH"
        self.current = curr
        self.point = node
        return "SUCC: REACHED"

    def remove_dir(self, word):

        """
        Method required to remove/delete a directory
        """

        word = word.strip().split('/')

        if len(word) == 1:

            for child in self.point.children:
                if child.char == word[0]:
                    self.current.pop(child.char)
                    return "SUCC: DELETED"
            return "ERR: INVALID PATH"

        curr = self.current
        node = self.point
        count = 0

        for char in word:

            found_in_child = False

            for child in node.children:

                if child.char == char:
                    found_in_child = True
                    count += 1
                    curr = node
                    node = child

                if found_in_child and count == len(word):
                    curr.children.remove(child)
                    return "SUCC: DELETED"

        return "ERR: INVALID PATH"
