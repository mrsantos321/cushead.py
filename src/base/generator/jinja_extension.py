# -*- coding: utf-8 -*-
from jinja2 import ext
from jinja2 import nodes
from jinja2 import parser
from jinja2 import runtime


class OneLineExtension(ext.Extension):
    """
    Removes whitespace between HTML tags at compile time, including tab and newline characters.
    It does not remove whitespace between Jinja2 tags or variables. Neither does it remove whitespace between tags
    """

    tags = {"oneline"}
    end_tags = [f"name:end{tag_name}" for tag_name in tags]

    def parse(self, parser: parser.Parser) -> nodes.CallBlock:
        """
        This method is called when any of tags is recognized

        The method apply transformation to the blocks inside the start and the end of the block.
        This transformation is the text without new lines and spaces between.
        The return is a node class initialized with this transformated text.
        The nodes are the elements that are used by the Abstract Syntax Tree of Jinja2 to represent
        the template.

        Args:
            parser: parser processor gived from Jinja2

        Return:
            CallBlock node type
        """

        # The first token is the token that started the tag.
        # Don't need it.
        next(parser.stream)

        # We need actual linenumber to append the final result to this line number
        lineno = parser.stream.current.lineno

        # Get the content inside the extension tag, with the second parameter as True,
        # we dont get, as final token, the end block of the extension tag, because we don't need it.
        body = parser.parse_statements(self.end_tags, True)

        # We parse te content calling our custom methods and generate the a CallBlock
        method = self.call_method("strip_spaces")
        call_block = nodes.CallBlock(method, [], [], body)

        # Return CallBlock seeted to the line number
        return call_block.set_lineno(lineno)

    def strip_spaces(self, caller: runtime.Macro) -> str:
        """
        Clean all the spaces and new lines of a content

        Args:
            caller: an anonymous Macro class, generated by CallBlock node.
                This class is callable and return a parsed version (variable replacement) of the content
                gived to the CallBlock.

        Return:
            return the cleaned content of the macro
        """
        return "".join(caller().split())
