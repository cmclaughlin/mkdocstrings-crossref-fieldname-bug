from fieldname_bug_example.Tag import Tag

from typing import List

@dataclass
class WorkingExample:
    """ Working Example class"""

    tag: Tag
    """ This crossref link works. tag!=Tag """

    tags: List[Tag]
    """ This crossref also works. tags!=Tag """
