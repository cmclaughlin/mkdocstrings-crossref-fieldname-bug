from fieldname_bug_example.Tag import Tag

from typing import List

@dataclass
class MixedExamples:
    """ In this example, the two crossrefs from the working example no longer work while in the same class as the broken example """

    tag: Tag
    """ ... """

    tags: List[Tag]
    """ ... """

    Tag: Tag
    """ ... """
